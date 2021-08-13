from django.db.models.fields import NullBooleanField
from django.forms.utils import ErrorDict
from django.http import request, response
from django.shortcuts import redirect, render
import requests
from . models import Optimization, ThumbnailImage
from . forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from keyword_tool.views import keyword_tool, Video_data, trends
import base64 


from django.conf import settings


# Create your views here.


def register (request):
     if request.user.is_authenticated:
        return redirect('/')
     else:

        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'You have successfully created an account for ' + user)
                return redirect('login')
     context={'form': form}
     return render(request, "register.html", context)


def login_page (request):
    if request.user.is_authenticated:
        return redirect('/')

    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                messages.info(request, 'Username OR Password incorrect')

    context={}
    return render(request, "login.html", context)
    

def logout_user(request):
    logout(request)
    return redirect('login')



def tags_getter (keyword):
    url = 'http://suggestqueries.google.com/complete/search?client=youtube&ds=yt&client=firefox&q='+ keyword

    r = requests.get(url)

    splitTags = r.json()[1]
    
    #print(splitTags)
    return splitTags


def home (request):

    video_titles=[]
    video_tags = []
    all_keywords = []
    if request.method=='POST':
        if request.POST.get("Search"):
            user_keyword_holder =  request.POST.get('keyword_form')
            user_keyword = user_keyword_holder.strip()

            if user_keyword:
                suggested = tags_getter(user_keyword)
                all_keywords.append(suggested)
                videos = Video_data(user_keyword)
                Competition, ReadableTVC = keyword_tool(user_keyword)
                trends_data = trends(user_keyword)
        
    else:
        videos = None
        suggested = None
        all_keywords = None
        Competition = None
        trends_data = None
        ReadableTVC = None
        user_keyword = None
        
    
        
    context = {'videos': videos, 'suggested': suggested, 'Competition': Competition, 'ReadableTVC': ReadableTVC, 'trends_data': trends_data,}
    return render(request, "home.html", context)









def test_view1():
    videos = []
    #Search URL Using API + parameters i.e exactly what data to return
    API_KEY = settings.YOUTUBE_API_KEY
    search_url =  'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    #Get User's search value
    # search = request.GET.get('search')


    #Do some research on YouTube API Parameters andd what they do
    #GETTING VIDEO IDS'
    search_params = {
        'part': 'snippet',
        'q': 'grinding',
        'maxResults': 9,
        'key': API_KEY,
        'type': 'video'

    }
    #####
    video_ids = []
    #####
    r = requests.get(search_url, params=search_params)
    results = r.json()['items']

    for result in results:
        video_ids.append(result['id']['videoId']) 

    #VIDEO PARAMTER GETS AND DISPLAYS VIDEOS 
    #SETTING UP A VIDEO URL USING ID'S FROM ABOVE
    video_params = {
        'key': API_KEY,
        'maxResults': 9,
        'part': 'snippet, contentDetails',
        'id': ','.join(video_ids),
        
    }
    
    
    r = requests.get(video_url, params=video_params).json()

    all_vid_data = r['items']

    for data in all_vid_data:
        try:

            video_data = {

                
                'title':data['snippet']['title'],
                'id':data['id'],
                'tags':data['snippet']['tags'],
            }
        except:

             video_data = {

                
                'title':data['snippet']['title'],
                'id':data['id'],
                'thumbnail':data['snippet']['thumbnails']['high']['url'],
            }

        

        videos.append(video_data)
        print(videos)

    return videos




    
    
@login_required(login_url='login')
def main_seo_studio (request):
    #Calling the keyword Explore function

    #Getting Suggested keywords and pasting them as tags
    keyword = request.GET['keyword_getter']
    tags = tags_getter(keyword)


    #This is the keyword reseacrh "Dummy" form
    keyword_research_form = Keyword_Research_form

    #This is the optimization form containiing Title, Description and Tags
    optimization_form = Optimization_form
    if request.method == 'POST':
        if request.POST.get('save'):
            optimization_form = Optimization_form(request.POST, request.FILES)
            if optimization_form.is_valid():
                optimization_form.save()
            return redirect('/main/all_opts')

        #Testing the request methods where it identifies what button is clicked and responds to each differently!
        if request.POST.get('testbutton'):
            return redirect('/main/all_opts')
            

    context ={
        "keyword_research_form": keyword_research_form,
     "optimization_form": optimization_form,
     "tags": tags,
     "keyword": keyword
     }
    return render (request, 'main_seo_studio.html', context)


def seo_studio (request):

    form = Optimization_form()
    if request.method == 'POST':
        if request.user.is_authenticated:
            form = Optimization_form(request.POST)
            if form.is_valid():
                form.save()
            return redirect('/all_opts')
        else:
            return redirect('/login')

    context = {'form': form}
    return render (request, "seo_studio.html", context)



#for user to be able to use the edit optimization 
#user has to save their optimization (Requires signup/login)


def all_opts (request):
    opts = Optimization.objects.all()
    context = {"opts": opts}
    return render (request, "all_opts.html", context)


def read_optimization (request, pk):


    get_opt = Optimization.objects.get(id=pk)
    context = {"read_opt": get_opt}
    return render (request, "read_optimization.html", context)


def edit_opt (request, pk):
    get_opt = Optimization.objects.get(id=pk)
    form = Optimization_form(instance=get_opt)
    if request.method == 'POST':
        form = Optimization_form(request.POST, instance=get_opt)
        if form.is_valid():
            form.save()
        return redirect('/all_opts')
    context = {"form": form}
    return render (request, "edit_opt.html", context)



def thumbnails(request):
    videos = []
    if request.method == 'POST':
    
        #Search URL Using API + parameters i.e exactly what data to return
        API_KEY = settings.YOUTUBE_API_KEY
        search_url =  'https://www.googleapis.com/youtube/v3/search'
        video_url = 'https://www.googleapis.com/youtube/v3/videos'

        #Get User's search value
        search_query = request.POST['search']
        #Do some research on YouTube API Parameters andd what they do
        #GETTING VIDEO IDS'
        search_params = {
            'part': 'snippet',
            'q': search_query,
            'maxResults': 9,
            'key': API_KEY,
            'type': 'video'

        }
        #####
        video_ids = []
        #####
        r = requests.get(search_url, params=search_params)
        results = r.json()['items']

        for result in results:
            video_ids.append(result['id']['videoId']) 

        #VIDEO PARAMTER GETS AND DISPLAYS VIDEOS 
        #SETTING UP A VIDEO URL USING ID'S FROM ABOVE
        video_params = {
            'key': API_KEY,
            'maxResults': 9,
            'part': 'snippet, contentDetails',
            'id': ','.join(video_ids),
            
        }


        r = requests.get(video_url, params=video_params).json()

        all_vid_data = r['items']

        for data in all_vid_data:
            
            video_data = {

                
                'title':data['snippet']['title'],
                'id':data['id'],
                'thumbnail':data['snippet']['thumbnails']['high']['url'],
            }
            

            videos.append(video_data)




        print(videos)
    context = {"videos": videos}
    return render(request, "thumbnails.html", context)



def YoutubeTemplate(request):

    context = {}
    return  render(request, 'youtubetemplate.html', context)


def compare_vid(request, pk):



    get_opt = Optimization.objects.get(id=pk)
    
    opt_title = get_opt.title
    print(opt_title)
    
    try:
        competition_videos =  test_view1(opt_title)
    except KeyError:
        competition_videos = test_view1('Leo Messi')


    context = {'competition_videos': competition_videos, "get_opt": get_opt}
    return render(request, 'compare_vid.html', context)