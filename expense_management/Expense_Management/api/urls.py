from django.urls import path, include
from .views import SignupView, UserLoginView, AddExpenses, CreateCategory, CreateMonth, ProfileDetail, UserListView

app_name = 'api'

urlpatterns = [
    path('signup/', SignupView.as_view(), name='api-signup'),
    path('userlist/', UserListView.as_view(), name='list_users'),
    path('profile/<int:pk>', ProfileDetail.as_view(), name='api-profile'),
    path('login/', UserLoginView.as_view(), name='api-login'),
    path('add_expenses/', AddExpenses.as_view(), name='add-expenses'),
    path('add_category/', CreateCategory.as_view(), name='add-category'),
    path('add_month/', CreateMonth.as_view(), name='add-month'),
]
