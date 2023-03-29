from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .forms import *
from .models import *
import os

# Create your views here.

def fileupload(request):
    if request.method=='POST':
        a=employeeform(request.POST,request.FILES)
        if a.is_valid():
            fn=a.cleaned_data['fname']
            nm=a.cleaned_data['name']
            em=a.cleaned_data['email']
            ad = a.cleaned_data['address']
            ph = a.cleaned_data['photo']
            ds=a.cleaned_data['designation']
            b=employeemodel(fname=fn,name=nm,email=em,address=ad,photo=ph,designation=ds)
            b.save()
            return HttpResponse("file upload successfully")
        else:
            return HttpResponse("file upload failed")
    else:
        return render(request,"fileupload.html")

def filedisplay(request):
    a=employeemodel.objects.all()
    pho=[]
    nam=[]
    ema=[]
    addr=[]
    design=[]
    fna = []
    id=[]
    for i in a:
        im = i.photo
        pho.append(str(im).split('/')[-1])
        nm=i.name
        nam.append(nm)
        em=i.email
        ema.append(em)
        ad=i.address
        addr.append(ad)
        ds=i.designation
        design.append(ds)
        fn = i.fname
        fna.append(fn)
        id1 = i.id
        id.append(id1)
    mylist=zip(pho,nam,ema,addr,design,fna,id)
    return render(request,'filedisplay.html',{'list':mylist})


def editfile(request,id):
    a=employeemodel.objects.get(id=id)
    photo=str(a.photo).split('/')[-1]
    if request.method=='POST':
        if len(request.FILES) !=0:
            if len(a.photo)>0:
                os.remove(a.photo.path)
            a.photo=request.FILES['photo']
        a.fname=request.POST.get('fname')
        a.name=request.POST.get('name')
        a.email = request.POST.get('email')
        a.address = request.POST.get('address')
        a.designation = request.POST.get('designation')
        a.save()
        return redirect(filedisplay)
    return render(request,'editfile.html',{'a':a,'photo':photo})


def deletefile(request,id):
    a=employeemodel.objects.get(id=id)
    if len(a.photo)>0:
        os.remove(a.photo.path)
    a.delete()
    return redirect(filedisplay)



