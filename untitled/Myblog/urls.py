from django.conf.urls import patterns, include, url
from  views import  chcodeex2
import views
global key
key=chcodeex2
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'BBS_Pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    (r'^$',views.index ),
    # (r'^index',views.index ),
    (r'^detail/(\d+)/$', views.bbs_detail),
    (r'^sub_comment/$', views.sub_comment),
    # (r'^bbs_pub/$', views.bbs_pub),
    (r'^bbs_sub/$', views.bbs_sub),
    (r'^category/(\d+)/$',views.category),
    (r'^delete/$', views.delete),
    (r'^bianji/$', views.bianji),
    (r'^zhuce/$', views.zhuce),
    (r'^ziliao/$', views.ziliao),
    (r'^zhucesave/$', views.zhucesave),
    (r'^deletepin/$', views.deletepin),
    (r'^xcode/$', views.chcodee),
    (r'^chcodeex2/$', views.chcodeex2),
    # (r"'^changemi/[+]('+key+')/$'", views.changemi),
    (r'^changemi/(\w+)/$', views.changemii),
    (r'^so/$', views.so),
    (r'^changcodev/$', views.changcodev),
    # (r'^so/main/$', views.main),

)
