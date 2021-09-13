from django.shortcuts import redirect, render
import requests
from collections import Counter
import re
from pytrends.request import TrendReq

import datetime as dt
from django.conf import settings

# Create your views here.

from pytrends.request import TrendReq
import numpy

""" 
def related_terms(keyword):
    url = 'http://suggestqueries.google.com/complete/search?client=youtube&ds=yt&client=firefox&q='+ keyword

    r = requests.get(url)

    splitTags = r.json()[1]
    
    #print(splitTags)
    return splitTags



def the_test_view (request):


    context = {}
    return render(request, 'the_test_view.html', context)



def trends(keyword):
    pytrends = TrendReq(hl='en-US')

    all_keywords = [
                    keyword
                    ]
    keywords = []
    category = '0'
    geolocation = ''

    def check_trends():
        pytrends.build_payload(
            kw_list = all_keywords,
            timeframe='today 3-m',
            cat=category,
            geo=geolocation,
            gprop='youtube'
        )
        try:
            data = pytrends.interest_over_time()
            mean = round(data.mean(),2)
            avg = round(data[kw][-4:].mean(), 2)
            trend = round(((avg/mean[kw])-1)*100,2)
            if data.empty:
                raise RuntimeError ('no results, please alter search and try again...')

        except Exception as e:
            trend = 'Null'
            print("There's no trend data for this keyword")

        
        #print(trend)
        return str(trend)+"%"         

    for kw in all_keywords:
        keywords.append(kw)
        check_trends()
        keywords.pop()
    
       
    return check_trends()


"""

def searchVolume(keyword):

    content = []
    averageSearchVolume = []
    #Specify content type and form the request body
    headers = {'Content-Type': 'application/json'}
    job_params = {
        'q': keyword,
        "scraper": "google_msv", 
    }
    #Post job and get response
    response = requests.post(
        'https://rt.serpmaster.com',
        headers=headers,
        json=job_params,
        auth=('daudakolo16', 'aU7gR5q4ku')
    )
    data = response.json()
    results = data['results']
 
    for result in results:
        content.append(result['content']['seeds'])

    for data in content[0]:
        averageSearchVolume.append(data['averageSearchVolume'])

    return averageSearchVolume
    
def Video_data(user_keyword):
    videos = []
    all_publish_dates = []
    API_KEY = settings.YOUTUBE_API_KEY
    search_url =  'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    #Get User's search value
    searchHolder = 'valorant'
    #Do some research on YouTube API Parameters andd what they do
    #GETTING VIDEO IDS'

    #Dummy user input
    User_keyword = user_keyword
    search_params = {
        'part': 'snippet',
        'q': User_keyword,
        'maxResults': 20,
        'key': API_KEY,
        'type': 'video'

    }
    #####
    video_ids = []
    #####
    r = requests.get(search_url, params=search_params).json()
    

    results = r['items']


    for result in results:
        video_ids.append(result['id']['videoId']) 

    #VIDEO PARAMTER GETS AND DISPLAYS VIDEOS 
    #SETTING UP A VIDEO URL USING ID'S FROM ABOVE

    video_params = {
        'key': API_KEY,
        'maxResults': 20,
        'part': 'snippet, contentDetails, statistics',
        'id': ','.join(video_ids),
        
    }
    
    
    r = requests.get(video_url, params=video_params).json()
    
    all_vid_data = r['items']

#Getting video titles from the api
    for data in all_vid_data:
    
        try:

            video_data = {

                
                'title':data['snippet']['title'],
                'description':data['snippet']['description'],
                'id':data['id'],
                'tags': data['snippet']['tags'],
                'thumbnail':data['snippet']['thumbnails']['maxres']['url'],
                'viewCount': data['statistics']['viewCount'],
                'datePublished': data['snippet']["publishedAt"]
            }
        except KeyError:

                video_data = {
                'title':data['snippet']['title'],
                'description':data['snippet']['description'],
                'id':data['id'],
                'thumbnail':data['snippet']['thumbnails']['high']['url'],
                'viewCount': data['statistics']['viewCount'],
                'datePublished': data['snippet']["publishedAt"]

            }
        
        
        videos.append(video_data)


    context = {"videos": videos
     }

    return videos


def keyword_tool(user_keyword):
    videos = []
    video_titles = []
    allVideo_views = []
    video_tags = []
    all_tags = []

    API_KEY = settings.YOUTUBE_API_KEY
    search_url =  'https://www.googleapis.com/youtube/v3/search'
    video_url = 'https://www.googleapis.com/youtube/v3/videos'

    #Get User's search value
    searchHolder = 'valorant'
    #Do some research on YouTube API Parameters andd what they do
    #GETTING VIDEO IDS'

    #Dummy user input
    User_keyword = user_keyword
    search_params = {
        'part': 'snippet',
        'q': User_keyword,
        'maxResults': 20,
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
        'maxResults': 20,
        'part': 'snippet, contentDetails, statistics',
        'id': ','.join(video_ids),
        
    }
    
    
    r = requests.get(video_url, params=video_params).json()
    
    all_vid_data = r['items']

#Getting video titles from the api
    for data in all_vid_data:
    
        try:

            video_data = {

                
                'title':data['snippet']['title'],
                'id':data['id'],
                'tags': data['snippet']['tags'],
                'thumbnail':data['snippet']['thumbnails']['high']['url'],
                'viewCount': data['statistics']['viewCount'],
            }
        except:

                video_data = {
                'title':data['snippet']['title'],
                'id':data['id'],
                'thumbnail':data['snippet']['thumbnails']['high']['url'],
                'viewCount': data['statistics']['viewCount'],
            }

        
        videos.append(video_data)
        #Getting Tags
        
    for video in videos:
        video_titles.append(video['title'])
        allVideo_views.append(video['viewCount'])


    #Occurance Function FOR COMPETITION
    PreTitles = ' '.join(video_titles) 
    allTitles = PreTitles.lower().replace(' ', '')
    #print(allTitles)
    sorted_user_keywords = user_keyword.lower().replace(' ', '')
    #print(sorted_user_keywords)
    occurance = []
    pattern = re.compile(sorted_user_keywords)
    matches = pattern.findall(allTitles)
    for match in matches:
        occurance.append(match)
    Opt_strength = len(occurance)
    competition = str(Opt_strength) + ' Out Of the top 20 Videos have these Phrase in search Results '   
    

    #We get the total view count of the top 10 videos below code
    viewCount = ([int(x) for x in allVideo_views])
    totalViewCount = sum(viewCount) 
    ReadableTVC = "{:,}".format(totalViewCount)


    context = {"videos": videos, 
    'video_titles': video_titles, 
    "competition": competition, 
    'r': r,
    'video_tags': video_tags,
    'ReadableTVC': ReadableTVC
     }

    return competition, ReadableTVC, Opt_strength


#TOTAL VIEW COUNT FUNCTION
def all_videoViews_count():
     #This code turns the list of viewsCount into A List of Integers and adds them all together
    views, allVideo_views, video_titles = keyword_tool()
    viewCount = ([int(x) for x in allVideo_views])
    
    
    totalViewCount = sum(viewCount) 
    ReadableTVC = "{:,}".format(totalViewCount)

    return ReadableTVC

#COMPETITION ALGORITHM FUNCTION
def competition(user_keyword):
    views, allVideo_views, video_titles = keyword_tool()
    PreTitles = ' '.join(video_titles) 
    
    allTitles = PreTitles.lower().replace(' ', '')
    #print(allTitles)
        
        
    sorted_user_keywords = user_keyword.lower().replace(' ', '')
    #print(sorted_user_keywords)

   
    occurance = []
    pattern = re.compile(sorted_user_keywords)

    matches = pattern.findall(allTitles)

    for match in matches:
        occurance.append(match)
        

    #print(len(occurance))

    Opt_strength = len(occurance)
    competition = str(Opt_strength) + ' Out Of the top 20 Videos have these Phrase in search Results '
    return competition



