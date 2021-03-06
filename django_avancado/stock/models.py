from django.db import models


# Create your models here.


class TimestampableMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    """Define a classe como abstrata para não criar outra tabela na migration"""

    class Meta:
        abstract = True


class Product(TimestampableMixin):
    name = models.CharField(max_length=255)
    stock = models.IntegerField(default=-0)
    stock_max = models.IntegerField()
    price_sale = models.DecimalField(decimal_places=2, max_digits=6)
    price_purchase = models.DecimalField(decimal_places=2, max_digits=6)

    def __str__(self):
        return self.name

    def decrement(self, amount):
        if self.stock - amount < 0:
            raise ValueError('Sem estoque disponível')
        self.stock = self.stock - amount

    # receptor do signal, metodo static através da anotation classmethod
    # @classmethod
    # def increment_stock(self, sender, instance, **kwargs):
    #     product = instance.product
    #     product.stock = product.stock + instance.amount
    #     product.save()


class StockEntry(TimestampableMixin):
    amount = models.IntegerField()
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

# signal
# post_save.connect(Product.increment_stock, sender=StockEntry)
