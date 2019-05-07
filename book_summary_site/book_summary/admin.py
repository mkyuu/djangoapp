from django.contrib import admin
from .models import Comment,Category,Publisher,Book,Good


admin.site.register(Comment)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Book)
admin.site.register(Good)
