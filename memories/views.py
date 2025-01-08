from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.contrib import messages
from django.views.generic import TemplateView, CreateView, UpdateView
from django.views.generic import DeleteView, ListView
from django.urls import reverse
from django.utils.text import slugify
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.http import JsonResponse
from django.shortcuts import HttpResponseRedirect
from .models import Post, Favourite, Comment
from .forms import CommentForm, PostForm, EditPostForm

# Create your views here.


class PostList(generic.ListView):
    """
    View to display a list of published posts on the homepage.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "memories/home.html"


class PostLists(generic.ListView):
    """
    View to display a paginated list of published posts on the 'memories' page.
    """
    queryset = Post.objects.filter(status=1)
    template_name = "memories/memories.html"
    paginate_by = 6


class AboutView(TemplateView):
    """
    View to display the 'About' page.
    """
    template_name = 'memories/about.html'


class AddPost(LoginRequiredMixin, CreateView):
    """
    View for authenticated users to create a new post.
    """
    model = Post
    form_class = PostForm
    template_name = 'memories/create_post.html'

    def form_valid(self, form):
        """
        Sets the author, slug, and status of the post before saving.
        """
        form.instance.author = self.request.user
        form.instance.slug = slugify(form.instance.title)
        form.instance.status = 0
        messages.success(self.request, "Post created and awaiting approval.")
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to a 'post pending' page upon successful form submission.
        """
        return reverse('post_pending')


class PendingPostView(TemplateView):
    """
    View to display a 'post pending approval' page.
    """
    template_name = 'memories/post_pending.html'


class UpdatePost(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for authenticated users to update their own posts.
    """
    model = Post
    form_class = EditPostForm
    template_name = 'memories/edit_post.html'

    def form_valid(self, form):
        """
        Add a success message when the post is updated.
        """
        messages.success(self.request, f'"{
            self.object.title}" has been successfully updated.')
        return super().form_valid(form)

    def test_func(self):
        """
        Verify that the logged-in user is the author of the post.
        """
        return self.request.user == self.get_object().author

    def handle_no_permission(self):
        """
        Handle cases where the user does not have permission to update the post
        """
        messages.error(
            self.request, "You do not have permission to edit this post.")
        return redirect('home')

    def get_success_url(self):
        """
        Redirect to the updated post's detail page upon success.
        """
        return reverse('post_detail', args=[self.object.slug])


class DeletePost(LoginRequiredMixin, UserPassesTestMixin,
                 SuccessMessageMixin, DeleteView):
    """
    View for authenticated users to delete their own posts.
    """
    model = Post
    template_name = 'memories/delete_post.html'
    success_url = reverse_lazy('memories')

    def form_valid(self, form):
        """
        Add a success message when the post is deleted.
        """
        messages.success(self.request, f'"{
            self.object.title}" has been successfully deleted.')
        return super().form_valid(form)

    def test_func(self):
        """
        Verify that the logged-in user is the author of the post.
        """
        post = self.get_object()
        return self.request.user == post.author

    def handle_no_permission(self):
        """
        Handle cases where the user does not have permission to delete the post
        """
        messages.error(
            self.request, "You do not have permission to delete this post.")
        return redirect('home')
    

def post_detail(request, slug):
    """
    View to display the details of a specific post, including its comments.
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
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )
            return HttpResponseRedirect(request.path_info)

    comment_form = CommentForm()

    return render(
        request,
        "memories/post_detail.html",
        {
            "post": post,
            "comments": comments,
            "comment_count": comment_count,
            "comment_form": comment_form,
        }
    )


class EditComment(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """
    View for authenticated users to edit their own comments.
    """
    model = Comment
    form_class = CommentForm
    template_name = 'memories/edit_comment.html'

    def test_func(self):
        """
        Verify that the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author

    def form_valid(self, form):
        """
        Add a success message when the comment is updated.
        """
        messages.success(self.request, "Your comment has been updated.")
        return super().form_valid(form)

    def get_success_url(self):
        """
        Redirect to the related post's detail page upon success.
        """
        return reverse('post_detail', args=[self.object.post.slug])


class DeleteComment(LoginRequiredMixin, UserPassesTestMixin,
                    SuccessMessageMixin, DeleteView):
    """
    View for authenticated users to delete their own comments.
    """
    model = Comment
    template_name = 'memories/delete_comment.html'
    success_message = "Your comment has been deleted."

    def test_func(self):
        """
        Verify that the logged-in user is the author of the comment.
        """
        comment = self.get_object()
        return self.request.user == comment.author

    def get_success_url(self):
        """
        Redirect to the related post's detail page upon success.
        """
        return reverse('post_detail', args=[self.object.post.slug])


class FavouritesListView(LoginRequiredMixin, ListView):
    """
    View to display a list of posts that the user
    has added to their favourites.
    """
    model = Favourite
    template_name = "memories/favourites_list.html"
    context_object_name = "favourites"

    def get_queryset(self):
        """
        Return a queryset of the user's favourites,
        including related post data.
        """
        return Favourite.objects.filter(
            user=self.request.user).select_related('blog_post')


class AddToFavouritesView(LoginRequiredMixin, generic.View):
    """
    View to add a specific post to the user's favourites.
    """
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        blog_post = get_object_or_404(Post, id=post_id)
        favourite, created = Favourite.objects.get_or_create(
            user=request.user, blog_post=blog_post)
        if created:
            messages.success(request, f'"{
                blog_post.title}" has been added to your favourites.')
        else:
            messages.info(request, f'"{
                blog_post.title}" is already in your favourites.')
        return self.get_success_url()

    def get_success_url(self):
        """
        Redirect to the favourites list page.
        """
        return redirect('favourites_list')


class RemoveFromFavouritesView(LoginRequiredMixin, generic.View):
    """
    View to remove a specific post from the user's favourites.
    """
    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        blog_post = get_object_or_404(Post, id=post_id)
        favourite = Favourite.objects.filter(
            user=request.user, blog_post=blog_post)
        if favourite.exists():
            favourite.delete()
            messages.success(request, f'"{
                blog_post.title}" has been removed from your favourites.')
        else:
            messages.info(request, f'"{
                blog_post.title}" was not in your favourites.')
        return self.get_success_url()

    def get_success_url(self):
        """
        Redirect to the favourites list page.
        """
        return redirect('favourites_list')


def custom_404(request, exception):
    """
    Custom view for handling 404 errors.
    """
    return render(request, 'memories/404.html', status=404)


def custom_500(request):
    """
    Custom view for handling 500 errors.
    """
    return render(request, 'memories/500.html', status=500)
