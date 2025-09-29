from django.contrib import admin
from django.utils.html import format_html
from .models import Band, Venue, Concert, Ticket, Payment, Review

# Remove the basic registrations and replace with enhanced ones below
# admin.site.register(Band)
# admin.site.register(Venue) 
# admin.site.register(Concert)
# admin.site.register(Ticket)
# admin.site.register(Payment)
# admin.site.register(Review)


@admin.register(Band)
class BandAdmin(admin.ModelAdmin):
    list_display = ['name', 'genre', 'formed_date', 'created_at']
    list_filter = ['genre', 'created_at']
    search_fields = ['name', 'genre']
    ordering = ['name']
    
    fieldsets = (
        (None, {
            'fields': ('name', 'bio', 'genre') # CORRECTED: Changed 'description' to 'bio'
        }),
        ('Details', {
            'fields': ('formed_date', 'website', 'image')
        }),
    )


@admin.register(Venue)
class VenueAdmin(admin.ModelAdmin):
    list_display = ['name', 'city', 'capacity', 'phone']
    list_filter = ['city']
    search_fields = ['name', 'city', 'address']
    ordering = ['city', 'name']


@admin.register(Concert)
class ConcertAdmin(admin.ModelAdmin):
    list_display = ['name', 'band', 'venue', 'date', 'ticket_price', 'tickets_sold', 'tickets_remaining', 'is_active']
    list_filter = ['is_active', 'date', 'band__genre', 'venue__city']
    search_fields = ['name', 'band__name', 'venue__name', 'location']
    ordering = ['-date']
    date_hierarchy = 'date'
    
    readonly_fields = ['tickets_sold', 'created_at']
    
    fieldsets = (
        (None, {
            'fields': ('band', 'venue', 'name', 'location', 'date', 'doors_open')
        }),
        ('Ticketing', {
            'fields': ('ticket_price', 'total_tickets', 'tickets_sold', 'is_active')
        }),
        ('Additional Info', {
            'fields': ('description', 'image'),
            'classes': ('collapse',)
        }),
    )
    
    def tickets_remaining(self, obj):
        remaining = obj.tickets_remaining
        if remaining <= 0:
            return format_html('<span style="color: red;">SOLD OUT</span>')
        elif remaining <= 10:
            return format_html('<span style="color: orange;">{}</span>', remaining)
        else:
            return remaining
    tickets_remaining.short_description = 'Remaining'
    
    actions = ['mark_active', 'mark_inactive']
    
    def mark_active(self, request, queryset):
        queryset.update(is_active=True)
    mark_active.short_description = "Mark selected concerts as active"
    
    def mark_inactive(self, request, queryset):
        queryset.update(is_active=False)
    mark_inactive.short_description = "Mark selected concerts as inactive"


@admin.register(Ticket)
class TicketAdmin(admin.ModelAdmin):
    list_display = ['ticket_number', 'concert', 'buyer', 'price_paid', 'status', 'purchase_date']
    list_filter = ['status', 'purchase_date', 'concert__date']
    search_fields = ['ticket_number', 'buyer__username', 'buyer__email', 'buyer_email']
    ordering = ['-purchase_date']
    date_hierarchy = 'purchase_date'
    
    readonly_fields = ['ticket_number', 'purchase_date']
    
    fieldsets = (
        (None, {
            'fields': ('concert', 'buyer', 'ticket_number', 'status')
        }),
        ('Payment Info', {
            'fields': ('price_paid', 'purchase_date')
        }),
        ('Contact Info', {
            'fields': ('buyer_email', 'buyer_phone')
        }),
    )
    
    actions = ['mark_used', 'mark_cancelled']
    
    def mark_used(self, request, queryset):
        queryset.update(status='used')
    mark_used.short_description = "Mark selected tickets as used"
    
    def mark_cancelled(self, request, queryset):
        queryset.update(status='cancelled')
    mark_cancelled.short_description = "Mark selected tickets as cancelled"


@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ['transaction_id', 'ticket', 'amount', 'payment_method', 'status', 'payment_date']
    list_filter = ['status', 'payment_method', 'payment_date']
    search_fields = ['transaction_id', 'ticket__ticket_number']
    ordering = ['-payment_date']
    date_hierarchy = 'payment_date'
    
    readonly_fields = ['payment_date']
    
    def get_readonly_fields(self, request, obj=None):
        if obj:  # editing an existing object
            return self.readonly_fields + ['ticket', 'amount']
        return self.readonly_fields


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['concert', 'reviewer', 'rating', 'created_at']
    list_filter = ['rating', 'created_at']
    search_fields = ['concert__title', 'reviewer__username', 'comment']
    ordering = ['-created_at']
    date_hierarchy = 'created_at'
    
    readonly_fields = ['created_at']


# Customize admin site headers
admin.site.site_header = "Rock Aria Admin"
admin.site.site_title = "Rock Aria Admin Portal"
admin.site.index_title = "Welcome to Rock Aria Administration"