import src.functions_computrabajo_scrapper as functions_computrabajo_scrapper
import config
from datetime import datetime
from datetime import date
import src.send_email as send_email

#parametros de inicio
today = date.today()
data_pagina=[]
data=[]
job_type = config.job_type
job_location = config.job_location
url = config.url
today = config.today
email_receiver_list = config.email_receiver_list
subject= config.subject
attachment_filename = config.attachment_filename
body = config.body

#Main program
tiempo_inicial = datetime.now()
functions_computrabajo_scrapper.abrir_pagina(url)
functions_computrabajo_scrapper.realizar_busqueda(job_type, job_location)
functions_computrabajo_scrapper.popup_cancelar()
total_paginas=functions_computrabajo_scrapper.obtener_total_paginas()

#bucle para revisar la informacion del total paginas
for i in range(total_paginas): 
    print(f"Pagina numero : {i+1}")
    pagina_actual=functions_computrabajo_scrapper.load_soup()
    trabajos = functions_computrabajo_scrapper.cargar_id_trabajos(pagina_actual)
    #time.sleep(0.1)
    data_pagina=functions_computrabajo_scrapper.iterar_trabajos(trabajos) 
    data.extend(data_pagina)  
    functions_computrabajo_scrapper.siguiente_bloque_ofertas()
    #time.sleep(0.1)
    functions_computrabajo_scrapper.delete_cookies()


#enviar la informacion a una tabla de csv
functions_computrabajo_scrapper.guardar_csv(data)

#stats
tiempo_final=datetime.now()
tiempo_ejecucion=tiempo_final-tiempo_inicial
total_trabajos= len(data)
print(f"tiempo ejecucion: {tiempo_ejecucion}")
print(f"Total de paginas: {total_paginas}")
print(f"Total trabajos: {total_trabajos}")


body = f"""
        Data scrapped from Computrabajo
        On:  {today}
        Tiempo ejecucion: {tiempo_ejecucion}
        Total trabajos: {total_trabajos}
        Tipo de trabajo: {job_type}
        Lugar de ofertas: {job_location}
      """

#enviar email con la informacion recolectada
send_email.send_email_attach(email_receiver_list, subject, body, attachment_filename)