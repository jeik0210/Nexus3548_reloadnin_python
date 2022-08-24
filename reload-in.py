#!/isan/bin/python
from cisco import *
import sys, time
from cisco.vrf import *
from cisco.interface import *
import datetime

numArg = len(sys.argv)
# check if cancel
if sys.argv[1] == "cancel":
    schedCLIjob = 'conf t ; no scheduler job name reloadinCommand5657373'
    schedCLItime = 'conf t ; no scheduler schedule name reloadinCommand5657373'
    print ("Canceling reload")
# check number of argvs and if first one is an integer
elif numArg <= 3:
    try: #Python error handling 
        requestTime = int(sys.argv[1])
    except:
        print ("Enter a integer for time")
sys.exit() #bail out if input is wrong #exit if input is incorrect
now = datetime.datetime.now() #get the current time
actionTime = now + datetime.timedelta(minutes = requestTime) #set the reload time
reloadTime = str(actionTime) # reload time in astring
reloadTime = reloadTime[11:-10]
# build CLI with unique schedule name
schedCLIjob = 'conf t ; scheduler job name reloadincomando5657373 ; reload ; exit' schedCLItime = 'conf t ; scheduler schedule name reloadinCommand5657373 ; job name reloadinCommand5657373 ; time start ' + reloadTime + ' repeat 48:00 ; end '
# save configuration
if numArg == 3 and sys.argv[2] == "save".lower():
    cli('copy running-config startup-config')
    print ("Saving config before reload")
    #print script output
    print ("current time on the switch is ") + str(now)
    print ("reload scheduled at ") + reloadTime
# run the CLI
cli('conf t ; feature scheduler')
try:
    cli(schedCLIjob)
except:
    print ("operation failed..did you cancel a job that was not there?")
sys.exit()
cli(schedCLItime)
print ("Operation success")