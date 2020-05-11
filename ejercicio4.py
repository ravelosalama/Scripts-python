import sys
import datetime
print (sys.version)
print (sys.version_info)
ahora=datetime.datetime.now()
print (datetime.datetime.now())
print (ahora)
print (type(ahora))
ahora_formato=ahora.strftime('%d-%m-%Y %H:%M:%S')
print (ahora_formato)
#print (datetime.datetime.now().format('%d-%m-%y %h:%m:%s'))
#print (ahora.format('%d-%m-%y %h:%m:%s'))

