from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'chaithu_app'  # This is required for reverse URL resolution with namespace

urlpatterns = [
    # Home + Auth
    path('', views.home_redirect_view, name='home'),
    path('login/', views.login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='chaithu_app:login'), name='logout'),
    path('signup/', views.signup_view, name='signup'),
    path('user_login/', views.login_view, name='user_login'),
    path('login/', views.login_view, name='login'),

    # Main Pages
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),

    # User/Profile
    path('profile/', views.profile_view, name='profile'),
    path('account/', views.account_view, name='account'),
    path('settings/', views.settings_view, name='settings'),
    path('preferences/', views.preferences_view, name='preferences'),

    # Extra
    path('account-settings/', views.account_settings_view, name='account_settings'),
    path('change-password/', views.change_password_view, name='change_password'),
]
