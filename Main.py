import random
"""""
Este programa fue realizado por los estudiantes:
Un conversor de bases numericas
"""""
def bases():
  pass

def menu():

  Arreglo_de_bases = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

  #Definimos la estructura del menu y manejamos errores
  while True:
    try:
        print("\t----Bienvenido al Conversor de unidades FI UNAM----")
        base_entrada = int(input("\nPor favor ingrese la base actual:\t"))
        break
    
    except ValueError:
        print("ERROR: Ingrese un numero entero\n\n")
  

  numero_a_convertir = str(input("\nIngrese El numero a convertir:\t")).strip().upper()
  
  if numero_a_convertir[-1] != ".":
    numero_a_convertir += "."

  numero_entero_a_convertir = ""
  numero_flotante_a_convertir = "0"

  for i in range(len(numero_a_convertir)):
      if numero_a_convertir[i] == ".":
          numero_entero_a_convertir = numero_a_convertir[:i]
          numero_flotante_a_convertir = numero_a_convertir[i + 1:len(numero_a_convertir) - 1]
          break;

  while True:
    try:
        base_destino = int(input("\n¿A que base quieres ir?:\t"))
        break
    
    except ValueError:
        print("ERROR: Ingrese un numero entero\n\n")

  base_maxima = max(base_destino,base_entrada)

  if base_maxima > len(Arreglo_de_bases):
     
     print(f"\n La base maxima a convertir es {len(Arreglo_de_bases)}")

     return 
  
  Arreglo_a_utilizar = Arreglo_de_bases[0:base_entrada]


  parte_entera_convertida = conversor_bases_parte_entera(numero_entero_a_convertir,base_entrada,base_destino,Arreglo_a_utilizar, Arreglo_de_bases)
  parte_flotante_convertida = conversor_bases_parte_decimal(numero_flotante_a_convertir,base_entrada,base_destino,Arreglo_a_utilizar, Arreglo_de_bases)
  if parte_entera_convertida == -1 or parte_flotante_convertida == -1:
      print(f"El numero {numero_a_convertir} no esta en base {base_entrada}")
      return
  
  print(f"El numero es {parte_entera_convertida}", end="")
  if len(set(parte_flotante_convertida)) > 1 or parte_flotante_convertida[0] != "0":
    print(f".{parte_flotante_convertida}")


def conversor_bases_parte_entera(numero_a_convertir, base_entrada, base_destino, Arreglo_a_utilizar, Arreglo_de_bases):

  numero_convertido = ""
  numero_apoyo_en_decimal = 0
  contador_de_exponente = 0
  numero_a_convertir = numero_a_convertir[::-1]
  residuo = 0
     
  for valor in numero_a_convertir:
      try:
          
          valor_arreglo = Arreglo_a_utilizar.index(valor)
            
          numero_apoyo_en_decimal += valor_arreglo*(base_entrada**(contador_de_exponente))

          contador_de_exponente += 1
          
      except ValueError:
        
            return -1


  while(numero_apoyo_en_decimal!=0):

    residuo = numero_apoyo_en_decimal % base_destino

    residuo = Arreglo_de_bases[residuo]

    numero_apoyo_en_decimal = numero_apoyo_en_decimal//base_destino
    
    numero_convertido += residuo

  return numero_convertido[::-1]


def conversor_bases_parte_decimal(numero_a_convertir, base_entrada, base_destino, Arreglo_a_utilizar, Arreglo_de_bases):

  numero_convertido = ""
  numero_apoyo_en_decimal = 0
  contador_de_exponente = -1

  for valor in numero_a_convertir:
      try:
          
          valor_arreglo = Arreglo_a_utilizar.index(valor)
            
          numero_apoyo_en_decimal += valor_arreglo*(base_entrada**(contador_de_exponente))

          contador_de_exponente -= 1
          
      except ValueError:
        
            return -1

  for potencia_actual in range(6):
      numero_apoyo_en_decimal *= base_destino
      valor_actual = int(numero_apoyo_en_decimal)
      numero_convertido += Arreglo_de_bases[valor_actual]
      numero_apoyo_en_decimal -= valor_actual

  return numero_convertido
    


menu()
