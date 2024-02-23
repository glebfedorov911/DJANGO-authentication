from django.urls import path, include

from .views import index, SignUpView, LoginView, log_out

urlpatterns = [
    path('', index, name='index'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', log_out, name='logout'),
]