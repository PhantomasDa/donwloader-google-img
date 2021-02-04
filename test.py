from selenium import webdriver
import time, requests
import pandas as pd
import os
import shutil

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
    except OSError:
        print ('Error: Creating directory. ' +  directory)


def search_google(search_query):
    try:
        browser = webdriver.Chrome()
        search_url = f"https://www.google.com/search?site=&tbm=isch&source=hp&biw=1873&bih=990&q={search_query}"
        images_url = []

        # open browser and begin search
        browser.get(search_url)
        elements = browser.find_elements_by_class_name('rg_i')
        # print("abriendo buscador...")
        count = 0
        for e in elements:
            # get images source url
            e.click()
            time.sleep(1)
            element = browser.find_elements_by_class_name('v4dQwb')
            # Google image web site logic
            if count == 0:
                big_img = element[0].find_element_by_tag_name("img")
            else:
                 big_img = element[1].find_element_by_tag_name("img")

            images_url.append(big_img.get_attribute("src"))
            # print("Guardando")

            # write image to file
            
            reponse = requests.get(images_url[count])
            if reponse.status_code == 200:
                with open(f"{query_string}{count+1}.png","wb") as file:    
                    file.write(reponse.content)
                # print("imagen descargada :D")
           
            count += 1
            # shutil.move(f'{quer_string}.png', '{query_string}')

            # Stop get and save after 5
            if count == 5:
                break
        return images_url
    except (RuntimeError, TypeError, NameError, OSError):
        print(f'{query_string} ERROR.1')
        return images_url
        
    except:
        print(f'{query_string} ERROR.2')
        return images_url    
   



# Leer el documento y definir query_string
Products= pd.read_csv('Producto.csv')
List_Name = Products['Nombre']
sizeCicle = len(List_Name)


for i in List_Name:
    print(i, end="Completo" +'\n')
    query_string = i
    items = search_google(query_string)
    createFolder(f'{query_string}')

    time.sleep(5)
