from django.contrib import admin
from tracker.models import *
admin.site.register(CurrentBalance)

class TrackingHistoryAdmin(admin.ModelAdmin):
    list_display = ('current_balance', 'amount', 'expense_type', 'description', 'created_at', 'updated_at')
    list_filter = ('expense_type', 'created_at', 'updated_at')
    search_fields = ('description',)


admin.site.register(TrackingHistory, TrackingHistoryAdmin)
