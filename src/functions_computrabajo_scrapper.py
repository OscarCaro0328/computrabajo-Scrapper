from typing import List

import requests
import csv
import time
import math
from bs4 import BeautifulSoup
import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import ElementNotInteractableException

ofertas_empleos = []
errores = 0
headers = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36"}
# driver.set_window_size(1920, 1080)
service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)
wait = WebDriverWait(driver, 10)


# abrimos pagina deseada
def abrir_pagina(url: str):
    driver.get(url)  # ir a la pagina deseada

# enviamos parametros de busqueda y realizamos busqueda
def realizar_busqueda(job_type: str, job_location: str):
    # Locate the search input elements and enter the search parameters
    driver.find_element(By.ID, "prof-cat-search-input").send_keys(job_type)
    driver.find_element(By.ID, "place-search-input").send_keys(job_location)
    time.sleep(0.2)
    driver.find_element(By.ID, "search-button").click()
    time.sleep(0.2)

# obtenemos la url actual para examinarla con beautifulSoup
def load_soup() -> BeautifulSoup:
    current_url = driver.current_url
    html_text = requests.get(
        current_url, headers=headers)
    soup = BeautifulSoup(html_text.text, 'lxml')
    return soup

# pop up notificaciones /rechazar
def popup_cancelar():
    try:
        notification_button = driver.find_element(
            By.XPATH, '//*[@id="pop-up-webpush-sub"]/div[2]/div/button[1]')
        time.sleep(1)
        notification_button.click()
    except Exception as e:
        print("No popup", e)
    else:
        print("pop up clicked")


def cargar_id_trabajos(pagina_actual):
    """
    Extracts the IDs of all the job postings on a web page.

    Args:
        pagina_actual (obj): The beautifulSoup object of the actual page.

    Returns:
        list: A list of all the jobs.
    """
    trabajos = pagina_actual.find_all('article')
    return trabajos


def iterar_trabajos(trabajos):
    ofertas_empleos = []

    for trabajo in trabajos:
        try:
            # Click on each job posting to get the details
            box_element = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.ID, trabajo['id'])))
            driver.execute_script("arguments[0].click();", box_element)
            detalle_trabajo = load_soup()

            # Extract the details from the job posting page
            titulo_oferta = detalle_trabajo.find("h1", class_='fwB fs24 mb5 box_detail w100_m').text
            empresa_oferta = detalle_trabajo.find("p", class_='fs16').text
            descripcion_oferta = detalle_trabajo.find('p', class_='mbB').text
            detalles_ofertas = detalle_trabajo.find_all("span", class_='tag base mb10')
            detalles_oferta_concatenados = ' '.join([detalle.text for detalle in detalles_ofertas])

            # Add the job details to the list of jobs
            ofertas_empleos.append([titulo_oferta, empresa_oferta, descripcion_oferta, detalles_oferta_concatenados])

            # Go back to the search results page
            driver.back()
            time.sleep(0.2)
        except Exception as e:
            print("error: ", e)
            global errores
            errores += 1
            print("errores: ", errores)

    return ofertas_empleos

 # funcion para dar click a siguiente pagina
def siguiente_bloque_ofertas():
    """
    Clicks on the 'Next' button to load the next page of offers on a specific website.

    Returns:
        None

    Raises:
        Exception: If there is an error locating or clicking the 'Next' button.
    """
    try:
        siguiente = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="offersGridOfferContainer"]/div[8]/span[2]')))
        driver.execute_script("arguments[0].click();", siguiente)
    except Exception as e:
        print("Error: ", e)


def delete_cookies():
    driver.delete_all_cookies()
    time.sleep(0.1)
    driver.refresh()


def obtener_total_paginas():
    soup = load_soup()
    h1_element = soup.select_one('h1.title_page')
    total_ofertas = int(h1_element.select_one('span.fwB').text.replace('.', ''))
    total_paginas = math.ceil(total_ofertas / 20)
    return total_paginas


def guardar_csv(attachment, data):
    # Open the file for writing
    with open(attachment, mode='w', newline='', encoding='UTF-16') as file:
        # Create a CSV writer object
        writer = csv.writer(file, delimiter="\t")

        # Write the data to the file
        for row in data:
            try:
                writer.writerow(row)
            except Exception as e:
                print(f"exception: {e}")
                print("caracter no valido")

    print('Data written successfully.')
    
