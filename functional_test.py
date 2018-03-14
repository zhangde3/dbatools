from selenium import webdriver
import unittest

class NewDBATest(unittest.TestCase):
    
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_oraclemgmt_can_list_dbservices_connect_disconnect(self):

        # oracle dba tom is accessing dbatools for oracle tab with url 'http://127.0.0.1:8000/oraclemgmt'
        self.browser.get('http://127.0.0.1:8000/oraclemgmt')

        # he saw keyword dbatools in browser title
        self.assertIn('DBATools',self.browser.title)

        # and the page header says "Oracle Database Services"
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('Oracle Database Services',header_text)

        # and a list below above header, one of them is "csqa4"
        litags = self.browser.find_elements_by_tag_name('li')
        dbsrvs = [ tag.text for tag in litags ]
        self.assertIn('csqa4',dbsrvs)

        # click "csqa4" at services list will jump to "url: http://127.0.0.1:8000/oraclemgmt/csqa4"
        atag = self.browser.find_element_by_link_text('csqa4')
        atag.click()
        url = self.browser.current_url
        self.assertEqual(url,'http://127.0.0.1:8000/oraclemgmt/csqa4')
        
        # and see connect information "connected: 10.222.90.88:1521/csqa4" at top of page
        conn_info = self.browser.find_element_by_tag_name('p').text
        self.assertEqual("connected: 10.222.90.88:1521/csqa4",conn_info)

        # and a "disconnect" link at besides
        # click on that link will back to 'http://127.0.0.1:8000/oraclemgmt'
        disconnect_link = self.browser.find_element_by_link_text('disconnect')
        disconnect_link.click()
        url = self.browser.current_url
        self.assertEqual(url,'http://127.0.0.1:8000/oraclemgmt/')

        # and see text "actions" at below, and action list, one of the action list is "query sessions"
        # click link "query sessions" will jump to url: "http://127.0.0.1:8000/oraclemgmt/csqa4/sessions"
        # and list a table of current sessions, see username in one of sessions is "super"
        # and see "back to actions" button at both top and botton of page
        # click the button "back to actions", will jump to url: "http://127.0.0.1:8000/oraclemgmt/csqa4"
        # click the button "disconnect" will jump to url: "http://127.0.0.1:8000/oraclemgmt"
        self.fail('Finish the test!')

if __name__ == '__main__':
    unittest.main()

