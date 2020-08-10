from django.http import HttpResponse
from TestModel.models import Test

def testdb_add(reuest):
    test1 = Test(name='run')
    test1.save()
    return HttpResponse("<p>数据添加成功</p>")

def testdb_select(request):
    response = ""
    response1 = ""

    #获取所有行
    list = Test.objects.all()
    for var in list:
        response += var.name + " "
    response1 = response
    return  HttpResponse(response1)

def testdb_update(request):
    test1 = Test.objects.get(id=1)
    test1.name = 'google'
    test1.save()
    return HttpResponse("<p>数据修改成功</p>")

def testdb_delete(request):
    test1 = Test.objects.get(id=5)
    test1.delete()
    return HttpResponse("<p>数据删除成功</p>")


