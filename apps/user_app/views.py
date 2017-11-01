from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import User
# from ..wish_app.models import Join
from django.contrib import messages

def index(request):
    # User.userManager.all().delete()
    # Quote.quoteManager.all().delete()
    # Join.objects.all().delete()
    return render(request, 'user_app/index.html')

def register(request):
    print request.POST
    user = User.userManager.validator(request.POST['first_name'], request.POST['last_name'], request.POST['username'], request.POST['password'], request.POST['confirm_password'], request.POST['date_ofbirth'])

    if user[0]:
        request.session['name'] = request.POST['first_name']
        request.session['id'] = User.userManager.last().id
        return redirect('/')
    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')

def login(request):
    # print request.POST
    user = User.userManager.login_val(username=request.POST['username'], password=request.POST['password'])

    if user[0]:
        request.session['id'] = User.userManager.get(username = request.POST['username']).id
        request.session['name'] = User.userManager.get(username = request.POST['username']).first_name
        return redirect('/dashboard') #redirect to dashboard
    else:
        for error in user[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/')
