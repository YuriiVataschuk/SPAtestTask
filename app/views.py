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

    def get(self, request):
        comments = Comment.objects.filter(parent_comment=None)  # Fetch top-level comments
        return render(request, self.template_name, {'comments': comments})

