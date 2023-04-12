import os

#Parametros para configurar la busqueda
job_type = 'Ingeniero Mecatronico'
job_location = 'Bogota'

#Parametros para configurar envio de email.
email_sender ='ingenieros.caroni@gmail.com'
email_password =os.environ.get('gmail_password') #clave creada por gmail para la aplicacion. 
#Diferente a clave usada para ingresar al correo. https://www.youtube.com/watch?v=g_j6ILT-X0k&ab_channel=ThePyCoach

email_receiver_list =['oscar@ingenierocaro.co', 'oscar.ricardo.caro@gmail.com']
subject='Computrabajo data'

#Configuracion para gmail (no es necesario cambiar si usa gmail)
smtp_port=587
smtp_server= 'smtp.gmail.com'




#parametros staticos ( No es necesario cambiar)
url = 'http://co.computrabajo.com/'
attachment_filename = 'data\data.csv'