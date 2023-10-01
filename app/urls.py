from django.contrib import admin
from django.urls import path


#for account.models
'''
Note, however, that when you're routing to this view in urls.py, you need a different regex as mentioned here, e.g.:

urlpatterns = [
    url(r'mymodel/(?P<pk>[^/]+)/$', MyModelDetailView.as_view(),
        name='mymodel'),
]
'''

from account.views import register_view, login_view, logout_view
from main.views import HomeView, DetailItemView, ItemUpdateView, CreateItemView, DeleteItemView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', login_view, name='login'),
    path('register/', register_view, name='register'),
    path('logout/', logout_view, name='logout'),
    path('home/', HomeView.as_view(), name='home'),
    path('detail/<uuid:pk>/', DetailItemView.as_view(), name='item_detail'),
    path('update/<uuid:pk>/', ItemUpdateView.as_view(), name="ItemUpdate"),
    path('create/', CreateItemView.as_view(), name="createItem"),
    path('delete/<uuid:pk>/', DeleteItemView.as_view(), name="deleteItem"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


