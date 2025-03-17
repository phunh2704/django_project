from django.shortcuts import render, redirect
from .models import Product
from django.contrib import messages



def product_create(request):
    if request.method == 'POST':
        name = request.POST['name']
        price_purchase = float(request.POST['price_purchase'])
        price_selling = float(request.POST['price_selling'])
        quantity = int(request.POST['quantity'])

        item_product = Product(name=name, price_purchase=price_purchase, price_selling=price_selling, quantity=quantity)
        item_product.save()
        messages.success(request,'Sản phẩm đã được tạo thành công!')
        return redirect('/')
        
    return render(request, 'product_create.html',{})
def product_list(request):
    item_product = Product.objects.all()
    total_revenue = sum(product.price_selling * product.quantity_sold for product in item_product)
    total_profit = sum((product.price_selling - product.price_purchase) * product.quantity_sold for product in item_product)

    if request.method == 'POST':
        name = request.POST['name']
        price_purchase = float(request.POST['price_purchase'])
        price_selling = float(request.POST['price_selling'])
        quantity = int(request.POST['quantity'])

        item_product = Product(name=name, price_purchase=price_purchase, price_selling=price_selling, quantity=quantity)
        item_product.save()
        messages.success(request,'Sản phẩm đã được tạo thành công!')
        return redirect('/')

    return render(request, 'product_list.html',{
        'item_product': item_product,
        'total_revenue': total_revenue,
        'total_profit': total_profit
    })
def product_update(request, product_id):
    item_product = Product.objects.get(id=product_id)
    if request.method == 'POST':
        item_product.name = request.POST['name']
        item_product.price_purchase = float(request.POST['price_purchase'])
        item_product.price_selling = float(request.POST['price_selling'])
        item_product.quantity = int(request.POST['quantity'])
        item_product.quantity_sold = int(request.POST['quantity_sold'])        
        item_product.save()

        messages.success(request,'Sản phẩm đã được cập nhật thành công!')

        return redirect('/')
    return render(request, 'product_update.html',{
        'item_product': item_product
    })
def product_delete(request, product_id):
    item_product = Product.objects.get(id=product_id)
    item_product.delete()
    messages.success(request,'Sản phẩm đã được xóa thành công!')
    return redirect('/')
def product_sell(request, product_id):
    item_product = Product.objects.get(id=product_id)
    quantity = int(request.GET.get('quantity'))

    item_product.quantity -= quantity
    item_product.quantity_sold += quantity
    item_product.save()
                                
    messages.success(request,'Sản phẩm đã được bán thành công!')
    return redirect('/')