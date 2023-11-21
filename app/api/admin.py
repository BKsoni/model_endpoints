from django.contrib import admin
from .models import Person

class PersonAdmin(admin.ModelAdmin):
    ordering = ['id']
    list_display = ('id', 'name', 'age')
    fieldsets = (
        (None, {'fields': ('name','age')}),
    )
    # search_fields = ('name',)
    # list_per_page = 25


admin.site.register(Person, PersonAdmin)
