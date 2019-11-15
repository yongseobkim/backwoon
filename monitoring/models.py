from django.db import models

# Create your models here.


class Data(models.Model):
    a_rdate = models.DateField()
    fwc_num = models.CharField(max_length=30, null=True, blank=True)

    car_id = models.CharField(max_length=30, null=True, blank=True)
    car_num1 = models.CharField(max_length=20, null=True, help_text="원차량번호")
    car_num2 = models.CharField(max_length=20, null=True, help_text="반납차량번호")
    car_num3 = models.CharField(max_length=20, null=True, help_text="변경차량호")
    car_type = models.CharField(max_length=100, null=True, blank=True)
    car_model = models.CharField(max_length=100, null=True, blank=True)
    car_sdate = models.DateField(null=True, blank=True)
    car_year = models.CharField(max_length=10, null=True, blank=True)
    car_cor = models.CharField(max_length=20, null=True, blank=True)
    car_price = models.IntegerField(default=0)
    car_dc = models.IntegerField(default=0)
    car_ms = models.CharField(max_length=10, null=True, blank=True)
    car_ap = models.CharField(max_length=200, null=True, blank=True)
    car_ap2 = models.CharField(max_length=200, null=True, blank=True)
    car_acd = models.CharField(max_length=150, null=True, blank=True)

    fwc_sdate = models.DateField(null=True, blank=True)
    fwc_stdprice = models.IntegerField(default=0)
    fwc_limm = models.IntegerField(default=0, null=True, blank=True)
    fwc_pr_code = models.CharField(max_length=10, null=True, blank=True)
    fwc_pt_dept = models.CharField(max_length=20, null=True, blank=True)
    fwc_pt_dept_mgr = models.CharField(max_length=20, null=True, blank=True)
    fwc_3pt = models.CharField(max_length=20, null=True, blank=True)

    a_limm = models.IntegerField(default=0)
    cus_name = models.CharField(max_length=100, null=True, blank=True)
    cus_add = models.CharField(max_length=100, null=True, blank=True)
    cus_add2 = models.CharField(max_length=100, null=True, blank=True)
    a_type = models.CharField(max_length=20, null=True, blank=True)
    a_mgr = models.CharField(max_length=20, null=True, blank=True)
    a_spot = models.CharField(max_length=100, null=True, blank=True)
    a_move = models.CharField(max_length=30, null=True, blank=True)
    text = models.TextField(blank=True, null=True)


from django.contrib.auth.models import User
from django.urls import reverse

class MassBoard(models.Model):
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='mass_board')
    fdate = models.DateField(blank=True, null=True, verbose_name="반납(예정)일", help_text="날짜 형식은 'YYYY-MM-DD' 입니다.")
    cus = models.CharField(max_length=50, blank=True, null=True, verbose_name="고객명")
    car = models.CharField(max_length=50, blank=True, null=True, verbose_name="차명")
    num = models.IntegerField(default=0, verbose_name="대수")
    spot = models.CharField(max_length=50, blank=True, null=True, verbose_name="반납(예정)지")
    text = models.TextField(blank=True, null=True, verbose_name="비고")
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-fdate']
        verbose_name = 'mass'
        verbose_name_plural = 'mass'

    def get_absolute_url(self):
        return reverse('monitoring:mass_board', args = [str(self.id)])
