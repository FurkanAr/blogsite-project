from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import FormView
from . forms import ContactForm
from post.models import Post


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.order_by('-publishing_date')[:2]
        return context


class AboutView(TemplateView):
    template_name='about.html'

# def about(request):
#     return render(request, 'about.html')

class ContactView(SuccessMessageMixin, FormView):
    template_name='contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('contact')
    success_message = 'We received your message'
    def form_valid(self,form):
        form.save()
        return super().form_valid(form)