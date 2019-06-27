import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from scipy import signal
import matplotlib.dates as mdates
from datetime import datetime
formato_tiempo=mdates.DateFormatter("%H:%M")
plt.figure("Análisis de temperaturas en latas de diversos colores")
plt.gca().xaxis.set_major_formatter(formato_tiempo)

#Lata Blanca 2
dataBlanca2=np.genfromtxt("lata_blanca_2.txt",names=True,delimiter=", ",dtype=None,encoding=None)
date_listBlanca2=list()
for i in range(0,len(dataBlanca2)):
    fecha_horaBlanca2=dataBlanca2["fecha"][i]+" "+dataBlanca2["hora"][i]
    date_listBlanca2.append(datetime.strptime(fecha_horaBlanca2, "%d-%m-%Y %H:%M:%S"))
plt.plot(date_listBlanca2,dataBlanca2["temperatura_lata"],color="olive", linestyle= "solid", label="Lata blanca 2", linewidth=1.0)
plt.plot(date_listBlanca2,signal.medfilt(dataBlanca2["temperatura_ambiente"],31),color="green", linestyle= "dashed", label="Ambiente 2", linewidth=0.8)

#Lata Aluminio 3
data=np.genfromtxt("lata_aluminio_3.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura"], color="red", linestyle= "solid", label="Lata aluminio 3", linewidth=1.0)

#Lata Negra 4
data=np.genfromtxt("lata_negra_4.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d.%m.%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura_lata"], color="k", linestyle= "solid", label="Lata negra 4",linewidth=1.0)

# Lata Blanca 5
data=np.genfromtxt("lata_blanca_5.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura_lata"],color="orchid", linestyle= "solid", label="Lata blanca 5", linewidth=1.0)
plt.plot(date_list,signal.medfilt(data["temperatura_ambiente"],595), color="purple", linestyle= "dotted", label="Ambiente 5", linewidth=0.8)

#Lata Azul 7
data=np.genfromtxt("lata_azul_7.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d-%m-%Y %H:%M:%S"))
plt.plot(date_list,data["temperatura"],color="royalblue", linestyle= "solid", label="Lata azul 7", linewidth=0.7, markersize=3)

#Lata Blanca 8
data=np.genfromtxt("lata_blanca_8.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d.%m.%Y %H:%M:%S"))
plt.plot(date_list,signal.medfilt(data["temperatura_lata"],295), color="darkcyan", linestyle= "solid" , label="Lata blanca 8", linewidth=1.0)
plt.plot(date_list,signal.medfilt(data["temperatura_ambiente"],9), color="teal", linestyle= "dotted", label="Ambiente 8", linewidth=0.8)

#Lata Aluminio 9
data=np.genfromtxt("lata_aluminio_9.txt",names=True,delimiter=",",dtype=None,encoding=None)
date_list=list()
for i in range(0,len(data)):
    fecha_hora=data["fecha"][i]+" "+data["hora"][i]
    date_list.append(datetime.strptime(fecha_hora, "%d.%m.%Y %H:%M:%S"))
plt.plot(date_list,signal.medfilt(data["temperatura_lata"],389), color="gray", linestyle= "solid", label="Lata aluminio 9", linewidth=1.0)


plt.xlabel("Hora [HH:MM]")
plt.ylabel("Temperatura [°C]")
#plt.title("Análisis de temperaturas en latas de diversos colores")
plt.grid(color="gray", linestyle= "none", linewidth=0.01)
plt.legend(loc="best")
plt.show()
