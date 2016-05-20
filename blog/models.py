from django.db import models
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    #class 객체정의하는키워드
    #Post 모델=객체 (Post모델 = Post객체) 첫글자 대문자
    #models.Model은 Post가 장고모델(객체)임을 의미한다.
    #->장고가 Post가 DB에 저장되어야 된다는 것을 인지

    #속성정의를 위해 각 필드의 데이터 타입이 필요함
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200) #CharField글자수제한있는 텍스트정의.
    text = models.TextField() #TextField글자수 제한 없는 텍스트정의
    created_date = models.DateTimeField(default=timezone.now) #DateTimeField 날짜와 시간
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self): #def는 함수(Method) publish - Method이름
        self.published_date = timezone.now()
        self.save()

    def __str__(self): # __str__ Method
        return self.title #__str__를 호출하면 Post모델에 제목을 얻게됨
