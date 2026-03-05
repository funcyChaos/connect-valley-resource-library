from modeltranslation.translator import register, TranslationOptions

from .models import Organization, Program

@register(Organization)
class OrganizationTranslationOptions(TranslationOptions):
    fields = ('description',)

@register(Program)
class ProgramTranslationOptions(TranslationOptions):
    fields = ('name', 'description',)