from django.contrib import admin
from .models import Author
from .models import book
class AuthorAdmin(admin.ModelAdmin):
    def delete_model(self, request, obj):
        if not Book.objects.filter(authors=obj).exists():
            obj.delete()
        else:
            self.message_user(request, "Author is associated with books and cannot be deleted.")


admin.site.register(Author, AuthorAdmin)

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic')
    list_filter = ('name', 'surname')