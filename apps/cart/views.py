from django.shortcuts import render
from django.conf import settings

from .cart import Cart


def cart_detail(request):
    cart = Cart(request)
    productstring = ''

    for item in cart:
        product = item['product']
        url = f'/{product.category.slug}/{product.slug}'
        b = "{'id': '%s', 'title': '%s', 'price': '%s', 'quantity': '%s', 'total_price': '%s', 'thumbnail': '%s', 'url': '%s', 'num_available': '%s',},"\
            % ( product.id, product.title, product.price, item['quantity'], item['total_price'], product.thumbnail.url, url, product.num_available)

        productstring = productstring + b

    if request.user.is_authenticated:
        first_name = request.user.first_name
        last_name = request.user.last_name
        email = request.user.email
        phone = request.user.userprofile.phone
        address = request.user.userprofile.address
        zipcode = request.user.userprofile.zipcode
        place = request.user.userprofile.place

    else:
        first_name = last_name = email = phone = address = zipcode = place = ''

    context = {
        'cart': cart,
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'phone': phone,
        'address': address,
        'zipcode': zipcode,
        'place': place,
        'pub_key': settings.STRIPE_API_KEY_PUBLISHABLE,
        'productstring': productstring
    }
    return render(request, 'cart.html', context)


def success(request):
    cart = Cart(request)
    cart.clear()

    return render(request, 'success.html')
