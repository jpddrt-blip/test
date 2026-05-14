import time

segundos = 0
minutos = 0
horas = 0

while horas < 2:
    time.sleep(0.01)
    if segundos == 60:
        segundos = 0
        minutos += 1
    if minutos == 60:
        minutos = 0
        horas += 1

print(f'\r', horas, minutos, segundos, end='')
time.sleep(0.01)