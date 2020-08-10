from django.contrib import admin
from TestModel.models import Test,Contact,Tag

# Register your models here.
class TagInline(admin.TabularInline):
    model = Tag

class ContacAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # 定义列表展示的字段
    search_fields = ('name',)  #定义列表搜索
    inlines = [TagInline]
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )
admin.site.register(Contact,ContacAdmin)
admin.site.register([Test])

