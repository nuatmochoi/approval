from django.shortcuts import render,redirect
from django.http import HttpResponse,Http404, HttpResponseRedirect
from .models import Tag,uploaded_doc, document,approved_doc,denied_doc,tag_str,TagModel,chat_record
from .forms import *
from django.views import View
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import auth
from OurDEV import RequestProcess,TagProcess

import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from django.views.generic.edit import FormView
from django.utils.safestring import mark_safe
import json


@csrf_exempt
@csrf_protect
class LoginView(View):
    def get(self, request, *args, **kwargs):
        context={'parm1':'hello', 'parm2':'django','auth':request.user.is_authenticated}

        #print(request.user)
        return render(request, 'chat.html', context=context)

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('dj:login'))

def profile(request):
    if not request.user.is_authenticated:
        data = {'username':request.user, 'is_authenticated':request.user.is_authenticated}
    else:
        data={'last_login':request.user.last_login, 'username':request.user.username,
              'password':request.user.password, 'is_authenticated':request.user.is_authenticated}
    return render(request, 'dj/profile.html', context={'data':data})

class IndexView(View):
    def get(self, request, *args,**kwargs):
        context ={'parm1':'hello', 'parm2': 'django', 'auth':request.user.is_authenticated}
        #print(request.user)
        return render(request, 'chat.html', context=context)

class ProfileView(LoginRequiredMixin,View):
    def get(self, request, *args, **kwargs):
        data = {'last_login': request.user.last_login, 'username': request.user.username,
                'password': request.user.password, 'is_authenticated': request.user.is_authenticated}
        return render(request, 'dj/profile.html', context={'data': data})

def signup(request):
    if request.method == "POST":
        if request.POST["password1"]== request.POST["password2"]:
            user =User.objects.create_user(
                username=request.POST["username"], password= request.POST["password1"])

            auth.login(request, user)
            return HttpResponseRedirect(reverse('dj:login'))
        return render(request, "dj/signup.html")
    return render(request, 'dj/signup.html')

def tag_button(request):
    return render(request,'dj/tag_button.html')

def tag_list(request):
    if request.method=='POST':
        form_tag=TagForm(request.POST)

        obj=Tag(string1=form_tag.data['string1'],string2=form_tag.data['string2'],string3=form_tag.data['string3'],
                string4=form_tag.data['string4'])
        #obj.save()
        #tmp= tag_str.objects.all().order_by('-name')[obj.formtype.]]
        #tag_str.objects.all().order_by('-name')
        """tmp=tag_str.objects.all()[int(str(obj.formtype))-1]
        tmp=str(tmp)
        print(type(tmp),tmp)"""
        docx_doc=RequestProcess.createApproval(obj.string1,obj.string2,obj.string3,obj.string4)
        docx_doc.save("ttt.docx")

        model = TagModel.objects.get(tag_document=obj.string4)
        if model.tag_target1 is not None:
            from OurDEV import TagProcess
            docx_doc = TagProcess.modifyAddtion(docx_doc, model, form_tag.data['string5'], form_tag.data['string6'],
                                                form_tag.data['string7'], form_tag.data['string8'],
                                                form_tag.data['string9'])
            docx_doc.save("ttt.docx")

        return HttpResponseRedirect(reverse('dj:upload_doc'))  # or redirect('dj:upload_doc) -> dj/~/dj/~
    #return HttpResponse("fail")  # 마지막 string!='A' 일때 예외처리 해줘야함(수정!!!)
    elif request.method =='GET':
        form_tag=TagForm()
        return render(request,'dj/tag_list.html',{'form':form_tag})
    else:
        pass

def model_form_upload(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dj:tag_button')
    else:
        form = DocumentForm()
    return render(request, 'dj/model_form_upload.html', {
        'form': form
    })

def download(request):
    file_path = os.path.join(settings.BASE_DIR,'ttt.docx')

    file_name=os.path.basename(file_path)

    with open(file_path, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document') #doc로 저장되는 문제

        response['Contdent-Disposition'] = 'attachment; filename="{}"'.format(file_name)

        return response

def approval_download(request):
    file=os.path.abspath('media/documents/다운로드.docx') #should modify for each user
    file_path = os.path.join(file)

    file_name=os.path.basename(file_path)

    with open(file_path, 'rb') as f:
        response = HttpResponse(f, content_type='application/vnd.openxmlformats-officedocument.wordprocessingml.document')

        response['Contdent-Disposition'] = 'attachment; filename="{}"'.format(file_name)

        return response

def chat(request):
    return render(request, 'chat/chat.html', {})

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name))
    })

def mail_li(request):
    mail_li=document.objects.all()
    context={'mail_li':mail_li}
    return render(request,'dj/mail_li.html',context)

def mail_detail(request,pid):
    mail=document.objects.get(pk=pid)
    context={'mail':mail}
    return render(request,'dj/mail_detail.html',context)

def approve(request,pid):
    docu=document.objects.get(pk=pid)
    obj=approved_doc(title=docu.title, description=docu.description, document=docu.document, approval='approve')
    obj.save()
    return HttpResponseRedirect(reverse('dj:tag_button'))


def deny(request, pid):
    docu = document.objects.get(pk=pid)
    obj = denied_doc(title=docu.title, description=docu.description, document=docu.document, deny='deny')
    obj.save()
    return HttpResponseRedirect(reverse('dj:tag_button'))

def tag_add_button(request):
    if request.method=='POST':
        form=TagForm_temp(request.POST, request.FILES)
        form.save()

        obj=tag_str(name=form.data['tag_document'])
        obj.save()

        return HttpResponseRedirect(reverse('dj:login'))

    elif request.method == 'GET':
        form = TagForm_temp()
        return render(request, 'make_tag/tag_add_button.html', {'form': form})

def approve_list(request):
    approved_document = approved_doc.objects.all()
    context = {'approved_document': approved_document}
    return render(request, 'dj/approve_list.html', context)

def approve_detail(request,pid):
    a_doc=approved_doc.objects.get(pk=pid)
    context={'a_doc':a_doc}
    return render(request, 'dj/approve_detail.html',context)

def deny_list(request):
    denied_document = denied_doc.objects.all()
    context={'denied_document':denied_document}
    return render(request, 'dj/deny_list.html',context)

def deny_detail(request,pid):
    d_doc=denied_doc.objects.get(pk=pid)
    context={'d_doc':d_doc}
    return render(request, 'dj/deny_detail.html',context)

def chat_list(request):
    chat_strings = chat_record.objects.all()
    context={'chat_strings':chat_strings}
    return render(request, 'dj/chat_list.html',context)

def chat_detail(request,pid):
    c_doc= chat_record.objects.get(pk=pid)
    context={'c_doc':c_doc}
    return render(request, 'dj/chat_detail.html',context)

def document_list(request):
    return render(request,'dj/document_list.html')

