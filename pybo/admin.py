from django.contrib import admin
from .models import Question, Answer, Comment, Guestbook, Board, Category

class QuestionAdmin(admin.ModelAdmin):
    search_fields = ['subject']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Comment)
admin.site.register(Guestbook)
admin.site.register(Board)
admin.site.register(Category)