from django.shortcuts import render
from keyword_tool.views import Video_data

# Create your views here.


def home_display(request):
    videos = []
    if request.method == 'POST':
         if request.POST.get("Search"):
            user_keyword_holder =  request.POST.get('keyword_form')
            user_keyword = user_keyword_holder.strip()

            videos = Video_data(user_keyword)
        
    context = {"videos": videos}

    return render(request, 'home_display.html', context)


def compare_opt(request, title):

    opt_title = request.GET['opt_title']
    opt_thumbnail = None
    videos = Video_data(title)

    context={"videos":videos, "opt_title":opt_title, "opt_thumbnail":opt_thumbnail}
    return render (request, 'compare_opt.html', context)




def suggested_display(request):
    videos = []
    if request.method == 'POST':
         if request.POST.get("Search"):
            user_keyword_holder =  request.POST.get('keyword_form')
            user_keyword = user_keyword_holder.strip()

            videos = Video_data(user_keyword)
        
    context = {"videos": videos}

    return render(request, 'suggested.html', context)