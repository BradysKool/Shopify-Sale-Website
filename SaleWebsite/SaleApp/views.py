from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.renderers import TemplateHTMLRenderer
from .models import Products

# Create your views here.


@api_view(['GET'])
def MainView(request):
    products = Products.objects.all()
    brandSearch = request.query_params.get('brand')
    productSearch = request.query_params.get('name')
    if brandSearch:
        products = products.filter(brand__icontains=brandSearch)
    if productSearch:
        products = products.filter(name__icontains=productSearch)
    products = products.order_by('-percentOnSale')
    return render(request,'index.html',{'products':products})