from django.shortcuts import render, get_object_or_404
from django.views import View
from . models import testData

class Home(View):

    def get(self, request):
        datas=testData.objects.all
        return render(request, "home.html",{'datas':datas})

def detail(request, id):
    data=get_object_or_404(testData, pk = id)
    return render(request, 'detail.html', {'data': data})