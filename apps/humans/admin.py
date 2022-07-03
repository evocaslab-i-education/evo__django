from django.contrib import admin

from .models import Human, Color, SuperHuman

admin.site.register(Human)


class SuperHumanInlineAdmin(admin.TabularInline):
    model = SuperHuman


@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    inlines = (SuperHumanInlineAdmin,)


@admin.register(SuperHuman)
class SuperHumanAdmin(admin.ModelAdmin):
    ...
