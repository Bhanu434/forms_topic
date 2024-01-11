from django.shortcuts import render
from app.forms import *
from app.models import *
from django.http import HttpResponse

# Create your views here.
def Create_topic(request):
    ETFO=TopicForms()
    d={'ETFO':ETFO}
    if request.method=='POST':
        ETDO=TopicForms(request.POST)
        if ETDO.is_valid():
            tn=ETDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('data inserted')
        else:
            return HttpResponse('no data inserted')

    return render (request,'Select_topic.html',d)

def Create_webpage(request):
    EWFO=WebpageForms()
    d={'EWFO':EWFO}
    if request.method=='POST':
        EWDO=WebpageForms(request.POST)
        if EWDO.is_valid():
            tn=EWDO.cleaned_data['topic_name']
            na=EWDO.cleaned_data['name']
            url=EWDO.cleaned_data['url']
            email=EWDO.cleaned_data['email']
            TO=Topic.objects.get(topic_name=tn)
            WO=Webpage.objects.get_or_create(topic_name=TO,name=na,url=url,email=email)[0]
            WO.save()
            return HttpResponse('data enter into webpage')
    return render(request,'Select_webpage.html',d)

def Create_accessrecord(request):
    EAFO=AccessRecordForms()
    d={'EAFO':EAFO}
    if request.method=='POST':
        EADO=AccessRecordForms(request.POST)
        if EADO.is_valid():
            na=EADO.cleaned_data['name']
            date=EADO.cleaned_data['date']
            a=EADO.cleaned_data['author']
            WO=Webpage.objects.get(pk=na)
            AO=AccessRecord.objects.get_or_create(name=WO,date=date,author=a)[0]
            AO.save()
            return HttpResponse('data insert into Accessrecords')
        else:
            return HttpResponse(' no data insert into Accessrecords')

    return render(request,'Select_accessrecord.html',d)