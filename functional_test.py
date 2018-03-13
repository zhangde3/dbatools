from selenium import webdriver

browser = webdriver.Firefox()

# login dbatools app 


browser.get('http://127.0.0.1:8000')

# see keyword dbatools in browser title

assert 'DBATools' in browser.title

# see "Oracle, MySQL, MongoDB" tabs at the navigate bar

# click "Oracle" tab will jump to url: "http://127.0.0.1:8000/oraclemgmt" 

# and list all oracle services, one of them is "csqa4"

# click "csqa4" at services list will jump to "url: http://127.0.0.1:8000/oraclemgmt/csqa4"

# and see connect information "connected: 10.222.90.88:1521/csqa4" at top of page, "disconnect" button at besides

# and see text "actions" at below, and action list, one of the action list is "query sessions"

# click link "query sessions" will jump to url: "http://127.0.0.1:8000/oraclemgmt/csqa4/sessions"

# and list a table of current sessions, see username in one of sessions is "super"

# and see "back to actions" button at both top and botton of page

# click the button "back to actions", will jump to url: "http://127.0.0.1:8000/oraclemgmt/csqa4"

# click the button "disconnect" will jump to url: "http://127.0.0.1:8000/oraclemgmt"

browser.quit()
