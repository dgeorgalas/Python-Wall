from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages


def home(request):
    print("======================")

    return render(request, 'wall_app/home.html')

def register(request):
    errors = Users.object.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect("/")
    else:
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        email = request.POST["email"]
        password = request.POST["password"]
        user = Users.object.create(first_name=first_name, last_name=last_name, email=email, password=password)
        request.session['id'] = user.id
        return redirect("/wall")



def log_out(request):
    del request.session["id"]
    return redirect("/")


def login(request):
    if(Users.object.filter(email=request.POST["email"]).exists()):
        user = Users.object.filter(email=request.POST["email"]) [0]
        if(Users.object.filter(password=request.POST["password"]).exists()):
            request.session["id"] = user.id
            return redirect("/wall")
    return redirect("/")

def wall(request):
    # if not request.session['id']:
    #     return redirect('/')
    # else:
        user = Users.object.get(id=request.session['id'])
        users = Users.object.all()
        messages = Messages.objects.all()
        comments = Comments.objects.all()
        context = {
            "user" : user,
            "users" : users,
            "messages" : messages,
            "comments" : comments
            }
        return render(request, 'wall_app/wall.html', context)


def post_message(request):
    if request.method == "POST":
        user = Users.object.get(id=request.session['id'])
        message = request.POST['message']
        Messages.objects.create(description=message, user=user)
    return redirect("/wall")


def post_comment(request):
    user = Users.object.get(id=request.session['id'])
    Comments.objects.create(description = request.POST['comment'], user=user, message=Messages.objects.get(id=request.POST["message_comment"]))
    print(((((((((((())))))))))))
    print(Comments.objects.all())
    return redirect('/wall')

def delete_message(request, message_id):
    x = Messages.objects.get(id=message_id)
    x.delete()
    return redirect('/wall')