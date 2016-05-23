from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    #post_list라는 name의 View에 문자열의 시작^과 끝$을 검색.
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    #^는 시작/ url이 post를 포함하는 경우
    #모든변수를 pk변수에 넣어 뷰로 전송하겠다 +는 하나이상의 숫자가 와야함
    #http://127.0.0.1:8000/post//는 안되지만
    #http://127.0.0.1:8000/post/1231232/는 가능하다는 이야기
    # /는 마지막에 /가 한번더 와야한다는 의미
    # $마지막이라는 의미 뒤로 더이상 문자가 오면 안된다.
# ex) http://127.0.0.1:8000/post/5/의 경우 pk가 5와 일치하는 view로 정보를 보내게 된다


]
#자주쓰는 정규표현식
#^ 문자열이 시작할 떄
#$ 문자열이 끝날 때
#\d 숫자
#+ 바로 앞에 나오는 항목이 계속 나올 때
#() 패턴의 부분을 저장할 때
