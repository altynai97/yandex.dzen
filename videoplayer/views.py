from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import Video
from .forms import VideoForm
from .registration_forms import LoginForm, RegistrationForm


def video_list(request):
    videos = Video.objects.all()
    return render(request, 'videoplayer/video_list.html', {'videos': videos})


def video_detail(request, pk):
    video = get_object_or_404(Video, pk=pk)
    return render(request, 'videoplayer/video_detail.html', {'video': video})


def video_upload(request):
    if request.method == 'POST':
        form = VideoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
        return redirect('video_list')
    else:
        form = VideoForm()
    return render(request, 'videoplayer/video_upload.html', {'form': form})


class CustomLoginView(LoginView):
    form_class = LoginForm
    template_name = 'registration/login.html'


class CustomLogoutView(LogoutView):
    template_name = 'registration/logged_out.html'


class RegistrationView(CreateView):
    form_class = RegistrationForm
    template_name = 'registration/register.html'
    success_url = reverse_lazy('login')

