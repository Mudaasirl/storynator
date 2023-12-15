from django import forms
from django.contrib.auth.models import User

from users.models import Profile

class DocumentForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('voice_sample_1','voice_sample_2','voice_sample_3',)