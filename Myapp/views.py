from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature

# Create your views here.
def index(request):
    feature_1= Feature()
    feature_1.id = 0
    feature_1.name = 'Fast'
    feature_1.details = 'Our service is real quick'

    feature_2 = Feature()
    feature_2.id = 1
    feature_2.name = 'Reliable'
    feature_2.details = 'Our service is really reliable'

    feature_3 = Feature()
    feature_3.id = 2
    feature_3.name = 'Easy to use'
    feature_3.details = 'Our service is easy to use'

    feature_4 = Feature()
    feature_4.id = 3
    feature_4.name = 'Affordable'
    feature_4.details = 'Our service is very much affordable and pocket friendly'
    
    features = [feature_1, feature_2, feature_3, feature_4]
    # context = {
    #     'name' : 'Zeddi',
    #     'age' : 24,
    #     'nationality' : 'Kenyan'

    # }
    return render(request, 'index.html', {'features': features})
    # return HttpResponse('<h1>Hey, Welcome</h1>')

def counter(request):
    text = request.POST['text']
    number_of_words = len(text.split())
    return render(request, 'counter.html', {'number' : number_of_words})