from django.contrib import admin
from .models import Advertisement

# импорт классов для подсказок
from django.db.models.query import QuerySet

# Register your models here.

class AdvertisementsAdmin(admin.ModelAdmin):
    list_display = ['id', 'text', 'title', 'price', 'user', 'auction', 'created_date', 'created_at', 'update_at']
    list_filter = ['auction', 'price', 'created_at']
    actions = ['make_auction_as_false', 'make_auction_as_true'] # указываем функции
    fieldsets = (
        ( # Первый блок
            'Общее', # название блока
            {
                "fields": ('title', 'text')
            }
        ),
        ( # Второй блок
            'Финансы', # название блока
            {
                "fields": ('price', 'auction'),
                'classes': ['collapse'] # для скрытия
            }
        )
    )

    # создаём функции
    @admin.action(description='Убрать возможность торга') # менять у записей возможность торга на False
    def make_auction_as_false(self, request, queryset: QuerySet):
        queryset.update(auction=False)

    
    @admin.action(description='Добавить возможность торга') # менять у записей возможность торга на False
    def make_auction_as_true(self, request, queryset: QuerySet):
        queryset.update(auction=True)









# указали модель и админ класс (для кастомизации)
admin.site.register(Advertisement, AdvertisementsAdmin)