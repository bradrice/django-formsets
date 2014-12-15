from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.forms.models import inlineformset_factory
from django.core.urlresolvers import reverse_lazy, reverse
from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, View
from models import Author, Book
from forms import AuthorForm, BookForm, BookFormset
from django.forms.models import inlineformset_factory

# Create your views here.

class AuthorCreate(CreateView):
	model = Author
	form_class = AuthorForm
	template_name = 'author_template.html'
	success_url = u"/dp/book_create/"

	def form_valid(self, form):
		# override the ModelFormMixin definition so you don't save twice
		obj = form.save()
	 	return HttpResponseRedirect(reverse('dp:book_create', kwargs={'author_id': obj.id}))

	def form_invalid(self, formset):
		return self.render_to_response(self.get_context_data(form=form, formset=formset))


class Thanks(View):

	def get(self, request):
		return HttpResponse('Thanks')


class BookCreate(CreateView):
	model = Book
	form_class = BookForm
	template_name = 'book_template.html'
	success_url = u'/dp/thanks'

	def get(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		author = Author.objects.get(id=self.kwargs['author_id'])
		formset = BookFormset(instance=author)
		return self.render_to_response(self.get_context_data(formset=formset))

	def post(self, request, *args, **kwargs):
		self.object = None
		form_class = self.get_form_class()
		author = Author.objects.get(id=self.kwargs['author_id'])
		formset = BookFormset(request.POST,request.FILES,instance=author)
		if formset.is_valid():
			formset.save()
		return HttpResponseRedirect(reverse('dp:thanks'))

	def form_valid(self, formset):
	    context = self.get_context_data()
	    book_formset = context['formset']
	    if book_formset.is_valid():
	        # self.object = book_formset.save()
	        book_formset.instance = self.object
	        book_formset.save()
	        return HttpResponseRedirect(self.get_success_url())
	    else:
	        return self.render_to_response(self.get_context_data(formset=book_formset))

	# def form_invalid(self, formset):
	# 	return self.render_to_response(self.get_context_data(formset=formset))