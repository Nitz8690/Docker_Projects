from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50, default="")
    subcategory = models.CharField(max_length=50, default="")
    price = models.IntegerField(default=0)
    desc = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='shop/images', default="")

    def __str__(self):
        return self.product_name


class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True)
    items_json = models.CharField(max_length=5000)
    amount = models.IntegerField(default=0)
    name = models.CharField(max_length=90)
    email = models.CharField(max_length=111)
    address = models.CharField(max_length=111)
    city = models.CharField(max_length=111)
    state = models.CharField(max_length=111)
    zip_code = models.CharField(max_length=111)
    phone = models.CharField(max_length=111, default="")


#
class OrderUpdate(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField(default="")
    update_desc = models.CharField(max_length=5000)
    timestamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.update_desc[0:7] + "..."

# class Customer(models.Model):
#     user = models.OneToOneField(User,on_delete=models.CASCADE,blank=True)
#     name = models.CharField(max_length=100,  null=True)
#     email = models.EmailField(max_length=100)
#
#     def __str__(self):
#         return self.name
#
# class Product(models.Model):
#     # product_id=models.AutoField
#
#     name = models.CharField(max_length=100, null=True)
#     price =models.DecimalField(max_digits=5, decimal_places=2 )
#     digital = models.BooleanField(default=False,blank=True)
#     image = models.ImageField(null=True,blank=True)
#
#     def __str__(self):
#         return self.name
#
#     @property
#     def imageURL(self):
#         try:
#             url = self.image.url
#         except:
#             url = ''
#         return url
#
# class Order(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL,blank=True,null=True)
#     date =  models.DateTimeField(auto_now_add=True)
#     complete = models.BooleanField(default=False, null=True, blank=False)
#     transaction_Id = models.CharField(max_length=100, null=True)
#
#     def __str__(self):
#         return str(self.id)
#
#     @property
#     def shipping(self):
#         shipping = False
#         orderitems =  self.orderitem_set.all()
#         for i in orderitems:
#             if i.product.digital == False:
#                 shipping == True
#         return shipping
#
#     @property
#     def get_cart_total(self):
#         orderitems = self.orderitem_set.all()
#         total = sum([item.get_total for item in orderitems])
#         return total
#
#     @property
#     def get_cart_items(self):
#         orderitems = self.orderitem_set.all()
#         total = int(sum([item.quantity for item in orderitems]))
#         return total
#
#
# class OrderItem(models.Model):
#     product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
#     order = models.ForeignKey(Order,on_delete=models.SET_NULL, blank = True,  null=True)
#     quantity = models.IntegerField(default=0, null=True, blank=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     @property
#     def get_total(self):
#         total = self.product.price * self.quantity
#         return total
#
# class ShippingAddress(models.Model):
#     customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
#     order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
#     address = models.CharField(max_length=200, null=False)
#     city = models.CharField(max_length=200, null=False)
#     state = models.CharField(max_length=200, null=False)
#     zipcode = models.CharField(max_length=200, null=False)
#     date_added = models.DateTimeField(auto_now_add=True)
#
#     def __str__(self):
#         return self.address


# class Product(models.Model):
#     product_id = models.AutoField
#     product_name = models.CharField(max_length=50)
#     category = models.CharField(max_length=50, default="")
#     subcategory = models.CharField(max_length=50, default="")
#     price = models.IntegerField(default=0)
#     desc = models.CharField(max_length=300)
#     pub_date = models.DateField()
#     image = models.ImageField(upload_to='shop/images', default="")
#
#     def __str__(self):
#         return self.product_name
#
#
# class Contact(models.Model):
#     msg_id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=50)
#     email = models.CharField(max_length=70, default="")
#     phone = models.CharField(max_length=70, default="")
#     desc = models.CharField(max_length=500, default="")
#
#
#     def __str__(self):
#         return self.name
#
# class Orders(models.Model):
#     order_id = models.AutoField(primary_key=True)
#     items_json = models.CharField(max_length=5000)
#     amount = models.IntegerField( default=0)
#     name = models.CharField(max_length=90)
#     email = models.CharField(max_length=111)
#     address = models.CharField(max_length=111)
#     city = models.CharField(max_length=111)
#     state = models.CharField(max_length=111)
#     zip_code = models.CharField(max_length=111)
#     phone = models.CharField(max_length=111, default="")
#
# class OrderUpdate(models.Model):
#     update_id  = models.AutoField(primary_key=True)
#     order_id = models.IntegerField(default="")
#     update_desc = models.CharField(max_length=5000)
#     timestamp = models.DateField(auto_now_add=True)
#
#     def __str__(self):
#         return self.update_desc[0:7] + "..."