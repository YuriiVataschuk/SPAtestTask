from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from app import views
from app.views import AddCommentView, CommentListView

app_name = "app"

urlpatterns = [
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('add_nested_comment/<int:parent_comment_id>/', AddCommentView.as_view(), name='add_nested_comment'),
    path('comment_list/', CommentListView.as_view(), name='comment_list'),
    path('comment_preview/', views.comment_preview, name='comment_preview'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += [
    path('media/files/<str:filename>/', views.serve_text_file, name='serve_text_file'),
]
