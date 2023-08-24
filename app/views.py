from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.views import View
from .models import Comment
from .forms import CommentForm
from PIL import Image, ImageOps


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
        form = CommentForm(request.POST, request.FILES)
        comment = None
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            email = form.cleaned_data['email']
            text = form.cleaned_data['text']
            image = form.cleaned_data['image']
            text_file = form.cleaned_data['text_file']

            if parent_comment:
                comment = Comment(
                    parent_comment=parent_comment,
                    user_name=user_name,
                    email=email,
                    text=text,
                    image=image,
                    text_file=text_file
                )
            else:
                comment = Comment(
                    user_name=user_name,
                    email=email,
                    text=text,
                    image=image,
                    text_file=text_file
                )

            comment.save()

            if comment.image:
                max_width = 320
                max_height = 240
                image = Image.open(comment.image.path)
                image = ImageOps.fit(image, (max_width, max_height), Image.Resampling.BICUBIC)
                image.save(comment.image.path)

            return redirect('app:comment_list')
        return render(request, self.template_name, {'form': form, 'parent_comment': parent_comment})


class CommentListView(View):
    template_name = 'comment_list.html'
    page_size = 25

    def get(self, request):
        sort_by = request.GET.get('sort_by', '-timestamp')
        allowed_sort_fields = ['user_name', 'email', 'timestamp']
        if sort_by not in allowed_sort_fields:
            sort_by = '-timestamp'

        comments = Comment.objects.filter(parent_comment=None).order_by(sort_by)

        paginator = Paginator(comments, self.page_size)
        page_number = request.GET.get('page')
        page_comments = paginator.get_page(page_number)

        return render(request, self.template_name, {'page_comments': page_comments, 'sort_by': sort_by})

    def post(self, request):
        comment_id = request.POST.get('comment_id')
        comment = Comment.objects.get(pk=comment_id)

        image_file = request.FILES.get('image')
        text_file = request.FILES.get('text_file')

        comment.image = image_file
        comment.text_file = text_file
        comment.save()

        return redirect('app:comment_list')
