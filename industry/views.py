from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Articles
import requests #  to scrap the www
from bs4 import BeautifulSoup # to handel our scrapped data
import datetime # to make the datetime stamp and
import time

from django.http import JsonResponse
#make time algorithm to update news weekly
#save all the news in the database
#Make your API from the database not the online request
#for the sake of the effeciency ,(Ya genius)
#save each link wih it's site as separate column in the database
#any one who want to save a link, will just add the article id to his user table
#then make the site aesthetics
#submit and celebrate`

#   datetime.datetime.now()

#project steps:
#make sure that links are working for each title first
#Make save button to save all retrived articles in the database
#id|url|article(UNIQUE)|timeaccessed
#make JS code to open the article in the same page
#scale to add more websites
#add users and link it to save button
#make up, headers/footers
#apply make the video and celebrate (date today 5th June 2021)


def agregator(url, element):
    """Scrapping data from news website by entrin the url and the kind of element that contain the news"""
    #setting user agent manually as it gave me forbidden 403
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    result = requests.get(url, headers=headers)
    soup = BeautifulSoup(result.content, 'html5lib')

    headings = soup.find_all(element)
    #print(soup)
    # ("div", {"class": "rpwe-summary"}))
    headings = headings[0:-13] #trying to remove unwanted links
    out = [] # list to store the output to be exported as JSON API to our template
    for heading in headings:
        head = str(heading)
        out.append(head)#storing the news piece as it's as string to keep the same HTML format
        #storing only unique articles in the database

    #    if  str(Articles.objects.filter(title=f"{heading.text}")[:1]) == str(heading.text):
    #        print("not")
    #        continue
    #    else:
    #        print("saved")
    #        db_news=Articles(url=head, title=str(heading.text), datetime=datetime.datetime.now()) # storing each piece of article in the databas
    #        db_news.save()
    for i in out:
        print(i)
    return out
    #returning output as list


# Create your views here.
def index(request):
    return render(request, 'industry/index.html')

def posts(request):
    """making posts(news) as list (API) to be used in our template as JSON API"""
    time.sleep(1)  # delay the speed not to surprise the user
    # Return list of posts
    return JsonResponse({
        "posts":  agregator("https://dronelife.com/drone-delivery/","h3")#agregator("https://dronelife.com/drone-delivery/","h3") #special function to convert the data list to an API
    })


    #scrap old code for my reference only and has nothing to do with my current application
    # Get start and end points
    #start = int(request.GET.get("start") or 0) #getting the start integer plugged in to the url
    #end = int(request.GET.get("end") or (start + 9))# same but end instead

    # Generate list of posts
    #data = []
    #for i in range(start, end + 1):  #generating sample data

    #    data.append(f"Post #{i}")    # Actually you can use this to generate real world posts
                                     #Or perhaps drone news :)
    # Artificially delay speed of response


#congratulation you got your first API
# I know we borrowed it, but I can still congratulate you
# Harvard Cs is probably the most lovely Coding braces you ever had

def news(request):
    """Dummy function to try the news on, consider deleting or modifying it before submitting the project"""
    #the topics of drone delivery form dronelife website
    return render(request, "industry/news.html", {
        "headings": agregator("https://dronelife.com/drone-delivery/","h3")
        })
