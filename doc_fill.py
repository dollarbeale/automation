from selenium import webdriver

print('hello, what is up')

web = webdriver.Chrome(executable_path='./chromedriver.exe')
web.get('https://google.com')

