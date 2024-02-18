from django.shortcuts import render,redirect
from mysqlapp.models import Employee
from django.contrib.auth.models import User
# Create your views here.
def home_view(request):
    employees=Employee.objects.all()
    # mydict={'employees':employees}
    return render(request,'result.html',{'employees':employees})

def register_view(request):
    msg=''
    if request.method=='POST':
        eno=request.POST['eno']
        ename=request.POST['ename']
        esal=request.POST['esal']
        emobile=request.POST['emobile']
        eemail=request.POST['eemail']
        eaddress=request.POST['eaddress']
        user=Employee.objects.get_or_create(eno=eno,ename=ename,esal=esal,emobile=emobile,eemail=eemail,eaddress=eaddress)
        if user is not None:
            msg='Employee created successfully'
            return render(request,'register.html',{'msg':msg})
        else:
            msg='unable to create employee record'
    else:
        return render(request,'register.html',{'msg':msg})
