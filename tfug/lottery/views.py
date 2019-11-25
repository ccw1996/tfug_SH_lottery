from django.shortcuts import render
from django.http import HttpResponse
from lottery.models import Person
from lottery.models import Result
from lottery.privacy import filterTel

import json
import time
import numpy as np

# Create your views here.
def index(request):
    user_obj_list=Person.objects.filter(is_Lucky=0)
    user_list=[]
    for user_obj in user_obj_list:
         tel=filterTel(user_obj.telephone)
         user_list.append({'id':user_obj.id,'name':user_obj.personname,'tel':tel})
    return render(request, 'index.html', {'userlist':json.dumps(user_list)})


def update(request):
    uid=request.GET['uid']
    hour=time.strftime('%H',time.localtime(time.time()))
    uid=int(uid)
    p=Person.objects.get(id=uid)
    Person.objects.filter(id=uid).update(is_Lucky=1)
    Result.objects.create(uid=uid,personname=p.personname,telephone=p.telephone,hours=hour)
    return HttpResponse(1)

def get(request):
    user_obj_list = Person.objects.filter(is_Lucky=0)
    user_list = []
    for user_obj in user_obj_list:
        tel = filterTel(user_obj.telephone)
        user_list.append({'id': user_obj.id, 'name': user_obj.personname, 'tel': tel})
    return HttpResponse(json.dumps(user_list))

def allpeople(request):
    user_obj_list=Person.objects.filter(is_Lucky=0)
    return  HttpResponse(len(user_obj_list))

def luckypeople(request):
    user_lucky_list=Person.objects.filter(is_Lucky=1)
    return HttpResponse(len(user_lucky_list))

def multilucky(request):
    user_obj_list = Person.objects.filter(is_Lucky=0)
    hight=len(user_obj_list)-1 # 为参会人数
    num=5 #中奖人数
    ary1 = set()
    while len(ary1) < num: # num
        a = np.random.random_integers(low=0, high=hight, size=1)
        ary1.add(a[0])
    ary = list(ary1)