import psutil

class temp:
    def getTemp():
        try:
            cpuTemp = psutil.sensors_temperatures()['k10temp'][0][1]
            return(cpuTemp)																			#gives temp in celsius
        except:
            try:
                cpuTemp = psutil.sensors_temperatures()['coretemp'][0][1]
                return(cpuTemp)		
            except:
                return(0)