from selenium.common.exceptions import NoSuchElementException, ElementNotInteractableException
from tbselenium.tbdriver import TorBrowserDriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 
from bs4 import BeautifulSoup
from databaseConnection import collection2,collection3
from datetime import date
import time
# from startDisplay import *
from flag import sendData,sendLog
from driverpath import torPath
from dateformat import *

def scroll(driver):
    reached_page_end = False
    last_height = driver.execute_script("return document.body.scrollHeight")
    while not reached_page_end:
        driver.find_element(By.XPATH,'//body').send_keys(Keys.END)   
        time.sleep(10)
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
            time.sleep(10)
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

def scrap_nonSpa(driver,post_links,title_xpath,body_xpath,date_xpath):
    print("Data scraping....")
    # sendLog("Data scraping....")
    for lnk in post_links:
        try:
            driver.get(lnk)
            time.sleep(10)
        except:
            pass    
        temp = ''
        try:
            title = driver.find_element(By.XPATH, title_xpath)
            element_html=title.get_attribute('outerHTML')
            title=BeautifulSoup(element_html,'html.parser')
            title=title.text
            temp += title+' '
            
        except:
            title='Not found'

        try:
            for xp in body_xpath:
                try:
                    bodys = driver.find_elements(By.XPATH, xp)
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
            if date_xpath !=None:
                date = driver.find_element(By.XPATH, date_xpath)
                element_html=date.get_attribute('outerHTML')
                date=BeautifulSoup(element_html,'html.parser')
                date=date.text
            else:
                date=None    
        except:
            date='Not found'

        # print("Data scraped!!")    
        # sendLog("Data scraped!!")    
        
        if title !='Not found':
            dateChecker=False
            if date==None:
                date_d =int(datetime.now().timestamp())
                date_d =int(date_d)
            else:
                date_d= date_coverter(date)

                if (date_d.lower()=='not found' ):
                    date_d =int(datetime.now().timestamp())
                    date_d =str(date_d)+"$"
                    date_for_error_collection='not found( may be error in XPATH)'
                    dateChecker=True
                    # add in thired collection-------- error in xpath
                else:
                    try:
                        date_d =int(date_d)
                    except:
                        date_d =int(datetime.now().timestamp())
                        date_d =str(date_d)+"$"
                        date_for_error_collection=date
                        dateChecker=True
                        # add in thired collection--------

            if dateChecker==True:
                erroredDataDict = {'Title': title, 'Body': body_data, 'Date': date_for_error_collection, 'Url': lnk}
                existing_errored_data = collection3.find_one({'Url':lnk})
                if not existing_errored_data:
                    collection3.insert_one(erroredDataDict)
                
            print("Data storing in DB in progress....")  
            # sendLog("Data storing in DB in progress....")  
            db_dict = {'Title': title, 'Body': body_data, 'Date': date_d, 'Url': lnk}  #change here
            existing_data = collection2.find_one({'Url': lnk})

            print(db_dict)
            # sendData(db_dict)
            if existing_data:
                if existing_data['Body'] != body_data or existing_data['Date'] != date_d:
                    update_query = {'$set': {'Title': title,'Body': body_data, 'Date': date_d, 'Url': lnk}}
                    collection2.update_one({'Url': lnk}, update_query)
                    print("Database Updated!!")
            
            else:
                collection2.insert_one(db_dict)
                print("New data inserted!!...")          
                # sendLog("New data inserted!!...")          
              
        else:
            print("Data not fetched!!")        
            # sendLog("Data not fetched!!")        

def Non_spa(darkweb_url, iterator, title_xpath, body_xpath,date_xpath=None,scrollable=False,clickable=False,clickable_btn_xpath=None,pagination = False,is_nextbtn=True,xpath_of_next_btn=None,xpath_of_pagination_container=None,tag_name_of_pages=None,waitTime=10):
    # xvfb_display = start_xvfb()
    with TorBrowserDriver(torPath) as driver:
 
        driver.maximize_window()
        print("Website is opening....")
        # sendLog("Site opening....")
        driver.get(darkweb_url)
        print("Waiting....")
        # sendLog("Waiting....")
        print("Sleep time is ",waitTime," sec")
        # sendLog("Sleep time is ",waitTime," sec")
        time.sleep(waitTime)
        print("Site opened")
        # sendLog("Site opened")
        if scrollable==True:
            print("Site is scrollable...please wait")
            # sendLog("Site is scrollable...please wait")
            scroll(driver)

        while clickable == True :
            print("Site is clickable")
            # sendLog("Site is clickable")
            if clickable_btn_xpath!=None:
                clickable = press_next_btn(driver,clickable_btn_xpath)

        perv_url=None
        post_links=[]
        if pagination == True:
            i=0
            while pagination == True :
                print("Site contains pagination")
                # sendLog("Site contains pagination")
                post_link=driver.find_elements(By.XPATH,iterator)
                for inside_lnk in post_link:
                    try:
                        lnk=inside_lnk.get_attribute('href')
                        if lnk !='#' and lnk!=None:
                            post_links.append(lnk) 
                    except:
                        pass
                    try:
                        lnk2=inside_lnk.get_attribute("onclick")
                        ind=lnk2.index("'")
                        temp_link=""
                        for i in range(ind+1,len(lnk2)):
                            if lnk2[i]!="'":
                                temp_link+=lnk2[i]
                            else:
                                break
                        if temp_link!="" and lnk2 !=None:
                            lnk=  darkweb_url + temp_link
                            post_links.append(lnk)
                    except: 
                        pass
                    

                if is_nextbtn == True and xpath_of_next_btn!=None:

                    curr_url=driver.current_url
                    if curr_url==perv_url:
                        break
                    else:
                        perv_url=curr_url

                    pagination = press_next_btn(driver,xpath_of_next_btn)
                    if pagination==False:
                        break

                if is_nextbtn == False and xpath_of_pagination_container!=None and tag_name_of_pages!=None:
                    i = i + 1
                    pagination = no_next_btn(driver,i,xpath_of_pagination_container,tag_name_of_pages)
                    if pagination==False:
                        break
        else:
            post_link=driver.find_elements(By.XPATH,iterator)
            for inside_lnk in post_link:
                try:
                    lnk=inside_lnk.get_attribute('href')
                    if lnk !='#' and lnk!=None:
                        post_links.append(lnk) 
                except:
                    pass
                try:
                    lnk2=inside_lnk.get_attribute("onclick")
                    ind=lnk2.index("'")
                    temp_link=""
                    for i in range(ind+1,len(lnk2)):
                        if lnk2[i]!="'":
                            temp_link+=lnk2[i]
                        else:
                            break
                    if temp_link!="" and lnk2 !=None:
                        lnk=  darkweb_url + temp_link
                        post_links.append(lnk)
                      
                except:
                    pass 

        if len(post_links)>0:
            scrap_nonSpa (driver,post_links,title_xpath,body_xpath,date_xpath)   

        driver.close()
    # stop_xvfb(xvfb_display)