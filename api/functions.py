#ESTE ARCHIVO CONTIENE LAS COSAS PARA PODER HACER FUNCIONAR LA APLICACION XD
def getGateway(ip):
  result = ""
  octeto1 = 0
  octeto2 = 0
  octeto3 = 0
  octeto4 = 0
  #Seccion para encontrar los string de la IP
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
  #Octeto 4
  octeto4 = int(temp)
  #Aqui se va a sumar el 1 para poder obtener el gateway
  octeto4 = octeto4 + 1
  #esta parte la comente por que no estoy seguro que hacer en estos caso xd
  #if(suma > 255):
  # print("sumo mas de 255")
  #else:
  # print("no suma mas de 255")
  #volver a unir las cosas 
  result = str(octeto1) + "." + str(octeto2) + "." + str(octeto3) + "." + str(octeto4)
  return result
def Encontrar_red(mascara):
  result = []
  tamanio = 32 - mascara
  for i in range(32):
    if (i <= mascara):
      result.append(1)
    elif (i > mascara):
      result.append(0)
  return result
  
def Obtener_ip_en_binario(octeto1, octeto2, octeto3, octeto4):
  seccion1 = ConvertirABinario(octeto1)
  seccion2 = ConvertirABinario(octeto2)
  seccion3 = ConvertirABinario(octeto3)
  seccion4 = ConvertirABinario(octeto4)
  resultado = seccion1 + seccion2 + seccion3 + seccion4
  return resultado

print(Obtener_ip_en_binario(10,0,0,3))

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
  binario = np.binary_repr(numero)
  result = binario
  tamanio = 8-len(binario)
  for i in range(tamanio):
    nuevo_modulo.append(0)
  for ii in range(len(binario)):
    modulos.append(int(binario[ii]))
  result = nuevo_modulo + modulos
  return result

def PerteneceARed(ip_base,ip_comparacion):
  #Declaracion de las variables
  matriz = [['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',''],
           ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','',],
           ['','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','','']]
  octeto_ip_base_1 = 0
  octeto_ip_base_2 = 0
  octeto_ip_base_3 = 0
  octeto_ip_base_4 = 0
  octeto_id_comparacion_1 = 0
  octeto_id_comparacion_2 = 0
  octeto_id_comparacion_3 = 0
  octeto_id_comparacion_4 = 0
  
  #Seccion paar encontrar los string de la ip base
  #Octeto 1
  temp = ip_base
  primer_string = ip_base[0:ip_base.find('.')]
  temp = ip_base[ip_base.find('.') + 1:len(ip_base)]
  octeto_ip_base_1 = int(primer_string)
  #Octeto 2
  segundo_string = temp[0:temp.find('.')]
  temp = temp[temp.find('.') + 1:len(temp)]
  octeto_ip_base_2 = int(segundo_string)
  #Octeto 3
  tercer_string = temp[0:temp.find('.')]
  temp = temp[temp.find('.') + 1:len(temp)]
  octeto_ip_base_3 = int(tercer_string)
  # Octeto 4
  cuarto_string = temp[0:temp.find('/')]
  temp = temp[temp.find('/') + 1:len(temp)]
  octeto_ip_base_4 = int(cuarto_string)
  #Mascara de red
  quinto_string = temp
  mascara_de_red = int(quinto_string)
 
  #Seccion para poder encontrar los octetos del ip base comparacion
   #Octeto 1
  temp1 = ip_comparacion
  primer_string_2 = ip_comparacion[0:ip_comparacion.find('.')]
  temp1 = ip_comparacion[ip_comparacion.find('.') + 1:len(ip_comparacion)]
  octeto_id_comparacion_1 = int(primer_string_2)
  #Octeto 2
  segundo_string_2 = temp1[0:temp1.find('.')]
  temp1 = temp1[temp1.find('.') + 1:len(temp1)]
  octeto_id_comparacion_2 = int(segundo_string_2)
  #Octeto 3
  tercer_string_2 = temp1[0:temp1.find('.')]
  temp1 = temp1[temp1.find('.') + 1:len(temp1)]
  octeto_id_comparacion_3 = int(tercer_string_2)
  # Octeto 4
  cuarto_string_2 = temp1
  octeto_id_comparacion_4 = int(cuarto_string_2)

  #Convertir los numeros decimales a binarios
  binario_de_mascara = Encontrar_red(mascara_de_red)
  binario_de_base = Obtener_ip_en_binario(octeto_ip_base_1,octeto_ip_base_2,octeto_ip_base_3,octeto_ip_base_4)
  binario_de_comparacion = Obtener_ip_en_binario(octeto_id_comparacion_1,octeto_id_comparacion_2,octeto_id_comparacion_3,octeto_id_comparacion_4)

  matriz[0] = binario_de_comparacion
  matriz[1] = binario_de_mascara
  #Ahora toca saber si es la misma, para ello vamos a multiplicar el binario de ip comparacion con el de la mascara de la red, por que es lo mismo que hacer un AND
  pos = 0
  while (pos < len(matriz[0])):
    matriz[2][pos] = binario_de_comparacion[pos] * binario_de_mascara[pos]
    pos = pos + 1

  if (matriz[2] == binario_de_base):
    return "Si pertence a red"
  else:
    return "No pertence a red"