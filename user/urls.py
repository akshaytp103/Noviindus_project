from user import views
from django.urls import path


urlpatterns = [
    # path('', views.home, name='home'),
    # path('home/', views.home, name='home'),
    path('/', views.signup, name='signup'),
    path('login/',views.loginpage,name="login"),
    path('logout/',views.logoutuser,name='logout'),
]
