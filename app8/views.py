from django.shortcuts import render, HttpResponse
def index(request):
    return render(request,"form.html")
def disp(request):
    #info=[request.POST.get("firstname"),request.POST.get("lastname"),request.POST.get("emailid"),request.POST.get("emailid"),int(request.POST.get("day")),request.POST.get("month"),int(request.POST.get("year")),request.POST.get("male"),request.POST.get("female"),request.POST.get("address"),request.POST.get("city"),int(request.POST.get("pincode"))]
    info={
        "username":request.POST.get("username"),
        "email":request.POST.get("email"),
        "password":request.POST.get("password"),
        "confirm_password":request.POST.get("confirm_password"),
    }
    
    return render(request,"show.html",info)