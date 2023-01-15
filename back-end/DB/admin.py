from django.contrib import admin
from DB.models import User, Country, City, Categorey, Tag, Store, Product, FavouriteCategories,FavouriteTags, CategoriesStores,TagsStores,Branch,BranchImages,Product,ProductImages,FavouriteProducts
admin.site.register(User)
admin.site.register(Country)
admin.site.register(City)
admin.site.register(Categorey)
admin.site.register(Tag)
admin.site.register(Store)
admin.site.register(Product)
admin.site.register(FavouriteCategories)
admin.site.register(FavouriteTags)
admin.site.register(CategoriesStores)
admin.site.register(TagsStores)
admin.site.register(BranchImages)
admin.site.register(Branch)
admin.site.register(ProductImages)
admin.site.register(FavouriteProducts)
# Register your models here.
