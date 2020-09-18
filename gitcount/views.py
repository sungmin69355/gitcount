from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

def home(request):
    url = 'https://github.com/sungmin69355'
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
    return render(request,'home.html',{'gitcommit':gitcommit})