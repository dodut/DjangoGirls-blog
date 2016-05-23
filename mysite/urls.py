from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #admin/으로 시작하는 모든URL을 장고가 view와 대조해 찾아낸다.
    url(r'', include('blog.urls')),
    #http://127.0.0.1:8000/으로 들어오는 모든 접속요청을 blog.urls로 전송하고 추가하는 명령을 찾는다.
    #파이썬에서 정규표현식을 넣을때 항상 문자열 앞에 r을 붙인다(특수문자가 있을 수 있다는것을 알려줌)
]

#^post/(/d+)/$
#^post/ url시작점 오른쪽부터 post/가 있다
#(\d+)는 숫자가 있다. 뽑아내고자 하는 글 번호
#/뒤에 문자가 있음
#$는 URL의 끝이 방금전에 있던 /로 끝나야 매칭될 수 있다는 것을 나타냄.
