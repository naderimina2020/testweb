from django.shortcuts import render
from django.shortcuts import HttpResponse
import random
def about(request):
#    return HttpResponse('hi world')
     nam1=request.GET.get('t1')
     c=list("abcdefghijklomnp")
     thepass=""
     for _ in range(5):
         thepass+=random.choice(c)


     return render(request,'about.html',{'nam':nam1,'ps':thepass})
def home(request):
#    return HttpResponse('home')

     return render(request,'home.html')
def password(request):
#    return HttpResponse('home')
     c=list("abcdefghijklomnp")
     thepass=""
     for _ in range(5):
         thepass+=random.choice(c)
     nam=request.GET.get('t1')
     return render(request,'password.html',{'password':thepass,'n':nam})
