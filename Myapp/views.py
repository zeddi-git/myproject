from django.shortcuts import render, redirect # this is going to allow to redirect the user to another page if the user successfully logs in
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})
    # feature_1= Feature()
    # feature_1.id = 1
    # feature_1.name = 'Fast'
    # feature_1.is_true = True
    # feature_1.details = 'Our service is real quick'

    # feature_2 = Feature()
    # feature_2.id = 2
    # feature_2.name = 'Reliable'
    # feature_2.is_true = True
    # feature_2.details = 'Our service is really reliable'

    # feature_3 = Feature()
    # feature_3.id = 3
    # feature_3.name = 'Easy to use'
    # feature_3.is_true = False
    # feature_3.details = 'Our service is easy to use'

    # feature_4 = Feature()
    # feature_4.id = 4
    # feature_4.name = 'Affordable'
    # feature_4.is_true = True
    # feature_4.details = 'Our service is very much affordable and pocket friendly'
    
    # features = [feature_1, feature_2, feature_3, feature_4]
    # # context = {
    # #     'name' : 'Zeddi',
    # #     'age' : 24,
    # #     'nationality' : 'Kenyan'

    # # }
    # return render(request, 'index.html', {'features': features})
    # # return HttpResponse('<h1>Hey, Welcome</h1>')

def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'number' : number_of_words})

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password_confirmation']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, "Email already exist. Sign up with a new email.")
                return redirect('register')

            elif User.objects.filter(username=username).exists():
                messages.info(request, "The Username already exists")
                return redirect('register')

            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save(); 
                return redirect('login')

        else:
            messages.info(request, 'The Password do not match')
            return redirect('register')
    else:
        return render(request, 'register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user= auth.authenticate(username=username, password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')

        else:
            messages.info(request, 'Credentials do not exist. Please sign up')
            return redirect('register')
        
    else:
        return render (request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def post(request, pk):
    return render(request, 'post.html', {'pk': pk})

