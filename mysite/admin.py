from django.contrib import admin
from mysite.models import Post,Country,City,Note,User,Photo
#Profile
#呼叫mysite資料夾下的models.py 呼叫Post,Country,City類別
from mysite.models import RichPost #在models呼叫RichPost類別

# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date')
admin.site.register(Post,PostAdmin) #在admin下註冊Post

class CountryAdmin(admin.ModelAdmin):
    list_display = ('name','country_id')
admin.site.register(Country, CountryAdmin) #在admin下註冊Country, CountryAdmin

class CityAdmin(admin.ModelAdmin):
    list_display = ('name','population','country')
admin.site.register(City, CityAdmin) #在admin下註冊City, CityAdmin

class NoteAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date')
admin.site.register(Note, NoteAdmin) #在admin下註冊NoteAdmin

class RichPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_date')
admin.site.register(RichPost, RichPostAdmin) #在admin下註冊RichPostAdmin

class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'c_time')
admin.site.register(User,UserAdmin)

class PhotoAdmin(admin.ModelAdmin):
    list_display = ('pictitle', 'piccontent', 'image','upload_date')
admin.site.register(Photo,PhotoAdmin)

#admin.site.register(models.Profile)