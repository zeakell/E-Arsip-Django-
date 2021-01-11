from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
# Panggil model dan form
from dapur.forms import SuratMasuk, FSuratKeluar, Disposisii
from dapur.models import Surats, TSuratKeluar, tbl_pejabat, Disposisi, tbl_dispo, tbl_login 
from dapur.decorators import unauthenticated_user, admin_only, analis_only
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from django.db.models import Sum
from datetime import date,datetime,timedelta
from django.db.models.functions import TruncMonth
from random import random,randrange

def tua(request):
    return render(request, "homepage.html", {'name' : 'Harada'})


def berhasil(request):
    return render(request, "aksi.html")

def search(request):
    pk = 123
    hasil_pencarian = Surats.objects.get(nomor_surat=pk)
    return render(request, "userbagum/homeuser3.html", {'search' : str(hasil_pencarian)})



# @login_required(login_url='masuk')
# @admin_only
# @analis_only
def homeuser1(request):
    yy= date.today().year
    w = date.today().month
    z = date.today().day


    boris=[]
    boris1=[]
    boris2=[]
    fatima=[]
    zining=[]

    for i in [1,0]:
        y=yy-i
        boris.append(str(y))
        for x in range(1,13):
            test=Surats.objects.filter(tanggal_surat__year=y,tanggal_surat__month=x).count()
            fatima.append(test)
            test=TSuratKeluar.objects.filter(Tanggal_surat__year=y,Tanggal_surat__month=x).count()
            zining.append(test)
            pass
        boris1.append(fatima)
        boris2.append(zining)
        fatima=[]
        zining=[]
        pass

    a = boris
    b1 = boris1
    b2 = boris2
    c = [[ 'rgba(253, 29, 32, 0.09)' ],[ 'rgba(55, 92, 32, 0.09)' ],[ 'rgba(55, 59, 12, 0.09)' ],[ 'rgba(215, 139, 134, 0.09)' ],[ 'rgba(155, 49, 122, 0.09)' ],[ 'rgba(251, 29, 32, 0.09)' ],[ 'rgba(255, 99, 132, 0.09)' ],[ 'rgba(255, 99, 132, 0.09)' ],[ 'rgba(255, 39, 132, 0.09)' ],[ 'rgba(215, 29, 135, 0.09)' ],[ 'rgba(245, 19, 132, 0.09)' ],[ 'rgba(221, 39, 121, 0.09)' ]]
    d = [[ 'rgba(253, 29, 32, 1)' ],[ 'rgba(55, 92, 32, 1)' ],[ 'rgba(55, 59, 12, 1)' ],[ 'rgba(215, 139, 134, 1)' ],[ 'rgba(155, 49, 122, 1)' ],[ 'rgba(251, 29, 32, 1)' ],[ 'rgba(255, 99, 132, 1)' ],[ 'rgba(255, 99, 132, 1)' ],[ 'rgba(255, 39, 132, 1)' ],[ 'rgba(215, 29, 135, 1)' ],[ 'rgba(245, 19, 132, 1)' ],[ 'rgba(221, 39, 121, 1)' ]]
    e = [1,1,1,1,1,1,1,1,1,1,1,1]

    aa=[]
    bb=[]

    for x in range(0,2):
        datalist = { 
            "label": a[x],
            "data" : b1[x],
            "backgroundColor" : c[x],
            "borderColor" : d[x],
            "borderWidth" : e[x],
        }
        aa.append(datalist)
        pass

    for x in range(0,2):
        datalist = { 
            "label": a[x],
            "data" : b2[x],
            "backgroundColor" : c[x],
            "borderColor" : d[x],
            "borderWidth" : e[x],
        }
        bb.append(datalist)
        pass

    boris = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    cc=[]
    dd=[]
    f1=["Kilat","Express","Biasa"]
    f2=["Umum","Khusus","Kilat"]
    h1=[]
    h2=[]
    for x in range(0,3):
        test=Surats.objects.filter(klasifikasi=f1[x]).count()
        h1.append(test)
        test=TSuratKeluar.objects.filter(Klasifikasi=f2[x]).count()
        h2.append(test)
        pass
    cc=h1
    dd=h2

    return render(request, "userbagum/homeuser.html", {'Jan':boris,'Jan1':f1,'Jan2':f2,'Feb':aa,'Mar':bb,'Apr1':cc,'Apr2':dd})

@login_required(login_url='masuk')
# @admin_only
def homeuser1_a(request):
    startdate = date.today().year
    # enddate = startdate + timedelta(days=7)

    boris=[]

    fatima=[]
    zining=[]
    for x in [5,4,3,2,1,0]:
        y=startdate-x
        boris.append(str(y))
        test=Surats.objects.filter(tanggal_surat__year=y).count()
        fatima.append(test)
        test=TSuratKeluar.objects.filter(Tanggal_surat__year=y).count()
        zining.append(test)
        pass

    a = "Akumulasi Surat 5 Tahun Terakhir"
    b1 = fatima
    b2 = zining
    c = [[ 'rgba(253, 29, 32, 0.09)' ],[ 'rgba(55, 92, 32, 0.09)' ],[ 'rgba(55, 59, 12, 0.09)' ],[ 'rgba(215, 139, 134, 0.09)' ],[ 'rgba(155, 49, 122, 0.09)' ],[ 'rgba(251, 29, 32, 0.09)' ],[ 'rgba(255, 99, 132, 0.09)' ],[ 'rgba(255, 99, 132, 0.09)' ],[ 'rgba(255, 39, 132, 0.09)' ],[ 'rgba(215, 29, 135, 0.09)' ],[ 'rgba(245, 19, 132, 0.09)' ],[ 'rgba(221, 39, 121, 0.09)' ]]
    d = [[ 'rgba(253, 29, 32, 1)' ],[ 'rgba(55, 92, 32, 1)' ],[ 'rgba(55, 59, 12, 1)' ],[ 'rgba(215, 139, 134, 1)' ],[ 'rgba(155, 49, 122, 1)' ],[ 'rgba(251, 29, 32, 1)' ],[ 'rgba(255, 99, 132, 1)' ],[ 'rgba(255, 99, 132, 1)' ],[ 'rgba(255, 39, 132, 1)' ],[ 'rgba(215, 29, 135, 1)' ],[ 'rgba(245, 19, 132, 1)' ],[ 'rgba(221, 39, 121, 1)' ]]
    e = [1,1,1,1,1,1,1,1,1,1,1,1]

    aa=[]
    bb=[]

    for x in range(0,1):
        datalist = { 
            "label": a,
            "data" : b1,
            "backgroundColor" : c[x],
            "borderColor" : d[x],
            "borderWidth" : e[x],
        }
        aa.append(datalist)
        pass

    for x in range(0,1):
        datalist = { 
            "label": a,
            "data" : b2,
            "backgroundColor" : c[x],
            "borderColor" : d[x],
            "borderWidth" : e[x],
        }
        bb.append(datalist)
        pass
    cc=[]
    dd=[]
    f1=["Kilat","Express","Biasa"]
    f2=["Umum","Khusus","Kilat"]
    h1=[]
    h2=[]
    for x in range(0,3):
        test=Surats.objects.filter(klasifikasi=f1[x]).count()
        h1.append(test)
        test=TSuratKeluar.objects.filter(Klasifikasi=f2[x]).count()
        h2.append(test)
        pass

    cc=h1
    dd=h2

    return render(request, "userbagum/homeuser.html", {'Jan':boris,'Jan1':f1,'Jan2':f2,'Feb':aa,'Mar':bb,'Apr1':cc,'Apr2':dd})  

@login_required(login_url='masuk')
# @admin_only
def homeuser1_b(request): #--> Per Hari
    y = date.today().year
    w = date.today().month
    z = date.today().day

    if y%4 == 0:
        v = [31,29,31,30,31,30,31,31,30,31,30,31]
    else:
        v = [31,28,31,30,31,30,31,31,30,31,30,31]
        pass
    
    boris=[]
    boris1=[]
    boris2=[]
    fatima=[]
    zining=[]

    for x in range(1,32):
        boris.append(str(x))
        pass

    for i in range(1,13):
        for x in range(1,v[i-1]+1):
            test=Surats.objects.filter(tanggal_surat__year=y,tanggal_surat__month=i,tanggal_surat__day=x).count()
            fatima.append(test)
            test=TSuratKeluar.objects.filter(Tanggal_surat__year=y,Tanggal_surat__month=i,Tanggal_surat__day=x).count()
            zining.append(test)
            pass
        boris1.append(fatima)
        boris2.append(zining)
        fatima=[]
        zining=[]
        pass

    a = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    b1 = boris1
    b2 = boris2
    c = [[ 'rgba(253, 29, 32, 0.09)' ],[ 'rgba(55, 92, 32, 0.09)' ],[ 'rgba(55, 59, 12, 0.09)' ],[ 'rgba(215, 139, 134, 0.09)' ],[ 'rgba(155, 49, 122, 0.09)' ],[ 'rgba(251, 29, 32, 0.09)' ],[ 'rgba(255, 99, 132, 0.09)' ],[ 'rgba(255, 99, 132, 0.09)' ],[ 'rgba(255, 39, 132, 0.09)' ],[ 'rgba(215, 29, 135, 0.09)' ],[ 'rgba(245, 19, 132, 0.09)' ],[ 'rgba(221, 39, 121, 0.09)' ]]
    d = [[ 'rgba(253, 29, 32, 1)' ],[ 'rgba(55, 92, 32, 1)' ],[ 'rgba(55, 59, 12, 1)' ],[ 'rgba(215, 139, 134, 1)' ],[ 'rgba(155, 49, 122, 1)' ],[ 'rgba(251, 29, 32, 1)' ],[ 'rgba(255, 99, 132, 1)' ],[ 'rgba(255, 99, 132, 1)' ],[ 'rgba(255, 39, 132, 1)' ],[ 'rgba(215, 29, 135, 1)' ],[ 'rgba(245, 19, 132, 1)' ],[ 'rgba(221, 39, 121, 1)' ]]
    e = [1,1,1,1,1,1,1,1,1,1,1,1]

    aa=[]
    bb=[]

    for x in range(0,12):
        datalist = { 
            "label": a[x],
            "data" : b1[x],
            "backgroundColor" : c[x],
            "borderColor" : d[x],
            "borderWidth" : e[x],
        }
        aa.append(datalist)
        pass

    for x in range(0,12):
        datalist = { 
            "label": a[x],
            "data" : b2[x],
            "backgroundColor" : c[x],
            "borderColor" : d[x],
            "borderWidth" : e[x],
        }
        bb.append(datalist)
        pass

    cc=[]
    dd=[]
    f1=["Kilat","Express","Biasa"]
    f2=["Umum","Khusus","Kilat"]
    h1=[]
    h2=[]
    for x in range(0,3):
        test=Surats.objects.filter(klasifikasi=f1[x]).count()
        h1.append(test)
        test=TSuratKeluar.objects.filter(Klasifikasi=f2[x]).count()
        h2.append(test)
        pass

    cc=h1
    dd=h2

    return render(request, "userbagum/homeuser.html", {'Jan':boris,'Jan1':f1,'Jan2':f2,'Feb':aa,'Mar':bb,'Apr1':cc,'Apr2':dd})
  
@login_required(login_url='masuk')
# @admin_only
# @analis_only
def shkotakmasuk(request):
    upload = Surats.objects.all().order_by('-klasifikasi').filter(st_arsip='False')
    # Surats.objects.filter(nomor_surat=pk).update(st_dispo='False')
    return render(request, 'userbagum/kotakmasuk/kotakmasuk.html', {'upload_form': upload})

@login_required(login_url='masuk')
# @admin_only
def sharsip(request):
    upload = Surats.objects.all().order_by('-klasifikasi').filter(st_arsip='True')
    # Surats.objects.filter(nomor_surat=pk).update(st_dispo='False')
    return render(request, 'userbagum/arsip/data_arsip.html', {'upload_form': upload})

@login_required(login_url='masuk')
# @admin_only
def k_sharsip(request):
    tmplsuratkeluar = TSuratKeluar.objects.all().order_by('-Klasifikasi').filter(st_arsip='True')
    #'name' adalah variabel untuk dictonary
    return render(request, 'userbagum/arsip/k_data_arsip.html', {'tmpldata': tmplsuratkeluar})

@login_required(login_url='masuk')
# @admin_only
def arsipkan(request, pk):
    Surats.objects.filter(id=pk).update(st_arsip='True')
    return redirect('shkotakmasuk')
    # return render(request, 'userbagum/kotakmasuk/kotakmasuk.html', {'upload_form': upload})

@login_required(login_url='masuk')
# @admin_only
def k_arsipkan(request, pk):
    TSuratKeluar.objects.filter(id=pk).update(st_arsip='True')
    return redirect('shkotakkeluar')
    # return render(request, 'userbagum/kotakmasuk/kotakmasuk.html', {'upload_form': upload})

@login_required(login_url='masuk')
# @admin_only
def noarsipkan(request, pk):
    Surats.objects.filter(id=pk).update(st_arsip='False')
    return redirect('sharsip')

@login_required(login_url='masuk')
# @admin_only
def k_noarsipkan(request, pk):
    TSuratKeluar.objects.filter(id=pk).update(st_arsip='False')
    return redirect('k_sharsip')

@login_required(login_url='masuk')
@admin_only
def tmbhsurat(request):
    a=tbl_pejabat.objects.all()
    return render(request, 'userbagum/kotakmasuk/tmbhkotak.html', {'aa': a})

@login_required(login_url='masuk')
@admin_only
def kotakmasuk22(request):
    print(request.POST)
    if request.method == 'POST':  
        form = SuratMasuk(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shkotakmasuk')
    else:
        form = SuratMasuk()
    return render(request, 'userbagum/kotakmasuk/kotakmasuk.html')

@login_required(login_url='masuk')
@admin_only
def updatekotakmasuk(request, pk):

    order = Surats.objects.get(id=pk)
    usm = SuratMasuk(instance=order)
    print(request.POST)

    if request.method == 'POST':
        usm = SuratMasuk(request.POST, instance=order)
        if usm.is_valid():
            usm.save()
            return redirect('shkotakmasuk')

    return render(request, 'userbagum/kotakmasuk/UKotakMasuk.html',  {'update_data1':usm})

@login_required(login_url='masuk')
@analis_only
def dis1(request):
    # print(request.POST)
    a=request.POST
    
    pk=a['idsurat']
    print(pk)
    if request.method == 'POST':  
        form = Disposisii(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            pk=Surats.objects.all().filter(id=pk).update(st_dispo='True')
            print(pk)
            return redirect('shkotakmasuk')
        else:
            return redirect('shkotakmasuk')
    else:
        form = Disposisii()
    return render(request, 'userbagum/kotakmasuk/kotakmasuk.html')

@login_required(login_url='masuk')
@analis_only
def canceldis(request,pk):
    Surats.objects.filter(id=pk).update(st_dispo='False')
    a=Surats.objects.filter(id=pk)
    print(a[0])
 
    try:
        book_sel = Disposisi.objects.get(Nomor_Surat=a[0])
    except Disposisi.DoesNotExist:
        return redirect('homeuser1')
    book_sel.delete()
    return redirect('shkotakmasuk')

@login_required(login_url='masuk')
# @admin_only
@analis_only
def dis(request, pk):

    a=tbl_dispo.objects.all()
    b=Surats.objects.filter(id=pk)
    d=pk    
    c=round(a.count()/50,0)+2
    return render(request, 'userbagum/disposisi/data_disposisi.html',  {'bb':b,'aa':a,'cc':c,'dd':d})

@login_required(login_url='masuk')
@admin_only
def shdis2(request, pk):

    a=Surats.objects.filter(id=pk)
    # print(a[0])
    order = Disposisi.objects.get(Nomor_Surat=a[0])
    usm = Disposisii(instance=order)
    # print(usm)
    g="bagum"
    p=pk
    # print(request.POST)

    # if request.method == 'POST':
    #     usm = SuratMasuk(request.POST, instance=order)
    #     if usm.is_valid():
    #         usm.save()
    #         return redirect('shkotakmasuk')

    return render(request, 'userbagum/disposisi/sh_disposisi.html',  {'update_data1':usm,'group':g,'pk':p})

@login_required(login_url='masuk')
# @analis_only
def shdis(request, pk):

    a=Surats.objects.filter(id=pk)
    # print(a[0])
    order = Disposisi.objects.get(Nomor_Surat=a[0])
    usm = Disposisii(instance=order)
    # print(usm)
    g="analis"
    p=pk
    # print(request.POST)

    if request.method == 'POST':
        usm = Disposisii(request.POST, instance=order)
        if usm.is_valid():
            usm.save()
            return redirect('shkotakmasuk')

    return render(request, 'userbagum/disposisi/sh_disposisi.html',  {'update_data1':usm,'group':g,'pk':p})

@login_required(login_url='masuk')
@admin_only
def Dkotakmasuk(request, nsurat):
    nsurat = int(nsurat)
    try:
        book_sel = Surats.objects.get(id = nsurat)
    except Surats.DoesNotExist:
        return redirect('homeuser1')
    book_sel.delete()
    return redirect('shkotakmasuk')

@login_required(login_url='masuk')
# @admin_only
def shkotakkeluar(request):
    #render untuk mentriggerkan file htmlnya supaya tampil
    tmplsuratkeluar = TSuratKeluar.objects.all().order_by('-Klasifikasi').filter(st_arsip='False')
    #'name' adalah variabel untuk dictonary
    return render(request, "userbagum/kotakkeluar/kotakkeluar.html", {'tmpldata': tmplsuratkeluar})


@login_required(login_url='masuk')
@admin_only
def tmbhsuratkeluar(request):
    a=tbl_pejabat.objects.all()
    return render(request, 'userbagum/kotakkeluar/tmbh_data_keluar.html', {'aa': a})

@login_required(login_url='masuk')
@admin_only
def svkotakkeluar(request):
    
    if request.method == 'POST':  
        form = FSuratKeluar(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('shkotakkeluar')
        else:
            return redirect('shkotakkeluar')
    else:
        form = FSuratKeluar()

    return render(request, 'userbagum/kotakkeluar/kotakkeluar.html')

@login_required(login_url='masuk')
@admin_only
def updatekotakkeluar(request, nsurat):

    order = TSuratKeluar.objects.get(id=nsurat)
    usk = FSuratKeluar(instance=order)

    if request.method == 'POST':
        usk = FSuratKeluar(request.POST, instance=order)
        if usk.is_valid():
            usk.save()
            return redirect('shkotakkeluar')

    return render(request, 'userbagum/kotakkeluar/UKotakKeluar.html', {'ubahdata':usk})

@login_required(login_url='masuk')
@admin_only
def Dkotakeluar(request, nsurat):
    nsurat = int(nsurat)
    try:
        book_sel = TSuratKeluar.objects.get(id = nsurat)
    except TSuratKeluar.DoesNotExist:
        return redirect('homeuser1')
    book_sel.delete()
    return redirect('shkotakkeluar')

# @login_required(login_url='masuk')
def homeuser2(request):
    return render(request, "analis/homepage.html")

@unauthenticated_user
def regist(request):
    if request.method == 'POST':    
        firstname = request.POST['fn']
        lastname = request.POST['ln']
        username = request.POST['nama']
        password = request.POST['psw']
        email    = request.POST['email']
        if User.objects.filter(username=username).exists():
            messages.info (request,'username taken')
            return redirect('regist')
        elif User.objects.filter(email=email).exists():
            messages.info (request,'email taken')
            return redirect('regist')
        else:
            varuser2 = User.objects.create_user(first_name=firstname, last_name=lastname,  username=username, password=password, email=email)
            varuser2.save()
            print ('user created')
            return redirect('tua')
    else:
        return render(request, 'daftar.html')

@unauthenticated_user
def masuk(request):
    if request.method == 'POST':    
        username=request.POST['nama']
        password=request.POST['psw']
        varuser =auth.authenticate(username=username,password=password)

        if varuser is not None:
            auth.login(request, varuser)
            return redirect('homeuser1')
        else:
            messages.info(request,'invalid credentials')
            return redirect('masuk')
    else:
        return render(request, 'login.html')

def keluar(request):
    auth.logout(request)
    return redirect('masuk')

def a(request):
    return render(request, 'homepage.html')