from django.shortcuts import render, get_object_or_404
from django.views import View
from . models import testData

class Home(View):

    def get(self, request):
        datas=testData.objects.all
        return render(request, "index.html",{'datas':datas})

def click(request, id):
    data=get_object_or_404(testData, pk = id)
    data.views_cnt+=1
    return render(request, 'click.html', {'data': data})