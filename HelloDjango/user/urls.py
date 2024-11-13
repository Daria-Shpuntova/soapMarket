from django.contrib import admin
from django.urls import path, include
from user import views as userViews

from django.contrib.auth import views as authViews
from django.conf import settings
from django.conf.urls.static import static
from . import views
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView


urlpatterns = [
    path('enter/', authViews.LoginView.as_view(template_name='user/enter.html'), name='enter'),
    path('reg/', userViews.register, name='reg'),
    path('exit/', authViews.LogoutView.as_view(template_name='user/exit.html'), name='exit'),
    path('password-change/', PasswordChangeView.as_view(template_name='user/password_change_form.html'), name='password_change'),
    path('password-change/done/', PasswordChangeDoneView.as_view(template_name='user/password_change_done.html'), name='password_change_done'),
    path('pass-reset/',
         PasswordResetView.as_view(template_name='user/pass_reset.html'),
         name='password_reset'),
    path('password-reset/done/',
         PasswordResetDoneView.as_view(template_name = "user/password_reset_done.html"),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name="user/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password-reset/complete/', PasswordResetCompleteView.as_view(template_name="user/password_reset_complete.html"), name='password_reset_complete'),
    path('profile/', userViews.profile, name='profile'),
    path('basket/', userViews.Basket_page.as_view(), name='basket'),
    path('update_quantity/', views.update_quantity, name='update_quantity'),
    path('delete_prod/', views.delete_prod, name='delete_prod')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)