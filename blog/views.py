from django.shortcuts import render
from django.utils import timezone
from .models import Post
#장고ORM을 이용하여 쿼리셋을 화면에 나타낼 수 있게 코딩하는중
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    #쿼리셋을 나타내는 변수를 만드는 중
    return render(request, 'blog/post_list.html', { 'posts': posts})
    #'posts':posts로 넘겨주는것 parameter값
