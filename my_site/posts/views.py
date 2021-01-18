from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from groups.models import *
from django.http import Http404
from django.views.generic import *

from django.core.paginator import Paginator

from braces.views import SelectRelatedMixin
from django.contrib import messages

from .import models,forms

from django.contrib.auth import get_user_model
User = get_user_model()

# Create your views here.

class PostList(SelectRelatedMixin,ListView):
    model = models.Post
    select_related = ('user','group')
    

    paginate_by = 5

    """
    def post_list(request):
        post_list = models.Post.objects.order_by('-date_added')
        # keywords
        # city
        post_list = models.Post.objects.filter(title__contains = request.search)

        paginator = Paginator(post_list, 2) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        # print(context['request'])
        context = {'post_list': post_list,'page_obj':page_obj
                }
        return render(request, 'post/post_list.html', context)


    def get_queryset(self,request):
        super(PostList, self,request).get_queryset()
        #super().get_queryset(self,request)
        if request.method == 'POST':
            word = request.POST.get('search')
        try:
            print("workinggggg")
            self.post_list = models.Post.objects.filter(title__contains = word)
        except:
            print(word+"not workingggggg")
            raise Http404
        else:
            return self.post_list.posts.all()
            #  post_lis = models.Post.objects.all
    """

    def searchart(request):	
        if request.method == 'POST':	    
            word = request.POST.get('search')
            try:
                print("workinggggg")
                post_lis = models.Post.objects.filter(title__contains = word)
            except:
                print(word+"not workingggggg")
                raise Http404
            else:
                pass
            pos_list = {'post_list':post_lis,'word':word}
            return render(request,'posts/post_search.html',context=pos_list)

class UserPosts(ListView):
    model = models.Post
    template_name = 'posts/user_post_list.html'


    def get_queryset(self):
        try:
            self.post_user = User.objects.prefetch_related('posts').get(username__iexact=self.kwargs.get('username'))
        except User.DoesNotExist:
            raise Http404
        else:
            return self.post_user.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_user'] = self.post_user
        return context


class Group1Posts(ListView):
    model = models.Post
    template_name = 'posts/post_list.html'
    
    paginate_by = 5


    def get_queryset(self):
        try:
            self.post_name = Group.objects.prefetch_related('posts').get(name__iexact="Covid 19")
        except Group.DoesNotExist:
            raise Http404
        else:
            return self.post_name.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_name'] = self.post_name
        return context

class Group2Posts(ListView):
    model = models.Post
    template_name = 'posts/post_list.html'

    paginate_by = 5

    def get_queryset(self):
        try:
            self.post_name = Group.objects.prefetch_related('posts').get(name__iexact="Astronomy")
        except Group.DoesNotExist:
            raise Http404
        else:
            return self.post_name.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_name'] = self.post_name
        return context


class Group3Posts(ListView):
    model = models.Post
    template_name = 'posts/post_list.html'

    paginate_by = 5

    def get_queryset(self):
        try:
            self.post_name = Group.objects.prefetch_related('posts').get(name__iexact="Sciences")
        except Group.DoesNotExist:
            raise Http404
        else:
            return self.post_name.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_name'] = self.post_name
        return context


class Group4Posts(ListView):
    model = models.Post
    template_name = 'posts/post_list.html'

    paginate_by = 5


    def get_queryset(self):
        try:
            self.post_name = Group.objects.prefetch_related('posts').get(name__iexact="Medical Sciences")
        except Group.DoesNotExist:
            raise Http404
        else:
            return self.post_name.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_name'] = self.post_name
        return context

class Group5Posts(ListView):

    model = models.Post
    template_name = 'posts/post_list.html'

    paginate_by = 5

    def get_queryset(self):
        try:
            self.post_name = Group.objects.prefetch_related('posts').get(name__iexact="Technology")
        except Group.DoesNotExist:
            raise Http404
        else:
            return self.post_name.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_name'] = self.post_name
        return context

class Group6Posts(ListView):
    model = models.Post
    template_name = 'posts/post_list.html'
    paginate_by = 5


    def get_queryset(self):
        try:
            self.post_name = Group.objects.prefetch_related('posts').get(name__iexact="Economics")
        except Group.DoesNotExist:
            raise Http404
        else:
            return self.post_name.posts.all()

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['post_name'] = self.post_name
        return context



class PostDetail(SelectRelatedMixin,DetailView):
    model = models.Post
    select_related = ('user','group')
    template_name = 'posts/post_detail.html'
    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user__username__iexact=self.kwargs.get('username'))



class CreatePost(LoginRequiredMixin,SelectRelatedMixin,CreateView):
    fields = ('title','content','group')
    model = models.Post

    template_name = "posts/post_form.html"

    def form_valid(self,form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        #form.save()
        self.object.save()
        return super().form_valid(form)


class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = models.Post
    fields = ['title', 'content']

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False


class DeletePost(LoginRequiredMixin,SelectRelatedMixin,DeleteView):
    model = models.Post
    select_related = ('user','group')
    success_url = reverse_lazy('posts:all')

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(user_id = self.request.user.id)

    def delete(self,*args,**kwargs):
        messages.success(self.request,'Post Deleted')
        return super().delete(*args,**kwargs)
