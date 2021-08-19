from django.shortcuts import render
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

import json

from .models import Product, Category, Order, OrderedProducts

class ProductListView(generic.ListView):
    template_name = 'shop/products.html'
    model = Product

class ProductDetailView(generic.DetailView):
    template_name = 'shop/product_detail.html'
    model = Product

class CategoryListView(generic.ListView):
    template_name = 'shop/category.html'
    model = Category

class CategoryDetailView(generic.DetailView):
    template_name = 'shop/category_detail.html'
    model = Category

class OrderListView(generic.ListView, LoginRequiredMixin):
    template_name = 'shop/orders.html'
    model = Order
    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user.pk)
        return qs

class OrderDetailView(generic.DetailView, LoginRequiredMixin):
    template_name = 'shop/order_detail.html'
    model = Order
    def get_queryset(self):
        qs = Order.objects.filter(user=self.request.user.pk)
        return qs

@login_required
def cart(request):
    cookies = json.loads(request.COOKIES.get('cart',"{}"))
    
    if request.method == "GET":
        context = {}
        context['objects'] = [{'p':Product.objects.get(pk=i),
                                'q':cookies[i]} 
                                for i in cookies.keys()]

        return render(request, "shop/cart.html", context)
    elif request.method == "POST":
        o = Order(user=User.objects.get(pk=request.user.pk))
        o.save()
        for i in cookies:
            product=Product.objects.get(pk=i)
            quantity=cookies[i]
            price=product.price
            p = OrderedProducts(order=o,
                              product=product,
                              quantity=quantity,
                              price=price)
            p.save()
        res = HttpResponseRedirect(reverse('shop:orders'))
        res.delete_cookie('cart')
        return res

def index(request):
    return render(request, 'shop/index.html')



