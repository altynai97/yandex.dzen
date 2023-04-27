from django import forms
from .models import Video
from django.core.exceptions import ValidationError
import magic
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ('title', 'description', 'video_file')

    def clean_video_file(self):
        video_file = self.cleaned_data.get('video_file')
        if video_file:
            # Check file type
            mime = magic.Magic(mime=True)
            file_type = mime.from_buffer(video_file.read())
            if not file_type.startswith('video'):
                raise ValidationError('Invalid file type. Only video files are allowed.')
            # Check file size
            if video_file.size > 50 * 1024 * 1024:  # 50 MB
                raise ValidationError('File size exceeds the limit of 50 MB.')
        return video_file



