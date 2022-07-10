from django.shortcuts import render
from django.http import HttpResponse
from .models import Goblincakesales

# Create your views here.

def index(request):
    return render(request, 'goblin_index.html')

def sales(request):
    context = {
        "sales_quarters" : range(1,5), 
        "headers" : Goblincakesales.headers,
        "quarter" : 0,
        "product_types" : Goblincakesales.product_types,
        "product" : "",
        # Goblincakesales.objects.order_by(
        #     "product_type").distinct("product_type"),
        "cakes" : Goblincakesales.objects.all()}

    if request.method == 'POST':
        query_filter = {}

        quarter = int(request.POST.get('quarter', 0))
        if quarter > 0:
            context["quarter"] = quarter
            query_filter["quarter"] = quarter

        product = request.POST.get('product', "")
        if product:
            context["product"] = product
            query_filter["product_type"] = product

        if query_filter:
            context["cakes"] = Goblincakesales.objects.filter(**query_filter)

    return render(request, 'goblin_sales.html', context)