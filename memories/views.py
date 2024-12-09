from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from .models import Post, Favourite
from .forms import CommentForm, PostForm, EditPostForm
from django.views.generic import TemplateView, CreateView, UpdateView, DeleteView, ListView
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.http import JsonResponse

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
    # fields = ('title', 'theme', 'excerpt', 'content', 'post_image')
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
    # fields = ('theme', 'excerpt', 'content', 'post_image')
    def form_valid(self, form):
        form.instance.title = self.object.title  
        form.instance.slug = self.object.slug
        form.instance.author = self.object.author
        return super().form_valid(form)
    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    def handle_no_permission(self):
        messages.error(self.request, "You do not have permission to edit this post.")
        return redirect('home')
    def get_success_url(self):
        return reverse('post_detail', args=[self.object.slug])
    
class DeletePost(DeleteView):
    model = Post
    template_name = 'memories/delete_post.html'
    success_url = reverse_lazy('home')
    # THIS DOES NOT WORK? BUG DO I NEED THIS
    def delete(self, request, *args, **kwargs):
        """
        Override the delete method to add a success message.
        """
        response = super().delete(request, *args, **kwargs)  # Call the parent delete method
        messages.success(request, "Post deleted successfully.")  # Add the success message
        return response

def post_detail(request, slug):
    """
    Display an individual :model:`memories.Post`.

    **Context**

    ``post``
        An instance of :model:`memories.Post`.

    **Template:**

    :template:`memories/post_detail.html`
    """

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

class FavouritesListView(LoginRequiredMixin, ListView):
    """
    Displays the list of favourite blog posts for the logged-in user.
    """
    model = Favourite
    template_name = "memories/favourites_list.html"
    context_object_name = "favourites"

    def get_queryset(self):
        return Favourite.objects.filter(user=self.request.user).select_related('blog_post')


class AddToFavouritesView(LoginRequiredMixin, generic.View):
    """
    Handles adding a blog post to the user's favorites.
    """

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        blog_post = get_object_or_404(Post, id=post_id)
        favourite, created = Favourite.objects.get_or_create(user=request.user, blog_post=blog_post)
        if created:
            messages.success(request, f'"{blog_post.title}" has been added to your favourites.')
            return JsonResponse({'message': 'Added to favourites'}, status=201)
        return JsonResponse({'message': 'Already in favourites'}, status=200)


class RemoveFromFavouritesView(LoginRequiredMixin, generic.View):
    """
    Handles removing a blog post from the user's favourites.
    """

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        blog_post = get_object_or_404(Post, id=post_id)
        favourite = Favourite.objects.filter(user=request.user, blog_post=blog_post)
        if favourite.exists():
            favourite.delete()
            messages.success(request, f'"{blog_post.title}" has been removed from your favourites.')
            return JsonResponse({'message': 'Removed from favourites'}, status=200)
        return JsonResponse({'message': 'Not in favourites'}, status=404)
