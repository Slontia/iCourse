from django.dispatch import Signal, receiver
from .models import *
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from notifications.signals import notify

def post_is_followed(sender, **kwargs):
    #print(kwargs)
    created = kwargs['created']
    if(created == True):
        follow = kwargs['instance']
        #print(type(follow))
        message = {}
        message['actor'] = User.objects.get(id=follow.user_id)
        post = Post.objects.get(id=follow.post_id)
        if(post.main_follow_id != -1):
            message['recipient'] = User.objects.get(id=Follow.objects.get(id=post.main_follow_id).user_id)
            message['verb'] = u'%s 在你的贴子 %s 下发表了跟贴' % (message['actor'].username, post.title)
            message['action_object'] = follow
            notify.send(message['actor'], **message)

def follow_is_commented(sender, **kwargs):
    comment = kwargs['instance']
    message = {}
    message['actor'] = User.objects.get(id=comment.user_id)
    message['action_object'] = comment
    follow = Follow.objects.get(id=comment.follow_id)
    post = Post.objects.get(id=follow.post_id)
    if(comment.to_comment_id == -1):
        message['recipient'] = User.objects.get(id=follow.user_id)
        if(follow.is_main):
            message['verb'] = u'%s 评论了你的贴子 %s' % (message['actor'].username, post.title)
        else:
            message['verb'] = u'%s 评论了你在贴子 %s 下的跟贴' % (message['actor'].username, post.title)
    else:
        message['recipient'] = User.objects.get(id=comment.user_id)
        message['verb'] = u'%s 回复了你在贴子 %s 下的评论' % (message['actor'].username, post.title)
    notify.send(message['actor'], **message)

def follow_is_evaluated(sender, **kwargs):
    evaluate = kwargs['instance']
    message = {}
    message['actor'] = User.objects.get(id=evaluate.user_id)
    message['action_object'] = evaluate
    follow = Follow.objects.get(id=evaluate.follow_id)
    message['recipient'] = User.objects.get(id=follow.user_id)
    post = Post.objects.get(id=follow.post_id)
    if(evaluate.grade == 1):
        if(follow.is_main):
            message['verb'] = u'%s 赞了你的贴子 %s' % (message['actor'].username, post.title)
        else:
            message['verb'] = u'%s 赞了你在贴子 %s 下的跟贴' % (message['actor'].username, post.title)
    else:
        if(follow.is_main):
            message['verb'] = u'%s 踩了你的贴子 %s' % (message['actor'].username, post.title)
        else:
            message['verb'] = u'%s 踩了你在贴子 %s 下的跟贴' % (message['actor'].username, post.title)
    notify.send(message['actor'], **message)

post_save.connect(post_is_followed, sender=Follow)
post_save.connect(follow_is_commented, sender=Follow_Comment)
post_save.connect(follow_is_evaluated, sender=Follow_Evaluation)
