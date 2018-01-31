from django.db.models.signals import post_save

from stock.models import StockEntry


# receptor
def increment_stock(sender, instance, created, **kwargs):
    if created is True:
        product = instance.product
        product.stock = product.stock + instance.amount
        product.save()


def test_save(sender, instance, created, **kwargs):
    print(created)


def test_pre_save(sender, instance, **kwargs):
    print("Pre save disparado")


# signal
post_save.connect(increment_stock, sender=StockEntry)

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
