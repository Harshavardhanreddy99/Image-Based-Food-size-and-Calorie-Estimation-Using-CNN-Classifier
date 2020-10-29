from django.shortcuts import render

from django.http import HttpResponse, request

from django.template import Context

import xlrd


from .models import dataset
from .models import users


def home(request):
	return render(request, 'index.html')

def adminlogin(request):
	if request.method=='POST':
		uid=request.POST['uid']
		pwd=request.POST['pwd']
		
		if uid=='admin' and pwd=='admin':
			request.session['adminid']='admin'
			return render(request, 'admin_home.html')

		else:
			return render(request, 'admin.html',{'msg':"Login Fail"})

	else:
		return render(request, 'admin.html')

def adminhome(request):
	if "adminid" in request.session:
		uid=request.session["adminid"]
		return render(request, 'admin_home.html')

	else:
		return render(request, 'admin.html')

def adminlogout(request):
	try:
		del request.session['adminid']
	except:
		pass
	return render(request, 'admin.html')	
	
def uploaddataset(request):
	if "adminid" in request.session:
		
		return render(request, 'upload.html')

	else:
		return render(request, 'admin.html')

def xlupload(request):
	if "adminid" in request.session:
		file=request.POST['file']
		book = xlrd.open_workbook(file)
		sheet = book.sheet_by_index(0)
		dataset.objects.all().delete()
		for r in range(1, sheet.nrows):
			f0 = sheet.cell(r, 0).value
			f1 = sheet.cell(r, 1).value
			d=dataset(name=f0, calorie=f1)
			d.save()
		return render(request, 'upload.html',{'msg':"Dataset Uploaded Successfully"})
	else:
		return render(request, 'admin.html')

def viewdataset(request):
	if "adminid" in request.session:
		data=dataset.objects.all()
		return render(request, 'viewdataset.html',{'data':data})
		
	else:
		return render(request, 'admin.html')

def signupaction(request):
	if request.method=='POST':
		email=request.POST['mail']
		pwd=request.POST['pwd']
		
		tele=request.POST['tele']
		name=request.POST['name']
		
		city=request.POST['city']

		
		d=users.objects.filter(email__exact=email).count()
		if d>0:
			return render(request, 'signup.html',{'msg':"Email Already Registered"})
		else:
			d=users(name=name,email=email,tele=tele,city=city,pwd=pwd)
			d.save()
			return render(request, 'signup.html',{'msg':"Register Success, You can Login.."})
	else:

		return render(request, 'signup.html')

def userlogin(request):
	if request.method=='POST':
		uid=request.POST['mail']
		pwd=request.POST['pwd']
		d=users.objects.filter(email__exact=uid).filter(pwd__exact=pwd).count()
		
		if d>0:
			d=users.objects.filter(email__exact=uid)
			request.session['email']=uid
			return render(request, 'user_home.html',{'data': d[0]})

		else:
			return render(request, 'userlogin.html',{'msg':"Login Fail"})

	else:

		return render(request, 'userlogin.html')



def userhome(request):
	if "email" in request.session:
		uid=request.session["email"]
		d=users.objects.filter(email__exact=uid)
		return render(request, 'user_home.html',{'data': d[0]})

	else:
		return render(request, 'userlogin.html')

def userlogout(request):
	try:
		del request.session['email']
	except:
		pass
	return render(request, 'userlogin.html')	
	
def getcalories(request):
	if "email" in request.session:
		
		return render(request, 'uploadimage.html')

	else:
		return render(request, 'userlogin.html')
