from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

session = HTMLSession()

def get_video_title(url):
    response = session.get(url)

    #Execute Javascript
    response.html.render(sleep=1, timeout=30)

    soup = bs(response.html.html, 'html.parser')

    video_meta = {}

    #Video Title
    video_meta["title"] = soup.find("h1").text.strip()

    #Video tags
    



    return video_meta() 
