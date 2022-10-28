from Categories.models import Category


def CategoriesItem(request):
    categories = Category.objects.all().exclude(Parentitem=None).values('ParentCategory')
    category_item = []
    for category in categories:
        for key in category:
            category_item.append(category.get(key))
    return dict(CategoriesItem=set(category_item))
def getGategroyName(name):
    Category.pass_value_to_url(name)
    pass
