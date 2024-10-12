# Generated by Django 5.1.1 on 2024-10-06 14:31

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ChatRoom',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('chatroom_title', models.CharField(blank=True, max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('topic', models.CharField(choices=[('school_info', '학교정보'), ('pdf_questions', '교재관련질문'), ('QnA', '예상문제')], max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('user_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.CharField(choices=[('user', '사용자'), ('system', '시스템')], max_length=10)),
                ('text', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('chatroom', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='chat_app.chatroom')),
            ],
        ),
        migrations.AddField(
            model_name='chatroom',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chatrooms', to='chat_app.user'),
        ),
    ]
