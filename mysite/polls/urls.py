from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path("<int:question_id>/", views.detail, name="detail"),
    path("<int:question_id>/results/", views.results, name="results"),
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # path("<str:q_txt>/define/", views.define, name="define")
    # path("/j/k", views.something, name="something")
]
