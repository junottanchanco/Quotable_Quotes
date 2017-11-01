from __future__ import unicode_literals
from django.shortcuts import render, redirect
from .models import Quote, Join
from ..user_app.models import User #imports User table from user_app
from django.contrib import messages

def dashboard(request):
    others = Quote.quoteManager.all()
    quotes = Join.objects.filter(user_id=request.session['id'])
    for quote in quotes:
        others = others.exclude(id=quote.quote.id)
    context = {
        'others': others,
        'quotes': quotes
    }
    return render(request, 'quote_app/dashboard.html', context) #neverforget

def add(request, user_id):
    return redirect('/additem')

def additem(request):
    return render(request, 'quote_app/add.html')

def add_item(request):
    quote = Quote.quoteManager.val(request.POST['quote_by'], request.POST['quote'], request.session['id'])

    if quote[0]:
        return redirect('/dashboard')
    else:
        for error in quote[1]:
            messages.add_message(request, messages.ERROR, error)
        return redirect('/additem')

def addto(request, quote_id):
    Join.objects.create(user_id=request.session['id'], quote_id=quote_id)
    return redirect('/dashboard')

def remove(request, quote_id): #removes other users' quotes from list of user in session. it DOES NOT delete it from DB
    Join.objects.filter(user_id=request.session['id']).get(quote_id=quote_id).delete()
    return redirect('/dashboard')

def info(request, quote_id): #quote_id comes from urls.py of the quote_app passed from the href(/add) tag in dashboard.html
    quotes = Quote.quoteManager.filter(quoter_id=quote_id)
    # "quotes" grabs ONLY Quote IDs w/c equal the given quote_id
    others = Join.objects.all().filter(user_id=quote_id)
    request.session['name1'] = User.userManager.get(id=quote_id).first_name
    # "others" grabs from ALL Joins and gives you quote_ids w/c equal the given quote_id
    request.session['count'] = Quote.quoteManager.filter(quoter_id=quote_id).count()
    context = {
        'quotes': quotes,
        'others': others,
    }
    return render(request, 'quote_app/info.html', context) #neverforget

def delete(request, quote_id): #removes quote from list of user in session and deletes item completely from DB
    Quote.quoteManager.get(id=quote_id).delete()
    return redirect('/dashboard')

def logout(request):
    return redirect('/')
