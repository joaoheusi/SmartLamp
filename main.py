# Complete project details at https://RandomNerdTutorials.com


def web_page():
    if led.value() == 1:
        gpio_state="ON"
    else:
        gpio_state="OFF"

    html = """<html> <head> <title>Smart Lamp</title> <meta name="viewport" content="width=device-width, initial-scale=1" /> <link rel="icon" href="data:," /> <link rel="stylesheet" 
    href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.3/dist/css/bootstrap.min.css" integrity="sha384-TX8t27EcRE3e/ihU7zmQxVncDAy5uIKz4rEkgIXeMed4M0jlfIDPvg6uqKI2xXr2" crossorigin="anonymous" />
     <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/all.css"> <link rel="stylesheet" href="https://use.fontawesome.com/releases/v5.15.1/css/v4-shims.css"> <style> 
     mainbody { font-family: Helvetica; display: inline-block; margin: 0px auto; text-align: center; } .button { display: inline-block; border: none; border-radius: 4px; color: white; padding: 
     16px 40px; text-decoration: none; font-size: 30px; margin: 4px; cursor: pointer; } p { font-size: 1.5rem; } </style> </head> <body> <div class="container"> <div class="jumbotron"> <h1>Smart 
     Lamp &nbsp <a href="/"><span><i class="fa fa-refresh" aria-hidden="true"></i></span></a></h1> </div> <div class="mainbody"> <p>Estado da Led <strong> """ + gpio_state + """</strong></p> <p> 
     <a href="/?led=on" ><button class="button btn btn-success btn-lg btn-lg"> Ligar </button></a > </p> <p> <a href="/?led=off" ><button class="button btn btn-danger btn-lg btn-lg"> Desligar 
     </button></a > </p> </div> </div> </body></html>"""
    return html

  

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 80))
s.listen(5)
from machine import Pin, ADC 
from time import sleep

verify click()


while True:

   
    if led_on == 6 or led_off == 6:
        if led_on == 6:
            print('LED ON')
            led.value(1)
        elif led_off == 6:
            print('LED OFF')
            led.value(0)
        continue

    sleep(1/10)
    #Sensor de luminosidade
    adc = ADC(Pin(32))
    adc.atten(ADC.ATTN_11DB)
    adc.width(ADC.WIDTH_12BIT)

    print(adc.read())

    # Sensor de movimentacao
    infra_mov = Pin(22, Pin.IN)
    print(infra_mov.value())

    # Conexao via web
    conn, addr = s.accept()
    print('Got a connection from %s' % str(addr))
    request = conn.recv(1024)
    request = str(request)
    print('Content = %s' % request)
    # Caso sejam encontradas requests para ligar ou desligar, valor passado para as variaveis
    led_on = request.find('/?led=on')
    led_off = request.find('/?led=off')

    if adc.read() >= 3800 and infra_mov.value()==1:
        led.value(1)

    response = web_page()
    conn.send('HTTP/1.1 200 OK\n')
    conn.send('Content-Type: text/html\n')
    conn.send('Connection: close\n\n')
    conn.sendall(response)
    conn.close()
