from shop.models import Category

def menu_links(request):
    c=Category.objects.filter()
    return {'links':c}