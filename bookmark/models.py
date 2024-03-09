from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름: " + self.site_name + ", 주소: " + self.url
    
    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])   # 특정 작업이 성공하면 이동할 페이지 인듯, views.py의 success_url 또는 model.py의 get_absolute_url 메서드를 통해 결정된다.
        # 자동완성: return reverse("model_detail", kwargs={"pk": self.pk})
        # reverse : URL 패턴의 이름과 추가 인자를 전달받아 URL을 생성하는 메서드
    