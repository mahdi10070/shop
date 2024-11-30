from django.contrib.auth.models import User
from accounts.models import Wallet
from products.models import Product, Category
from carts import session


def get_wallet(request):
    if request.user.is_authenticated and Wallet.objects.filter(user = request.user).exists():
        wallet = Wallet.objects.get(user=request.user)
        cart = session.Cart(request)
        return {'cart': cart, 'wallet': wallet}
    else:
        return {}

def get_category(request):
    category = Category.objects.all()
    return {'static_category': category}
