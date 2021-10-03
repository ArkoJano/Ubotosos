from selenium import webdriver
from .usos import Ubotosos, Botogaz
from .passy import USERNAME, PASSWORD, dict_of_sub, list_of_courses, ids_of_courses
import time


base_url = "https://login.uj.edu.pl/login"



def start_usos():

    
    
    bot = Ubotosos()
    bot.login(USERNAME, PASSWORD)

    # time.sleep(2)
    for index, (course, group) in enumerate(dict_of_sub.items()):
        window_name = bot.open_new_tab(index)
        bot.switch_window(window_name)
        bot.sec_go_to_list_of_courses()
        bot.go_to_register_page(course)

    # time.sleep(2)  

    all_tabs = bot.get_all_tabs()
    bot.switch_window(all_tabs[0])
    bot.close_window()
    all_tabs = bot.get_all_tabs()

    while True:

        try:
            for index, (course, group) in enumerate(dict_of_sub.items()):
                bot.switch_window(all_tabs[index])
                bot.main_go_to_list_of_courses()
                bot.go_to_register_page(course)
                # bot.register()
            
            break
        except:
            pass
            # time.sleep(.5)
    time.sleep(2)


    
        # bot.unregister(course, group)  
        # bot.go_to_list_of_courses()
        # bot.unregister(course, group)  
        # bot.go_to_list_of_courses()
        # bot.register(course, group)  
        # bot.go_to_list_of_courses()
        # bot.unregister(course, group)  
        
    
    
def start_pegaz():

    bot = Botogaz()
    bot.login(USERNAME, PASSWORD)

    # bot.go_to_pegaz()
    # titles = bot.get_titles_of_all_courses()

    # for index, name in enumerate(list_of_courses):
    #     window_name = bot.open_new_tab(index)
    #     bot.switch_window(window_name)
    #     bot.go_to_pegaz()
    #     bot.go_to_course(name, titles)

    course_base_url = "https://pegaz.uj.edu.pl/course/view.php?id="
    for index, id in enumerate(ids_of_courses):
        bot.open_link_in_new_tab(course_base_url + id, index)
        bot.get_section_info()
    