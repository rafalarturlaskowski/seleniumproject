from selenium import webdriver

if __name__ == '__main__':
    print('helloworld')
    driver = webdriver.Chrome(r'C:\drivers\chromedriver.exe')
    driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
    driver.maximize_window()
    button_add = driver.find_element_by_xpath('//button[text()=\'Add Element\']')
    button_add.click()
    button_add.click()
    button_add.click()
    
    buttons_delete = driver.find_elements_by_xpath('//div[@id=\'elements\']/button')
    buttons_delete[1].click()