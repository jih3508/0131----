from django.db import models

# Create your models here.
'''
Todo {
id: number; # 숫자, 자동 생성
title: string; # 문자열, 필수값
description: string; // 문자열, 필수 값,
is_completed: boolean; // 참불, 초깃값: false
created_at: Date; // 날짜, 생성시 자동 생성
updated_at: Date; // 날짜, 생성시 자동 생성, 수정시 자동 갱신,
}

Comment {
id: number; // 숫자, 자동 생성
contents: string; // 문자열, 필수
created_at: Date; // 날짜, 생성시 자동 생성
updated_at: Date; // 날짜, 생성시 자동 생성, 수정시 자동 갱신,
}
'''


class Todo(models.Model):
    id = models.BigAutoField(primary_key=True)
    title = models.CharField(max_length=200,null=False)
    description = models.CharField(max_length=200,null=False)
    id_completed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Comment(models.Model):
    id = models.BigAutoField(primary_key=True)
    contents = models.CharField(max_length=200,null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
