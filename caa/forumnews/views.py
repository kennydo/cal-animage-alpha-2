from django.conf import settings
from django.views.generic import ListView

from caa.forumnews.models import Forum, Topic, Post

class NewsPostsList(ListView):
    template_name = 'news_list.html'
    paginate_by = 6
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.using('forum').filter(
                first_post_of_topic__forum_id=settings.NEWS_FORUM_ID)
