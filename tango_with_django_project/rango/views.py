# Create your views here.

from django.http import HttpResponse
from django.template import RequestContext 
from django.shortcuts import render_to_response

# Import the Category model
from rango.models import Category
from rango.models import Page


def index(request):
    context = RequestContext(request)
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {'categories': category_list}
    # The following two lines are new.
    # We loop through each category returned, and create a URL attribute.
    # This attribute stores an encoded URL (e.g. spaces replaced with underscores).
    for category in category_list:
        category.url = category.name.replace(' ', '_')
    return render_to_response('rango/index.html', context_dict, context)
    # return HttpResponse("Rango says hello world! <a href='/rango/about'>About</a>")

def about(request):
    return render_to_response('rango/about.html')
    # return HttpResponse("Rango Says: Here is the about page. <a href='/rango/'>Index</a>")

def category(request, category_name_url):
    # Request our context from the request passed to us.
    context = RequestContext(request)

    # Change underscores in the category name to spaces.
    # URLs don't handle spaces well, so we encode them as underscores
    # We can then simply replace the underscores with paces against to get the name.
    category_name = category_name_url.replace('_', ' ')

    context_dict = {'category_name': category_name}

    try:
        # Can we find a category with the given name?
        # If we can't, the .get() method raises a DoesNotExist exception
        # so the .get() method returns one model instance or raises an exception
        category = Category.objects.get(name=category_name)

        # Retrieve all of the associated pages.
        # Note that filter returns >= 1 model intsance.
        pages = Page.objects.filter(category=category)

        # Adds our results list to the template context under name pages
        context_dict['pages'] = pages
        # We also add the category object from the database to the context dictionary
        # We'll use this in the template to verify that the category exists
        context_dict['category'] = category
    except:
        # We get here if we didn't find the specified category
        # Don't do anything, the template displays the 'no category' message for us
        pass

    # Go render the response and return it to the client
    return render_to_response('rango/category.html', context_dict, context)
