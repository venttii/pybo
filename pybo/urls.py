from django.urls import path

from .views import base_views, question_views, answer_views, comment_views, vote_views, guestbook_view, userupload_view

app_name = 'pybo'

urlpatterns = [
    # base_views.py
    path('',
         base_views.index, name='index'),
    path('<int:question_id>/',
         base_views.detail, name='detail'),

    # question_views.py
    path('question/create/',
         question_views.question_create, name='question_create'),
    path('question/modify/<int:question_id>/',
         question_views.question_modify, name='question_modify'),
    path('question/delete/<int:question_id>/',
         question_views.question_delete, name='question_delete'),

    # answer_views.py
    path('answer/create/<int:question_id>/',
         answer_views.answer_create, name='answer_create'),
    path('answer/modify/<int:answer_id>/',
         answer_views.answer_modify, name='answer_modify'),
    path('answer/delete/<int:answer_id>/',
         answer_views.answer_delete, name='answer_delete'),

    # comment_views.py
    path('comment/create/question/<int:question_id>/',
         comment_views.comment_create_question, name='comment_create_question'),
    path('comment/modify/question/<int:comment_id>/',
         comment_views.comment_modify_question, name='comment_modify_question'),
    path('comment/delete/question/<int:comment_id>/',
         comment_views.comment_delete_question, name='comment_delete_question'),
    path('comment/create/answer/<int:answer_id>/',
         comment_views.comment_create_answer, name='comment_create_answer'),
    path('comment/modify/answer/<int:comment_id>/',
         comment_views.comment_modify_answer, name='comment_modify_answer'),
    path('comment/delete/answer/<int:comment_id>/',
         comment_views.comment_delete_answer, name='comment_delete_answer'),

    # vote_view.py
    path('vote/question/<int:question_id>/', vote_views.vote_question, name='vote_question'),
    path('vote/answer/<int:answer_id>/', vote_views.vote_answer, name='vote_answer'),

    # guestbook_view.py
    path('guestbook/', guestbook_view.index, name='guestbook'),
    path('guestbook/create', guestbook_view.guestbook_create, name='guestbook_create'),
    
    # userupload_view.py
    path('userupload/', userupload_view.index, name='userupload'),
    path('userupload/<int:userupload_id>/', userupload_view.detail, name='userupload_detail'),
    path('userupload/create/', userupload_view.userupload_create, name='userupload_create'),
]
