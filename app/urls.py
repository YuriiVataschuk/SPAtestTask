from django.urls import path
from .views import AddCommentView, CommentListView


urlpatterns = [
    path('add_comment/', AddCommentView.as_view(), name='add_comment'),
    path('add_comment/<int:parent_comment_id>/', AddCommentView.as_view(), name='add_nested_comment'),
    path('comment_list/', CommentListView.as_view(), name='comment_list'),
]