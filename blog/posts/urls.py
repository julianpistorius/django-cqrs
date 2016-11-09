from django.conf.urls import url

from posts.views import PostView, EditPostView


urlpatterns = [
    url(r'^edit/(?P<id>[0-9-]+)', EditPostView.as_view()),
    url(r'^', PostView.as_view()),
]
