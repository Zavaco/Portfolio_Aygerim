from django.contrib import admin
from .models import Menu, Footer
from .models import Home, Work, About
# Register your models here.

admin.site.register(Menu)
admin.site.register(Footer)
admin.site.register(Home)
admin.site.register(Work)
admin.site.register(About)