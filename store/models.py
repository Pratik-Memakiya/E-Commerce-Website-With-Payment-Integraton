from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Customer(models.Model):
    user = models.OneToOneField(
        User, null=True, blank=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, null=True)
    email = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Product(models.Model):
    category=models.CharField(max_length=200 ,default='Men', choices=[('Men','Men'),('badminton','badminton'),('Women','Women'),('Gadgets','Gadgets'),('Shoes','Shoes')])
    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=7,decimal_places=2)
    digital = models.BooleanField(default=False, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

#If there is no any image of the product and is its url is typed and not found to fix this error we created this function
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url


   


#
class Order(models.Model):
    customer = models.ForeignKey(
        # if customer gets deleted its order remains in the cart and the customer is set to null.
        Customer, on_delete=models.SET_NULL, null=True, blank=True)
    date_ordered = models.DateTimeField(auto_now_add=True)
    # complete here is used to check whether the order is completed if yes then it is set to true
    complete = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.id)

    @property
    def shipping(self):
        shipping = False
        orderitems = self.orderitem_set.all()
        for i in orderitems:
            if i.product.digital == False:
                shipping = True
        return shipping

    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total

# models for the product stored in the order .
# also the items that should be added to order with many to one relation.


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)

    # order is the child of the Order model as one order can have multiple orders.
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    date_added = models.DateTimeField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total


class ShippingAddress(models.Model):
    # if customer gets deleted its adress remains.
    customer = models.ForeignKey(
        Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zipcode = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address
