from turtle import home
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, Category, Profile, Comment
from .forms import EditForm, PostForm, CommentForm

# Create your views here.
#def home(request):
    #return render(request,'home.html',{})

class ShowProfilePage(DetailView):
    model = Profile
    template_name = 'registration/user_profile.html'

    def get_context_data(self, *args,**kwargs):
        #users = Profile.objects.all()
        context = super(ShowProfilePage, self).get_context_data(*args,**kwargs)
        page_user = get_object_or_404(Profile, id=self.kwargs['pk'])
        context["page_user"] = page_user
        return context

def LikePage(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    Liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        Liked = False
    else:
        post.likes.add(request.user)
        Liked = True

    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

class HomePage(ListView):
    model = Post
    template_name = 'homepage.html'
    ordering = ['-post_date']

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(HomePage, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu
        return context

class PostDetail(DetailView):
    model = Post
    template_name = 'homedetail.html'

    def get_context_data(self, *args,**kwargs):
        cat_menu = Category.objects.all()
        context = super(PostDetail, self).get_context_data(*args,**kwargs)
        context["cat_menu"] = cat_menu

        stuff = get_object_or_404(Post, id = self.kwargs['pk'])
        total_likes = stuff.total_likes
        
        Liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            Liked = True
        
        context["total_likes"] = total_likes
        context["Liked"] = Liked

        return context

class PostPage(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'postpage.html'
    #fields = '__all__'

class CommentPage(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'comment.html'
    #fields = '__all__'
    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        return super().form_valid(form)
    success_url = reverse_lazy('home')
    

class CategoryPage(CreateView):
    model = Category
    form_class = PostForm
    template_name = 'categorypage.html'
    #fields = '__all__'

def Categories(request,cats):
    category_post = Post.objects.filter(category=cats.replace('-', ' '))
    return render(request,'categories.html',{'cats':cats.title().replace('-', ' '), 'category_post':category_post})

def Category_list(request):
    cat_menu_list = Category.objects.all()
    return render(request,'category_list.html',{'cat_menu_list':cat_menu_list})

class EditPage(UpdateView):
    model = Post
    form_class = EditForm
    template_name = 'edit_post.html'
    #fields = ['title', 'body']

class DeletePost(DeleteView):
    model = Post
    template_name = 'deletepage.html'
    success_url = reverse_lazy('home')
