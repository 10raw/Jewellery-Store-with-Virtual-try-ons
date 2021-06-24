from django import forms
from django.http import response
from django.shortcuts import render

# Create your views here.
from .models import Products, User
from .forms import Userform

def product(request,filvalue):
    prod=Products.objects.filter(profil=filvalue)
    return render(request, 'goldpage/goldpage.html', {'prod':prod, 'filid1':filvalue})
   
def showhomepage(request):
    return render(request, 'allpages/homepage.html')

def showprodpage(request,proname1):
    product=Products.objects.filter(pronm=proname1)
    print(product)
    message=""
    c=0
    context={'product':product}
    if request.method=='POST':
        form=Userform(request.POST,request.FILES)
        if form.is_valid():
            email=form.cleaned_data['usrmail']
            print(email)
            passw=form.cleaned_data['usrpass']
            profile=form.cleaned_data['usrprofile']
            lehimg=form.cleaned_data['usrphoto']
            userdets=User.objects.all()
            print('userdets',userdets)
            for i in userdets:
                if i.usrmail==email:
                    if i.usrpass==passw:
                        print("already registered")
                        i.usrphoto.delete()
                        i.usrphoto=lehimg
                        i.usrprofile=profile
                        
                        i.save()
                        context['lehimg']="/media/usrphotos/"+str(i.usrphoto)
                        
                        c=1
                        print(i.usrphoto)
                    else:
                        message="Incorrrect Email or Password"
            if c!=1:
                print("new registration")
                newobject=User(
                    usrmail=email,
                    usrpass=passw,
                    usrprofile=profile,
                    usrphoto=lehimg,)
                newobject.save()
                context['mail']=email
                context['passw']=passw
                context['lehimg']="/media/usrphotos/"+str(lehimg)
                context['profile']=profile
                print('userdets',userdets)
                print(newobject)
    else:
        form=Userform()
    context['form']=form
    print('message',message)
    response=render(request,'prodpage/prodpage.html', context)
    return response

def filtercategory(request,filp,filw,filo,filvalue1):
    print(filvalue1,filo,filp,filw)

    if filp:
        if filp[0]=='1':
            filteredprod=Products.objects.filter(propri__gte=10000).filter(propri__lte=25000)
        elif filp[0]=='2':
            filteredprod=Products.objects.filter(propri__gte=25000).filter(propri__lte=40000)
        elif filp[0]=='3':
            filteredprod=Products.objects.filter(propri__gte=40000).filter(propri__lte=60000)
        elif filp[0]=='4':
            filteredprod=Products.objects.filter(propri__gte=60000).filter(propri__lte=80000)
        elif filp[0]=='0':
            filteredprod=Products.objects.all()
    
    if filw:
        if filw[0]=='1':
            filteredprod=filteredprod.filter(proamt__gte=1).filter(proamt__lte=5)
        elif filw[0]=='2':
            filteredprod=filteredprod.filter(proamt__gte=5).filter(proamt__lte=10)
        elif filw[0]=='3':
            filteredprod=filteredprod.filter(proamt__gte=10).filter(proamt__lte=15)
    elif filw[0]=='0':
            filteredprod=Products.objects.all()
    if filo:
        if filo[0]=='1':
            filteredprod=filteredprod.filter(profil=1)
        elif filo[0]=='2':
            filteredprod=filteredprod.filter(profil=2)
        elif filo[0]=='3':
            filteredprod=filteredprod.filter(profil=3)
        elif filo[0]=='4':
            filteredprod=filteredprod.filter(profil=4)
        elif filo[0]=='5':
            filteredprod=filteredprod.filter(profil=5)
    elif filo[0]=='0':
            filteredprod=Products.objects.all()
    
    return render(request, 'goldpage/goldpage.html',{'prod':filteredprod,'filp':filp, 'filo':filo,'filw':filw,'filid1':filvalue1})







