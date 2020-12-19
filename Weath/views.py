from django.shortcuts import render
from .forms import ReqForm
import requests
# Create your views here.

def countt(s,c):
    k = 0
    for i in range(len(s)):
        if s[i]==c:
            k+=1
    return k

def index(request):
    form = ReqForm()
    context = {
        'form':form,
        'errors': [],
        'info': ''
    }
    if request.method == "POST":
        reqq = request.POST['r']
        if countt(reqq,',')==0:
            url  = f'http://api.openweathermap.org/data/2.5/weather?q={reqq}&appid=5f6c687f2ff84ba78c36f5bbc28d5e38'
            r = requests.get(url).json()
            tempp = str(int(r['main']['temp'])-273)
            diicc = {
                'city':url[url.find('=')+1:url.find('&')],
                'weath':r['weather'][0]['main'],
                'desc':r['weather'][0]['description'],
                'temp':tempp
            }
            context.update({'info':diicc})
            return render(request, 'Weath/main.html', context)
        elif countt(reqq,',')==1:
            ind = reqq.find(',')
            url = f'http://api.openweathermap.org/data/2.5/weather?q={reqq[:ind]},{reqq[ind+1:len(reqq)]}&appid=5f6c687f2ff84ba78c36f5bbc28d5e38'
            r = requests.get(url).json()
            tempp = str(int(r['main']['temp'])-273)
            diicc = {
                'city':url[url.find('=')+1:url.find('&')],
                'weath':r['weather'][0]['main'],
                'desc':r['weather'][0]['description'],
                'temp':tempp
            }
            context.update({'info':diicc})
            return render(request, 'Weath/main.html', context)
        elif countt(reqq, ',')==2:
            ind = reqq.find(',')
            ind1 = reqq.rfind(',')
            url =  f'http://api.openweathermap.org/data/2.5/weather?q={reqq[:ind]},{reqq[ind+1:ind1]},{reqq[ind1+1:len(reqq)]}&appid=5f6c687f2ff84ba78c36f5bbc28d5e38'
            r = requests.get(url).json()
            tempp = str(int(r['main']['temp'])-273)
            diicc = {
                'city':url[url.find('=')+1:url.find('&')],
                'weath':r['weather'][0]['main'],
                'desc':r['weather'][0]['description'],
                'temp':tempp
            }
            context.update({'info':diicc})
            return render(request, 'Weath/main.html', context)
        else:
            context['errors'].append("INVALID INPUT")
            return render(request, 'Weath/main.html', context)
    else:
        context['errors'].append("Fill the form, please!")
        return render(request, 'Weath/main.html', context)