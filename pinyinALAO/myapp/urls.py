from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

# url configuration
urlpatterns = [
    path('home', views.home, name="home"), # homepage
    path('', views.index, name="index"), # homepage1

    path('hsk1_view', views.hsk1_view, name='hsk1_view'), # HSK1-viewpage
    path('hsk1', views.hsk1, name='hsk1'), # Evaluation du HSK1

    path('hsk2_view', views.hsk2_view, name='hsk2_view'), # HSK2-viewpage
    path('hsk2', views.hsk2, name='hsk2'), # Evaluation du HSK2

    path('hsk3_view', views.hsk3_view, name='hsk3_view'), # HSK3-viewpage
    path('hsk3', views.hsk3, name='hsk3'), # Evaluation du HSK3

    path('hsk4_view', views.hsk4_view, name='hsk4_view'), # HSK4-viewpage
    path('hsk4', views.hsk4, name='hsk4'), # Evaluation du HSK4

    path('pinyinDict', views.pinyin_dict, name='pinyinDict'), # Recherche pinyin
    path('pinyinAffi', views.pinyin_dict_affiche, name='pinyinAffi'), # Information sur le pinyin


    # 测试 test
    # path('apprentissage/', views.boucle, name='test2'), # page de boucle
    # path('analyze_spacy/',views.analyze_spacy, name='analyze_spacy'),
    # path('analyze/', views.analyze),
    # path('test_request', views.test_request),
    # path('test_get_post', views.test_get_post),
]