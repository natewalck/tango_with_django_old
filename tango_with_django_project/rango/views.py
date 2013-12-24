# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext 
from django.shortcuts import render_to_response

# Import the Category model
from rango.models import Category


def index(request):
    context = RequestContext(request)
    catergory_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': catergory_list}
    return render_to_response('rango/index.html', context_dict, context)
    # return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

def about(request):
    return render_to_response('rango/about.html')
    # return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")