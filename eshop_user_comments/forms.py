from django import forms
from django.core import validators


class ContactForm(forms.Form):
    full_name = forms.CharField(
        validators=[validators.MaxLengthValidator(30, 'نام و نام خانوادگی شما نمیتواند بیش از ۳۰ کاراکتر باشد')],
        label='نام و نام خانوادگی',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام و نام خانوادگی'}))

    email = forms.EmailField(
        validators=[validators.MaxLengthValidator(50, 'ایمیل شما نمیتوادن بیشتر از ۵۰ کاراکتر باشد')],
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}))

    subject = forms.CharField(
        label='موضوع',
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'موضوع'}))

    message = forms.CharField(
        label='متن پیام',
        widget=forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'پیام شما'}))
