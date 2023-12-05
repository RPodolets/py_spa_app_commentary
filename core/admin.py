from django.contrib import admin

from core.models import User, Commentary


class UserAdmin(admin.ModelAdmin):
    pass


class CommentaryAdmin(admin.ModelAdmin):
    pass


admin.site.register(User, UserAdmin)
admin.site.register(Commentary, CommentaryAdmin)
