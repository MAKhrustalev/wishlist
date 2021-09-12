from django.shortcuts import render, get_object_or_404

from .models import WishList
from .forms import ProductForm

from datetime import datetime


def index(request):
    return render(request, "index.html", {})


def about_my(request):
    return render(request, "about_my.html", {})


def about(request):
    return render(request, "about.html", {'title': 'Wishlist | about project'})


def list_page(request, pk):
    """
    FBV - views основанные на функциях (это все views на этой странице)
    CBV - views основанные на классах (меньше возможности кастомизации)
    View page of the particular wishlist
    """

    wishlist = get_object_or_404(WishList, pk=pk)

    if request.method == "POST":
        form = ProductForm(request.POST)
        isinstance_product = form.save()
        wishlist.product.add(isinstance_product)
        wishlist.save()
    elif request.method == "GET":
        form = ProductForm()

    return render(
        request,
        'wish_list.html',
        {
            "wishlist": wishlist,
            "is_owner_list": wishlist.owner == request.user,
            "form": form,
        }
    )
