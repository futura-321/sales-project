from django.contrib import admin
from main_app import models

# Register your models here.
admin.site.register(models.login_view)
admin.site.register(models.customer)
admin.site.register(models.Seller)
admin.site.register(models.mobileproduct)
admin.site.register(models.Payment)
admin.site.register(models.Cart)

