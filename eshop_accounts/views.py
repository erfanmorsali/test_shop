from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.shortcuts import render, redirect
from .forms import LoginForm, RegisterForm, EditProfile
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.models import User


# Create your views here.


def login_page(request):
    if request.user.is_authenticated:
        return redirect("/")
    message = messages.get_messages(request)
    login_form = LoginForm(request.POST or None)
    context = {
        "login_form": login_form,
        "message": message
    }
    if login_form.is_valid():
        user_name = login_form.cleaned_data.get("user_name")
        password = login_form.cleaned_data.get("password")
        user = authenticate(request, username=user_name, password=password)
        if user is not None:
            login(request, user)
            message = messages.success(request, "شما با موفقت وارد شدید")
            context["login_form"] = LoginForm()
            if request.user.is_superuser:
                return redirect("/admin")
            else:
                return redirect("/")
        else:
            login_form.add_error("user_name", "کاربری با این مشخصات یافت نشد")
    return render(request, "login.html", context)


def register_page(request):
    if request.user.is_authenticated:
        return redirect('/')
    register_form = RegisterForm(request.POST or None)
    context = {
        'register_form': register_form
    }
    if register_form.is_valid():
        username = register_form.cleaned_data.get("user_name")
        email = register_form.cleaned_data.get("email")
        password = register_form.cleaned_data.get("password")
        newuser = User.objects.create_user(username=username, email=email, password=password)
        context["register_form"] = RegisterForm()
        messages.success(request, 'ثبت نام با موفقیت انجام شد')
        return redirect('/login')
    return render(request, 'register.html', context)


def log_out(request):
    logout(request)
    messages.success(request, "شما با موفقیت خارج شدید")
    return redirect("/login")


@login_required(login_url="/login")
def user_profile(request):
    message = messages.get_messages(request)
    return render(request, 'user_profile.html', {"message" : message})


def edit_profile(request):
    user = User.objects.get(id=request.user.id)
    if user is None:
        raise Http404("کاربری با این مشخصات وجود ندارد")
    edit_profile_form = EditProfile(request.POST or None,
                                    initial={"first_name": user.first_name, "last_name": user.last_name })
    if edit_profile_form.is_valid():
        first_name = edit_profile_form.cleaned_data.get("first_name")
        last_name = edit_profile_form.cleaned_data.get("last_name")
        password = edit_profile_form.cleaned_data.get("password")
        user.first_name = first_name
        user.last_name = last_name
        user.save()
        messages.success(request,"اطلاعات با موفقت ویرایش شد")
        return redirect("/user_profile")
    context = {
        "edit_profile_form" : edit_profile_form
    }
    return render(request, "edit_profile.html", context)
