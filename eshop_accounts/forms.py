from django import forms
from django.contrib.auth.models import User


class EditProfile(forms.Form):
    first_name = forms.CharField(
        label='نام ',
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام خود را وارد کنید", "class": "form-control"}))
    last_name = forms.CharField(
        label='نام خانوادگی',
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام خانوادگی خود را وارد کنید", "class": "form-control"}))


class RegisterForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}))
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={"placeholder": "لطفا ایمیل خود را وارد کنید"}))
    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز عبور خود را وارد کنید"}))
    password2 = forms.CharField(
        label='تکرار کلمه ی عبور',
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا مجددا رمز عبور خود را وارد کنید"}))

    def clean_email(self):
        email = self.cleaned_data.get("email")
        qs = User.objects.filter(email=email)
        if qs.exists():
            raise forms.ValidationError("کاربری با این ایمیل در سایت موجود میباشد")
        return email

    def clean_user_name(self):
        user_name = self.cleaned_data.get("user_name")
        qs = User.objects.filter(username=user_name)
        if qs.exists():
            raise forms.ValidationError("کاربری با این ایمیل در سایت موجود میباشد")
        return user_name

    def clean_password2(self):
        password = self.cleaned_data.get("password")
        password2 = self.cleaned_data.get("password2")
        if password != password2:
            raise forms.ValidationError('کلمه های عبور با هم مغایرت دارند')
        return password


class LoginForm(forms.Form):
    user_name = forms.CharField(
        label='نام کاربری',
        widget=forms.TextInput(attrs={"placeholder": "لطفا نام کاربری خود را وارد کنید"}))

    password = forms.CharField(
        label='کلمه ی عبور',
        widget=forms.PasswordInput(attrs={"placeholder": "لطفا رمز عبور خود را وارد کنید"}))
