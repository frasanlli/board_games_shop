class Cart:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        #cart is a dictionary {item.id1: {<item_properties>}, item.id2: {<item_properties>},}
        cart: dict = self.session.get("cart")

        if not cart:
            cart = self.session["cart"] = {}

        self.cart = cart


    def add(self, item):
        if (str(item.id) not in self.cart.keys()):
            self.cart[item.id]={
                "item_id": item.id,
                "name": item.name,
                "price": str(item.price),
                "quantity": 1,
                "image": item.image.url
            }
        else:
            self.join(item)

        self.save_cart()


    def join(self, item):
        for key, value in self.cart.items():
            if key == str(item.id):
                value["quantity"]=value["quantity"]+1
                break


    def save_cart(self):
        self.session["cart"] = self.cart
        self.session.modified = True


    def substract(self, item):
        if (str(item.id) in self.cart.keys()):
            for key, value in self.cart.items():
                if key == str(item.id):
                    value["quantity"] = value["quantity"]-1
                    if value["quantity"] == 0:
                        self.delete(item, True)
                    break
        self.save_cart()


    def delete(self, item, substract=False):
        del self.cart[item.id]
        if not substract:
            self.save_cart()

    def clean_cart(self):
        self.session["cart"] = {}
        self.session.modified = True