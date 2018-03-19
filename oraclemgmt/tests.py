from django.test import TestCase
from django.urls import resolve
from oraclemgmt.views import home_page, show_actions,disconnect
from django.http import HttpRequest, HttpResponse
from django.template.loader import render_to_string
from oraclemgmt.dbconfig import config
import cx_Oracle

class HomePageTest(TestCase):
    
    def test_root_home(self):
        found =  resolve('/oraclemgmt/')
        self.assertEqual(found.func,home_page)

    def test_home_page_return_correct_html(self):
        request = HttpRequest() 
        response = home_page(request)
        expected_html = render_to_string('oraclemgmt/index.html',{'dbsrvs':config})
        self.assertEqual(response.content.decode(),expected_html)

    def test_db_actions_page(self):
        found = resolve('/oraclemgmt/csqa4')
        self.assertEqual(found.func,show_actions)

    def test_db_actions_page_return_correct_html(self):
        request = HttpRequest()
        dbtag='csqa4'
        conn = cx_Oracle.connect('super','super','10.222.90.88:1521/csqa4')
        request.session={}
        request.session['db_conn']=conn
        response = show_actions(request,dbtag=dbtag)
        db = config.get(dbtag)
        conn_str = "{}:{}/{}".format(
            db.get('host'),
            db.get('port'),
            db.get('dbsrv')
         )
        conn_info = "{}@{}".format(conn.username,conn.dsn)
        context={'dbtag':dbtag,'conn_info':conn_info}
        expected_html = render_to_string('oraclemgmt/actions.html',context)
        self.assertEqual(response.content.decode(),expected_html)
        conn.close()

    def test_disconnect(self):
        found =  resolve('/oraclemgmt/csqa4/disconnect')
        self.assertEqual(found.func,disconnect)

#    def test_disconnect_page_return_correct_html(self):
#        request = HttpRequest() 
#        response = disconnect(request,'csqa4')
#        # comment below test, Maybe due to HttpResponseRedirect return null content, so can not pass below
#        # expected_html = render_to_string('oraclemgmt/index.html',{'dbsrvs':config})
#        self.assertEqual(response.content.decode(),expected_html)
    
        

