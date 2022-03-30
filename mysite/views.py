from . import models
from django.shortcuts import render,redirect
from django.http import HttpResponse, HttpResponseBadRequest, HttpResponseForbidden
from django.views.generic import View
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout #django的登入權限,登入登出模組
from django.contrib.auth.decorators import login_required #載入模組以管控登入前後權限
from django.contrib.auth.forms import UserCreationForm #載入模組初始化UserCreationForm表單
from mysite.models import Post,Country,City,Note #呼叫mysite資料夾下的資料庫models.py 呼叫Post,Country,City類別取得資料
from mysite.models import Expense,User,Photo
from django.contrib.auth.models import User
#Profile,
from mysite.forms import ExpenseModelForm,RegisterForm,LoginForm,UploadModelForm #載入forms.py的表單們
from django.contrib.sessions.models import Session
import os
from django.conf import settings
from pathlib import Path
from PIL import Image

import hashlib
import random
from plotly.offline import plot
import plotly.graph_objs as go
import numpy as np
#from django.views.decorators.csrf import csrf_exempt
#from django.conf import settings
#from linebot import LineBotApi, WebhookParser
#from linebot.exceptions import InvalidSignatureError, LineBotApiError
#from linebot.models import MessageEvent, TextSendMessage

#所有request和取出database在此撰寫

def hash_code(s, salt='East'): #Hash
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())  # update方法只接收bytes类型
    return h.hexdigest()

def index(request): #首頁
	if 'user_name' in request.session:
		user_name = request.session['user_name']
	else:
		user_name = "訪客"
	return render(request, "index.html", locals())

def news(request): #文章列表顯示
	posts = Post.objects.all()
	return render(request, "news.html", locals())

@login_required(login_url="/login/") #未登入就要求登入
def show(request, id): #文章內容
	try:
		post = Post.objects.get(id=id) #找出符合條件的第一個紀錄
		#posts = Post.objects.filter(id=id) #找出符合條件的所有紀錄
	except:
		return redirect("/news")
	return render(request, "show.html", locals())

def rank(request): #排序資料
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


def chart(request): #CHART圖表
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

def ulogout(request): #登出
	Session.objects.all().delete() #刪除session
	logout(request) #django logout模組的登出方法
	return redirect('/') #返回根目錄

def delete(request,id): #刪除文章
	try:
		post = Post.objects.get(id=id)
		post.delete()
		return redirect('/news')
	except:
		return redirect('/news')

def ulogin(request): #登入
	form = LoginForm()
	if request.method == "POST":
		username = request.POST.get("username")
		password = request.POST.get("password")
		if username == "admin":
			user = authenticate(request, username=username, password=password)
			login(request,user)
			return render(request,'index.html',locals())
		else:
			hash_pwd = hash_code(password)
		try:
			user = models.User.objects.get(username=username) #登入自設會員
			if user.password == hash_pwd:
				request.session['is_login'] = True
				request.session['user_name'] = user.username
				user = authenticate(request, username=username, password=hash_pwd) #驗證會員
				if user is not None: #此帳號存在
					login(request, user) #登入後台成功
				else:
					User.objects.create_user(username, email, hash_code(password1)) #在後台建立帳號
				return render(request,'index.html',locals())
			if user.password != hash_pwd:
				message = '帳號密碼有誤，請再次確認！'
		except:
			message = "無效的使用者名稱。"
		return render(request, 'login.html', locals())
	else: #不是POST來的
		message = '請輸入帳號、密碼、圖形驗證碼。'
	login_form = LoginForm()
	context = {
        'form': form
    }
	return render(request, 'login.html', locals())

def usignup(request): #註冊
	form = RegisterForm()
	if request.method == "POST":
		username = request.POST.get("username")
		password1 = request.POST.get("password1")
		password2 = request.POST.get("password2")
		email = request.POST.get("email")
		if password1 != password2:
			message = "第二次輸入的密碼應與密碼一致！"
			return render(request, 'register.html', locals())
		if models.User.objects.filter(username=username):
			message = "此使用者名稱已經被註冊"
			return render(request, 'register.html', locals())
		if models.User.objects.filter(email=email):
			message = '此電子信箱已經被使用'
			return render(request, 'register.html', locals())
		new_user = models.User.objects.create() #創建新物件 自訂使用者帳號
		new_user.username = username
		new_user.password = hash_code(password1) #密碼加密
		new_user.email = email
		new_user.save() #儲存
		User.objects.create_user(username, email, hash_code(password1)) #創建管理後台使用者帳號
		return redirect('/login')  #成功後重新導向到登入畫面
	context = {
		'form': form
	}
	return render(request, 'register.html', context)

def resetPwd(request): #重置密碼
	return render(request, 'resetPwd.html', context)

@login_required(login_url="/login") #未登入就要求登入
def edit(request,id): #編輯文章
	try:
		post = Post.objects.get(id=id)
	except:
		return redirect('/news')

@login_required(login_url="/login") #未登入就要求登入
def note(request): #留言板
	notes = Note.objects.all()
	return render(request, 'note.html', locals())

def addnote(request): #新增留言
	if request.method=='POST':
		title = request.POST["title"]
		if len(title)>1:
			note = Note(title=title)
			note.save()
			
		return redirect('/note')

def about(request): #我的履歷
	notes = Note.objects.all()
	return render(request, 'about.html', locals())

def photosview(request): #作品集顯示
	photos = Photo.objects.all()  #查詢所有資料
	context = {
		'photos': photos,
	}
	return render(request, 'photos/index.html', context)

def photos(request): #作品集上傳
	form = UploadModelForm()
	if request.method == "POST":
		form = UploadModelForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/photos')
		else:
			print("error")
	return render(request, 'photos/upload.html', locals())

@login_required(login_url="/login") #未登入就要求登入
def expenses(request): #記帳表
    expenses = Expense.objects.all()  # 查詢所有資料
    form = ExpenseModelForm()
    if request.method == "POST":
        form = ExpenseModelForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("/expenses")
    context = {
        'expenses': expenses,
        'form': form
    }
    return render(request, 'expenses/index.html', context)

def upexp(request, pk): #更新記帳紀錄
    expense = Expense.objects.get(id=pk)
    form = ExpenseModelForm(instance=expense)
    if request.method == 'POST':
        form = ExpenseModelForm(request.POST, instance=expense)
        if form.is_valid():
            form.save()
        return redirect('/expenses')
    context = {
        'form': form
    }
    return render(request, 'expenses/up.html', context)

def delexp(request, pk): #刪除記帳紀錄
    expense = Expense.objects.get(id=pk)
    if request.method == "POST":
        expense.delete()
        return redirect('/expenses')
    context = {
        'expense': expense
    }
    return render(request, 'expenses/del.html', context)

def getlotto(request): #隨機樂透
	lotto = [random.randint(1,42) for i in range(6)]
	sp = lotto[5]
	lotto = lotto[0:4]
	return render(request, "lotto.html", locals())

def sincos(request): #印出動態圖表PLOTLY
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
	return render(request, "plot.html", locals())

##line
#line_bot_api = LineBotApi(settings.LINE_CHANNEL_ACCESS_TOKEN)
#parser = WebhookParser(settings.LINE_CHANNEL_SECRET)
#@csrf_exempt
#def callback(request):
#    if request.method == 'POST':
#        signature = request.META['HTTP_X_LINE_SIGNATURE']
#        body = request.body.decode('utf-8')
#        try:
#            events = parser.parse(body, signature)  # 傳入的事件
#        except InvalidSignatureError:
#            return HttpResponseForbidden()
#        except LineBotApiError:
#            return HttpResponseBadRequest()
 
#        for event in events:
#            if isinstance(event, MessageEvent):  # 如果有訊息事件
#                line_bot_api.reply_message(  # 回復傳入的訊息文字
#                    event.reply_token,
#                    TextSendMessage(text=event.message.text)
#                )
#        return HttpResponse()
#    else:
#        return HttpResponseBadRequest()