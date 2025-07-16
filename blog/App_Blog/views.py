from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, TemplateView, DeleteView
from .models import Blog, Comment, Like
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

# Create your views here.

class BlogList(ListView):
    model = Blog
    template_name = 'App_Blog/blog_list.html'
    context_object_name = 'blogs'
    ordering = ['-created_at']
    
class CreateBlog(LoginRequiredMixin, CreateView):
    model = Blog
    template_name = 'App_Blog/create_blog.html'
    fields = ('blog_title', 'content', 'blog_image')

    def form_valid(self, form):
        blog_obj = form.save(commit=False)
        blog_obj.author = self.request.user
        tittle = blog_obj.blog_title
        blog_obj.slug = tittle.replace(" ", "-") + "-" + str(uuid.uuid4())
        blog_obj.save()
        return HttpResponseRedirect(reverse('index'))


def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)

    return render(request, 'App_Blog/blog_details.html', context={'blog':blog})
