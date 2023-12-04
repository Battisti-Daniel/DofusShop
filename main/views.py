from django.urls import reverse_lazy
from django.contrib.auth.hashers import make_password
from account.models import Item, Gear, Account, Conjunto ,Transacao
from account.forms import AccountUpdateForm
from django.views.generic import (
    ListView,
    DetailView,
    UpdateView,
    CreateView,
    DeleteView,
)
from main.forms import ItemModelForm, ItemModelCreateForm, ConjuntoForm, TransacaoForm
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required


def sucess(self):
    return reverse_lazy("item_detail", kwargs={"pk": self.object.pk})


class HomeView(ListView):
    model = Item
    template_name = "home.html"
    context_object_name = "item"

    def get_queryset(self):
        item = super().get_queryset().order_by("updated_at")
        search = self.request.GET.get("search")

        if search:
            item = item.filter(name__icontains=search)

        if search is None:
            item = super().get_queryset().order_by("updated_at")
            search = self.request.GET.get("searchIcon")
            if search:
                item = item.filter(gear__name__icontains=search)
        return item

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["gear"] = Gear.objects.all()
        return context


class DetailItemView(DetailView):
    model = Item
    template_name = "item_detail.html"


@method_decorator(login_required(login_url="login"), name="dispatch")
class AccountUpdate(UpdateView):
    model = Account
    template_name = "accountEdit.html"
    form_class = AccountUpdateForm

    def form_valid(self, form):
        new_password = form.cleaned_data.get("new_password")
        if new_password:
            form.instance.password = make_password(new_password)

        return super().form_valid(form)

    success_url = "/home/"
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class AccountDeleteView(DeleteView):
    model = Account
    template_name = 'accountDelete.html'
    success_url = reverse_lazy('home')

    def get_object(self, queryset=None):
        return self.request.user

    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        return response

@method_decorator(login_required(login_url='login'), name='dispatch')
class AccountDetailView(DetailView):
    model = Account
    template_name = 'accountDetail.html'
    context_object_name = 'account'

    def get_object(self, queryset=None):
        return self.request.user

@method_decorator(login_required(login_url="login"), name="dispatch")
class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemModelForm
    template_name = "item_update.html"

    def get_success_url(self):
        return sucess(self)


@method_decorator(login_required(login_url="login"), name="dispatch")
class CreateItemView(CreateView):
    model = Item
    form_class = ItemModelCreateForm
    template_name = "create_item.html"

    def form_valid(self, form):
        form.instance.account = self.request.user
        return super().form_valid(form)

    def get_success_url(self):
        return sucess(self)


@method_decorator(login_required(login_url="login"), name="dispatch")
class DeleteItemView(DeleteView):
    model = Item
    template_name = "item_delete.html"
    success_url = "/home/"

@method_decorator(login_required(login_url='login'), name='dispatch')
class ConjuntoListView(ListView):
    model = Conjunto
    template_name = 'conjuntoList.html'
    context_object_name = 'conjuntos'

@method_decorator(login_required(login_url='login'), name='dispatch')
class ConjuntoDetailView(DetailView):
    model = Conjunto
    template_name = 'conjuntoDetail.html'
    context_object_name = 'conjunto'

@method_decorator(login_required(login_url='login'), name='dispatch')
class ConjuntoCreateView(CreateView):
    model = Conjunto
    form_class = ConjuntoForm
    template_name = 'conjuntoForm.html'
    success_url = reverse_lazy('conjuntoList')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

@method_decorator(login_required(login_url='login'), name='dispatch')
class ConjuntoUpdateView(UpdateView):
    model = Conjunto
    form_class = ConjuntoForm
    template_name = 'conjuntoForm.html'
    success_url = reverse_lazy('conjuntoList')

@method_decorator(login_required(login_url='login'), name='dispatch')
class ConjuntoDeleteView(DeleteView):
    model = Conjunto
    template_name = 'conjuntoDelete.html'
    success_url = reverse_lazy('conjuntoList')
    
@method_decorator(login_required(login_url='login'), name='dispatch')
class TransacaoListView(ListView):
    model = Transacao
    template_name = 'transacaoList.html'
    context_object_name = 'transacoes'

@method_decorator(login_required(login_url='login'), name='dispatch')
class TransacaoDetailView(DetailView):
    model = Transacao
    template_name = 'transacaoDetail.html'
    context_object_name = 'transacao'

@method_decorator(login_required(login_url='login'), name='dispatch')
class TransacaoCreateView(CreateView):
    model = Transacao
    form_class = TransacaoForm
    template_name = 'transacaoForm.html'
    success_url = reverse_lazy('transacaoList')

@method_decorator(login_required(login_url='login'), name='dispatch')
class TransacaoUpdateView(UpdateView):
    model = Transacao
    form_class = TransacaoForm
    template_name = 'transacaoForm.html'
    success_url = reverse_lazy('transacaoList')

@method_decorator(login_required(login_url='login'), name='dispatch')
class TransacaoDeleteView(DeleteView):
    model = Transacao
    template_name = 'transacaoDelete.html'
    success_url = reverse_lazy('transacaoList')