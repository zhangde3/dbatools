from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from oraclemgmt.dbconfig import config 
from django.urls import reverse
import cx_Oracle

def get_connect(func):
    def _inner(args,**kwargs):
        dbinfo = config.get(dbtag)
        host = dbinfo.get('host')
        port = dbinfo.get('port')
        dbsrv = dbinfo.get('dbsrv')    
        user = dbinfo.get('user')
        passwd = dbinfo.get('passwd')
        conn_str = "{}:{}/{}".format(host,port,dbsrv)
        with cx_Oracle.connect(user,passwd,conn_str) as conn:
            res = func(conn,args,**kwargs)
        return res
    return _inner

def home_page(request):
    context = {"dbsrvs":config}
    return render(request,'oraclemgmt/index.html',context)

@get_connect
def show_actions(request,conn):
    conn_info = "{}@{}".format(conn.username,conn.dsn)
    context={'dbtag':dbtag,'conn_info':conn_info}
    return render(request,'oraclemgmt/actions.html',context)

@get_connect
def query_sessions(request,conn):
    sql="select sid,serial#,username,status,cast(logon_time as timestamp) as login_time,machine,terminal from v$session where status!='KILLED' order by logon_time desc;".split(';')[0].strip()
    cur = conn.cursor()
    cur.prepare(sql)
    records = cur.execute(None).fetchall()
    columns = [ it[0] for it in cur.description ]
    return HttpResponse(records)

def disconnect(request,dbtag):
    return HttpResponseRedirect(reverse('home_page'))
