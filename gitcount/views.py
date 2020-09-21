from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt
from .models import CountModel

def home(request):
    return render(request,'home.html')

@csrf_exempt #CSRF token missing or incorrect오류 해결
def result(request):
    if request.method == "POST":
        gitID = request.POST['gitID']
    url = 'https://github.com/'+gitID
    req = requests.get(url)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    commit = 0
    countArray =''
    for i in range(1,10):
        countArray = 'rect[class="day"][data-count=\"'+ str(i)+'\"]'
        for tag in soup.select(countArray):
            commit+=1
    gitcommit = "1일 1커밋한 날은 총 "+str(commit)+"일입니다."
    day = round(commit/365*100,1)

    account = CountModel()
    account.gitid = gitID
    account.gitcommitcount = commit
    account.save()
    

    return render(request,'result.html',{'gitcommit':gitcommit,'day':day,'gitID':gitID,'account':account})