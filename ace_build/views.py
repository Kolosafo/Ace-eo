from django.shortcuts import redirect, render, HttpResponse
import requests
from . models import Optimization, ThumbnailImage
from . forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from keyword_tool.views import keyword_tool, Video_data, searchVolume
from ratelimit.exception import RateLimitException

from django.contrib import messages



import base64 


from django.conf import settings


# Create your views here.


def home_page(request):


    context = {}
    return render(request, "home_page.html", context)


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
                return redirect('/main/all_opts')
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
    search_volume = None
    videos = None
    suggested = None
    all_keywords = None
    UKC = None
    UKTV = None
    title_occurance = None
    trends_data = None
    user_keyword = None
    tags = None

       
    all_keywords = []
    if request.method=='GET':
        if request.GET.get("Search"):
            user_keyword_holder =  request.GET.get('keyword_form')
            user_keyword = str(user_keyword_holder).strip()

            if user_keyword:
                search_volume = searchVolume(user_keyword)
                suggested = tags_getter(user_keyword)
                all_keywords.append(suggested)
                videos = Video_data(user_keyword)

                # UKC stands for "User Keyword Competiton" result
                # and UKTV stands for "User Keyword Total View Count" result
                UKC, UKTV, title_occurance = keyword_tool(user_keyword)


    optimization_form = Optimization_form
    if request.method == 'POST':
        if request.POST.get('save'):
            if request.user.is_authenticated:
                optimization_form = Optimization_form(request.POST, request.FILES)
                if optimization_form.is_valid():
                    user_title = optimization_form.cleaned_data["title"]
                    user_description = optimization_form.cleaned_data["description"]
                    user_tags = optimization_form.cleaned_data["tags"]
                    
                    opt = Optimization(title=user_title, description=user_description, tags=user_tags)
                    opt.save()
                    request.user.optimization.add(opt)
            else:
                messages.info(request, "You need to be Logged in to save your optimization")
                messages.info(request, "You can still view your optimization by going back and clicking 'View' ")

            return redirect('/main/all_opts')
         
    context = {
        'videos': videos, 'suggested': suggested, 'UKTV':UKTV, 'UKC':UKC, "title_occurance": title_occurance,
        'trends_data': trends_data, 'user_keyword': user_keyword, 'search_volume':search_volume, 'tags':tags, 'optimization_form': optimization_form}
    return render(request, "home.html", context) 

    
    
def main_seo_studio (request):
    display_videos = []
    #Calling the keyword Explore function

    #Getting Suggested keywords and pasting them as tags
    tags = None
    keyword = request.GET['keyword_getter']

    transfered_data = {
    'display_titles': request.post.GET['transferTitle'],
    'display_tags' : request.post.GET['transferTags'],
    'display_viewCount': request.post.GET['transferviewCount'],
    'display_dates': request.post.GET['transferDates'] 
    }

    display_videos.append(transfered_data) 

    testTitles =  request.post.GET['transferTitle']
    print(testTitles)

    #This is the keyword reseacrh "Dummy" form
    keyword_research_form = Keyword_Research_form

    #This is the optimization form containiing Title, Description and Tags
    optimization_form = Optimization_form
    if request.method == 'POST':
        if request.POST.get('save'):
            if request.user.is_authenticated:
                optimization_form = Optimization_form(request.POST, request.FILES)
                if optimization_form.is_valid():
                    user_title = optimization_form.cleaned_data["title"]
                    user_description = optimization_form.cleaned_data["description"]
                    user_tags = optimization_form.cleaned_data["tags"]
                    
                    opt = Optimization(title=user_title, description=user_description, tags=user_tags)
                    opt.save()
                    request.user.optimization.add(opt)
            else:
                messages.info(request, "You need to be Logged in to save your optimization")
                messages.info(request, "You can still view your optimization by going back and clicking 'View' ")

            return redirect('/main/all_opts')

        #Testing the request methods where it identifies what button is clicked and responds to each differently!
            
    context ={
    "keyword_research_form": keyword_research_form,
     "optimization_form": optimization_form,
     "tags": tags,
     "keyword": keyword,
     "display_videos": display_videos
     }
    return render (request, 'main_seo_studio.html', context)

#IF USER IS NOT OPTIMIZING FROM MAIN PAGE AFTER KEYWORD RESEARCH, LET THEM USE THIS PAGE
def seo_studio (request):

    form = Optimization_form()
    if request.method == 'POST':
        if request.POST.get('save'):
            if request.user.is_authenticated:
                form = Optimization_form(request.POST, request.FILES)
                if form.is_valid():
                    user_title = form.cleaned_data["title"]
                    user_description = form.cleaned_data["description"]
                    user_tags = form.cleaned_data["tags"]
                    opt = Optimization(title=user_title, description=user_description, tags=user_tags)
                    opt.save()
                    request.user.optimization.add(opt)
                return redirect('/main/all_opts')
            else:
                messages.info(request, "You need to be Logged in to save your optimization")
                messages.info(request, "You can still view your optimization by going back and clicking 'View' ")
                return redirect('/main/login')
       

    context = {'form': form}
    return render (request, "seo_studio.html", context)

def view_current_opt (request):
  

    title = request.GET["opt_title"]
    description =  request.GET["opt_description"]
    tags =  request.GET["opt_tags"]

    if title and description and tags != '':
        title = title
        description = description
        tags = tags
    else:
        title = None
        description = None
        tags = None
    
    context = {"title": title, "description": description, "tags": tags}
    return render (request, "view_current_opt.html", context)



#for user to be able to use the edit optimization 
#user has to save their optimization (Requires signup/login)

@login_required(login_url='login')
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
        return redirect('/main/all_opts')
    context = {"form": form}
    return render (request, "edit_opt.html", context)


def YoutubeTemplate(request):

    context = {}
    return  render(request, 'youtubetemplate.html', context)



    context = {'competition_videos': competition_videos, "get_opt": get_opt}
    return render(request, 'compare_vid.html', context)

def thumbnails(request):
    return render(request, 'thumbnails.html')

    
