from django.urls import path

from authentication import views


urlpatterns = [
    path('login/', views.LoginView.as_view(), name='login'),
    path('face/login/', views.FaceLoginView.as_view(), name='face_login'),
]
