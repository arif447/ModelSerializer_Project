from django.db import models


# Create your models here.
class product(models.Model):
    product_name = models.CharField(max_length=200)
    price = models.IntegerField()
    quantity = models.IntegerField(default=1)
    scanner_code = models.CharField(max_length=200)

    def __str__(self):
        return self.product_name

class payment(models.Model):
    order = models.ForeignKey(product, on_delete=models.CASCADE)
    payments_type = (
        ("Bkash", "Bkash"),
        ("Nagad", "Nagad"),
        ("Card", "Card"),
    )
    tax = models.IntegerField()
    payment_type = models.CharField(choices=payments_type, max_length=300)
    payment = models.IntegerField()
    change = models.IntegerField()

    # def get_total(self):
    #     total = self.order.price * self.order.quantity
    #     self.subtotal = total
    #     return self.subtotal









