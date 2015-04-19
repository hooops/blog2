# -*- coding: utf-8 -*-
import urllib2
import re
import sys
global arr
arr=[]
global arr2
arr2=[]
from django.shortcuts import render,render_to_response
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.template.context import RequestContext
from django.contrib import auth
from models import User
import models
from django.contrib.sessions.models import Session
from models import Category,Blog_user
from django.contrib import comments
from django.contrib.contenttypes.models import ContentType
# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
import socket
import smtplib
import hashlib
import datetime
import string
def acc_login(request):
 try:
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = auth.authenticate(username=username,password=password)
    print username,password
    if user is not None: #and user.is_active:
        #correct password and user is marked "active"
        auth.login(request,user)
        content = '''
        Welcome %s !!!
        
        <a href='/logout/' >Logout</a>
        
         ''' % user.username
        #return HttpResponse(content)

        return HttpResponseRedirect('/')
    else:
        return render_to_response('login.html',{'login_err':'Wrong username or password!'})
    
 except:
     return HttpResponse('ERROR 0001')#0001

def logout_view(request):
 try:
    user = request.user
    auth.logout(request)
    # Redirect to a success page.
    # return HttpResponse("<b>%s</b> logged out! <br/><a href='/index/'>Re-login</a>" % user)
    return index(request)
 except:
     return HttpResponse('ERROR 0002')#0002

def Login(request):
 try:
    return render_to_response('login.html')
 except:
     return HttpResponse('ERROR 0003')#0003



def index(request):
 try:
    # blog_list = models.Blog.objects.all()
    blog_list = models.Blog.objects.order_by('-id').all()

    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html', {
                                             'blog_list':blog_list,
                                             'user':request.user,
                                             'bbs_category':bbs_categories,
                                             'cata_id': 0})
 except:
     return HttpResponse('ERROR 0004')#0004


def category(request,cata_id):
 try:
    bbs_list = models.Blog.objects.filter(category__id=cata_id)
    bbs_categories = models.Category.objects.all()
    return render_to_response('index.html',
                               {'bbs_list':bbs_list,
                                 'user':request.user,
                                 'bbs_category':bbs_categories,
                                 'cata_id': int(cata_id),
                              })

 except:
     return HttpResponse('ERROR 0005')#0005

def bbs_detail(request, bbs_id):
 # try:
    bbs = models.Blog.objects.get(id=bbs_id)
    print '--->', bbs
    user=models.Blog.objects.get(id=bbs_id)
    usert=User.objects.get(id=user.author_id)
    return render_to_response('blog_detail.html', {'blog_obj':bbs,'user':request.user,'username_':usert})
 # except:
 #    return HttpResponse('ERROR 0006')#0006
    
def sub_comment(request):
 try:
    print  request.POST
    bbs_id = request.POST.get('bbs_id')
    comment = request.POST.get('comment_content')
    
    if comment is not None:
        hostname=socket.gethostname()
        ip=socket.gethostbyname(hostname)

        comments.models.Comment.objects.create(
            content_type_id = 7,
            object_pk= bbs_id,
            site_id = 1,
            user = request.user,                       
            comment =   comment,
            ip_address=ip,
                                   )
        return  HttpResponseRedirect('/detail/%s' % bbs_id)
    else:
        return  HttpResponseRedirect('/detail/' )


 except:
     return HttpResponse('ERROR 0007')#0007

def bbs_sub(request):
 try:
    print ',==>', request.POST.get('content')
    title=  request.POST.get('title')
    content=  request.POST.get('content')
    # category=request.user.blog_user.user_id
    # author = models.Blog_user.objects.get(user__username=request.user)
    author = models.Blog_user.objects.get(user__username=request.user)
    # author = models.Blog_user.objects.get(user__username=request.user)
    # category_id = models.Blog_user.objects.get(category_id=category)
    # authorid=author.user_id
    # authorid=models.Category.objects.get(administrator_id=author.id)
    # author_id = models.Blog_user.objects.get(user__username=request.user)
    category = request.POST.get('category_id')
    # print 'user_id_'
    # print user_id_
    # user = request.user
    # print '1'
    # print user.blog_user.user_id
    # category=  request.POST.get('category_id')
    # models.Blog_user.objects.create(
    #     # name=title,
    #     user_id=user.blog_user.user_id,
    #
    # )
    models.Blog.objects.create(
        title = title,
        summary = 'github',
        content = content,
        author =author,
        view_count= 1,
        ranking = 1,
        category_id=category,
           )

    return index(request)
 except:
     return HttpResponse('ERROR 0008')#0008
def bbs_pub(request):
 # try:
    # bbs_categories = models.Category.objects.all()
    author = models.Blog_user.objects.get(user__username=request.user)
    category_ids=models.Category.objects.all()
    category_id=[]
    for s in category_ids:
        category_id.append(s)
        print category_id
    # category_id2=category_id
    # category=  request.POST.get('category')
    # models.Category.objects.create(
    #     name=category,
    #     administrator_id=author,
    #
    # )
    return render_to_response('bbs_pub.html',{'category_id':category_id})
    # t= loader.get_template('bbs_pub.html')
    # c=Context({'category_id':category_id})
    # return HttpResponse(t.render(c))
 # except:
 #     return HttpResponse('ERROR 0009')#0009

def delete(request):
     blog_id=request.POST.get('blog_id')
     p=models.Blog.objects.get(id=blog_id)
     p.delete()
     blog_list = models.Blog.objects.all()
     bbs_categories = models.Category.objects.all()
     return render_to_response('index.html', {
                                             'blog_list':blog_list,
                                             'user':request.user,
                                             'bbs_category':bbs_categories,
                                             'cata_id': 0})

def bianji(request):


    author = models.Blog_user.objects.get(user__username=request.user)
    category_ids=models.Category.objects.all()
    blog_id=request.POST.get('blog_id')
    p=models.Blog.objects.get(id=blog_id)
    category_id=[]
    for s in category_ids:
        category_id.append(s)
        print category_id

    return render_to_response('bbs_bianji.html',{'category_id':category_id,'p':p})

def bbs_bianji(request):
 try:
    print ',==>', request.POST.get('content')
    title=  request.POST.get('title')
    content=  request.POST.get('content')
    blog_id=request.POST.get('blog_id')
    # category=request.user.blog_user.user_id
    # author = models.Blog_user.objects.get(user__username=request.user)
    author = models.Blog_user.objects.get(user__username=request.user)
    # author = models.Blog_user.objects.get(user__username=request.user)
    # category_id = models.Blog_user.objects.get(category_id=category)
    # authorid=author.user_id
    # authorid=models.Category.objects.get(administrator_id=author.id)
    # author_id = models.Blog_user.objects.get(user__username=request.user)
    category = request.POST.get('category_id')
    # print 'user_id_'
    # print user_id_
    # user = request.user
    # print '1'
    # print user.blog_user.user_id
    # category=  request.POST.get('category_id')
    # models.Blog_user.objects.create(
    #     # name=title,
    #     user_id=user.blog_user.user_id,
    #
    # )
    p=models.Blog.objects.get(id=blog_id)
    p.title = title
    p.summary = 'github'
    p.content = content
    p.author =author
    p.view_count= 1
    p.ranking = 1
    p.category_id=category
    p.save()


    return index(request)
 except:
     return HttpResponse('ERROR 0008')#0008

def zhucesave(request):
 try:
    username=request.POST.get('username')
    password=request.POST.get('password')
    first_name=request.POST.get('first_name')
    last_name=request.POST.get('last_name')
    email=request.POST.get('email')

    if username and password is not None:

        models.User.objects.create(
             username=username,
            password=make_password(password,None,'pbkdf2_sha256'),
            first_name=first_name,
            last_name=last_name,
            email=email,)
        s=models.User.objects.get(username=username)

        models.Blog_user.objects.create(
        signature='This guy is too lazy to levave anything here.',
        user_id=s.id)





        blog_list = models.Blog.objects.all()
        bbs_categories = models.Category.objects.all()
        return render_to_response('index.html', {
                                             'blog_list':blog_list,
                                             'user':request.user,
                                             'bbs_category':bbs_categories,
                                             'cata_id': 0})


    else:
        return HttpResponse('password and uasename is not None~~')
 except:
        return HttpResponse('ERROR 0009')#0009

def ziliao(request):
    return render_to_response('user.html')

def zhuce(request):
    return render_to_response('user.html')

def deletepin(request):
    pin_id=request.POST.get('pin_id')
    p=comments.models.Comment.objects.get(id=pin_id)


    p.delete()
    return HttpResponse('ok')
    # return bbs_detail(request, pin_id)


def chcodeex2(request):
    username2=request.POST.get('username')
    print username2
    px=User.objects.filter(username=username2)
    if len(px)<=0:
        return HttpResponse('该用户名不存在')
    elif  px[0].email is None:

            return HttpResponse('该用户名没有邮箱')
    else:



        us=User.objects.filter(username=username2)
        md5=hashlib.md5(us[0].password).hexdigest()
        md51=hashlib.md5(us[0].username).hexdigest()
        md52=hashlib.md5((datetime.datetime.now().strftime('%Y%m%d'))).hexdigest()
        # print(md52+md5+md51)

        md=md51+md5+md52
        print md
        print px[0].email
        from_mail='hooops1994@163.com'
        to_mail=px[0].email
        server=smtplib.SMTP('smtp.163.com')
        server.docmd('ehlo','hooops1994@163.com')
        server.login('hooops1994@163.com','dhy2010')
        msg='''from:Myblog
        to:hooops@qq.com
        subject:blog密码修改

        修改密码 http://127.0.0.1:8000/changemi/'''+md+'''
        .
        '''

        server.sendmail(from_mail,to_mail,msg)
        server.quit()
        userkey=models.Blog_user_key.objects.filter(user_id=request.user.id)

        # userkey=request.user.id
        users=request.POST.get('username')
        u=User.objects.filter(username=users)[0]

        if u.id is None:
            return HttpResponse('用户不存在')
        else:

            if userkey is not  None:
                sk=models.Blog_user_key.objects.create(
                    user_id=u.id,
                    emailKey=md
                )
                sk.save()
                return HttpResponse('改密码邮件已经发送到你的邮箱，请查收1')
            else:
                models.Blog_user_key.objects.filter(user_id=u.id).update(emailKey=md)
                return HttpResponse('改密码邮件已经发送到你的邮箱，请查收...')

def chcodee(request):
    return render_to_response('xcode.html')


def changemii(id,key):

    # userk=models.Blog_user_key.objects.get(user_id=)
    s=models.Blog_user_key.objects.filter(emailKey=key)[0]
    if s.user_id is not None:
        t = loader.get_template('changecode.html')
        c=Context({'key':s.user_id})
        return HttpResponse(t.render(c))



    else:
        return HttpResponse('链接不存在')




        # print s.user_id

def changcodev(request):
        print 'k'

        print request.get_full_path()

        pwd=request.POST.get('passwordv')
        users=request.POST.get('userkey')
        password=make_password(pwd,None,'pbkdf2_sha256')



        User.objects.filter(id=users).update(password=password)
        s=models.Blog_user_key.objects.filter(user_id=users)[0]
        s.delete()
        return  HttpResponse('密码修改成功')






def so(request):
    return render_to_response('so.html')

# def zhizhu(url,value):
#     cong=urllib2.urlopen(url)
#     print type(cong)
#     target=cong.read()
#     zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
#     imgre = re.compile(zhengze)
#     imglist = re.findall(imgre,target)
#     if value is not None:
#         key = re.search(value,target)
#         if key is not None:
#             print url
#     else:
#         for s in imglist:
#             arr=s[:-2]
#             print s[:-2]
#             zhizhu2(arr,value)
#
#
# def zhizhu2(url,value):
#  try:
#     cong=urllib2.urlopen(url)
#
#     target=cong.read()
#     zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
#     imgre = re.compile(zhengze)
#     imglist = re.findall(imgre,target)
#     if value is not None:
#         key = re.search(value,target)
#         if key is not None:
#             print url
#     else:
#         for s in imglist:
#             arr=s[:-2]
#             print s[:-2]
#             zhizhu3(arr,value)
#  except:
#      pass
#
#
# def zhizhu3(url,value):
#  try:
#     cong=urllib2.urlopen(url)
#
#     target=cong.read()
#     zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
#     imgre = re.compile(zhengze)
#     imglist = re.findall(imgre,target)
#     if value is not None:
#         key = re.search(value,target)
#         if key is not None:
#             print url
#     else:
#         for s in imglist:
#             arr=s[:-2]
#             print s[:-2]
#             zhizhu4(arr,value)
#  except:
#      pass
#
#
# def zhizhu4(url,value):
#  try:
#     cong=urllib2.urlopen(url)
#
#     target=cong.read()
#     zhengze=(r'http://[a-zA-z0-9]+.[a-zA-z0-9]+.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*.[a-zA-z0-9]*[ ]')
#     imgre = re.compile(zhengze)
#     imglist = re.findall(imgre,target)
#     if value is not None:
#         key = re.search(value,target)
#         if key is not None:
#             print url
#     else:
#         for s in imglist:
#             arr=s[:-2]
#             print s[:-2]
#  except:
#      pass
#
#
#
# def main(request):
#     xurl=request.GET.get('http')
#     xvalue=request.GET.get('values')
#     print xurl
#     print xvalue
#     zhizhu(('http://'+xurl),xvalue)
#     return index(request)
