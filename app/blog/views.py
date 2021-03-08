from django.shortcuts import render
from django.views import generic 
from blog.models import Post, Category


def index(request):

    try:
        category = Category.objects.all()
    except:
        return render(request, 'info_missing.html')
    else:
        context = {
            'categories': category
        }

    return render(request, 'blog/index.html', context)

class PostListView(generic.ListView):
    context_object_name = 'post_list'
    template_name = 'post_list.html'
    paginate_by = '4'
    def get_queryset(self):
        return Post.objects.all()
    
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
