from django.contrib import admin

# Register your models here.

from .models import Product, ProductImage


class ProductAdmin(admin.ModelAdmin):
    # to show the dates (in links)
    date_hierarchy = 'timestamp'  # updated
    # product list data shown on admin page
    list_display = ['title', 'price', 'active', 'updated']
    # search on admin page
    search_fields = ['title', 'description']
    # to edit on the list automatically
    list_editable = ['price', 'active']
    # to filter the data list
    list_filter = ['price', 'active']
    # for read only fields
    readonly_fields = ['updated', 'timestamp']
    # automatically fill the field
    prepopulated_fields = {"slug": ("title",)}

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)

admin.site.register(ProductImage)
