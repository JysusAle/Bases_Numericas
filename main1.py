import random
"""""
Este programa fue realizado por los estudiantes:
Un conversor de bases numericas
"""""

# convierte un numero dado en una base a otra base donde ambas bases deben ser menor o igual a 36 y mayor o igual a 2
def conversor(numero_a_convertir, base_entrada, base_destino):
    # todos los caracteres posibles que puede tener un numero en base 36
    Arreglo_de_bases = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    # se crean variables para guardar parte entera del numero y parte flotante
    numero_entero_a_convertir = ""
    numero_flotante_a_convertir = "0"

    # se agrega punto al final para que el siguiente ciclo siempre encuentre el punto y separe adecuadamente el output
    numero_a_convertir += "."

    # separa la parte entera de la parte flotante
    for i in range(len(numero_a_convertir)):
        if numero_a_convertir[i] == ".":
            numero_entero_a_convertir = numero_a_convertir[:i]
            numero_flotante_a_convertir = numero_a_convertir[i + 1:len(numero_a_convertir) - 1]
            break;

    # se revisan bases minimas y maximas dadas en el input para verificar que cumplan las restricciones dadas
    base_maxima = max(base_destino,base_entrada)
    base_minima = min(base_destino, base_entrada)

    # si alguna base es mayor a 36, se indica que hay error
    if base_maxima > len(Arreglo_de_bases):
      
      return(f"\n La base maxima a convertir es {len(Arreglo_de_bases)}")
    
    # si alguna base es menor a 2, se indica que hay error
    if base_minima < 2:

      return(f"\n La base minima a convertir es 2")

    # se toman solo los caracteres que puede tener el numero dada la base de entrada
    Arreglo_a_utilizar = Arreglo_de_bases[0:base_entrada]

    respuesta = ""

    # se convierte parte flotante y entera
    parte_entera_convertida = conversor_bases_parte_entera(numero_entero_a_convertir,base_entrada,base_destino,Arreglo_a_utilizar, Arreglo_de_bases)
    parte_flotante_convertida = conversor_bases_parte_decimal(numero_flotante_a_convertir,base_entrada,base_destino,Arreglo_a_utilizar, Arreglo_de_bases)
    
    # si hubo algun error en los datos se entrada se devuelve mensaje de error
    if parte_entera_convertida == -1 or parte_flotante_convertida == -1:
        return(f"El numero {numero_a_convertir[:len(numero_a_convertir) - 1]} no esta en base {base_entrada}")
    
    # se devuelve numero convertido
    respuesta += str(parte_entera_convertida)
    if len(set(parte_flotante_convertida)) > 1 or parte_flotante_convertida[0] != "0":
        respuesta += (f".{parte_flotante_convertida}")

    return respuesta

# funcion para convertir parte entera de un numero a otra base
def conversor_bases_parte_entera(numero_a_convertir, base_entrada, base_destino, Arreglo_a_utilizar, Arreglo_de_bases):
  
  numero_convertido = ""
  numero_apoyo_en_decimal = 0
  contador_de_exponente = 0
  numero_a_convertir = numero_a_convertir[::-1]
  residuo = 0
     
  # se convierte el numero a base 10
  for valor in numero_a_convertir:
      try:
          
          valor_arreglo = Arreglo_a_utilizar.index(valor)
            
          numero_apoyo_en_decimal += valor_arreglo*(base_entrada**(contador_de_exponente))

          contador_de_exponente += 1

      # si se da esta excepcion significa que el numero dado no esta en la base correcta ya que no se encuentra en el arreglo de caracteres
      except ValueError:
        
            return -1

  # con el numero ya en base 10, se convierte a la base destino dividiendo el numero entre la base_destino 
  # y tomando el residuo para saber que caracteres utilizar
  while(numero_apoyo_en_decimal!=0):

    residuo = numero_apoyo_en_decimal % base_destino
    
    residuo = Arreglo_de_bases[residuo]

    numero_apoyo_en_decimal = numero_apoyo_en_decimal//base_destino
    
    numero_convertido += residuo
  
  # se invierte el numero ya que lo hacemos del caracter con potencia mas baja a potencia mas alta
  return numero_convertido[::-1]


def conversor_bases_parte_decimal(numero_a_convertir, base_entrada, base_destino, Arreglo_a_utilizar, Arreglo_de_bases):
  
  # el exponente ahora empieza desde -1 y se le va restando uno debido a que estamos con las potencias negativas
  numero_convertido = ""
  numero_apoyo_en_decimal = 0
  contador_de_exponente = -1

  # se convierte el numero a base 10
  for valor in numero_a_convertir:
      try:
          
          valor_arreglo = Arreglo_a_utilizar.index(valor)
            
          numero_apoyo_en_decimal += valor_arreglo*(base_entrada**(contador_de_exponente))

          contador_de_exponente -= 1

      # si se da esta excepcion significa que el numero dado no esta en la base correcta ya que no se encuentra en el arreglo de caracteres
      except ValueError:
        
            return -1
  
  # se le agregan 6 digitos despues del punto decimal para mayor precision
  # para hacer esto se multiplica por la base destino y se toma la parte entera como el valor del caracter que se debe agregar
  # despues de tomar la parte entera se continua con la parte decimal nuevamente
  for potencia_actual in range(6):
      numero_apoyo_en_decimal *= base_destino
      valor_actual = int(numero_apoyo_en_decimal)
      numero_convertido += Arreglo_de_bases[valor_actual]
      numero_apoyo_en_decimal -= valor_actual

  #se devuelve numero convertido 
  return numero_convertido
    