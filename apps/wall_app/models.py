from __future__ import unicode_literals
from django.db import models
import re

class UsersManager(models.Manager):
    def basic_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 3:
            errors["first_name"] = "First Name must be more than 2 characters"
        if len(postData['last_name']) < 3:
            errors["last_name"] = "Last Name must be more than 2 characters"
        if len(postData['password']) < 7:
            errors["password"] = "Password must be at least 8 characters"
        if(postData["password"] != postData['confirm_pw']):
            errors["password"] = "Passwords do not match" 
        if (not bool(re.match('^[a-zA-Z]+$', postData['first_name']))):
            errors["first_name"] = "First name should consist of only letters"
        if (not bool(re.match('^[a-zA-Z]+$', postData['last_name']))):
            errors["last_name"] = "Last name should consist of only letters"
        if (not bool(re.match(r'(\w+[.l\w])*@(\w+[.])*\w+', postData['email']))):
            errors["email"] = "Email is not a valid format"
        return errors


class Users(models.Model):
    first_name = models.CharField(max_length=45)
    last_name = models.CharField(max_length=45)
    email = models.EmailField()
    password = models.CharField(max_length=45)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    object = UsersManager()

class Messages(models.Model):
    description = models.TextField()
    user = models.ForeignKey(Users, related_name='user_message')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comments(models.Model):
    description = models.TextField()
    user = models.ForeignKey(Users, related_name='user_comment')
    message = models.ForeignKey(Messages, related_name='message_comment')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
