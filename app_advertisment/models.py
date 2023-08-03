from django.db import models
from django.contrib import admin

# Create your models here.

class Advertisement(models.Model):
    title = models.CharField("заголовок", max_length=128)
    text = models.TextField("текст")
    price = models.FloatField("цена")
    user = models.CharField("пользователь", max_length=126) # пользователь (пока что просто имя) 
    #date = models.DateField("дата", auto_now_add=True)
    auction = models.BooleanField("торг", help_text="Возможен торг или нет", default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    # Представление в виде строки
    def __str__(self):
      return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"

    # настройки для таблицы
    class Meta:
      db_table = 'advertisments' # переименовали таблицу


    @admin.display(description="Дата создания")
    def created_date(self):
      from django.utils import timezone
      from django.utils.html import format_html
      
      if self.created_at.date() == timezone.now().date():
        create_time = self.created_at.time().strftime('%H:%M:%S')
        return format_html(
         '<span style = "color:green; font-weight = bold;">Сегодня в {}</span>',create_time

        )
      return self.created_at.strftime('%d.%m.%Y at %H:%M:%S')
      print(help(created_at))


    #
    def __str__(self):
      return f"Advertisement(id={self.id}, title={self.title}, price={self.price})"


    class Meta:
      db_table = 'advertisments' # переименовали таблицу