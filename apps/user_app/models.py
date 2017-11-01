from __future__ import unicode_literals
from django.db import models
from datetime import datetime
import re
import bcrypt

class UserManager(models.Manager):
    def validator(self, first_name, last_name, username, password, confirm_password, date_ofbirth):
        errors = []

        if len(first_name) < 1:
            errors.append('First Name cannot be empty.')
        elif not (first_name).isalpha():
            errors.append('First Name can only contain letters.')
        elif len(first_name) < 3:
            errors.append('First Name must be 3 characters or more.')

        if len(last_name) < 1:
            errors.append('Last Name cannot be empty.')
        elif not (last_name).isalpha():
            errors.append('Last Name can only contain letters.')
        elif len(last_name) < 2:
            errors.append('Last Name must be 2 characters or more.')

        if len(username) < 1:
            errors.append('Username cannot be empty.')
        elif len(username) < 5:
            errors.append('Username must be 5 characters or more.')

        if len(password) < 1:
            errors.append('Password is required.')
        elif len(password) < 8:
            errors.append('Password must be 8 characters or more.')

        if len(confirm_password) < 1:
            errors.append('Confirm Password is required')
        elif confirm_password != password:
            errors.append('Confirm Password must match Password.')

        if len(date_ofbirth) < 1:
            errors.append('Hire Date field cannot be blank.')
        elif datetime.strptime(date_ofbirth, '%Y-%m-%d') > datetime.now():
            errors.append('Hire Date must be in the past.')

        if len(errors) == 0:
            hashed_password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
            user = User.userManager.create(first_name=first_name, last_name=last_name, username=username, password=hashed_password, date_ofbirth=date_ofbirth)
            return (True, user)
        else:
            return (False, errors)

    def login_val(self, username, password):
        errors = []

        if len(username) < 1:
            errors.append('Please enter your Username')
        else:
            user = User.userManager.filter(username=username)
            if len(user) == 0:
                errors.append('Username not found. Please register first.')

        if len(password) < 1:
            errors.append('Please enter your password')

        if len(errors) > 0:
            return (False, errors)
        else:
            if bcrypt.checkpw(password.encode(), user[0].password.encode()):
                return (True, user[0])
            else:
                return (False, ['Invalid Password!'])

class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)
    date_ofbirth = models.DateTimeField('%Y-%d-%M')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    userManager = UserManager()
