from decimal import Decimal
from django.conf import setting
from shop.models import Product

class Cart():
    
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get(setting.CART_SESSION_ID)
        if not cart:
            cart = self.session[setting.CART_SESSION_ID]={}

        self.cart = cart    