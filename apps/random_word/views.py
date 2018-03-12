from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
# Create your views here.
def index(request):
    return render(request, "random_word/index.html")

def generate(request):
    if request.method == "POST":
        if 'attempt' in request.session:
            request.session['attempt'] += 1
        else:
            request.session['attempt'] = 0

        request.session['random_word'] = get_random_string(length=14)
        return redirect('/')
    else:
        return redirect('/')
    
def reset(request):
    request.session['attempt'] = 0
    request.session['random_word'] = get_random_string(length=14)
    return redirect('/')
