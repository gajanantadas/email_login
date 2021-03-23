from django.shortcuts import render,redirect
from .models import User
from.forms import RegistrationForm
login=False
# Create your views here.
def registration(request):
    if request.method=='GET':
        form=RegistrationForm()
    elif request.method=='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            fn=form.cleaned_data['fname']
            ln=form.cleaned_data['lname']
            mail=form.cleaned_data['email']
            ps=form.cleaned_data['conform_password']
            obj = User(fname=fn, lname=ln, email=mail, pword=ps)
            obj.save()
            return redirect('login')
    return render(request, 'webapp/registration.html', {'form':form})
def Userlogin(request):
    if request.method =='GET':
        return render(request, 'webapp/login.html')
    else :
        un=request.POST.get('email')
        pw=request.POST.get('Password')
        data=User.objects.all().values('pword','email')
        password=[n['pword'] for n in data]
        username=[n['email'] for n in data]
        if un in username:
            i = username.index(un)
            if pw == password[i]:
                global login
                login=True
                #return redirect('home')
                return render(request,'webapp/index.html',{'un':un,'login':login})
            else:
                msg='invalid user and password please try agian'
                return render(request, 'webapp/login.html', {'msg': msg})
        else:
            msg='Username invalid please make sure and try again'
            return render(request, 'webapp/login.html', {'msg': msg})
def view1(request):
    return render(request, 'webapp/index.html', {'login':login})
def logout(request):
    global login
    login=False
    return redirect('login')
