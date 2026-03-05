import core.translation
from django.contrib import admin
from modeltranslation.admin import TranslationAdmin
from .models import Organization, Program


# Register your models here.
@admin.register(Organization)
class OrganizationAdmin(TranslationAdmin):
    pass

@admin.register(Program)
class ProgramAdmin(TranslationAdmin):
    pass