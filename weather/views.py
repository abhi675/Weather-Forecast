import urllib.request
from django.shortcuts import render
import json
# Create your views here.
def index(request):
    if request.method=="POST":
        city=request.POST.get('city')
        url=urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&units=metric&APPID=9bd32ba272371b4c2ea0c383bac71503').read()
        r=json.loads(url)
        data={
            'city':city,
            'temprature':str(r['main']['temp'])+ 'C',
            'pressure':str(r['main']['pressure'])+ 'N/m2',
            'humidity':str(r['main']['humidity'])+ 'grams/m3',
            'icon':r['weather'][0]['icon'],
            'description':str(r['weather'][0]['description']),

        }
        return render(request,'index.html',{'data':data})
    return render(request,'index.html')