from django.contrib import admin
# Register your models here.
from .models import Question
from django.db.models import Q
from functools import reduce
import unidecode




class ListandoPerguntas(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_display_link = ('question_text',)
    search_fields = ('question_text__exact',)

    """ def get_search_results(self, request, queryset, search_term):
        queryset, may_have_duplicates = super().get_search_results(
            request, queryset, search_term,
        )
        
        search_term_as_int = int(search_term)
    
        queryset |= self.model.objects.filter(age=search_term_as_int)
        return queryset, may_have_duplicates
 """
      
	

admin.site.register(Question, ListandoPerguntas)