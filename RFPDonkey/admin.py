from django.contrib import admin
from .models import system_user,product_type,product,customer_type,customer
from .models import partner,rfp,questions_and_answers,system_user_role

# Register your models here.
admin.site.register(system_user)
admin.site.register(product)
admin.site.register(product_type)
admin.site.register(customer_type)
admin.site.register(customer)
admin.site.register(partner)
admin.site.register(rfp)
admin.site.register(questions_and_answers)
admin.site.register(system_user_role)
