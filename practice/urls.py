from . import views
from django.conf.urls import url

urlpatterns=[
    url(r'^$', views.login, name='login'),
    url(r'^index',views.index, name='index'),
    url(r'^logout', views.logout, name='logout'),
    url(r'^addemp',views.addemp,name='addemp'),
    url(r'^empdata',views.empdata,name='empdata'),
    url(r'^emplist',views.emplist,name='emplist'),
    url(r'^edit/(?P<id>\d+)/$',views.emp_edit,name='emp_edit'),
    url(r'^update',views.emp_update,name='emp_update'),
    url(r'^add-dept',views.add_dept,name='add_dept'),
    url(r'^add_dept_data',views.add_dept_data,name='add_dept_data'),
    url(r'deptlist',views.dept_list,name='deptlist'),
    url(r'^dept_edit/(?P<id>\d+)/$',views.dept_edit,name='dept_edit'),
    url(r'^dept_update',views.dept_update,name='dept_update'),
    url(r'^del_emp/(?P<id>\d+)/$',views.del_emp,name='del_emp'),
    url(r'^del_dept/(?P<id>\d+)/$',views.del_dept,name='del_dept'),
    url(r'^admin_profile',views.admin_profile,name='admin_profile'),
    url(r'^profile',views.update_profile,name='profile'),
    url(r'^home',views.home,name='home'),
    url(r'^change_pwd',views.change_pwd,name='change_pwd'),
    url(r'^updt_pwd',views.updt_pwd,name='updt_pwd'),
    url(r'^empdept',views.emp_dept,name='empdept'),
    url(r'^graph',views.graph,name='graph')
]