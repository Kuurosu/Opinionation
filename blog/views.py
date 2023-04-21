from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm
from django.contrib.auth.mixins import LoginRequiredMixin


class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class PostDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        disliked = False
        if post.dislikes.filter(id=self.request.user.id).exists():
            disliked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "liked": liked,
                "disliked": disliked,
                "comment_form": CommentForm
            },
        )


class PostLike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostDislike(View):
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)

        if post.dislikes.filter(id=request.user.id).exists():
            post.dislikes.remove(request.user)
        else:
            post.dislikes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class PostUpdate(View):
    def get_object(self, slug):
        post = get_object_or_404(Post, slug=slug)
        return post

    def get(self, request, slug):
        post = self.get_object(slug=slug)
        if request.user.is_staff:
            form = PostForm(instance=post)
            return render(
                request,
                'post_update.html',
                {'form': form, 'post': post}
                )
        else:
            raise Http404

    def post(self, request, slug):
        post = self.get_object(slug=slug)
        if request.user.is_staff:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return redirect('post_detail', slug=post.slug)
            else:
                return render(
                    request,
                    'post_update.html',
                    {'form': form, 'post': post}
                    )
        else:
            raise Http404


class PostDeleteView(LoginRequiredMixin, View):
    def get_object(self, slug):
        post = get_object_or_404(Post, slug=slug)
        return post

    def get(self, request, slug):
        post = self.get_object(slug=slug)
        if request.user.is_staff:
            return render(
                request,
                'post_delete.html',
                {'post': post}
            )
        else:
            raise Http404

    def post(self, request, slug):
        post = self.get_object(slug=slug)
        if request.user.is_staff:
            post.delete()
            return redirect('home')
        else:
            raise Http404
