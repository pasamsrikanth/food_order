from django.contrib import admin

# Register your models here.
from crud_app.models import category_model,food_model
# Register your models here.
class cat_admin(admin.ModelAdmin):
    list_display=['category_id','category_name','category_desc','category_image']
    
admin.site.register(category_model,cat_admin)

class p_admin(admin.ModelAdmin):
    list_display =['item_name','item_price','item_desc','category_id_id']
admin.site.register(food_model,p_admin)