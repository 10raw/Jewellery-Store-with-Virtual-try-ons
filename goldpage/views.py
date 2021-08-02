
from django import forms

from django.http import request, response
from django.shortcuts import render,redirect,HttpResponseRedirect
from .forms import detailsform
# Create your views here.
from .models import Details, Products,Order,OrderedItems
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
f=0
authusrname=""

def product(request,filvalue):
    if 'username' in request.session:
        print("1111session:::",request.session['username'])
        if request.session['username']=='':
            del request.session['username']
            print("session:::",request.session['username'])
                
        else:
            global authusrname
            authusrname=request.session['username']
    usrnnmm=authusrname
    print("usrnnmm",usrnnmm)
    prod=Products.objects.filter(profil=filvalue)
    return render(request, 'goldpage/goldpage.html', {'prod':prod, 'filid1':filvalue,'usrnnmm':usrnnmm})
   
def showhomepage(request):
    if 'cart' in request.session:
        del request.session['cart']
    if 'username' in request.session:
        print("1111session:::",request.session['username'])
        if request.session['username']=='':
            del request.session['username']
            print("session:::",request.session['username'])
                
        else:
            global authusrname
            authusrname=request.session['username']
    usrnnmm=authusrname
    print("usrnnmm",usrnnmm)
    return render(request, 'allpages/homepage.html',context={'usrnnmm':usrnnmm})
    
class Index(View):
    
    def showprodpage(request,proname1):
        
        context={}
        product=Products.objects.filter(pronm=proname1)
        context={'product':product}
        if request.POST.get:
            
            cart=request.session.get('cart')
            if request.POST.get('addincart'):
                addincart=request.POST.get('addincart')
                print("addincart:::::::::",addincart)
                cart[addincart]+=1
                request.session['cart']=cart
                print("addin cart",cart[addincart])
                redir="/home/prod/"+proname1
                return HttpResponseRedirect(redir)
            if request.POST.get('subfromcart'):
                subfromcart=request.POST.get('subfromcart')
                print("addincart:::::::::",subfromcart)
                cart[subfromcart]-=1
                request.session['cart']=cart
                print("addin cart",cart[subfromcart])
                redir="/home/prod/"+proname1
                return HttpResponseRedirect(redir)
            product=str(request.POST.get('product'))

            print("This ia product:: ",product)
            if cart:
                print("I'm inside if cart is there")
                
                cart[product]=1
            else:
                print("I'm inside if cart is NOT there")
                cart={}
                request.session['cart']=cart
                cart[product]=1
            if 'None' in request.session['cart']:
                del request.session['cart']['None']
            
            request.session['cart']=cart
            print("This is ur cart now: ",request.session.get('cart'))
        if 'username' in request.session:
            print("1111session:::",request.session['username'])
            if request.session['username']=='':
                del request.session['username']
                print("session:::",request.session['username'])
                
                username1=False
            else:
                global authusrname
                authusrname=request.session['username']
                
                username1= request.session['username']
        else:
            print("username is not there in session")
            username1=False
        context['usrnnmm']=username1
        
        print(product)
        usernmm=authusrname
        print("username :::: ",usernmm)
        
        if request.method=='POST':
            form=detailsform(request.POST,request.FILES)
            if 'username' in request.session:
                username1= request.session['username']
                context['usrnnmm']=username1
            if form.is_valid():
                
                if Details.objects.filter(usrname=usernmm).exists():
                    print("I am inside .")
                    y = Details.objects.get(usrname=usernmm)
                    y.usrph=form.cleaned_data['usrph']
                    context['usrfin']= y.usrph
                    # y.save()
                    print(usernmm)
                    print("y :::::",y.usrname)
                    print("already")
                    print("photo",y.usrph)
                    y.save()
                else:
                    newob=Details(usrph=form.cleaned_data['usrph'],usrname=usernmm)
                    newob.save()
                    context['usrfin']=newob.usrph
                    print("new")

                    
            else:
                print("not valid")
            context['form']=form
        else:
            if 'username' in request.session:
                if request.session['username']!='':
                    
                    username1= request.session['username']
                else:
                
                    username1=False
            else:
            
                username1=False
            context['usrnnmm']=username1
            print("not post")
            form=detailsform()
            context['form']=form
            context['login']=f
            context['one']=1
        
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


def signup(request):
    if request.method=='POST':
        formsu=UserCreationForm(request.POST)
        formsi=AuthenticationForm()
        if formsu.is_valid():
            formsu.save()
            return redirect('signin')
    else:
        formsu=UserCreationForm()
        formsi=AuthenticationForm()
    return render(request,'signinup/signinup.html',{'formsu':formsu,'formsi':formsi})

def signin(request):
    
    if request.method=='POST':
        formsi=AuthenticationForm(data=request.POST)
        formsu=UserCreationForm()
        if formsi.is_valid():
            global authusrname
            authusrname=formsi.cleaned_data.get('username')
            global f
            f=1
            request.session['username']=authusrname
            print("session:::",request.session['username'])
            return redirect('home')
    else:
        formsi=AuthenticationForm()
        formsu=UserCreationForm()
    return render(request,'signinup/signinup.html',{'formsi':formsi,'formsu':formsu})

def logout(request):
    if 'username' in request.session:
        del request.session['username']
        if 'cart' in request.session:
            del request.session['cart']
            print("yes it was in cart")
    return render(request,'allpages/homepage.html')

def cart(request):
    context={}
    mycart=request.session.get('cart')
    cartlist=[]
    if 'username' in request.session:
        if request.session['username']=='':
            del request.session['username']
            print("session:::",request.session['username'])          
        else:
            global authusrname
            authusrname=request.session['username']
        loginmessage=" "  
        context['msglogin']=loginmessage
    else:
        loginmessage="You must login"
        context['msglogin']=loginmessage
    # del mycart['total']
    total1=0
    print("mycart",mycart)
    print("authusername",authusrname)
    n=User.objects.get(username=authusrname).id
    print("n:::",n)
    if Order.objects.filter(user_id=n).exists():
        print("The order exists")
        previous=[]
        previous_orders=Order.objects.filter(user_id=n)
        coun=Order.objects.filter(user_id=n).count()
        print(coun)
        if coun >1:
            for k in previous_orders:
                print("prrevious::",k.date_time)
                t=str(k.date_time)
                p=str(k.grand_total)
                s=str(k.delivery_status)
                print("tps::::",t,p,s)
                print(previous)
                previous.append([t,p,s])
                
        else:
            t=str(previous_orders.date_time)
            p=str(previous_orders.grand_total)
            s=str(previous_orders.delivery_status)
            print("tps::::",t,p,s)
            print(previous)
            previous.append([t,p,s])
        context['prev']=previous
    print("Final previous list",previous)

    print(context)
    if mycart:
        
        for i in mycart:
            if i !='total':
                cart=Products.objects.get(proid=int(i))
                cartlist.append([cart.proid,cart.pronm,cart.propri,mycart[i],(cart.propri)*mycart[i]])
                total1=total1+(cart.propri)*mycart[i]
                
                
        tax=total1*3/100
        tot=tax+total1
        request.session['cart']['total']=total1
        request.session.modified=True
        print("total1",total1)
        print("this cart",mycart)
    else:
        tax=0
        tot=0
    context['mycart']=cartlist
    context['total']=total1
    context['tax']=tax
    context['tot']=tot
    return render(request,'cart/cart.html',context)
    

#     from shop.models.cart import CartManager

# cart = CartModel.objects.get_or_create_from_request(request)
# Adding a product to the cart, must be performed by invoking:

# from shop.models.cart import CartItemManager

# cart_item = CartItemManager.get_or_create(
#     cart=cart, product=product, quantity=quantity, **extras)
token=1
def confirmorder(request):
    
    if request.session['username']=='':
        del request.session['username']
        print("session:::",request.session['username'])          
    else:
        global authusrname
        authusrname=request.session['username']
    if request.method=='POST':
        
        print("inside post of order confirm")
        if authusrname!='':
            b=User.objects.get(username=authusrname)
            print("authusrname is not blank")
            if request.session.get('cart'):
                cart=request.session['cart']
                print("To see if total in cart",cart)
                if 'total' in cart:
                    totalt=cart['total']
                    print("cart  have total")
                global token
                token+=1
                order=Order.objects.create(
                    user=b,
                    order_token=authusrname[:2]+str(token),
                    tax=(totalt*3)/100,
                    grand_total=totalt,
                    )
                order.save()
                
                for i in cart:
                    if not i=='total':
                        x=OrderedItems.objects.create(
                            order=order,
                            item_name=Products.objects.get(proid=int(i)).pronm,
                            itemid=int(i),
                            item_price=Products.objects.get(proid=int(i)).propri,
                            order_qty=cart[i],
                            total_price=cart[i]*Products.objects.get(proid=int(i)).propri,)
                        x.save()
        else:
            print("authusrname is blank")
  

    else:
        print("Not inside post")
    return render(request,'confirmorder/confirmorder.html')

def wishlist(request):
    context={}
    msg=""
    if request.method=='POST':
        print("post")
        item=request.POST.get('wishitem')
        if 'wishlist' in request.session:
            wishlist=request.session['wishlist']
            wishlist.append(item)
            request.session['wishlist']=wishlist
            request.session.modified=True
            print("Now session::",request.session.get('wishlist'))
            
        else:
            wishlist=[item]
            request.session['wishlist']=wishlist
            request.session.modified=True
            print("Now session::",request.session.get('wishlist'))
        context['mywishlist']=request.session['wishlist']
    else:
        if 'wishlist' in request.session:
            mywishlist=request.session['wishlist']
            context['mywishlist']=mywishlist
        else:
            msg="Nothing in your wishlist"
            context['msg']=msg
    print("session",request.session.get('wishlist'))
    print("wish::",context)
    return render(request,'wishlist/wishlist.html',context)
