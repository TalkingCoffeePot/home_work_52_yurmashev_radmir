from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

app_name='accounts'

urlpatterns = [
    path('login/', LoginView.as_view(), name='log_in'),
    path('logout/', LogoutView.as_view(), name='log_out'),
]