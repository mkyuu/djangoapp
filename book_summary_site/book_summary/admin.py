from django.contrib import admin
from .models import Comment,BigCategory,Category,Author,Publisher,Book,Good


admin.site.register(Comment)
admin.site.register(BigCategory)
admin.site.register(Category)
admin.site.register(Author)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Good)
