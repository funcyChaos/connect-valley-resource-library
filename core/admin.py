import core.translation
from django.contrib             import admin
from django.contrib.gis.db 	    import models
from mapwidgets.widgets 	    import GoogleMapPointFieldWidget
from mapwidgets.widgets 	    import GoogleMapPointFieldInlineWidget
from modeltranslation.admin     import TranslationAdmin
from .models                    import Organization, Program, Location
from .forms import ProgramAdminForm

class LocationInline(admin.TabularInline):
    formfield_overrides		= {
        models.PointField: {"widget": GoogleMapPointFieldInlineWidget},
    }
    model = Location
    extra = 1
class ProgramInline(admin.TabularInline):
    model = Program
    extra = -1

@admin.register(Organization)
class OrganizationAdmin(TranslationAdmin):
    inlines = [LocationInline, ProgramInline]

    class Media:
        css = {'all': ('admin/css/map-admin.css',)}
        js  = ('admin/js/map-admin-inline.js',)

@admin.register(Program)
class ProgramAdmin(TranslationAdmin):
    pass

@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    formfield_overrides		= {
        models.PointField: {"widget": GoogleMapPointFieldWidget},
    }

    class Media:
        css = {'all': ('admin/css/map-admin.css',)}
        js  = ('admin/js/map-admin-single.js',)