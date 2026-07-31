from django.db import models



class Twohundered(models.Model):
    image = models.ImageField(upload_to='200k/')
    name = models.CharField(max_length=1000)
    desc = models.CharField(max_length=2000)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Kategoriya nomi")
    slug = models.SlugField(max_length=100, unique=True, verbose_name="URL slug")
    order = models.PositiveIntegerField(default=0, verbose_name="Tartib raqami")

    class Meta:
        verbose_name = "Kategoriya"
        verbose_name_plural = "Kategoriyalar"
        ordering = ['order', 'name']

    def __str__(self):
        return self.name


class MyProject(models.Model):

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects',
        verbose_name="Kategoriya"
    )
    title = models.CharField(max_length=200, verbose_name="Loyiha nomi")
    short_description = models.CharField(max_length=300, verbose_name="Qisqa tavsif")
    full_description = models.TextField(blank=True, null=True, verbose_name="Batafsil tavsif")

    # Media va Rasm
    cover_image = models.ImageField(upload_to='projects/covers/', verbose_name="Asosiy rasm")

    telegram_bot_url = models.URLField(blank=True, null=True, verbose_name="Telegram bot havolasi")
    website_url = models.URLField(blank=True, null=True, verbose_name="Sayt havolasi")
    github_url = models.URLField(blank=True, null=True, verbose_name="GitHub kodi havolasi")


    technologies = models.CharField(
        max_length=255,
        help_text="Vergul bilan ajratib yozing (masalan: Python, Django, Aiogram)",
        verbose_name="Ishlatilgan texnologiyalar"
    )

    # Qo'shimcha parametrlar
    price = models.CharField(max_length=100, blank=True, null=True, verbose_name="Narxi (masalan: 200 000 so'm)")
    delivery_time = models.CharField(max_length=100, blank=True, null=True,
                                     verbose_name="Bajarilish muddati (masalan: 2 kun)")

    # Status va Sozlamalar
    is_featured = models.BooleanField(default=False, verbose_name="Bosh sahifada ko'rsatilsinmi?")
    is_active = models.BooleanField(default=True, verbose_name="Faol holatdami?")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Yaratilgan vaqti")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Yangilangan vaqti")

    class Meta:
        verbose_name = "Loyiha"
        verbose_name_plural = "Loyihalar"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


class ProjectImage(models.Model):

    project = models.ForeignKey(
        MyProject,
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Loyiha"
    )
    image = models.ImageField(upload_to='projects/gallery/', verbose_name="Rasm")
    caption = models.CharField(max_length=200, blank=True, null=True, verbose_name="Rasm tavsifi")

    class Meta:
        verbose_name = "Loyiha rasmi"
        verbose_name_plural = "Loyiha rasmlari"

    def __str__(self):
        return f"{self.project.title} - Rasm"

class Izohlar(models.Model):
    Yulduzlar = [
        ("⭐", "1"),
        ("⭐⭐", "2"),
        ("⭐⭐⭐", "3"),
        ("⭐⭐⭐⭐", "4"),
        ("⭐⭐⭐⭐⭐", "5"),
    ]
    stars = models.CharField(choices=Yulduzlar)
    izoh = models.CharField(max_length=1000)
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='izohchi/')
    kasb = models.CharField(max_length=30)

