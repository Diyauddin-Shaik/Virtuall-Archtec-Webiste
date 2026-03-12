from django.contrib import admin
from .models import RoomDesign, ChatMessage


class RoomDesignAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'house_type',
        'room_type',
        'wall_color',
        'lamp_type',
        'furniture',
        'created_at'
    )

    search_fields = (
        'user__username',
        'room_type',
        'house_type'
    )

    list_filter = (
        'room_type',
        'house_type',
        'created_at'
    )


class ChatMessageAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'user',
        'message',
        'created_at'
    )

    search_fields = (
        'user__username',
        'message'
    )

    list_filter = (
        'created_at',
    )


admin.site.register(RoomDesign, RoomDesignAdmin)
admin.site.register(ChatMessage, ChatMessageAdmin)