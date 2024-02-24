from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(redirect_authenticated_user=True), name="login"),
    path("", include("django.contrib.auth.urls"))
]

# "django.contrib.auth.urls" gives access to all of the below:s

# account/login/ is used to log a user into your application. Refer to it by the name "login".

# account/logout/ is used to log a user out of your application. Refer to it by the name "logout".

# account/password_change/ is used to change a password. Refer to it by the name "password_change".

# account/password_change/done/ is used to show a confirmation that a password was changed. Refer to it by the name "password_change_done".

# account/password_reset/ is used to request an email with a password reset link. Refer to it by the name "password_reset".

# account/password_reset/done/ is used to show a confirmation that a password reset email was sent. Refer to it by the name "password_reset_done".

# account/reset/<uidb64>/<token>/ is used to set a new password using a password reset link. Refer to it by the name "password_reset_confirm".

# account/reset/done/ is used to show a confirmation that a password was reset. Refer to it by the name "password_reset_complete".