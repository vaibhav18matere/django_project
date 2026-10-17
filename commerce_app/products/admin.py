from django.contrib import admin
from .models import ChaiVariety, ChaiReviews, Store, ChaiCertificate
class ChaiReviewInline(admin.TabularInline):
    model = ChaiReviews
    extra = 2     # number of extra reviews to add
class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display = ('name', 'image', 'price', 'description', 'date_added')
    inlines = [ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issue_date')

admin.site.register(ChaiVariety, ChaiVarietyAdmin)
# admin.site.register(ChaiReviews, ChaiReviewAdmin)
admin.site.register(Store, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)