from django.shortcuts import render,HttpResponse,get_object_or_404
from portfolio.models import *

# Create your views here.
def portfolio(request):
    if request.method == 'POST':
        data=request.POST
        username=data.get('username')
        email=data.get('email')
        message=data.get('message')
        form.objects.create(username=username,email=email,message=message)

    value=projects.objects.all()
    context={"data":value}
    return render(request,'portfolio.html',context)



def fullview(request,view_id):
    data= get_object_or_404(projects,pk=view_id)
    context={"data":data}

    return render(request,'fullview.html',context)