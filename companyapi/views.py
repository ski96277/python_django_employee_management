from django.http import HttpResponse

def home_page(request):
    print('Home page requested')
    return HttpResponse('this is home page')