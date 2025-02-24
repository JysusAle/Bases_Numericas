import random
"""""
Este programa fue realizado por los estudiantes:
Un conversor de bases numericas
"""""
def bases():
  pass

def menu():

  Arreglo_de_bases = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","S","T"]

  #Definimos la estructura del menu y manejamos errores
  while True:
    try:
        print("\t----Bienvenido al Conversor de unidades FI UNAM----")
        base_entrada = int(input("\nPor favor ingrese la base actual:\t"))
        break
    
    except ValueError:
        print("ERROR: Ingrese un numero entero\n\n")
  

  numero_a_convertir= str(input("\nIngrese El numero a convertir:\t")).strip().upper()

  while True:
    try:
        base_destino = int(input("\n¿A que base quieres ir?:\t"))
        break
    
    except ValueError:
        print("ERROR: Ingrese un numero entero\n\n")

  base_maxima = max(base_destino,base_entrada)

  if base_maxima > 10 + len(Arreglo_de_bases):
     
     print(f"\n La base maxima a convertir es {10 + len(Arreglo_de_bases)}")

     return 
  
  elif base_maxima > 10:
    Arreglo_a_utilizar = Arreglo_de_bases[0:base_maxima-10]
  
  else:
     Arreglo_a_utilizar = [""]

  conversor_bases(numero_a_convertir,base_entrada,base_destino,Arreglo_a_utilizar)


def conversor_bases(numero_a_convertir, base_entrada, base_destino, Arreglo_a_utilizar):

  numero_convertido = ""
  numero_apoyo_en_decimal = 0
  contador_de_exponente = 0
  numero_a_convertir = numero_a_convertir[::-1]
  residuo = 1

  if base_entrada != 10:
     
    for valor in numero_a_convertir:
        try:
           
          valor = int(valor)

          numero_apoyo_en_decimal += valor*(base_entrada**(contador_de_exponente))

          contador_de_exponente += 1
           
        except ValueError:

          try:
             
            valor_arreglo = 10 + Arreglo_a_utilizar.index(valor)
             
            numero_apoyo_en_decimal += valor_arreglo*(base_entrada**(contador_de_exponente))

            contador_de_exponente += 1
        
          except ValueError:
             
             print(f"El numero {numero_a_convertir} no esta en base {base_entrada}")

             return
  else:
    numero_apoyo_en_decimal = int(numero_a_convertir)

  if base_destino !=10:

    while(numero_apoyo_en_decimal!=0):

      residuo = numero_apoyo_en_decimal - (numero_apoyo_en_decimal//base_destino)*base_destino

      if residuo >= 10:
        residuo = Arreglo_a_utilizar[residuo-10]

      numero_apoyo_en_decimal = numero_apoyo_en_decimal//base_destino
      
      numero_convertido += str(residuo)

    print(f"\nEl numero es: {numero_convertido[::-1]}")

  else:
    print(f"\nEl numero es: {numero_apoyo_en_decimal}")

menu()