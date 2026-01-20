from django.shortcuts import render, get_object_or_404
from django.http import Http404

# Sample in-memory product list (replace later by DB models)
PRODUCTS = [
    {
        "id": 1,
        "name": "Classic T-Shirt",
        "price": 499,
        "old_price": 699,
        "short_desc": "Comfortable cotton tee",
        "description": "A comfortable cotton T-shirt available in multiple sizes.",
        "image_url": "/static/images/tshirt.webp",
    },
    {
        "id": 2,
        "name": "Bluetooth Headphones",
        "price": 1299,
        "old_price": None,
        "short_desc": "Wireless & noise-cancelling",
        "description": "High-quality sound with long battery life.",
        "image_url": "/static/images/image.png",
    },
    # add more sample products as needed
]

def homepage(request):
    q = request.GET.get('q', '').lower()
    if q:
        products = [p for p in PRODUCTS if q in p['name'].lower() or q in p['short_desc'].lower()]
    else:
        products = PRODUCTS
    return render(request, "home.html", {"products": products})

def product_detail(request, pk):
    product = next((p for p in PRODUCTS if p["id"] == int(pk)), None)
    if not product:
        raise Http404("Product not found")
    return render(request, "product_detail.html", {"product": product})
