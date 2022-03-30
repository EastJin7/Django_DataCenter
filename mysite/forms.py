from django import forms
from django.contrib.auth.forms import UserCreationForm #預設的註冊表單
from django.contrib.auth.models import User #預設的使用者
from mysite.models import Expense,Photo
from captcha.fields import CaptchaField, CaptchaTextInput #圖形驗證碼表單

class RegisterForm(UserCreationForm):
    username = forms.CharField(
        label="帳號",
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    password1 = forms.CharField(
        label="密碼",
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    password2 = forms.CharField(
        label="密碼確認",
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )
    email = forms.EmailField(
        label="電子郵件",
        widget=forms.EmailInput(attrs={'class': 'form-control'})
    )
    class Meta:
        model = User
        fields = ('username', 'password1', 'password2','email')

class LoginForm(forms.Form):
    username = forms.CharField(
        label="帳號",
        max_length=16,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': "Username",'autofocus': ''})
    )
    password = forms.CharField(
        label="密碼",
        max_length=32,
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': "Password"})
    )
    #captcha = CaptchaField(
    #    label="圖形驗證碼", widget=CaptchaTextInput(attrs={'class': 'form-control'})
    #)

class ExpenseModelForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'})
        }
        labels = {
            'name': '花費項目',
            'price': '金額'
        }

class UploadModelForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields =['pictitle', 'piccontent', 'image']
        #, 'upload_date'
        widgets = {
            'pictitle':forms.TextInput(attrs={'class': 'form-control'}),
            'piccontent':forms.TextInput(attrs={'class': 'form-control','style': 'height: 200px'}),
            'image': forms.FileInput(attrs={'class': 'form-control-file'})
            }
        labels = {
            'pictitle': '作品名稱',
            'piccontent': '說明',
            'image': '選擇檔案',
            'upload_date': '上傳日期',
        }