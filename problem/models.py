# coding=utf-8
from django.db import models

from account.models import User


class ProblemTag(models.Model):
    pass


class AbstractProblem(models.Model):
    # 标题
    title = models.CharField(max_length=50)
    # 问题描述 HTML 格式
    description = models.TextField()
    # 样例输入 可能会存储 json 格式的数据
    sample_input = models.TextField(blank=True)
    # 样例输出 同上
    sample_output = models.TextField(blank=True)
    # 测试用例id 这个id 可以用来拼接得到测试用例的文件存储位置
    test_case_id = models.CharField(max_length=40)
    # 提示
    hint = models.TextField(blank=True)
    # 创建时间
    create_time = models.DateTimeField(auth_now_add=True)
    # 最后更新时间
    last_update_time = models.DateTimeField(auto_now=True)
    # 这个题是谁创建的
    created_by = models.ForeignKey(User)
    # 来源
    source = models.CharField(max_length=30, blank=True)
    # 时间限制 单位是毫秒
    time_limit = models.IntegerField()
    # 内存限制 单位是MB
    memory_limit = models.IntegerField()
    # 是否可见 false的话相当于删除
    visible = models.BooleanField(default=True)
    # 总共提交数量
    total_submit_number = models.IntegerField(default=0)
    # 通过数量
    total_accepted_number = models.IntegerField(default=0)
    # 标签
    tags = models.ManyToManyField(ProblemTag, null=True)
    # 难度 0 - n
    difficulty = models.IntegerField()

    class Meta:
        abstract = True


class Problem(AbstractProblem):
    pass