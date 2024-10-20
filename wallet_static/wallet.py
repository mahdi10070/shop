from django.contrib.auth.models import User

from accounts.models import Wallet
from products.models import Product, Category


def get_wallet(request):
    if request.user.is_authenticated and Wallet.objects.filter(user = request.user).exists():
        wallet = Wallet.objects.get(user=request.user)
        product = Product.objects.filter(wallet=wallet)
        total = 0
        for item in product:
            total += item.price

        return {'static_product': product, 'wallet': wallet, 'total': total}
    elif request.user.is_authenticated and Wallet.objects.filter(user = request.user).exists():
        return {}

    else:
        return {}

def get_category(request):
    category = Category.objects.all()
    return {'static_category': category, }
