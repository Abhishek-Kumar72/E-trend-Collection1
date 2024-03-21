from django.contrib import admin
from homes.models import SignupUser
from homes.models import Payment

admin.site.register(SignupUser)
admin.site.register(Payment)