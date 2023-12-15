from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import DocumentForm
from blog.models import Post
from users.models import Profile
from dotenv import load_dotenv
from elevenlabs import set_api_key, generate, play,clone
from pydub import AudioSegment
#from pydub.playback import play as pl

import openai
import io,os

load_dotenv()

api_key = os.getenv('OPENAI_KEY',None)
elevenLabs_key = os.getenv('ELEVENLABS_KEY',None)
set_api_key(elevenLabs_key)

def landing_page_view(request):
    context={
        'pass':'pass'
    }
    return render(request,'storynator/landing_page.html',context)

@login_required
def home_view(request):

    def requestGPT(user_input):                
        # openai.api_key = api_key
        # prompt = f"If the question is related to story then Create a Story and take this as story arguments : { user_input } else answer cant say"
        # response = openai.Completion.create(
        #     engine = 'text-davinci-003',
        #     prompt = prompt,
        #     max_tokens = 100,
        #     temperature = 0.7,
        # )        
        # return  response["choices"][0]["text"]        
        return user_input    
    
    if request.method  == 'POST':
        user_input = request.POST.get('prompt')
        user = request.user
        
        generated_story = requestGPT(user_input)  
        narration = 'something'

        post = Post.objects.create(title=user_input,content=generated_story,author=user,voice=narration)      

        return render(request,'storynator/generated_story.html', {'post':post}) 
    else:
        context = {
           'users' : 'users',
        }
        return render(request,'storynator/home.html',{'response':context})
    # views.py
@login_required
def voice_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():            
            
            profile = Profile.objects.get(user=request.user)
            profile.voice_sample_1 = form.cleaned_data['voice_sample_1']
            profile.voice_sample_2 = form.cleaned_data['voice_sample_2']
            profile.voice_sample_3 = form.cleaned_data['voice_sample_3']
            
            profile.save()
            return redirect('home-view')
    else:
        form = DocumentForm()
    return render(request, 'storynator/uploads.html', {'form': form  })

