from django.shortcuts import render, redirect
from .models import *
from .forms import computerAdd
from .filters import studFilter
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import studApi
# Create your views here.
def login(req):
	context = {
		'form': computerAdd
	}
	return render(req, 'login.html', context)
def home(req):
	obj = Computer.objects.all()
	noof = Computer.objects.count()
	male = Computer.objects.filter(gender='Male').count()
	female = Computer.objects.filter(gender='FeMale').count()
	context = {
		'data': obj,
		'noof': noof,
		'male': male,
		'female': female
	}
	return render(req, "index.html", context)

def register(req):
	if req.method == 'POST':
		form = computerAdd(req.POST)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {
		'form': computerAdd
	}
	return render(req, 'csregister.html', context)

def updateRegister(req, pid):
	obj = Computer.objects.get(id = pid)
	form = computerAdd(instance=obj)
	if req.method == 'POST':
		form = computerAdd(req.POST, instance=obj)
		if form.is_valid():
			form.save()
			return redirect('home')
	context = {
		'form': form
	}
	return render(req, 'update.html', context)
def deleteRegister(req, pid):
	obj = Computer.objects.get(id=pid)
	obj.delete()
	return redirect('home')

def viewall(req, pid):
	obj = Computer.objects.get(id=pid)
	context = {
		'data': obj
	}
	return render(req, 'viewall.html', context )

def departmet(req):
	title = req.GET.get('dept')
	year = req.GET.get('year')
	obj = Computer.objects.all()
	my = studFilter(req.GET, queryset=obj)
	obj = my.qs
	noof = Computer.objects.count()
	male = Computer.objects.filter(gender='Male').count()
	m = obj.filter(gender='Male').count()
	female = Computer.objects.filter(gender='FeMale').count()
	f = obj.filter(gender='FeMale').count()
	context = {
		'data': obj,
		'noof': noof,
		'male': male,
		'female': female,
		'my': my,
		'm': m,
		'f': f,
		'title': title,
		'year': year
		# 'dept': dept
	}
	return render(req,'dash.html', context)

def dashboard(req):
	return render(req,'choose.html')

class studApiView(APIView):
	def get(self, request, *args, **kwargs):
		obj = Computer.objects.all()
		data1 = studApi(obj, many=True)
		return Response(data1.data)
	def post(self, request):
		pass
# def studApiView(APIView):
# 	obj = Computer.objects.all()
# 	serializer = studApi(obj, many=True)
# 	return Response(serializer.data)


class Testview(APIView):
	def get(self, request, *args, **kwargs):
		data = {
			'name': 'Raja',
			'Age': 22
		}
		return Response(data);