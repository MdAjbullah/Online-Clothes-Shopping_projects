from django.shortcuts import render,redirect
from shop.models import NewRegister,NewProduct,AddOffer,user1,Rating
from django.core.files.storage import FileSystemStorage
from django.conf.urls.static import static
def home(request):
    return render(request,'template/index.html')
def createaccount(request):
  return render(request,'template/createaccount.html')
def loginform(request):
    return render(request,'template/login.html')
def logindata(request):
  if request.method=="POST":
        Email=request.POST['Email']
        Password=request.POST['Password']
        if Email=="admin@gmail.com" and Password=="admin":
             request.session['admin']=Email
             return redirect("/admin1/")
        else:
            user=NewRegister.objects.filter(email=Email,password=Password).count()
            if(user==0):
                msg="No data"
                return render(request,"template/msg1.html",{"msg":msg})
            else:
                request.session['Email']=Email
                return redirect("/user/")
  else:
          return render(request,'template/login.html')

def admin1(request):
    if request.session.has_key('admin'):
        Email=request.session['admin']
        return render(request,"template/admin.html",{"usetrname":Email})
    else:
        return redirect('/login/')
def addproduct(request):
    return render(request,'template/productadd.html')
def registerproduct(request):
  if request.method=="POST":
    a=request.POST['t1'];
    b=request.POST['t2'];
    c=request.POST['t3'];
    d=request.POST['t4'];
    e=request.POST['t5'];
    f=request.POST['t6'];
    g=request.POST['t7'];
    h=request.FILES['t8'];
    data=NewProduct(category=a,productname=b, productprice=c, featureofproduct=d, size=e , color=f ,productid=g,image=h)
    data.save()
    return redirect('/showproduct/')
  else:
    return redirect('/addproduct/')
def showproduct(request):
    data=NewProduct.objects.all()
    return render(request,'template/showproduct.html',{"alldata":data})
def deletepro(request,pk):
    id=pk
    NewProduct.objects.filter(p_id=id).delete()
    return redirect('/showproduct/')
def showuser(request):
    data=NewRegister.objects.all()   
    return render(request,'template/showuser.html', {"alldata":data})
def logout(request):
    if request.session.has_key('email'):
        del request.session['email']
    if request.session.has_key('admin'):
        del request.session['admin']
    return redirect("/login/")
def registerdata(request):
  if request.method=="POST":
    a=request.POST['t1']
    b=request.POST['t2']
    c=request.POST['t3']
    d=request.POST['t4']
    e=request.FILES['t5']
    data=NewRegister(user=a, email=b, password=c, cpassword=d,image=e)
    data.save()
    request.session['Email']=b
    return redirect("/user/")
  else:
    return redirect("/login/")
def user(request):
    if request.session.has_key('Email'):
        Email=request.session['Email']
        return render(request,"template/user.html",{"usetrname":Email})
    else:
        return redirect('/login/')
def deleteuser(request,pk):
    id=pk
    NewRegister.objects.filter(p_id=id).delete()
    return redirect('/showuser/')
def myordershow(request):
    data=user1.objects.all()
    return render(request,'template/myordershow.html',{"alldata":data})
def addoffer(request):
     return render(request,'template/addoffer.html')
def addofferdata(request):
  if request.method=="POST":
    a=request.POST['t1']
    b=request.POST['t2']
    c=request.POST['t3']
    d=request.POST['t4']
    e=request.POST['t5']
    data=AddOffer(Nameofoffer=a, Typeofoffer=b, Startingdate=c, Endingdate=d,message=e)
    data.save()
    msg="Data is register"
    return render(request,'template/msg1.html',{"abc":msg})
  else:
    return render(request,'template/addoffer.html')
def showoffer(request):
    data=AddOffer.objects.all()
    return render(request,'template/showoffer.html',{"alldata":data})

def deleteoffer(request,pk):
    id=pk
    AddOffer.objects.filter(p_id=id).delete()
    return redirect('/showoffer/')
def usershowproduct(request):
    data=NewProduct.objects.all()
    Email=request.session['Email']
    user=NewRegister.objects.filter(email=Email).all()
    return render(request,'template/usershowproduct.html',{"alldata":data,"alldata2":user})
def final(request):
  if request.method=="POST":
    a=request.POST['t1'];
    b=request.POST['t2'];
    c=request.POST['t3'];
    d=request.POST['t4'];
    e=request.POST['t5'];
    f=request.POST['t6'];
    g=request.POST['t7'];
    h=request.POST['t8'];
    i="Pending"
    data=user1(Productid=a, productname=b, category=c, productid2=d , image=e ,userid=f,email=g ,name=h,status=i)
    data.save()
    return redirect("/userorder/")
  else:
    return render(request,'template/productadd.html')
def myordershow(request):
    data=user1.objects.all()
    return render(request,'template/myordershow.html',{"alldata":data})
def updatestatus(request,pk):
    id=pk
    user1.objects.filter(p_id=id).update(status="BOOKED")
    return redirect('/myordershow/')
def deleteorder(request,pk):
    id=pk
    user1.objects.filter(p_id=id).delete()
    return redirect('/myordershow/')
def userorder(request):
    Email=request.session['Email']
    data=user1.objects.filter(email=Email).all()
    return render(request,'template/userorder.html',{"alldata":data})
def accountsetting(request):
    Email=request.session['Email']
    print("Name :- ",Email)
    data=NewRegister.objects.filter(email=Email).all()
    return render(request,'template/accountsetting.html',{"alldata":data})
def accountsetting1(request):
  if request.method=="POST":
    a=request.POST['t1'];
    b=request.POST['t11'];
    data=NewRegister.objects.filter(email=b).update(password=a)
    msg="Password changed"
    data=NewRegister.objects.filter(email=b).all()
    return render(request,'template/accountsetting.html',{"alldata":data,"abc":msg})
  else:
    return render(request,'template/accountsetting.html')
def showdetail(request,pk):
    id=pk
    data=NewProduct.objects.filter(p_id=id).all()
    Email=request.session['Email']
    user=NewRegister.objects.filter(email=Email).all()
    rating=Rating.objects.filter(Productid=id).all()
    return render(request,'template/showdetail.html',{"alldata":data,"alldata2":user,"alldata3":rating})
def saverating(request):
  if request.method=="POST":
    a=request.POST['t1'];
    b=request.POST['t2'];
    c=request.POST['t3'];
    d=request.POST['t4'];
    e=request.POST['t5'];
    f=request.POST['t6'];
    data=Rating(Productid=d, name=a, email=b, image=c , comment=e ,rating=f)
    data.save()
    return redirect("/usershowproduct/")
  else:
    return render(request,'template/productadd.html')
def deletemyproduct(request,pk):
    id=pk
    user1.objects.filter(p_id=id).delete()
    return redirect('/userorder/')
