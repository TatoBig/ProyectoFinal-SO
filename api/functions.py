#ESTE ARCHIVO CONTIENE LAS COSAS PARA PODER HACER FUNCIONAR LA APLICACION XD
def getGateway(ip):
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
    if (i < mascara):
      result.append(1)
    elif (i >= mascara):
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
