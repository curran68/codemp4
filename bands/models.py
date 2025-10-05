# bands/models.py

from django.db import models
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.utils import timezone
import uuid


class Band(models.Model):
    """
    A model to represent a musical band.
    """
    name = models.CharField(max_length=100, unique=True)
    genre = models.CharField(max_length=50)
    # Add the slug field for unique URLs
    slug = models.SlugField(unique=True, blank=True)
    # Add other fields like bio, image, and logo as needed
    bio = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='bands/', blank=True, null=True)
    logo = models.ImageField(upload_to='bands/logos/', blank=True, null=True)
    
    # Additional fields for enhanced functionality
    formed_date = models.DateField(blank=True, null=True)
    website = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically generate a slug from the name if it's not set
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']


class Venue(models.Model):
    """Model for concert venues"""
    name = models.CharField(max_length=200)
    address = models.TextField()
    city = models.CharField(max_length=100)
    capacity = models.IntegerField()
    phone = models.CharField(max_length=20, blank=True)
    
    def __str__(self):
        return f"{self.name}, {self.city}"
    
    class Meta:
        ordering = ['city', 'name']


class Concert(models.Model):
    """
    Enhanced model to represent a concert event with ticket sales.
    """
    name = models.CharField(max_length=100)
    date = models.DateTimeField()  # Changed from DateField to DateTimeField for more precision
    location = models.CharField(max_length=100)  # Keep your existing location field
    
    # Enhanced fields for ticket sales
    band = models.ForeignKey(Band, on_delete=models.CASCADE, related_name='concerts', null=True, blank=True)
    venue = models.ForeignKey(Venue, on_delete=models.CASCADE, related_name='concerts', null=True, blank=True)
    doors_open = models.TimeField(blank=True, null=True)
    ticket_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    total_tickets = models.IntegerField(default=0)
    tickets_sold = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)  # For enabling/disabling sales
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='concerts/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
    @property
    def tickets_remaining(self):
        return self.total_tickets - self.tickets_sold
    
    @property
    def is_sold_out(self):
        return self.tickets_sold >= self.total_tickets
    
    @property
    def is_upcoming(self):
        return self.date > timezone.now()
    
    class Meta:
        ordering = ['date']


class Ticket(models.Model):
    """Model for individual tickets"""
    TICKET_STATUS_CHOICES = [
        ('active', 'Active'),
        ('used', 'Used'),
        ('cancelled', 'Cancelled'),
        ('refunded', 'Refunded'),
    ]
    
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name='tickets')
    buyer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tickets')
    ticket_number = models.CharField(max_length=50, unique=True, editable=False)
    purchase_date = models.DateTimeField(auto_now_add=True)
    price_paid = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=TICKET_STATUS_CHOICES, default='active')
    
    # Contact information
    buyer_email = models.EmailField()
    buyer_phone = models.CharField(max_length=20, blank=True)
    
    def save(self, *args, **kwargs):
        if not self.ticket_number:
            # Generate unique ticket number
            self.ticket_number = f"TKT-{uuid.uuid4().hex[:8].upper()}"
        super().save(*args, **kwargs)
    
    def __str__(self):
        return f"Ticket {self.ticket_number} - {self.concert}"
    
    class Meta:
        ordering = ['-purchase_date']


class Payment(models.Model):
    """Model for payment transactions"""
    PAYMENT_STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('completed', 'Completed'),
        ('failed', 'Failed'),
        ('refunded', 'Refunded'),
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('card', 'Credit Card'),
        ('paypal', 'PayPal'),
        ('stripe', 'Stripe'),
    ]
    
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE, related_name='payment')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD_CHOICES)
    status = models.CharField(max_length=20, choices=PAYMENT_STATUS_CHOICES, default='pending')
    transaction_id = models.CharField(max_length=100, blank=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Payment {self.transaction_id} - {self.amount}"
    
    class Meta:
        ordering = ['-payment_date']


class Review(models.Model):
    """Model for concert reviews"""
    concert = models.ForeignKey(Concert, on_delete=models.CASCADE, related_name='reviews')
    reviewer = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])  # 1-5 stars
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.rating}★ - {self.concert}"
    
    class Meta:
        ordering = ['-created_at']
        unique_together = ['concert', 'reviewer']  # One review per user per concert

class ContactMessage(models.Model):
    """Model for contact form submissions"""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)  # So you can track which ones you've responded to
    
    def __str__(self):
        return f"Message from {self.name} - {self.created_at.strftime('%Y-%m-%d')}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Contact Message'
        verbose_name_plural = 'Contact Messages'