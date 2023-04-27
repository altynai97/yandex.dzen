from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from rest_framework.generics import get_object_or_404

from videoplayer.models import Video


@login_required
def dashboard(request):
    videos = Video.objects.filter(user=request.user)
    return render(request, 'videoplayer/dashboard.html', {'videos': videos})


@login_required
def delete_video(request, pk):
    video = get_object_or_404(Video, pk=pk)
    if video.user == request.user or request.user.is_superuser:
        video.delete()
        messages.success(request, 'Video deleted successfully.')
    else:
        messages.error(request, 'You are not authorized to delete this video.')
    return redirect('dashboard')
