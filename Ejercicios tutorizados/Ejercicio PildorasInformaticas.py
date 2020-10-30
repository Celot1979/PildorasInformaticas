'''Se trata de crear una clase que construya cuentas corrientes bancarias. Para ello deberás:
Crear una clase con el nombre de CuentaCorriente con tres atributos que serán:
El nº de la cuenta (un string numérico con el nº de cifras que quieras)
El titular de la cuenta
El saldo de la cuenta

Crear un método getter que nos muestre la información de la cuenta. Debe mostrarnos el nº, el titular y el saldo.
Crear un método que nos permita ingresar dinero en la cuenta
Crear un método que nos permita retirar dinero de la cuenta
Prueba el programa creando un objeto de tipo CuentaCorriente, ingresa y retira dinero de la 
cuenta y finalmente muestra los datos de la cuenta.'''

class CuentaCorriente():
    sal = []
    ingre = []
    despues = []
    sacar = []
    operacion = []
  
    def __init__(self):
        self.cuenta= int(input("Introduzca el número de cuenta, por favor: "))
        self.titular = str(input("Introduzca su nombre, por favor: "))
        self.saldo = int(input("Introduzca el saldo de la cuenta, por favor:  "))
        self.sal.append(self.saldo)
        #Creamos una lista para almacenar el saldo introduccido
    def getter(self):
        print( "El numero de la cuenta es: " + str(self.cuenta) + " El titular es: " + self.titular + " Su saldo es de: " + str(self.saldo))
    
    
    def ingresar(self):
        self.ingresar = int(input(" ¿Cuánto desea ingresar?  :"))
        self.ingre.append(self.ingresar)
        #Creamos una lista para almacenar el saldo a ingresar introduccido
        #print(self.sal)
        #print(self.ingre)
        for i in range(len(self.sal)):
            self.despues.append(self.sal[i] + self.ingre[i])
        #Tenemos dos listas las cuales queremos sumar los lementos de ambas. 
        #Para eso creamo una nueva lista que alojará la suma de ambas -despues= [] -
        self.men = "".join([str(_) for _ in self.despues])
        #Luego convertimo esa nueva lista, en una cadena para poder al final cambiar el valor de la lista sal por el nuevo 
        #Eso siempre nos permitiría poder operar con la lista base del programa que es - sal =[] -
        #self.sal = int(self.men)
        print("El nuevo saldo de su cuenta es de: " + str(self.men))
        #Finalmente convertiremos una lista en string con la función join.
        #Imprimimos por consola el resultado de la operación

    def retirar(self):
        self. retiro = int(input("Qué cantidad desea retirar: "))
        self.sacar.append(self.retiro)
        #print(self.sacar)
        
        for i in range(len(self.sal)):
            self.operacion.append(self.despues[i] - self.sacar[i])
            #print(self.operacion)
        self.buf = "".join([str(_) for _ in self.operacion])
        print(" El nuevo saldo de su cuenta es de: " + str(self.buf))        
                

            
        
            
        
c1 = CuentaCorriente()
c1.getter()
c1.ingresar()
c1.retirar()
