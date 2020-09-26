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

    #만약 아이디가 중복되어있으면 객체 생성x(수정완료!)
    account = CountModel()
    if request.method  == 'POST':
        #예외처리를 해줘야함....공백일떄, 널일떄, 등등....??
        if CountModel.objects.filter(gitid=request.POST['gitID']).exists(): #아이디 중복체크
             return render(request,'result.html',{'gitcommit':gitcommit,'day':day,'gitID':gitID,'account':account})
        else:
            account.gitid = gitID
            account.gitcommitcount = commit
            account.save()
    
    return render(request,'result.html',{'gitcommit':gitcommit,'day':day,'gitID':gitID,'account':account})

def rank(request):
    CountModels = CountModel.objects.all().order_by('-gitcommitcount')
    rank = 0
    return render(request,'rank.html',{'CountModels':CountModels,'rank':rank})