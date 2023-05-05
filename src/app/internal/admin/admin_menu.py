from django.contrib import admin

from app.internal.models.imenu import Gluten, Lactose, Lectins


@admin.register(Gluten)
class GlutenAdmin(admin.ModelAdmin):
    pass


@admin.register(Lactose)
class LactoseAdmin(admin.ModelAdmin):
    pass


@admin.register(Lectins)
class LectinsAdmin(admin.ModelAdmin):
    pass
