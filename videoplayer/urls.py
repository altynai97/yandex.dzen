from django.urls import path
from . import views
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView
from django.urls import path


from .views import CustomLoginView, CustomLogoutView, RegistrationView
from ..views import dashboard, delete_video

urlpatterns = [
    path('', views.video_list, name='video_list'),
    path('upload/', views.video_upload, name='video_upload'),
    path('<int:pk>/', views.video_detail, name='video_detail'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('register/', RegistrationView.as_view(), name='register'),
    path('', login_required(TemplateView.as_view(template_name='videoplayer/video_list.html')), name='video_list'),
    path('dashboard/', dashboard, name='dashboard'),
    path('delete_video/<int:pk>/', delete_video, name='delete_video')
]