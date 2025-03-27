from django.shortcuts import render, redirect
from .models import Computer_TXTS
from django.contrib import messages
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required, login_not_required
from django.contrib.auth import logout

@login_not_required
def index(request):    
    computer = Computer_TXTS.objects.all()        
    return render(request, 'computer_index.html',{'computer': computer})

@login_required
def computer_manage(request):
    computer = Computer_TXTS.objects.all()    

    if request.method == 'POST':
        pcname = request.POST['pcname']
        username = request.POST['username']
        userid = request.POST['userid']
        name = request.POST['name']
        phone = request.POST['phone']
        cd = request.POST['cd']
        job = request.POST['job']
        department = request.POST['department']
        buy = request.POST['buy']
        mainboard = request.POST['mainboard']
        cpu = request.POST['cpu']
        ram = request.POST['ram']
        disk = request.POST['disk']
        vga = request.POST['vga']
        monitor = request.POST['monitor']
        note = request.POST['note']


        computer = Computer_TXTS(pcname=pcname,username=username,userid=userid,name=name,phone=phone,cd=cd,job=job,department=department,buy=buy,mainboard=mainboard,cpu=cpu,ram=ram,disk=disk,vga=vga,monitor=monitor,note=note)
        computer.save()
        messages.success(request,'Máy tính đã được thêm thành công!')
        return redirect('/computer/manage')
    
    return render(request, 'computer_manage.html',{'computer': computer})

@login_required
def computer_update(request, pcname):
    computer = Computer_TXTS.objects.get(pcname=pcname)
    if request.method == 'POST':
        pcname = request.POST['pcname']
        computer.username = request.POST['username']
        computer.userid = request.POST['userid']
        computer.name = request.POST['name']
        computer.phone = request.POST['phone']
        computer.cd = request.POST['cd']
        computer.job = request.POST['job']
        computer.department = request.POST['department']
        computer.buy = request.POST['buy']
        computer.mainboard = request.POST['mainboard']
        computer.cpu = request.POST['cpu']
        computer.ram = request.POST['ram']
        computer.disk = request.POST['disk']
        computer.vga = request.POST['vga']
        computer.monitor = request.POST['monitor']
        computer.note = request.POST['note']       
        computer.save()

        messages.success(request,'Cập nhật thành công!')

        return redirect('/computer/manage')     
    return render(request, 'computer_update.html',{
        'computer': computer
    })

@login_required
def computer_delete(request, pcname):
    computer = Computer_TXTS.objects.get(pcname=pcname)
    computer.delete()
    messages.success(request,'Xóa máy tính thành công!')
    return redirect('/computer/manage')

@login_not_required
def computer_view(request, pcname):
    computer = Computer_TXTS.objects.get(pcname=pcname)
    return render(request, 'computer_view.html',{
        'computer': computer
    })
class SiteLoginView(LoginView):
     template_name = 'login.html'
def logout_view(request):
    logout(request)
    return redirect('/computer')