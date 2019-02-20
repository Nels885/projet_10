from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

import logging

from .models import Product

from .forms import RegistrationForm

logger = logging.getLogger(__name__)

# Create your views here.


def index(request):
    """
    View of the index page
    :param request:
        Parameters of the request
    :return:
        Index page
    """
    return render(request, 'app/index.html')


def notice(request):
    """
    View of the legal notice page
    :param request:
        Parameters of the request
    :return:
        legal notice page
    """
    return render(request, 'app/legal_notice.html')


def search(request):
    """
    View of the food search
    :param request:
        Parameters of the request
    :return:
        Results page or Index page if no found
    """
    logger.info('New search', exc_info=True, extra={
        'request': request,
    })
    query = request.GET.get('query')
    if not query:
        return redirect('/')
    else:

        # Search food in the database
        products = Product.objects.filter(name__istartswith=query).order_by('-nutrition_grades')

        # Alternative food search excluding user favorites
        if products:
            product = products[0]
            if request.user.is_authenticated:
                user = User.objects.get(pk=request.user.id)
                substitutes = Product.objects.filter(
                    category=product.category,
                    nutrition_grades__lt=product.nutrition_grades
                ).exclude(backup_substitute__user=user).order_by('nutrition_grades')
            else:
                substitutes = Product.objects.filter(
                    category=product.category,
                    nutrition_grades__lt=product.nutrition_grades
                ).order_by('nutrition_grades')
        else:
            product = substitutes = None

    context = {
        'search': query,
        'product': product,
        'substitutes': substitutes
    }
    return render(request, 'app/results.html', context)


def food(request, product_id):
    """
    View of the food in detail
    :param request:
        Parameters of the request
    :param product_id:
        Id of the food
    :return:
        Food page with the detail
    """
    product = get_object_or_404(Product, pk=product_id)
    picture_header = product.front_picture.replace("400.jpg", "full.jpg")
    context = {
        'picture_header': picture_header,
        'product': product
    }
    return render(request, 'app/food.html', context)


@login_required(login_url='/app/login/')
def account(request):
    """
    view of logged user information
    :param request:
        Parameters of the request
    :return:
        Account page with user information
    """
    return render(request, 'app/account.html')


def registration(request):
    """
    View for registration of a new user
    :param request:
        Parameters of the request
    :return:
        Registration page or login page
    """
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/app/login/')
        context = {'form': form}
    else:
        form = RegistrationForm()
        context = {'form': form}
    return render(request, 'app/registration.html', context)
