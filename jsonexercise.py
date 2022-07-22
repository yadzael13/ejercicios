"""Un pollito quiere llegar a asu mama que esta a 2m de distancia"""

def distancia(pio_step):
	general_distance = 0
	pasos = 0
	while general_distance < 200:
		pasos +=1
		general_distance += pio_step
	print(pasos * pio_step)
	return pasos

#print("necesitas", distancia(7), "pasos para llegar a la mama")



"""en una carrera hay una torutga y un caracol,la tortuga recorre medio metro 
en 20 minutos y el caracol recorre la misma cantidad en 26 minutos
cuanto tiempo se tardara en llegar cada uno si la distancia de la meta
 esa en 1500km, represanta la cantidad en horas"""

def conversion(d, t):
	return (d/1000)/(t/60)
def meta(vel):
	return (1500/vel)
tortuga = conversion(0.5, 20)
caracol = conversion(0.5, 26)
print(tortuga)
print(caracol)
print("la tortuga llegara en: ", (meta(tortuga)/24)/365, "años")
print("el caracol llegara en: ", (meta(caracol)/24)/365, "años")

