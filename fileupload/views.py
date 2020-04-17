from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from .models import userfile
# Create your views here.
# 用Form创建一个简单的表单
#class UserForm(forms.Form):
#    name = forms.CharField()    #字符串
#    upfile = forms.FileField()     #文件

#函数register里面的形参request是必须要填的
#render()和render_to_response()均是django中用来显示模板页面的

'''
register函数判断用户的是否为POST请求，如果是并验证是有效的，然后就返回upload ok!，在验证正确和返回OK的中间放我们的上传文件代码，因为只有文件上传成功能返回OK，我们一会说，如果是GET请求，就直接显示一个空表单，让用户输入。
'''
def register(request):
    uf=userfile()
    if request.method == "POST":
        uf.username = request.POST['name']
        uf.headImg = request.FILES.get('tttt',None)

        uf.save()
        return HttpResponse('upload ok!')
    return render(request,'fileupload/register.html',{'uf':uf})

def display(request):
    filelist = userfile.objects.all()
    context = {'filelist':filelist}
    return render(request,"fileupload/filelist.html",context)