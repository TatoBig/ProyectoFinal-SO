#ESTE ARCHIVO CONTIENE LAS COSAS PARA PODER HACER FUNCIONAR LA APLICACION XD
def getBroadcast(ip):
  result = ""
  octeto1 = 0
  octeto2 = 0
  octeto3 = 0
  octeto4 = 0
  #Seccion para encontrar los string
  #Octeto 1
  temp = ip
  primer_string = ip[0:ip.find('.')]
  temp = ip[ip.find('.') + 1:len(ip)]
  octeto1 = int(primer_string)
  #Octeto 2
  segundo_string = temp[0:temp.find('.')]
  temp = temp[temp.find('.') + 1:len(temp)]
  octeto2 = int(segundo_string)
  #Octeto 3
  tercer_string = temp[0:temp.find('.')]
  temp = temp[temp.find('.') + 1:len(temp)]
  octeto3 = int(tercer_string)
  # Octeto 4
  cuarto_string = temp[0:temp.find('/')]
  temp = temp[temp.find('/') + 1:len(temp)]
  octeto4 = int(cuarto_string)
  #Mascara de red
  quinto_string = temp
  mascara_de_red = int(quinto_string)
  #Aqui va para saber cuantas h van
  cantidad_de_hs = 32-mascara_de_red
  hs = ""
  for i in range(cantidad_de_hs):
    hs = hs + "1"
  if hs == '':
    octeto4 = 0
  else:
    octeto4 = int(hs,2)
  result = str(octeto1) + "." + str(octeto2) + "." + str(octeto3) + "." + str(octeto4)
  return result

def ConvertirABinario(numero):
  decimal = numero
  result = []
  nuevo_modulo = []
  modulos = []
  while decimal != 0:
    modulo = decimal % 2
    cociente = decimal // 2
    modulos.append(modulo)
    decimal = cociente
  tamanio = 8 - len(modulos)
  for i in range(tamanio):
    nuevo_modulo.append(0)
  result = nuevo_modulo + modulos
  return result
