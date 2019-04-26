from django.http import HttpResponse
from django.shortcuts import render
import operator
def homePage(request):
    return render(request,'home.html')
def count(request):
        data=request.GET['fulltextarea']
        words=data.split()
        word_len=len(words)
        my_dic={}
        for word in words:
            if word in my_dic:
                my_dic[word]=my_dic[word]+1
            else:
                my_dic[word]=1


        sortted_list=sorted(my_dic.items(),key=operator.itemgetter(1))

        return render(request,'count.html',{'fulltext':data,'newwords':word_len,'worddic':sortted_list})
def about(request):
    return render(request,'about.html')
