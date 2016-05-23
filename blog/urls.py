from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #post_list라는 name의 View에 문자열의 시작^과 끝$을 검색.
]
#자주쓰는 정규표현식
#^ 문자열이 시작할 떄
#$ 문자열이 끝날 때
#\d 숫자
#+ 바로 앞에 나오는 항목이 계속 나올 때
#() 패턴의 부분을 저장할 때
