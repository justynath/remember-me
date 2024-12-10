from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Favourite, Comment
from .forms import CommentForm, PostForm, EditPostForm
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect


# Create your views here.

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "memories/home.html"
    
class PostLists(generic.ListView):
    queryset = Post.objects.filter(status=1)
    template_name = "memories/memories.html"
    paginate_by = 6

class AboutView(TemplateView):
    template_name = 'memories/about.html'
    
class AddPost(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'memories/create_post.html'
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.instance.status = 0
        return super().form_valid(form)
    def get_success_url(self):
        if self.object.status == 0:  
            return reverse('post_pending') 
        return reverse('post_detail', args=[self.object.slug])
class PendingPostView(TemplateView):
    template_name = 'memories/post_pending.html'
    
class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = EditPostForm
    template_name = 'memories/edit_post.html'
    def form_valid(self, form):
        form.instance.title = self.object.title  
        form.instance.slug = self.object.slug
        form.instance.author = self.object.author
        messages.success(self.request, f'"{self.object.title}" has been successfully updated.')
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to edit this post.")
        return redirect('home')
    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])
    

class DeletePost(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'memories/delete_post.html'
    success_url = reverse_lazy('memories') 
    def delete(self, request, *args, **kwargs):
        response = super().delete(request, *args, **kwargs)
        messages.success(request, f'"{self.object.title}" has been successfully deleted.')
        return response
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to delete this post.")
        return redirect('home')


def post_detail(request, slug):

    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("-created_on")
    comment_count = post.comments.filter(approved=True).count()
    
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,'Comment submitted and awaiting approval'
    )
            # Redirect to avoid form resubmission
            return HttpResponseRedirect(request.path_info)

  
    comment_form = CommentForm()

    return render(
        request,
        "memories/post_detail.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,
        }
    )

class EditComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Comment
    form_class = CommentForm
    template_name = 'memories/edit_comment.html'
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    def form_valid(self, form):
        messages.success(self.request, "Your comment has been updated.")
        return super().form_valid(form)
    def get_success_url(self):
        return reverse('post_detail', args=[self.object.post.slug])

class DeleteComment(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Comment
    template_name = 'memories/delete_comment.html'
    def test_func(self):
        comment = self.get_object()
        return self.request.user == comment.author
    def delete(self, request, *args, **kwargs):
        messages.success(self.request, "Your comment has been deleted.")
        return super().delete(request, *args, **kwargs)
    def get_success_url(self):
        return reverse('post_detail', args=[self.object.post.slug])

class FavouritesListView(LoginRequiredMixin, ListView):
    model = Favourite
    template_name = "memories/favourites_list.html"
    context_object_name = "favourites"

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user).select_related('blog_post')

class AddToFavouritesView(LoginRequiredMixin, generic.View):
    
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        blog_post = get_object_or_404(Post, id=post_id)
        favourite, created = Favourite.objects.get_or_create(user=request.user, blog_post=blog_post)
        if created:
            messages.success(request, f'"{blog_post.title}" has been added to your favourites.')
        else:
            messages.info(request, f'"{blog_post.title}" is already in your favourites.')
        return self.get_success_url()
    
    def get_success_url(self):
        return redirect('favourites_list')

class RemoveFromFavouritesView(LoginRequiredMixin, generic.View):
    
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        blog_post = get_object_or_404(Post, id=post_id)
        favourite = Favourite.objects.filter(user=request.user, blog_post=blog_post)
        if favourite.exists():
            favourite.delete()
            messages.success(request, f'"{blog_post.title}" has been removed from your favourites.')
        else:
            messages.info(request, f'"{blog_post.title}" was not in your favourites.')
        return self.get_success_url()
    
    def get_success_url(self):
        return redirect('favourites_list')
