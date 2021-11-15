from rest_framework import serializers
from account.models import User
from expense.models import Category, Expense, ExpenseMonth
from django.contrib.auth.hashers import make_password
from api.exceptions import DuplicateMonth
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    """
    User sign up view. overwrite the create method
    """
    user_categories = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    password = serializers.CharField(write_only=True,
                                     style={'input_type': 'password'}
                                     )

    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password', 'user_categories']

    def create(self, validated_data):
        category_list = ['Fuel', 'Bill', 'Entertainment', 'Education', 'Food']
        validated_data['password'] = make_password(validated_data['password'])
        user = User.objects.create(**validated_data)
        for category in category_list:
            Category.objects.create(user=user, name=category)
        return user


class CreateCategory(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['name']

    def create(self, validated_data):
        category = Category.objects.create(user=self.context['request'].user, **validated_data)
        return category


class AddExpense(serializers.ModelSerializer):

    def __init__(self, *args, **kwargs):
        super(AddExpense, self).__init__(*args, **kwargs)
        user = self.context['request'].user
        self.fields['expense_category'].queryset = (user.user_categories.all())

    class Meta:
        model = Expense
        fields = ['type', 'expense_category', 'amount', 'date']

    def create(self, validated_data):
        expense = Expense.objects.create(user=self.context['request'].user, **validated_data)
        return expense


class CreateMonth(serializers.ModelSerializer):

    name = serializers.CharField(
        style={'input_type': 'month'}
    )

    class Meta:
        model = ExpenseMonth
        fields = ['name', 'income', 'limit']

    def create(self, validated_data):
        name = validated_data['name']

        user = self.context['request'].user
        if user.expense_months.filter(name=name).exists():
            raise DuplicateMonth()

        expense_month = ExpenseMonth.objects.create(user=self.context['request'].user, **validated_data)
        return expense_month

