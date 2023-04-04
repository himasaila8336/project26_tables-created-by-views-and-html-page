from django.shortcuts import render

# Create your views here.
from app.models import *
def display_topics(request):
   LOT=Topic.objects.all()
   d={'topics':LOT}
   return render (request,'display_topics.html',context=d)

def display_webpage(request):
   LOW=Webpage.objects.all()
   d={'webpage':LOW}
   return render (request,'display_webpage.html',context=d)

def display_accessrecord(request):
   LOA=AccessRecord.objects.all()
   d={'accessrecord':LOA}
   return render (request,'display_accessrecord.html',context=d)

