from rest_framework import serializers
from order import models

class productSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.product
        fields = '__all__'


class PaymentSerializer(serializers.ModelSerializer):
    # product = productSerializer()
    subtotal = serializers.SerializerMethodField()
    total = serializers.SerializerMethodField()

    class Meta:
        model = models.payment
        fields = ['order', 'subtotal', 'tax', 'total', 'payments_type', 'payment', 'change']

    def get_subtotal(self, value):
        subtotal = value.order. price * value.order.quantity
        return subtotal

    def get_total(self, value):
        # total = 0
        # total = total + value.tax
        # total += float(self.get_subtotal())
        total = value.tax + self.get_subtotal(value)

        return total
