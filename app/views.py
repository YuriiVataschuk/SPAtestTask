from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from .models import Comment
from .forms import CommentForm


class AddCommentView(View):
    template_name = 'add_comment.html'

    def get(self, request, parent_comment_id=None):
        parent_comment = None
        if parent_comment_id:
            parent_comment = Comment.objects.get(pk=parent_comment_id)
        form = CommentForm()
        return render(request, self.template_name, {'form': form, 'parent_comment': parent_comment})

    def post(self, request, parent_comment_id=None):
        parent_comment = None
        if parent_comment_id:
            parent_comment = Comment.objects.get(pk=parent_comment_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.parent_comment = parent_comment
            comment.save()
            return redirect('comment_list')  # Redirect to the comment list view
        return render(request, self.template_name, {'form': form, 'parent_comment': parent_comment})


class CommentListView(View):
    template_name = 'comment_list.html'
    page_size = 25

    def get(self, request):
        sort_by = request.GET.get('sort_by', '-timestamp')  # Change 'date_added' to 'timestamp'
        allowed_sort_fields = ['user_name', 'email', 'timestamp']  # Add other allowed sort fields
        if sort_by not in allowed_sort_fields:
            sort_by = '-timestamp'  # Default to sorting by timestamp

        comments = Comment.objects.filter(parent_comment=None).order_by(sort_by)

        paginator = Paginator(comments, self.page_size)
        page_number = request.GET.get('page')
        page_comments = paginator.get_page(page_number)

        return render(request, self.template_name, {'page_comments': page_comments, 'sort_by': sort_by})
