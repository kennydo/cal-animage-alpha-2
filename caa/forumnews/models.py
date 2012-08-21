import datetime
import re

from django.db import models

from caa.officers.models import Officer

class Forum(models.Model):
    forum_id = models.IntegerField(primary_key=True)
    forum_name = models.CharField(max_length=255)
    left_id = models.IntegerField()
    right_id = models.IntegerField()

    class Meta:
        db_table = 'forum_forums'

class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=255)

    def real_name(self):
        try:
            return Officer.objects.get(nickname=self.username).name
        except Officer.DoesNotExist:
            return None

    class Meta:
        db_table = 'forum_users'

class Topic(models.Model):
    topic_id = models.IntegerField(primary_key=True)
    forum = models.ForeignKey(Forum)
    topic_title = models.CharField(max_length=255)
    topic_first_post = models.OneToOneField('Post', related_name='first_post_of_topic')

    class Meta:
        db_table = 'forum_topics'

class Post(models.Model):
    post_id = models.IntegerField(primary_key=True)
    topic = models.ForeignKey(Topic)
    forum = models.ForeignKey(Forum)
    poster = models.ForeignKey(User)
    post_approved = models.BooleanField(required=False)
    post_time = models.IntegerField()
    bbcode_uid = models.CharField(max_length=8)
    post_text = models.TextField()

    def datetime(self):
        return datetime.datetime.fromtimestamp(self.post_time)

    def num_comments(self):
        return self.first_post_of_topic.post_set..filter(post_approved=True).count() - 1

    def bbcode_text(self):
        text = self.post_text

        # BBCode adds a bbcode_uid string to each bbcode tag,
        # so we must get rid of it for the django-bbcode app to work.
        text = re.sub('\[([^\]]*):%s\]' % self.bbcode_uid, '[\\1]', text)

        # Our youtube format is [youtube]youtube_video_id[/youtube],
        # not the [youtube]http_youtube_url[/youtube] format the app
        # supports.
        text = re.sub('\[youtube\](\S+)\[/youtube\]',
                      '[youtube]http://www.youtube.com/watch?feature=player_embedded&v=\\1[/youtube]', text)

        # The bbcode template tag escapes things again, so un-escape
        text = text.replace('&amp;', '&').replace('&lt;', '<').replace('&gt;', '>').replace('&quot;', '"').replace('&#39;',"'")

        return text

    class Meta:
        db_table = 'forum_posts'
        ordering = ['-post_time']
