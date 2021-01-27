from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=20, unique=True)
    description = models.CharField(max_length=200, null=True, blank=True)
    has_answer = models.BooleanField(default=True)  # 답변가능 여부

    def __str__(self):
        return self.name

class Board(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_board')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_board')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_board', default=0)
    view_count = models.IntegerField(default=0)
    notice = models.BooleanField(default=False)  # 공지사항 여부
    ip = models.CharField(max_length=50)

    def __str__(self):
        return self.subject

class Guestbook(models.Model):
    author = models.CharField(max_length=50)
    content = models.TextField()
    passwd = models.CharField(max_length=50)
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    ip_address = models.CharField(max_length=50)

    def __str__(self):
        return self.content

class Question(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_question')

    def __str__(self):
        return self.subject

class Answer(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')

    def __str__(self):
        return self.content

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    question = models.ForeignKey(Question, null=True, blank=True, on_delete=models.CASCADE)
    answer = models.ForeignKey(Answer, null=True, blank=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

# 게시글 조회 기록 저장
class HitCount(models.Model):
    ip = models.CharField(max_length=15, default=None, null=True)  # ip 주소
    post = models.ForeignKey(Board, on_delete=models.CASCADE, default=None, null=True)  # 게시글
    date = models.DateField(default=timezone.now(), null=True, blank=True)  # 조회수가 올라갔던 날짜 