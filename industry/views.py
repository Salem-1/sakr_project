from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
import time


from django.http import JsonResponse


# Create your views here.
def index(request):
    return render(request, 'industry/index.html')

def posts(request):

    # Get start and end points
    start = int(request.GET.get("start") or 0) #getting the start integer plugged in to the url
    end = int(request.GET.get("end") or (start + 9))# same but end instead

    # Generate list of posts
    data = []
    for i in range(start, end + 1):  #generating sample data

        data.append(f"Post #{i}")    # Actually you can use this to generate real world posts
                                     #Or perhaps drone news :)
    # Artificially delay speed of response
    time.sleep(1)  # delay the speed not to surprise the user

    # Return list of posts
    return JsonResponse({
        "posts": data #special function to convert the data list to an API
    })
#congratulation you got your first API
# I know we borrowed it, but I can still congratulate you
# Harvard Cs is probably the most lovely Coding braces you ever had
