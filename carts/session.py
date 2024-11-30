from products.models import Product

CART_SESSION_ID = 'cart'


class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(CART_SESSION_ID)
        if not cart:
            cart = self.session[CART_SESSION_ID] = {}
        self.cart = cart

    def __iter__(self):
        cart = self.cart.copy()
        for item in cart.values():
            item['product'] = Product.objects.get(id = int(item['product_id']))
            item['total'] = str(int(item['price']) * int(item['count']))
            item['id'] = str(self.create_id(item['price'], item['product_id']))
            yield item

    def create_id(self, price, product_id):
        return f"{price}-{product_id}"

    def save(self):
        self.session.modified = True

    def add_cart(self, product, count):
        print(f"in to cart ke {product.id}")
        id = self.create_id(product.price, product.id)
        if id not in self.cart:
            self.cart[id] = {'count': 0,
                             'price': str(product.price),
                             'product_id': product.id}
        self.cart[id]['count'] += int(count)
        print(f"type in hast: {type(int(self.cart[id]['product_id']))}")
        self.save()

    def remove_cart(self, id):
        if id in self.cart:
            self.cart[id]['count'] -= 1
            if self.cart[id]['count'] == 0:
                del self.cart[id]
        self.save()

    def all_total(self):
        cart = self.cart.values()
        total = 0
        for item in cart:
            total += int(item['price']) * int(item['count'])
        return total
