from django.db import models

class Brand(models.Model):
    brand_name = models.CharField(max_length=255)

    def __str__(self):
        return self.brand_name

class Category(models.Model):
    category_name = models.CharField(max_length=255)

    def __str__(self):
        return self.category_name

class Store(models.Model):
    store_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return self.store_name

class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=50, null=True, blank=True)
    active = models.BooleanField(default=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    manager = models.ForeignKey('self', null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(null=True, blank=True)
    street = models.CharField(max_length=255)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Product(models.Model):
    product_name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    model_year = models.PositiveIntegerField()
    list_price = models.FloatField()

    def __str__(self):
        return self.product_name

class Stock(models.Model):
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    class Meta:
        unique_together = ('store', 'product')

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order_status = models.IntegerField()
    order_date = models.DateField()
    required_date = models.DateField()
    shipped_date = models.DateField(null=True, blank=True)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)

    def __str__(self):
        return f"Order #{self.id}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    item_id = models.IntegerField()  # This field is redundant in Django, could use id
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    quantity = models.PositiveIntegerField()
    list_price = models.FloatField()
    discount = models.FloatField()

    class Meta:
        unique_together = ('order', 'item_id')


# Create your models here.
