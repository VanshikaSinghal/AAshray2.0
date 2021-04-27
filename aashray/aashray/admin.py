from django.contrib import admin
from .models import Contact, PlasmaDonorForm, Oxygen, Bed, Plasma, Medicine, Helpline, Other
from django.template.loader import render_to_string
from import_export.admin import ImportExportModelAdmin
from django.contrib import messages

# admin.site.register(Contact)

class ContactAdmin(ImportExportModelAdmin):
    """ Admin Panel for Contact Model """

    list_display = ('id','email','name','subject','answered','date')
    search_fields = ('email','name','subject','message','id')
    list_display_links = ('id','email','subject')
    list_filter = ('answered',)
    list_per_page= 60
    ordering = ('date',)

admin.site.register(Contact,ContactAdmin)

class PlasmaDonorFormAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('name','age','email', 'contact', 'bloodGroup', 'answered','verified')
    search_fields = ('bloodGroup','name','age', 'email', 'answered')
    list_display_links = ('name', 'age','email', 'contact', 'bloodGroup' )
    list_filter = ('answered','verified')
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(PlasmaDonorForm,PlasmaDonorFormAdmin)

class OxygenAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('name','email', 'contact', 'verified', )
    search_fields = ('name', 'answered')
    list_display_links = ('name','email', 'contact')
    list_filter = ('verified',)
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(Oxygen,OxygenAdmin)

class BedAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('name','email', 'contact', 'verified',)
    search_fields = ('name', 'answered')
    list_display_links = ('name','email', 'contact')
    list_filter = ('verified',)
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(Bed,BedAdmin)

class PlasmaAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('name','email', 'contact','bloodGroup', 'verified', )
    search_fields = ('bloodGroup','name', 'answered')
    list_display_links = ('name','email', 'bloodGroup','contact')
    list_filter = ('bloodGroup','verified')
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(Plasma,PlasmaAdmin)

class MedicineAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('name','email', 'contact','medicine', 'verified',)
    search_fields = ('name', 'answered',)
    list_display_links = ('name','email', 'contact','medicine',)
    list_filter = ('verified','medicine',)
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(Medicine,MedicineAdmin)

class OtherAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('name',)
    list_display_links = ('name',)
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(Other,OtherAdmin)

class HelplineAdmin(ImportExportModelAdmin):
    """ Admin Panel for PlasmaDonorForml """

    list_display = ('state',)
    list_display_links = ('state',)
    list_per_page= 60
    ordering = ('currDate',)

admin.site.register(Helpline,HelplineAdmin)