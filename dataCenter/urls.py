"""dataCenter URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from mysite import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index),
    path('admin/', admin.site.urls),
    path('news/', views.news),
    path('show/<int:id>/', views.show),
    path('delete/<int:id>/', views.delete),
    path('edit/<int:id/', views.edit),
    path('rank/', views.rank),
    path('chart/', views.chart),
    path('note/', views.note),
    path('addnote', views.addnote),
    path('logout',views.ulogout),
    path('login/',views.ulogin,name='Login'),
    path('about/',views.about),
    path('register/',views.usignup,name='Register'),
    path('captcha/', include('captcha.urls')), #驗證碼
    path('expenses/', views.expenses, name="Index"),
    path('expenses/up/<str:pk>', views.upexp, name='upexp'),
    path('expenses/del/<str:pk>', views.delexp, name='delexp'),
    path('lotto/', views.getlotto),
    path('plot/',views.sincos),
    path('resetPwd/',views.resetPwd),
    path('photos/upload', views.photos, name='imageUp'),
    path('photos/', views.photosview, name='imageIndex'),
    #path('callback/', views.callback),
]
# 在開發環境要顯示靜態檔案需加上此設定
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)