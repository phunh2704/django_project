from django.shortcuts import render, redirect
from .models import Computer
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, login_not_required
from django.contrib.auth import logout

@login_not_required
def index(request):    
    computer = Computer.objects.all()
    if request.method == 'POST':
        pcname = request.POST['pcname']
        username = request.POST['username']
        userid = request.POST['userid']
        name = request.POST['name']
        job = request.POST['job']
        department = request.POST['department']
        note = request.POST['note']

        computer = Computer(pcname=pcname,username=username,userid=userid,name=name,job=job,department=department,note=note)
        computer.save()
        messages.success(request,'Máy tính đã được thêm thành công!')
        return redirect('/')
    
    return render(request, 'computer_index.html',{'computer': computer})

@login_required
def computer_manage(request):
    computer = Computer.objects.all()    

    if request.method == 'POST':
        pcname = request.POST['pcname']
        username = request.POST['username']
        userid = request.POST['userid']
        name = request.POST['name']
        job = request.POST['job']
        department = request.POST['department']
        note = request.POST['note']


        computer = Computer(pcname=pcname,username=username,userid=userid,name=name,job=job,department=department,note=note)
        computer.save()
        messages.success(request,'Máy tính đã được thêm thành công!')
        return redirect('/computer/manage')
    
    return render(request, 'computer_manage.html',{'computer': computer})

@login_required
def computer_update(request, pcname):
    computer = Computer.objects.get(pcname=pcname)
    if request.method == 'POST':
        pcname = request.POST['pcname']
        computer.username = request.POST['username']
        computer.userid = request.POST['userid']
        computer.name = request.POST['name']
        computer.job = request.POST['job']
        computer.department = request.POST['department']
        computer.note = request.POST['note']       
        computer.save()

        messages.success(request,'Cập nhật thành công!')

        return redirect('/computer/manage')
    return render(request, 'computer_update.html',{
        'computer': computer
    })

@login_required
def computer_delete(request, pcname):
    computer = Computer.objects.get(pcname=pcname)
    computer.delete()
    messages.success(request,'Xóa máy tính thành công!')
    return redirect('/computer/manage')

@login_not_required
def computer_view(request, pcname):
    computer = Computer.objects.get(pcname=pcname)
    return render(request, 'computer_view.html',{
        'computer': computer
    })
class SiteLoginView(LoginView):
     template_name = 'login.html'
def logout_view(request):
    logout(request)
    return redirect('/computer')