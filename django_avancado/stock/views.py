from django.shortcuts import render, redirect

from stock.forms import StockEntryForm
from stock.models import StockEntry


# Create your views here.

def entries_list(request):
    results = StockEntry.objects.all()

    return render(request, 'stock/entries/list.html', {
        'entries': results
    })


def entries_new(request):
    return render(request, 'stock/entries/create.html', {
        'form': StockEntryForm()
    })


def entries_create(request):
    form = StockEntryForm(request.POST)
    if form.is_valid():
        # emissor do signal
        StockEntry.objects.create(
            amount=form.cleaned_data['amount'],
            product=form.cleaned_data['product'],
        )
    return redirect('entries_list')
