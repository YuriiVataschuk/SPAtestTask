from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from app.views import AddCommentView, CommentListView

app_name = "app"

urlpatterns = [
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('add_nested_comment/<int:parent_comment_id>/', AddCommentView.as_view(), name='add_nested_comment'),
    path('comment_list/', CommentListView.as_view(), name='comment_list'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
