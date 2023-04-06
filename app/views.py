from django.shortcuts import render


# Create your views here.
from django.db.models.functions import Length 
from app.models import *
def display_topics(request):
   LOT=Topic.objects.all()
   d={'topics':LOT}
   return render (request,'display_topics.html',context=d)

def display_webpage(request):
   LOW=Webpage.objects.all()
   LOW=Webpage.objects.filter(topic_name='cricket')
   LOW=Webpage.objects.exclude(topic_name='cricket')
   LOW=Webpage.objects.all().order_by('topic_name') 
   LOW=Webpage.objects.all().order_by('-topic_name')
   LOW=Webpage.objects.all().order_by(Length('topic_name'))
   LOW=Webpage.objects.all().order_by(Length('topic_name').desc())
   d={'webpage':LOW}
   return render (request,'display_webpage.html',context=d)

def display_accessrecord(request):
   LOA=AccessRecord.objects.all()
   LOA=AccessRecord.objects.filter(date__gt='2000-05-07')
   LOA=AccessRecord.objects.filter(date__lt='2000-05-07')
   LOA=AccessRecord.objects.filter(date__gte='2000-05-07')
   LOA=AccessRecord.objects.filter(date__lte='2000-05-07')

   d={'accessrecord':LOA}
   return render (request,'display_accessrecord.html',context=d)

