from django.shortcuts import render
from products.models import Add_Products
def home(request):
    
    get_datas = Add_Products.objects.all()
    context = {
        'get_datas':get_datas
    }
    return render(request,'home.html',context)