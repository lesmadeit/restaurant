from django.db import models
from django.utils.text import slugify


class MenuCategory(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']
        verbose_name_plural = "Menu Categories"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
    
class MenuItem(models.Model):
    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        related_name='items'
    )

    name = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='menu/', blank=True, null=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['category', 'name']

    def __str__(self):
        return f"{self.name} - ${self.price}"


