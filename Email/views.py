from django.shortcuts import render,redirect
from django.core.mail import send_mail,EmailMessage
from .forms import *
from django.core.files.storage import FileSystemStorage
import qrcode

def generateQR(request):
    form = QRForm(request.POST or None)
    context = {
        "form":form
    }

    if form.is_valid():
        filename = form.cleaned_data.get("Name")
        data = 'http://127.0.0.1:8000/' + filename
        conversion_status = True
        context["conversion_status"] = conversion_status
        qr = qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)   
        qr.add_data(data)     
        qr.make(fit=True)
        img = qr.make_image(fill_color="black", back_color="white")
        context["data"] = data
        context["filename"] = filename
        return render(request,"success.html",context)       
    # print("invalid")
    return render(request,'form.html',context)

def index(request,username):    
    form = EmailForm(request.POST or None)
    context = {
        "form":form,
        "username":username
    }
    print(username)
    if form.is_valid():
        sub = 'hello from abhishek!'
        mes = 'hello this is message'
        host = 'vitkabaap@gmail.com'
        rec = form.cleaned_data.get("email")
        mail = EmailMessage(sub, mes, host,[rec])
        path = 'media/' + username +".pdf"
        print("path from index fn is: ",path)
        f = open(path)
        mail.attach_file(path)
        mail.send()
        f.close()
        conversion_status = True
        context["conversion_status"] = conversion_status
        context["rec"] = rec
        return render(request,'index.html',context)
    return render(request,'form.html',context)

def success(request):
    return render(request,'index.html')
    
