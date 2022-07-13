class CuentaBancaria:

    nombre_banco = "Primer Dojo Nacional"
    lista=[]
    def __init__(self,tasa,balance=0):
        self.tasa = tasa/100
        self.balance = balance
        CuentaBancaria.lista.append(self)
    
    def deposito(self,monto):
        self.balance += monto
        print("has depositado ${} el saldo actual de tu cuenta es {}".format(monto,self.balance))
        return self
    def retiro(self,monto):
        if monto > self.balance:
            self.balance -= 5
            print("Fondos insuficientes: se generara un cobro de $5 y tu saldo actual queda en {}".format(self.balance) )
        else:
            self.balance -= monto
            print("has retirado ${} el saldo actual de tu cuenta es {}".format(monto,self.balance))
        return self
    def mostrar_info_cuenta(self):
        print("Balance de la cuenta: $ {}".format(self.balance))
    def generar_interes(self):
        interes = self.balance * self.tasa
        self.balance += interes
        return self
    def imprimir(self):
        print("El interes de esta cuenta es de "+str(self.tasa)+" Balance de la cuenta "+str(self.balance))

    @classmethod
    def imprime_lista(cls):
        for cuenta in cls.lista:
            cuenta.imprimir()

class Usuario:	
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.cuenta = {'ahorros':CuentaBancaria(3,),'corriente':CuentaBancaria(7,)}
    
    def info_todas_las_cuentas_de_un_usuario(self):
        print('el saldo del usuario en la cuenta de ahorros es de:')
        self.cuenta['ahorros'].mostrar_info_cuenta()
        print('el saldo del usuario en la cuenta corriente es de:')
        self.cuenta['corriente'].mostrar_info_cuenta()      











