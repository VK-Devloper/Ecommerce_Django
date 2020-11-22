import datetime

from django.urls import reverse
from django.contrib import admin
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import mark_safe

from .models import Order, OrderItem


def order_name(obj):
    return f'{obj.first_name} {obj.last_name}'


order_name.short_description = 'Name'


def order_pdf(obj):
    return mark_safe('<a href="{}">PDF</a>'.format(reverse('admin_order_pdf', args=[obj.id])))


order_pdf.short_description = 'PDF'


def admin_order_shipped(modeladmin, request, queryset):
    for order in queryset:
        order.shipped_date = datetime.datetime.now()
        order.status = Order.SHIPPED
        order.save()

        html = render_to_string('order_sent.html', {'order': order})
        # send_mail('Order sent', 'Your order has been sent!', 'noreply@saulgadgets.com', ['vaibhavkotadiya27199@gmail.com', order.email], fail_silently=False, html_message=html)

    return


admin_order_shipped.short_description = 'Set Shipped'


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', order_name, 'status', 'created_at', order_pdf]
    list_filter = ['created_at', 'status']
    search_fields = ['first_name', 'address', 'id']
    inlines = [OrderItemInline]
    actions = [admin_order_shipped]


admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
