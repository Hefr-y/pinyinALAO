from django.urls import path
from . import views
from django.views.decorators.csrf import csrf_exempt

urlpatterns = [
    path('', views.index, name="index"), # homepage

    path('hsk1_view', views.hsk1_view, name='hsk1_view'), # HSK1视图
    path('hsk1', views.hsk1, name='hsk1'), # HSK1判断返回页面

    # path('hsk2_view', views.hsk2_view, name='hsk2_view'), # HSK2视图
    path('hsk2', views.hsk2, name='hsk2'), # HSK2判断返回页面

    # path('hsk3_view', views.hsk3_view, name='hsk3_view'), # HSK3视图
    path('hsk3', views.hsk3, name='hsk3'), # HSK3判断返回页面

    # path('hsk4_view', views.hsk4_view, name='hsk4_view'), # HSK4视图
    # path('hsk4', views.hsk4, name='hsk4'), # HSK4判断返回页面
    path('pinyinDict/', views.pinyin_dict, name='pinyinDict'), # page de recherche


    # 测试 test
    # path('apprentissage/', views.boucle, name='test2'), # page de boucle
    # path('analyze_spacy/',views.analyze_spacy, name='analyze_spacy'),
    # path('analyze/', views.analyze),
    # path('test_request', views.test_request),
    # path('test_get_post', views.test_get_post),
]