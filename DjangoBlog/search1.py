from django.http import HttpResponse
from django.shortcuts import render

def search_post(request):
    ctx = {}
    if request.POST:
        ctx['rlt'] = request.POST['q']
    return render(request,'post.html',ctx)
