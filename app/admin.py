from django.contrib import admin
from django.utils.html import format_html
from .models import Twohundered, Category, MyProject, ProjectImage, Izohlar


@admin.register(Twohundered)
class TwohunderedAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'name', 'desc')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'desc')

    @admin.display(description="Rasm")
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 6px;" />', obj.image.url)
        return "Rasm yo'q"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'slug', 'order')
    list_display_links = ('id', 'name')
    list_editable = ('order',)
    search_fields = ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}  # Nomini yozganda URL slug avtomatik to'ladi


class ProjectImageInline(admin.TabularInline):
    """Loyiha sahifasining o'zidayoq bir nechta rasm qo'shish uchun inline"""
    model = ProjectImage
    extra = 1
    readonly_fields = ('image_preview',)

    @admin.display(description="Oldindan ko'rish")
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 60px; height: 60px; object-fit: cover; border-radius: 6px;" />', obj.image.url)
        return "—"


@admin.register(MyProject)
class MyProjectAdmin(admin.ModelAdmin):
    list_display = ('id', 'cover_preview', 'title', 'category', 'price', 'is_featured', 'is_active', 'created_at')
    list_display_links = ('id', 'title')
    list_filter = ('category', 'is_featured', 'is_active', 'created_at')
    search_fields = ('title', 'short_description', 'technologies')
    list_editable = ('is_featured', 'is_active')
    inlines = [ProjectImageInline]
    date_hierarchy = 'created_at'

    # Admin forma oynasini chiroyli bo'limlarga ajratish (Fieldsets)
    fieldsets = (
        ("Asosiy ma'lumotlar", {
            'fields': ('title', 'category', 'short_description', 'full_description', 'cover_image')
        }),
        ("Havolalar (Links)", {
            'fields': ('telegram_bot_url', 'website_url', 'github_url')
        }),
        ("Xususiyatlar va Narx", {
            'fields': ('technologies', 'price', 'delivery_time')
        }),
        ("Status va Ko'rinish", {
            'fields': ('is_featured', 'is_active')
        }),
    )

    @admin.display(description="Muqova")
    def cover_preview(self, obj):
        if obj.cover_image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 6px;" />', obj.cover_image.url)
        return "Rasm yo'q"


@admin.register(ProjectImage)
class ProjectImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'image_preview', 'project', 'caption')
    list_display_links = ('id', 'project')
    list_filter = ('project',)

    @admin.display(description="Rasm")
    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 50px; height: 50px; object-fit: cover; border-radius: 6px;" />', obj.image.url)
        return "Rasm yo'q"


@admin.register(Izohlar)
class IzohlarAdmin(admin.ModelAdmin):
    list_display = ('id', 'avatar_preview', 'name', 'kasb', 'stars', 'izoh_short')
    list_display_links = ('id', 'name')
    list_filter = ('stars',)
    search_fields = ('name', 'kasb', 'izoh')

    @admin.display(description="Mijoz rasmi")
    def avatar_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 45px; height: 45px; border-radius: 50%; object-fit: cover;" />', obj.image.url)
        return "Rasm yo'q"

    @admin.display(description="Izoh")
    def izoh_short(self, obj):
        if len(obj.izoh) > 60:
            return f"{obj.izoh[:60]}..."
        return obj.izoh