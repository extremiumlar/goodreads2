from django.contrib import admin

from .models import Book, BookAuthor, BookReview, Author

class BookAdmin(admin.ModelAdmin):
    search_fields = ['title', 'isbn']
    list_display = ('title', 'isbn', 'description')

admin.site.register(Book, BookAdmin)

class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ('book', 'author')

admin.site.register(BookAuthor, BookAuthorAdmin)

admin.site.register(BookReview)
admin.site.register(Author)



