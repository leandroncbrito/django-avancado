from django.apps import AppConfig


# Application initial settings


class StockConfig(AppConfig):
    name = 'stock'

    def ready(self):
        from stock.signals import increment_stock
        #from django.db.models.signals import post_save
        #evita a importação
        # stock_entry = self.get_model('StockEntry')
        # post_save.connect(increment_stock, sender=stock_entry)
