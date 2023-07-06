from django.shortcuts import render
from . models import User
# Create your views here.

def home(request):
    users = User.objects.all()
    context = {'users' : users}

    return render(request, 'base/home.html', context)


def newUser(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        bio = request.POST['bio']
        image = request.FILES['image']

        User.objects.create(
            name=name,
            email=email,
            bio=bio,
            image=image
        )

    return render(request, 'base/newUser.html')