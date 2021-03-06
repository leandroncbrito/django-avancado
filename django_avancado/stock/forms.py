from django import forms

from stock.models import StockEntry, Product


class StockEntryForm(forms.Form):
    amount = forms.IntegerField(label='Quantidade', required=True)
    product = forms.ModelChoiceField(
        label='Produto',
        queryset=Product.objects.all(), required=True
    )

    class Meta:
        model = StockEntry