#!/isan/bin/python
from cisco import *
import sys, time
from cisco.vrf import *
from cisco.interface import *
import datetime

numArg = len(sys.argv)
# verificar si cancelar
if sys.argv[1] == "cancel":
    schedCLIjob = 'conf t ; no scheduler job name reloadinCommand5657373'
    schedCLItime = 'conf t ; no scheduler schedule name reloadinCommand5657373'
    print ("Canceling reload")
# verificando el número de argvs y si el primero es un número entero
elif numArg <= 3:
    try: #Manejo de errores de Python
        requestTime = int(sys.argv[1])
    except:
        print ("Enter a integer for time")
sys.exit() #rescatar si la entrada es incorrecta #salir si la entrada es incorrecta
now = datetime.datetime.now() #obtener la hora actual
actionTime = now + datetime.timedelta(minutes = requestTime) #establecer el tiempo de recarga
reloadTime = str(actionTime) # tiempo de recarga en una cadena
reloadTime = reloadTime[11:-10]
# compilar CLI con un nombre de programación único
schedCLIjob = 'conf t ; scheduler job name reloadincomando5657373 ; reload ; exit' schedCLItime = 'conf t ; scheduler schedule name reloadinCommand5657373 ; job name reloadinCommand5657373 ; time start ' + reloadTime + ' repeat 48:00 ; end '
# guardar configuración
if numArg == 3 and sys.argv[2] == "save".lower():
    cli('copy running-config startup-config')
    print ("Saving config before reload")
    #imprime salida del script
    print ("current time on the switch is ") + str(now)
    print ("reload scheduled at ") + reloadTime

cli('conf t ; feature scheduler')
try:
    cli(schedCLIjob)
except:
    print ("operation failed..did you cancel a job that was not there?")
sys.exit()
cli(schedCLItime)
print ("Operation success")