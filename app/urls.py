from django.contrib import admin
from django.urls import path


# for account.models
"""
Note, however, that when you're routing to this view in urls.py, you need a different regex as mentioned here, e.g.:

urlpatterns = [
    url(r'mymodel/(?P<pk>[^/]+)/$', MyModelDetailView.as_view(),
        name='mymodel'),
]
"""

from account.views import register_view, login_view, logout_view
from main.views import (
    HomeView,
    DetailItemView,
    ItemUpdateView,
    CreateItemView,
    DeleteItemView,
    AccountUpdate,
    AccountDeleteView,
    AccountDetailView,
    ConjuntoListView,
    ConjuntoCreateView,
    ConjuntoDetailView,
    ConjuntoUpdateView,
    ConjuntoDeleteView,
    TransacaoListView,
    TransacaoCreateView,
    TransacaoDeleteView,
    TransacaoDetailView,
    TransacaoUpdateView
)
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = (
    [
        path("admin/", admin.site.urls),
        path("login/", login_view, name="login"),
        path("register/", register_view, name="register"),
        path("logout/", logout_view, name="logout"),
        path("home/", HomeView.as_view(), name="home"),
        path("detail/<uuid:pk>/", DetailItemView.as_view(), name="item_detail"),
        path("update/<uuid:pk>/", ItemUpdateView.as_view(), name="ItemUpdate"),
        path("create/", CreateItemView.as_view(), name="createItem"),
        path('delete/<uuid:pk>/', DeleteItemView.as_view(), name="deleteItem"),
        path("accountUpdate/<uuid:pk>/", AccountUpdate.as_view(), name="accountUpdate"),
        path(
            "accountDelete/<uuid:pk>/", AccountDeleteView.as_view(), name="deleteAccount"
        ),
        path("accountDetail/", AccountDetailView.as_view(), name="accountDetail"),
        path("conjuntos/", ConjuntoListView.as_view(), name="conjuntoList"),
        path(
            "conjuntos/<int:pk>/", ConjuntoDetailView.as_view(), name="conjuntoDetail"
        ),
        path("conjuntosCreate/", ConjuntoCreateView.as_view(), name="conjuntoCreate"),
        path(
            "conjuntosUpdate/<int:pk>/",
            ConjuntoUpdateView.as_view(),
            name="conjuntoUpdate",
        ),
        path(
            "conjuntosdelete/<int:pk>/",
            ConjuntoDeleteView.as_view(),
            name="conjuntoDelete",
        ),
        path("transacoes/", TransacaoListView.as_view(), name="transacaoList"),
        path(
            "transacoes/<int:pk>/",
            TransacaoDetailView.as_view(),
            name="transacaoDetail",
        ),
        path(
            "transacoesCreate/", TransacaoCreateView.as_view(), name="transacoesCreate"
        ),
        path(
            "transacoesUpdate/<int:pk>/",
            TransacaoUpdateView.as_view(),
            name="transacaoUpdate",
        ),
        path(
            "transacoesDelete/<int:pk>/",
            TransacaoDeleteView.as_view(),
            name="transacaoDelete",
        ),
    ]
    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
)
