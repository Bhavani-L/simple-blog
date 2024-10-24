from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post,Category
from .forms import PostForm ,EditForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect

# Create your views here.

# def home(request):
#     return render(request,'home.html',{})

class HomeView(ListView):
    model=Post
    template_name='home.html'
    context_object_name='post'
    # ordering=['-id']

    def get_context_data(self,*args, **kwargs) :
        cat_menu=Category.objects.all()
        context=super(HomeView,self).get_context_data(*args, **kwargs)
        context["cat_menu"]=cat_menu
        return context
    
def LikeView(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.likes.filter(id=request.user.id).exists():
        post.likes.remove(request.user)
        liked = False
    else:
        post.likes.add(request.user)
        liked = True

    return HttpResponseRedirect(reverse('article-details', args=[str(pk)]))
       
class ArticleDetailedView(DetailView):
    model=Post
    context_object_name='post'
    template_name='article_details.html'

    def get_context_data(self, *args, **kwargs):
        cat_menu = Category.objects.all()
        context = super(ArticleDetailedView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked = True

        context["cat_menu"] = cat_menu
        context["total_likes"] = total_likes
        context["liked"] = liked
        return context
    
def CategoryListView(request):
    category_menu_list=Category.objects.all()
    return render(request,'category_list.html',{'category_menu_list':category_menu_list})


def CategoryView(request,cats):
    category_posts=Post.objects.filter(category=cats.replace('-',' '))
    return render(request,'categories.html',{'cats': cats.title().replace('-',' '),'category_posts':category_posts})

class AddPostView(CreateView):
    model=Post
    form_class=PostForm
    template_name='add_post.html'
    # fields='__all__'
    # fields=('title','body')
    
class AddCategoryView(CreateView):
    model=Category
    # form_class=PostForm
    template_name='add_category.html'
    fields='__all__'
    # fields=('title','body')    

class UpdatePostView(UpdateView):
    model=Post
    # fields=['title','title_tag','body']
    form_class=EditForm
    template_name='update_post.html'

class DeletePostView(DeleteView):
    model=Post
    template_name='delete_post.html'
    success_url=reverse_lazy('home')