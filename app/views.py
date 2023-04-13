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
   LOW=Webpage.objects.filter(name__startswith='h')
   LOW=Webpage.objects.filter(url__endswith='.com')
   LOW=Webpage.objects.filter(name__contains='n')
   LOW=Webpage.objects.filter(name__in=('hima','indhu'))
   LOW=Webpage.objects.filter(name__regex='[a-zA-Z]{5}')


   
   d={'webpage':LOW}
   return render (request,'display_webpage.html',context=d)

def display_accessrecord(request):
   LOA=AccessRecord.objects.all()
   LOA=AccessRecord.objects.filter(date__gt='2000-05-07')
   LOA=AccessRecord.objects.filter(date__lt='2000-05-07')
   LOA=AccessRecord.objects.filter(date__gte='2000-05-07')
   LOA=AccessRecord.objects.filter(date__lte='2000-05-07')
   LOA=AccessRecord.objects.filter(date__month='05')
   LOA=AccessRecord.objects.filter(date__year='2000')


   d={'accessrecord':LOA}
   return render (request,'display_accessrecord.html',context=d)


def update_display(request):
   LOW=Webpage.objects.filter(name='sailu').update(name='indhu')
   h1=webpage.objects.get_or_create(topic_name='football',name='sailu',url='https://hima.in')
   h1.save()
   d={'webpage':Webpage.objects.all()}
   return render (request,'display_webpage.html',context=d)

   

def delete_webpage(request):
   
   Webpage.objects.filter(name='hima').delete()
   d={'webpage':Webpage.objects.all()} 
   return render(request,'display_webpage.html',d)  

def display_accessupdate(request):
   AccessRecord.objects.filter(name=2).update(author='girish')
   LOA=AccessRecord.objects.all()
   d={'accessrecord':LOA}
   return render (request,'display_accessrecord.html',context=d) 

def display_webupdate(request):
   TO=Topic.objects.get_or_create(topic_name='rubby')[0]
   TO.save()

   Webpage.objects.update_or_create(topic_name=TO,name='mahi',url='http://mahi.com') 
   LOW=Webpage.objects.all()
   d={'webpage':LOW}
   return render(request,'display_webpage.html',d)























