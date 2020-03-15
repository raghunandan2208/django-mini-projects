from django.shortcuts import render
import random
import qrcode

# Create your views here.
otp = 0
def loginPage(request):
    return render(request, "qrauth/login.html")

def validateuser(request):
    username = request.POST.get("t1")
    password = request.POST.get("t2")

    if username == "raghu" and password == "123456":
        rno = random.randint(100000,999999)
        global otp
        otp = rno
        qr_img = qrcode.make("OTP is: " + str(rno))
        qr_img.save(r"qrauth/static/qrimages/qrcode_img.jpg")
        return render(request, "qrauth/qrcode_page.html")
    else:
        return render(request, "qrauth/login.html",{"message": "Invalid User"})

def validateOTP(request):
    user_otp = request.POST.get("otp")
    if user_otp == str(otp):
        return render(request, "qrauth/welcome.html")
    else:
        return render(request, "qrauth/login.html",{"message": "Invalid OTP"})
