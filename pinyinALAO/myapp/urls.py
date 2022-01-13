from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="index"), # homepage
    path('hsk1', views.hsk1_view, name='hsk1_view'), # HSK1视图
    # path('hsk1', views.hsk1_view, name='hsk1'), # HSK1判断

    path('hsk2', views.hsk2, name='hsk2'), # HSK2
    path('hsk3', views.hsk3, name='hsk3'), # HSK3
    path('pinyinDict/', views.pinyin_dict, name='pinyinDict'), # page de recherche

    path('apprentissage/', views.boucle, name='test2'), # page de boucle
    
    path('analyze_spacy/',views.analyze_spacy, name='analyze_spacy'),
    path('analyze/', views.analyze),

    path('test_request', views.test_request),
    path('test_get_post', views.test_get_post),
]