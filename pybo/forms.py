from django import forms
from pybo.models import Question, Answer, Comment, Guestbook, Board


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class BoardForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = ['subject', 'content']
        labels = {
            'subject': '제목',
            'content': '내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
            'content': '답변내용',
        }

class GuestbookForm(forms.ModelForm):
    class Meta:
        model = Guestbook
        fields = ['author', 'content', 'passwd']
        labels = {
            'author': '작성자',
            'content': '방명록 내용',
            'passwd': '패스워드',
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
        labels = {
            'content': '댓글내용',
        }