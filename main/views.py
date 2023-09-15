from django.urls import reverse_lazy

from account.models import Item
from django.views.generic import ListView, DetailView, UpdateView, CreateView
from main.forms import ItemModelForm, ItemModelCreateForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def sucess(self):
    return reverse_lazy('detailItem', kwargs={'pk': self.object.pk})


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


class DetailItemView(DetailView):
    model = Item
    template_name = 'detailItem.html'


class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemModelForm
    template_name = 'item_update.html'

    def get_success_url(self):
        return sucess(self)


@method_decorator(login_required(login_url='login'), name='dispatch')
class CreateItemView(CreateView):
    model = Item
    form_class = ItemModelCreateForm
    template_name = 'create_item.html'

    def get_success_url(self):
        return sucess(self)
