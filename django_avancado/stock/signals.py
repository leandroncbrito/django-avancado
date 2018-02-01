from django.db.models.signals import post_save
from django.dispatch.dispatcher import Signal

from django_avancado.settings import EMAIL_BOSS
from stock.emails import StockGreaterMax
from stock.models import StockEntry

product_stock_changed = Signal()


# receptor
def increment_stock(sender, instance, created, **kwargs):
    if created is True:
        product = instance.product
        product.stock = product.stock + instance.amount
        product.save()
        product_stock_changed.send(sender=None, instance=product)


def send_email_stock_max(sender, instance, **kwargs):
    if instance.stock > instance.stock_max:
        StockGreaterMax(instance).send(EMAIL_BOSS)


def test_save(sender, instance, created, **kwargs):
    print(created)


def test_pre_save(sender, instance, **kwargs):
    print("Pre save disparado")


# signal
post_save.connect(increment_stock, sender=StockEntry)
product_stock_changed.connect(send_email_stock_max, sender=None)

# post_save.connect(test_save, sender=StockEntry)
# pre_save.connect(test_pre_save, sender=StockEntry)

"""
m2m_changed - alteração em relacionamento NxM
pre_save - antes de salvar
post_save - depois de salvar
pre_delete - antes de excluir
post_delete - depois de excluir
request_started - quando uma requisição é recebida
request_finished - quando uma requisição estiver pronta para ser enviada
"""
