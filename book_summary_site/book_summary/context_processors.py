from .models import BigCategory,Category,Publisher,Author


def common(request):
    context = {
        'bigcategory_list':BigCategory.objects.all(),
        'category_list':Category.objects.all(),
        'publisher_list':Publisher.objects.all(),
        'author_list':Author.objects.all(),
    }
    return context