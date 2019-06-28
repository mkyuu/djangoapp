from .models import TopCategory,BigCategory,Category,Publisher,Author


def common(request):
    context = {
        'topcategory_list':TopCategory.objects.all(),
        'publisher_list':Publisher.objects.all(),
        'author_list':Author.objects.all(),
    }
    return context