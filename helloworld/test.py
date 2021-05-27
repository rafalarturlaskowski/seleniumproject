from selenium import webdriver
import unittest

class NamesTestCase(unittest.TestCase):


   def navigate(self):
       driver = webdriver.Chrome(r'C:\drivers\chromedriver.exe')
       driver.get('https://the-internet.herokuapp.com/add_remove_elements/')
       driver.maximize_window()
       return driver

   def test_button_add(self):
       
        driver = self.navigate()
        button_add = driver.find_element_by_xpath('//button[text()=\'Add Element\']')
        button_add.click()
        button_add.click()
        button_add.click()
        
        buttons_delete = driver.find_elements_by_xpath('//div[@id=\'elements\']/button')
               
        self.assertEqual(3, len(buttons_delete))
           
        driver.close()
        
   def test_button_delete(self):
        driver = self.navigate()
        button_add = driver.find_element_by_xpath('//button[text()=\'Add Element\']')
        button_add.click()
        button_add.click()
        
        buttons_delete = driver.find_elements_by_xpath('//div[@id=\'elements\']/button')
        buttons_delete[1].click()
        
        buttons_delete = driver.find_elements_by_xpath('//div[@id=\'elements\']/button')
        self.assertEqual(1, len(buttons_delete))
        driver.close()
        
        