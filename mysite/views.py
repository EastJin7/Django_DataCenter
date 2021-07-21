from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import logout #django的logout模組
from django.contrib.auth.decorators import login_required #載入模組以管控登入前後權限
from mysite.models import Post,Country,City,Note #呼叫mysite資料夾下的資料庫models.py 呼叫Post,Country,City類別取得資料
import random
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np

#所有request和取出database在此撰寫
def index(request):
	name = '東方'
	lotto = [random.randint(1,42) for i in range(6)]
	sp = lotto[5]
	lotto = lotto[0:4]

	x = np.linspace(0, 13*np.pi, 360)
	y1 = np.sin(x)
	y2 = np.cos(x)
	plot_div = plot([go.Scatter(x=x, y=y1,
		mode='lines', name='SIN', text="Title",
		opacity=0.8, marker_color='blue'),
		go.Scatter(x=x, y=y2,
		mode='lines', name='COS', 
		opacity=0.8, marker_color='red')],
		output_type='div')
	return render(request, "index.html", locals())

def news(request):
	posts = Post.objects.all()
	return render(request, "news.html", locals())

@login_required(login_url="/admin/login/") #未登入就要求登入
def show(request, id):
	try:
		post = Post.objects.get(id=id) #找出符合條件的第一個紀錄
		#posts = Post.objects.filter(id=id) #找出符合條件的所有紀錄
	except:
		return redirect("/news")
	return render(request, "show.html", locals())

@login_required(login_url="/admin/login/") #未登入就要求登入
def rank(request):
	if request.method == 'POST':
		country_id = request.POST["get_countryid"] #將從POST方法來的get_countryid值存為country_id
		try:
			country = Country.objects.get(id=country_id) #取出Country物件中id等於country_id的物件作為local變數country
		except:
			return redirect("/rank")
		cities = City.objects.filter(country=country).order_by('-population')
	else:
		cities = City.objects.all()
	countries = Country.objects.all()
	return render(request, 'rank.html', locals())

@login_required(login_url="/admin/login/") #未登入就要求登入
def chart(request):
	if request.method == 'POST':
		country_id = request.POST["get_countryid"] #將從POST方法來的get_countryid值存為country_id
		try:
			country = Country.objects.get(id=country_id) #取出Country物件中id等於country_id的物件作為local變數country
		except:
			return redirect("/chart")
		cities = City.objects.filter(country=country)
	else:
		cities = City.objects.all()
	countries = Country.objects.all()
	return render(request, 'chart.html', locals())

def ulogout(request):
	logout(request) #django logout模組的登出方法
	return redirect('/') #返回根目錄

def delete(request,id):
	try:
		post = Post.objects.get(id=id)
		post.delete()
		return redirect('/news')
	except:
		return redirect('/news')


def edit(request,id):
	try:
		post = Post.objects.get(id=id)
	except:
		return redirect('/news')

def note(request):
	notes = Note.objects.all()
	return render(request, 'note.html', locals())

def addnote(request):
	if request.method=='POST':
		title = request.POST["title"]
		if len(title)>1:
			note = Note(title=title)
			note.save()
		return redirect('/note')