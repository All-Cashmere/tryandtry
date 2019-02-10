"""colormethis URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
admin.autodiscover()
from django.urls import path

# to connect the link from products app
from products import views as cmt
# from carts.views import view, add_to_cart

# for static files
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', cmt.home),
    # path('s/', cmt.search, name='search'),
    path('products/', cmt.showall, name='products'),
    path('products/<slug:slug>/', cmt.single, name='single_product'),
    path('admin/', admin.site.urls),
    path('home/', cmt.home),
    # path('cart/', carts.views.view, name='cart'),
    # path('cart/<slug:slug>/', carts.views.add_to_cart, name='update_cart'),
    #(?P<all_items>.*)
    #(?P<id>\d+)
]

# +static is to load static files

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
