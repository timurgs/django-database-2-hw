from django.contrib import admin
from django.core.exceptions import ValidationError
from django.forms import BaseInlineFormSet

from .models import Article, Scope, Tag


class ScopeInlineFormset(BaseInlineFormSet):
    def clean(self):
        cache = []
        for i, form in enumerate(self.forms):
            data = form.cleaned_data.get('is_main')
            if data is True and data in cache:
                raise ValidationError('Основным может быть только один раздел')
            elif data is True:
                cache.append(data)
            if len(cache) == 0 and self.forms[-1] == self.forms[i]:
                raise ValidationError('Укажите основной раздел')
        return super().clean()


class ScopeInline(admin.TabularInline):
    model = Scope
    formset = ScopeInlineFormset


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]
