import datetime
from datetime import date, timedelta
from django.shortcuts import redirect
from django.shortcuts import render
from django.views import generic 
from blog.models import Post, Category

from .forms import PostForm

def index(request):

    try:
        category = Category.objects.all()
        post = Post.objects.all()
    except:
        return render(request, 'blog/info_missing.html')
    else:
        context = {
            'categories': category,
            'posts': post,

        }

    return render(request, 'blog/index.html', context)


def post_new(request):
     if request.method == "POST":
         form = PostForm(request.POST)
         if form.is_valid():
             post = form.save(commit=False)
             post.author = request.user
             post.published_date =  datetime.datetime.now()
             post.save()
             return redirect('blog:post', pk=post.pk)
     else:
         form = PostForm()
     return render(request, 'blog/post_edit.html', {'form': form})


class PostListView(generic.ListView):
    context_object_name = 'post_list'
    template_name = 'blog/post_list.html'
    paginate_by = '4'

    def get_queryset(self):
        startdate = date.today()
        enddate = startdate + timedelta(days=6)
        posts = Post.objects.filter(created__range=[startdate, enddate])

        return posts
    
    def get_context_data(self, **kwargs):
        context=super(PostListView, self).get_context_data(**kwargs)
        context['category_list'] = Category.objects.all()
        return context
    

class PostDetailView(generic.DetailView):
    model = Post
    template_name = 'blog/post_detail.html'



class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = 'blog/category_detail.html'
