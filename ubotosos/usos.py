from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException
import time

base_url = "https://login.uj.edu.pl/login"

class Ubotosos():
    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Dom\Desktop\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()

    def login(self, USERNAME, PASSWORD):
        self.driver.get(base_url)

        username = self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(USERNAME)

        password = self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(PASSWORD)

        submit = self.driver.find_element_by_name('submit')
        submit.click()

    def main_go_to_list_of_courses(self):
            
        self.driver.get("https://www.usosweb.uj.edu.pl/kontroler.php?_action=dla_stud/rejestracja/kalendarz")

        rejestracja = self.driver.find_element_by_xpath('//*[@id="layout-c22a"]/div/table[2]/tbody/tr[4]/td[6]/div/a')
        rejestracja.click()

    def sec_go_to_list_of_courses(self):
                
        self.driver.get("https://www.usosweb.uj.edu.pl/kontroler.php?_action=dla_stud/rejestracja/kalendarz")

        rejestracja = self.driver.find_element_by_xpath('//*[@id="layout-c22a"]/div/table[2]/tbody/tr[6]/td[6]/div/a')
        rejestracja.click()

    def open_new_tab(self, index):
        window_name = f"Tab{index}"
        self.driver.execute_script(f'window.open("about:blank", "{window_name}");')
        return window_name


    def open_link_in_new_tab(self, url, index):
        window_name = f"Tab{index}"
        self.driver.execute_script(f'window.open("about:blank", "{window_name}");')
        self.driver.get(url)
        return window_name

    def get_all_tabs(self):
        return self.driver.window_handles

    def switch_window(self, window_name):
        self.driver.switch_to_window(window_name)

    def close_window(self):
        self.driver.close()
    
    def go_to_register_page(self, course):
        subject = self.driver.find_element_by_link_text(course)
        subject.click()

    def register(self, course, group):


        koszyk = self.driver.find_element_by_xpath('//*[@id="layout-c22a"]/span/table[2]/tbody/tr[1]/td[3]/div[1]/span[2]/a[1]/img')
        
        # print(koszyk.get_attribute("src"))
        
        if 'koszyk_in' in koszyk.get_attribute('src'):
            koszyk.click()
            all_inputs = self.driver.find_elements_by_tag_name('input')
            for input in all_inputs:

                if len(group) > 1:
                    for index in range(len(group)-1):
                        if input.get_attribute("type") == 'radio':
                            if int(input.get_attribute('value')) == group[index]:
                                input.click()
                                all_submits = self.driver.find_elements_by_css_selector('input.submit')
                                
                                for submit in all_submits:
                                    if submit.get_attribute('value') == 'Rejestruj':
                                        submit.click()
                                        print("Pomyślnie zarejestrowano na ", course, " do grupy ", group[index])
                else:
                    if input.get_attribute("type") == 'radio':
                            if int(input.get_attribute('value')) == group[index]:
                                input.click()
                                all_submits = self.driver.find_elements_by_css_selector('input.submit')
                                
                                for submit in all_submits:
                                    if submit.get_attribute('value') == 'Rejestruj':
                                        submit.click()
                                        print("Pomyślnie zarejestrowano na ", course, " do grupy ", group[index])

                        
        else:
            print("Jesteś już zarejestrowany na ", course)


    def unregister(self, course, group):

        koszyk = self.driver.find_element_by_xpath('//*[@id="layout-c22a"]/span/table[2]/tbody/tr[1]/td[3]/div[1]/span[2]/a[1]/img')
        
        if 'koszyk_out' in koszyk.get_attribute('src'):
            koszyk.click()
            alert = self.driver.switch_to.alert
            alert.accept()
            print("Pomyślnie wyrejestrowano z ", course)
        else:
            print("Nie byłeś zarejestrowany na ", course)

    def register_to_full(self, course, group):
        subject = self.driver.find_element_by_link_text(course)
        subject.click()

        koszyk = self.driver.find_element_by_xpath('//*[@id="layout-c22a"]/span/table[2]/tbody/tr[1]/td[3]/div[1]/span[2]/a[1]/img')


class Botogaz:

    def __init__(self):
        self.driver = webdriver.Chrome(executable_path=r'C:\Users\Dom\Desktop\chromedriver_win32\chromedriver.exe')
        self.driver.maximize_window()

    def login(self, USERNAME, PASSWORD):
        self.driver.get(base_url)

        username = self.driver.find_element_by_name('username')
        username.clear()
        username.send_keys(USERNAME)

        password = self.driver.find_element_by_name('password')
        password.clear()
        password.send_keys(PASSWORD)

        submit = self.driver.find_element_by_name('submit')
        submit.click()

    def go_to_pegaz(self):
        self.driver.get("https://pegaz.uj.edu.pl/login/index.php?authCAS=CAS")
    
    def go_to_pegaz_exams(self):
        self.driver.get("https://egzaminy.uj.edu.pl/login/index.php?authCAS=CAS")

    def get_titles_of_all_courses(self):
        time.sleep(2)
        try:
            titles = self.driver.find_elements_by_xpath("//span[@class='multiline']")
            WebDriverWait(self.driver, 5)
            return titles
        except TimeoutException:
            print("Timed out waiting for page too long")
    
    def go_into_annoucment_and_forum(self):
        try:
            activitys = self.driver.find_elements_by_xpaty("//li[@class='activity forum modtype_forum '")
            # print(activitys)

            for activity in activitys:
                print(activity.text)



        except TimeoutException:
            print("Timed out waiting for page too long")


    def get_section_info(self):
        try:
            sections = self.driver.find_elements_by_xpath("//li[@class='section main clearfix']")
            WebDriverWait(self.driver, 5)
            
            for section in sections:
                print(section.text)

            # print(sections)
            # return sections
        except TimeoutException:
            print("Timed out waiting for page too long")
       
        

    # pozostałości po poprzedniej koncepcji (:
    def go_to_course(self, name, titles):



        # splited_name = name.split(" ")

        for title in titles:
            if title.text == name:
                print(title.text)

        # print(titles)
        # for title in titles:
        #     # print(title.text)
        #     splited_title = title.text.split(" ")
            
        #     true_list = list()
        #     if splited_title is not ['']:
        #         for word in range(0, len(splited_name)):
        #             # print(len(name.split(" ")), word, name.split(" "), title.text.split(" "))
        #             if splited_name[word] == splited_title[word]:
        #                 print(splited_name[word], splited_title[word])
        #                 true_list.append(bool(True))

        #         # print(true_list ,true_list.count(bool(True)), len(splited_name))
        #         if (true_list.count(bool(True)) + 1) == len(splited_name):
        #             print(title.text)
                    
        #             # if splited_name[word] == splited_title[word]:
        #             #     # title.click()
        #             #     print(title.text)
        #         # wierd_list = [name for index, word in enumerate(splited_name) if word == splited_title[word]]
        #         # print(wierd_list)


    def open_new_tab(self, index):
        window_name = f"Tab{index}"
        self.driver.execute_script(f'window.open("about:blank", "{window_name}");')
        return window_name


    def open_link_in_new_tab(self, url, index):
        window_name = f"Tab{index}"
        self.driver.execute_script(f'window.open("about:blank", "{window_name}");')
        self.driver.switch_to_window(window_name)
        self.driver.get(url)
        return window_name

    def get_all_tabs(self):
        return self.driver.window_handles

    def switch_window(self, window_name):
        self.driver.switch_to_window(window_name)

    def close_window(self):
        self.driver.close()
    
    