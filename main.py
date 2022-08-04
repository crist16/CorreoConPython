import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
#Para configurar gmail y poder enviar correos hay que setear 2 verification y crear una custom app en la cuenta de google
# Iniciamos los parámetros del script
remitente = "bolivariano.automated@gmail.com"

destinatarios = "cristobalnegocio@gmail.com"
asunto = '[RPI] Correo de prueba'
cuerpo = 'Este es el contenido del mensaje'
ruta_adjunto = "Outputs/constanciaTrabajo.docx"
nombre_adjunto = 'constanciaTrabajo.docx'

em = MIMEMultipart()
em['From'] = remitente
em['To'] = destinatarios
em['Subject'] = asunto
em.add_header('Content-Disposition', 'attachment', filename='bud.gif')

# Agregamos el cuerpo del mensaje como objeto MIME de tipo texto
em.attach(MIMEText(cuerpo, 'plain'))

# Abrimos el archivo que vamos a adjuntar
archivo_adjunto = open(ruta_adjunto, 'rb')

# Creamos un objeto MIME base
adjunto_MIME = MIMEBase('application', 'octet-stream')
# Y le cargamos el archivo adjunto
adjunto_MIME.set_payload((archivo_adjunto).read())
# Codificamos el objeto en BASE64
encoders.encode_base64(adjunto_MIME)
# Agregamos una cabecera al objeto
adjunto_MIME.add_header('Content-Disposition', "attachment; filename= %s" % nombre_adjunto)
# Y finalmente lo agregamos al mensaje
em.attach(adjunto_MIME)

# Creamos la conexión con el servidor
sesion_smtp = smtplib.SMTP('smtp.gmail.com', 587)

# Ciframos la conexión
sesion_smtp.starttls()

# Iniciamos sesión en el servidor
sesion_smtp.login(remitente,my_pass)

# Convertimos el objeto mensaje a texto
texto = em.as_string()

# Enviamos el mensaje
sesion_smtp.sendmail(remitente, destinatarios, texto)

# Cerramos la conexión
sesion_smtp.quit()
