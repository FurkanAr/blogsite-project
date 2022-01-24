from django.contrib import admin
from . models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):

    list_display = ('name','email','message')
    list_filter = ('name',)
    search_fields = ('name', 'email')

    class Meta:
        model = Contact