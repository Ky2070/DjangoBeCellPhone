from django.contrib import admin
from cellphoneApp.models import Product, Color, Product_Color, User, Role, Branch, Review, Manufacture, Laptop, \
    Smartphone, Promotion
from django.urls import path
# from ckeditor.fields import RichTextField
# from ckeditor.widgets import CKEditorWidget

#
# class ReviewAdmin(admin.ModelAdmin):
#     formfield_overrides = {
#         RichTextField: {'widget': CKEditorWidget}
#     }


# class UpdateManufacturerForm(forms.Form):
#     new_manufacturer = forms.CharField(label=('New manufacturer'), max_length=100)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('Name', 'nameManufacture', 'Type')
    list_filter = ('nameManufacture',)
    search_fields = ('nameManufacture__names__icontains',)


class ReviewAdmin(admin.ModelAdmin):
    list_display = ('Title', 'Content', 'idProduct')
    list_filter = ('idProduct',)


class Product_ColorAdmin(admin.ModelAdmin):
    list_display = ('Id', 'idProduct', 'nameColor', 'Price')
    list_display_links = ('Id', 'idProduct', 'nameColor')
    search_fields = ('Price__icontains',)
    ordering = ('Price',)


class PromotionAdmin(admin.ModelAdmin):
    list_display = ('Id', 'timeStart', 'timeEnd', 'Active',)


# Register your models here.
admin.site.register(Review, ReviewAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Product_Color, Product_ColorAdmin)
admin.site.register(Color)
admin.site.register(User)
admin.site.register(Branch)
admin.site.register(Manufacture)
admin.site.register(Laptop)
admin.site.register(Smartphone)
admin.site.register(Promotion, PromotionAdmin)
admin.site.register(Role)