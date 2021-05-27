from django.shortcuts import render
from django.utils.datastructures import MultiValueDictKeyError
# Create your views here.
def home(request):
    return render(request, 'index.html')


def result(request):
    try:
        user_input = request.POST['user_input']
    except MultiValueDictKeyError:
        user_input = False

    return render(request, 'result.html',{'home_input':user_input})
