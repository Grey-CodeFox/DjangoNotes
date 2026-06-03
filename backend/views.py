from django.shortcuts import render
from products.models import Add_Products


def about(request):
    return render(request,'about.html')

def home(request):
    # data is created to backend from here
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_descriptio = request.POST.get('descrition')
        get_price = request.POST.get('price')

        # print(get_name,get_descriptio,get_price)

        add_product = Add_Products(
            product_name=get_name,
            product_desc=get_descriptio,
            product_price=get_price
        )
        add_product.save()
   # data is created to backend from here


# data is fetched from database
    products = Add_Products.objects.all()
    context = {
        'products':products,
    }
    # data is fetched from database

    return render(request,'home.html',context)



def payment(request):
    return render(request,'payment.html')





