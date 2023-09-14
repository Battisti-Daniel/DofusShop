from django.urls import reverse_lazy

from account.models import Item
from django.views.generic import ListView, DetailView, UpdateView
from main.forms import ItemModelForm

class HomeView(ListView):
    model = Item
    template_name = 'home.html'
    context_object_name = 'item'

    def get_queryset(self):
        item = super().get_queryset().order_by('updated_at')
        search = self.request.GET.get('search')
        if search:
            item = item.filter(name__icontains=search)
        return item


class DetailItem(DetailView):
    model = Item
    template_name = 'detailItem.html'


class ItemUpdate(UpdateView):
    model = Item
    form_class = ItemModelForm
    template_name = 'item_update.html'

    def get_success_url(self):
        return reverse_lazy('detailItem', kwargs={'pk': self.object.pk})
