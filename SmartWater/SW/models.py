from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
"""
创建学生信息表模型
"""
from django.db import models

"""
 该类是用来生成数据库的 必须要继承models.Model
"""
class model_sensor(models.Model):
    """
    创建如下几个表的字段
    """
    # 学号 primary_key=True: 该字段为主键
    SW_id = models.CharField('设备ID', primary_key=True,null=False, max_length=50)

    SW_num = models.CharField('数值', null=False, max_length=50)
    SW_type = models.CharField('设备类型', max_length=25)
    SW_power = models.CharField('设备电量', max_length=25)
    # 姓名 字符串 最大长度20
    SW_status= models.CharField('设备状态', max_length=25)
    # 年龄 整数 null=False, 表示该字段不能为空

    # 性别 布尔类型 默认True: 男生 False:女生


    # 指定表名 不指定默认APP名字——类名(app_demo_Student)
    # class Meta:
    #     db_table = 'student'

