from __future__ import unicode_literals
from django.db import models
from ..user_app.models import User

class QuoteManager(models.Manager):
    def val(self, quote_by, quote, id):
        errors = []

        Flag = True

        if len(quote_by) < 1:
            errors.append('Quote By field cannot be empty.')
            Flag = False;
        elif len(quote_by) < 3:
            errors.append('Quoted by field must be 3 characters or more.')
            Flag = False;

        if len(quote) < 1:
            errors.append('Quote field cannot be empty.')
            Flag = False;
        elif len(quote) < 10:
            errors.append('Quote field must be 10 characters or more.')
            Flag = False;

        if Flag == True:
            quote = Quote.quoteManager.create(quote_by=quote_by, quote=quote, quoter_id=id)
            return (True, quote)
        else:
            return (False, errors)

class Quote(models.Model):
    quote_by = models.CharField(max_length=255)
    quote = models.CharField(max_length=1000)
    quoter = models.ForeignKey(User, related_name="added_quote")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    quoteManager = QuoteManager()

class Join(models.Model):
    user = models.ForeignKey(User, related_name="quotes")
    quote = models.ForeignKey(Quote, related_name="users")
