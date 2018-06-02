from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse
import MySQLdb
import json
import pdb
import matplotlib.pyplot as plt
import numpy


def login(request):
    if request.session.has_key('username'):
        username=request.session['username']
        return render(request, 'indexpage.html', {'username': username})
    else:
        return render(request, 'login.html', {})


def index(request):
    username=request.POST.get('username')
    password=request.POST.get('pwd')
    '''if username == 'admin' and password == 'adminoems':
        request.session['name']=username
        return render(request, 'indexpage.html', {'username':request.session['name']})
    else:
        message = 'invaid username or password'
        return render(request, 'login.html', {'message': message})'''
    # db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    db=MySQLdb.connect("localhost","root","newrootpassword","employees")
    cursor=db.cursor()
    sqlcmd="select count(*) from admin_oems where username='"+username+"' and password='"+password+"'"
    cursor.execute(sqlcmd)
    count=cursor.fetchone()
    db.close()
    #print (count)
    #pdb.set_trace()
    if count[0] == 1:
        request.session['username']=username
        return render(request, 'indexpage.html', {'username':username})
    else:
        message = 'invaid username or password'
        return render(request, 'login.html', {'message': message})
    return HttpResponse(count)


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return render(request, 'logout.html', {})


def empdata(request):
    fullname = request.POST.get('fullname')
    empid=request.POST.get('empid')
    gender = request.POST.get('gender')
    phone_number = request.POST.get('ph_num')
    email = request.POST.get('email')
    town = request.POST.get('town')
    state = request.POST.get('state')
    country = request.POST.get('country')
    department = request.POST.get('department')
    designation = request.POST.get('designation')
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "insert into emp values('" + fullname + "',"+ empid +", '" + gender + "', '" + phone_number + "', '" + email + "', '" + town + "', '" + state + "', '" + country + "', '" + department + "', '" + designation + "')"
    cursor.execute(sqlcmd)
    db.commit()
    # count=cursor.fetchone()
    # data=cursor.fetchall()
    db.close()
    return emplist(request)


def addemp(request):
    return render(request, 'addemp.html', {})


def emplist(request):
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "select * from emp"
    cursor.execute(sqlcmd)
    # count=cursor.fetchone()
    data=cursor.fetchall()
    db.close()
    allempdata={}
    allempdata['employees']=[]
    for d in data:
        fullname=d[0]
        empid=d[1]
        gen=d[2]
        phnum=d[3]
        email=d[4]
        place=d[5]
        state=d[6]
        country=d[7]
        department=d[8]
        designation=d[9]
        allempdata['employees'].append({'fullname':fullname,'empid':empid,'gender':gen,'phone_number':phnum,'email':email,'place':place,'state':state,'country':country,'department':department,'designation':designation})
    #return HttpResponse(json.dumps(allempdata))
    return render(request, 'emplist.html', {'empdata':allempdata['employees']})
    #return render(request, 'emplist.html', {'data':data})


def emp_edit(request, id):
    eid=id
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "select empid,phone_number,email from emp where empid="+eid+""
    cursor.execute(sqlcmd)
    # count=cursor.fetchone()
    data = cursor.fetchall()
    db.close()
    for d in data:
        empid=d[0]
        phone_number=d[1]
        email=d[2]
    return render(request, 'emp-update.html', {'empid':empid,'phone_number':phone_number,'email':email})


def emp_update(request):
    empid=request.POST.get('empid')
    new_phone_number=request.POST.get('ph_num')
    new_email=request.POST.get('email')
    db=MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor=db.cursor()
    cmd="update emp set phone_number='"+new_phone_number+"',email='"+new_email+"' where empid="+empid+""
    cursor.execute(cmd)
    db.commit()
    db.close()
    return emplist(request)


def add_dept(request):
    return render(request, 'add-dept.html', {})


def add_dept_data(request):
    dept_id = request.POST.get('deptid')
    dept_name = request.POST.get('dept_name')
    dept_head_name = request.POST.get('dept_head_name')
    dept_phone_number = request.POST.get('ph_num')
    dept_email = request.POST.get('email')

    db=MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor=db.cursor()
    cmd="insert into department values("+dept_id+",'"+dept_name+"','"+dept_head_name+"','"+dept_phone_number+"','"+dept_email+"')"
    cursor.execute(cmd)
    db.commit()
    db.close()

    return dept_list(request)


def dept_list(request):
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "select * from department"
    cursor.execute(sqlcmd)
    # count=cursor.fetchone()
    data=cursor.fetchall()
    db.close()
    all_departments={}
    all_departments['departments']=[]
    for d in data:
        department_id=d[0]
        dept_name=d[1]
        dept_head_name=d[2]
        dept_ph_number=d[3]
        dept_email=d[4]
        all_departments['departments'].append({'department_id':department_id,'dept_name':dept_name,'dept_head_name':dept_head_name,'dept_ph_number':dept_ph_number,'dept_email':dept_email})
    #return HttpResponse(json.dumps(allempdata))
    return render(request, 'dept-list.html', {'dept_data':all_departments['departments']})


def dept_edit(request,id):
    dept_id=id
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "select id,dept_head,phone_number,email from department where id=" + dept_id + ""
    cursor.execute(sqlcmd)
    # count=cursor.fetchone()
    data = cursor.fetchall()
    db.close()
    for d in data:
        deptid = d[0]
        dept_head=d[1]
        dept_ph_no = d[2]
        dept_email = d[3]
    return render(request, 'dept-update.html', {'dept_id':deptid,'dept_head':dept_head,'dept_ph_num':dept_ph_no,'dept_email':dept_email})


def dept_update(request):
    dept_id = request.POST.get('deptid')
    new_dept_head_name = request.POST.get('dept_head_name')
    new_dept_phone_number = request.POST.get('ph_num')
    new_dept_email = request.POST.get('email')
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    cmd = "update department set dept_head='"+new_dept_head_name+"', phone_number='" + new_dept_phone_number + "',email='" + new_dept_email + "' where id=" + dept_id + ""
    cursor.execute(cmd)
    db.commit()
    db.close()

    return dept_list(request)


def del_emp(request, id):
    emp_id=id
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    cmd = "delete from emp where empid="+emp_id+""
    cursor.execute(cmd)
    db.commit()
    db.close()

    return emplist(request)


def del_dept(request, id):
    dept_id=id
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    cmd = "delete from department where id="+dept_id+""
    cursor.execute(cmd)
    db.commit()
    db.close()

    return dept_list(request)


def admin_profile(request):
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    cmd = "select name,phone_number,email from admin_oems"
    cursor.execute(cmd)
    data=cursor.fetchall()
    db.close()
    for d in data:
        name=d[0]
        ph_num=d[1]
        email=d[2]
    #return HttpResponse(data)
    return render(request, 'admin-profile.html', {'name':name,'ph_num':ph_num,'email':email})


def update_profile(request):
    fullname = request.POST.get('fullname')
    gender = request.POST.get('gender')
    ph_num = request.POST.get('ph_num')
    email = request.POST.get('email')
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "update admin_oems set name='"+fullname+"',gender='"+gender+"',phone_number='"+ph_num+"',email='"+email+"' where username='admin'"
    cursor.execute(sqlcmd)
    db.commit()
    db.close()

    return home(request)


def home(request):
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd1 = "select count(*) from emp"
    cursor.execute(sqlcmd1)
    emp_count=cursor.fetchone()
    sqlcmd2 = "select count(*) from department"
    cursor.execute(sqlcmd2)
    dept_count = cursor.fetchone()
    db.close()
    return render(request, 'index.html', {'emp_count':emp_count[0],'dept_count':dept_count[0]})


def change_pwd(request):
    return render(request, 'change-pwd.html', {})


def updt_pwd(request):
    old_pwd=request.POST.get('old_pwd')
    new_pwd = request.POST.get('new_pwd')
    cnf_pwd = request.POST.get('cnf_pwd')
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "select password from admin_oems"
    cursor.execute(sqlcmd)
    data=cursor.fetchall()
    db.close()
    for d in data:
        pwd=d[0]
    if old_pwd!=pwd:
        err_msg="password incorrect"
        return render(request, 'change-pwd.html', {'err_msg':err_msg})
    else:
        if new_pwd!=cnf_pwd:
            err_msg1="passwords mismatch"
            return render(request, 'change-pwd.html', {'err_msg1': err_msg1})
        else:
            db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
            cursor = db.cursor()
            sqlcmd = "update admin_oems set password='"+new_pwd+"' where username='admin'"
            cursor.execute(sqlcmd)
            db.commit()
            db.close()

            return home(request)


def emp_dept(request):
    db = MySQLdb.connect("localhost", "root", "newrootpassword", "employees")
    cursor = db.cursor()
    sqlcmd = "select emp.empid,emp.fullname,emp.email,emp.designation,department.id,department.dept_head,department.email from emp inner join department where emp.department=department.dept_name"
    cursor.execute(sqlcmd)
    data=cursor.fetchall()
    db.close()
    empdept_data={}
    empdept_data['emp&dept']=[]
    for d in data:
        emp_id=d[0]
        emp_name=d[1]
        emp_email=d[2]
        emp_designation=d[3]
        dept_id=d[4]
        dept_head=d[5]
        dept_email=d[6]
        empdept_data['emp&dept'].append({'emp_id':emp_id,'emp_name':emp_name,'emp_email':emp_email,'emp_designation':emp_designation,'dept_id':dept_id,'dept_head':dept_head,'dept_email':dept_email})
    return render(request, 'emp-dept.html', {'empdept_data':empdept_data['emp&dept']})


def graph(request):
    x=['1-mon','2-tue','3-wen','4-thu','5-fri','6-sat']
    y=[8,7,9,10,6,8.5]
    plt.plot(x,y)
    plt.show()
    #return render(request, 'graph.html', {'gg':g.render()})
    #return home(request)