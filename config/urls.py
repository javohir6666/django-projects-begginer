from django.contrib import admin
from django.urls import path, include
from sender.views import *
from django.contrib.auth.views import LoginView, LogoutView
urlpatterns = [
    path("", LoginView.as_view(template_name="chatapp/LoginPage.html"), name="login-user"),
    path("admin/", admin.site.urls),
    path('texteditor/',include('texteditor.urls')),
    path('save-pass/',include('save_password.urls')),
    path("chat/", include("chatapp.urls")),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]
