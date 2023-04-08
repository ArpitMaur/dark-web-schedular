from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
from datetime import date
from databaseConnection import collection2
import time
from startDisplay import *
from driverpath import torPath
# from flag import sendLog,sendData
from dateformat import *

def scroll(driver):
    reached_page_end = False
    last_height = driver.execute_script("return document.body.scrollHeight")
    while not reached_page_end:
        driver.find_element(By.XPATH,'//body').send_keys(Keys.END)   
        time.sleep(15)
        print("Website is Scrolling now...")
        # sendLog("Website is Scrolling now...")
        
        new_height = driver.execute_script("return document.body.scrollHeight")
        if last_height == new_height:
                reached_page_end = True
                print("Page ended...Scrolling Done!!")
                # sendLog("Page ended...Scrolling Done!!")
                
        else:
                last_height = new_height

def press_next_btn(driver,xpath_of_next_btn) :
    try :
        time.sleep(10)
        next_btn = driver.find_element(By.XPATH,str(xpath_of_next_btn))
        if next_btn.is_enabled or next_btn.is_displayed  and not 'link-unactive' in next_btn.get_attribute('class') :
            driver.execute_script("arguments[0].scrollIntoView();", next_btn)
            time.sleep(8)
            print("Opening next page...")
            # sendLog("Opening next page...")
            next_btn.click()
            return True
        else :
            print("Reached at last page")
            # sendLog("Reached at last page")
            return False

    except NoSuchElementException:
        print("Reached at last page")
        # sendLog("Reached at last page")
        return False
    except ElementNotInteractableException:
        print("Reached at last page")
        # sendLog("Reached at last page")
        return False

def no_next_btn(driver,i,xpath_of_pagination_container,tag_name_of_pages) :
    time.sleep(10)
    pagination_container = driver.find_element(By.XPATH,str(xpath_of_pagination_container))
    all_pages = pagination_container.find_elements(By.TAG_NAME,str(tag_name_of_pages))
    if len(all_pages) == i :
        print("Reached at last page!!")
        # sendLog("Reached at last page!!")
        return False
    next_page = all_pages[i]
    driver.execute_script("arguments[0].scrollIntoView();", next_page)
    print("Opening next page...please wait...")
    # sendLog("Opening next page...please wait...")
    next_page.click()
    return True                

def scrap(driver,iterator,title_xpath,body_xpath,date_xpath,link):
    print("Data scraping....")
    # sendLog("Data scraping....")
    data = driver.find_elements(By.XPATH, iterator)
    for d in data:
        temp = ''
        try:
            title = d.find_element(By.XPATH, title_xpath)
            element_html=title.get_attribute('outerHTML')
            title=BeautifulSoup(element_html,'html.parser')
            title=title.text
            temp += title+' '
            
        except:
            title='Not found'
        try:
            for xp in body_xpath:
                try:
                    bodys = d.find_elements(By.XPATH, xp)
                    for body in bodys:
                        element_html=body.get_attribute('outerHTML')
                        body=BeautifulSoup(element_html,'html.parser')
                        temp += body.text+' '   
                except:
                    pass        
            body_data=temp
        except:
            body_data='Not found'

        try:
            if date!=None:
                date = d.find_element(By.XPATH, date_xpath)
                element_html=date.get_attribute('outerHTML')
                date=BeautifulSoup(element_html,'html.parser')
                date=date.text
            else:
                date=None    
        except:
            date='Not found'

        print("Data scrapped!!")    
        # sendLog("Data scrapped!!")    
         

        if title !='Not found':
            date_d= date_coverter(date)
            if (date_d.lower()=='not found' or date_d.lower()=='none'):
                date_d =datetime.now().timestamp()
            print("Data storing in DB....")        
            # sendLog("Data storing in DB....")        
            db_dict = {'Title': title, 'Body': body_data, 'Date': date_d, 'Url': link} #change here
            existing_data = collection2.find_one({'Title': title})

            print(db_dict)
            # sendData(db_dict)
            if existing_data:
                date_d= date_coverter(date)
                if (date_d.lower()=='not found' or date_d.lower()=='none'):
                    date_d =datetime.now().timestamp()
                if existing_data['Body'] != body_data or existing_data['Date'] != date:
                    update_query = {'$set': {'Body': body_data, 'Date': date_d, 'Url': link}}
                    collection2.update_one({'Title': title}, update_query)
            else:
                collection2.insert_one(db_dict)
            print("Database Updated!!")    
            # sendLog("Database Updated!!")    
               
        else:
            print("Data not fetched!!")            
            # sendLog("Data not fetched!!")            
            
def spa(darkweb_url, iterator, title_xpath, body_xpath,date_xpath=None,scrollable=False,clickable=False,clickable_btn_xpath=None,pagination = False,is_nextbtn=True,xpath_of_next_btn=None,xpath_of_pagination_container=None,tag_name_of_pages=None,waitTime=10):
    xvfb_display = start_xvfb()
    with TorBrowserDriver(torPath) as driver:
        driver.maximize_window()
        print("Website is opening....")
        # sendLog("Website is opening....")
        driver.get(darkweb_url)
        print("Waiting....")
        # sendLog("Waiting....")

        print("Sleep time is ",waitTime," sec")
        # sendLog("Sleep time is ",waitTime," sec")  #test

        time.sleep(waitTime)
        print("Site opened!!")
        # sendLog("Site opened!!")
        

        if scrollable==True:
            print("Site is scrollable...please wait")
            # sendLog("Site is scrollable...please wait")
            scroll(driver)

        while clickable == True :
            print("Site is clickable...")
            # sendLog("Site is clickable")
            if clickable_btn_xpath!=None:
                clickable = press_next_btn(driver,clickable_btn_xpath)
            

        if pagination == True:
            print("Site contains pagination...")
            # sendLog("Site contains pagination")
            i=0
            while pagination == True :
                scrap(driver,iterator,title_xpath,body_xpath,date_xpath,darkweb_url)
                if is_nextbtn == True and xpath_of_next_btn!=None:
                    pagination = press_next_btn(driver,xpath_of_next_btn)
                    if pagination==False:
                        break
                if is_nextbtn == False and xpath_of_pagination_container!=None and tag_name_of_pages!=None:
                    i = i + 1
                    pagination = no_next_btn(driver,i,xpath_of_pagination_container,tag_name_of_pages)
                    if pagination==False:
                        break

        else:  
            scrap(driver,iterator,title_xpath,body_xpath,date_xpath,darkweb_url)                      
        driver.close()
    stop_xvfb(xvfb_display)