import hashlib

class encriptacion:
    def __init__(self):
        self.lista = []
    #procesa datos de inicio de sesion y devuelve lista que contiene rut y contraseña encriptada
    def login(self,rut,contraseña):
        c_login = hashlib.sha256(contraseña.encode()).hexdigest()
        c_login = hashlib.md5(c_login.encode()).hexdigest()
        credenciales = [rut,c_login]
        return credenciales
    
    #Seccion donde se definen metodos para desencriptar mediante la encriptacion y comparación de hashes
    def desencriptar(self,parametro):
            for i in range(0,10):
                if parametro[0] == hashlib.md5(str(i).encode()).hexdigest(): 
                    self.lista.append(i)

            for i in "aeiou":
                h= hashlib.sha1((hashlib.sha256(i.encode()).hexdigest()).encode()).hexdigest()
                if parametro[1] == h: 
                    self.lista.append(i)
            
            for i in range(100,1000,50):
                h= hashlib.md5(hashlib.md5(str(i).encode()).hexdigest().encode()).hexdigest()
                if parametro[2] == h: 
                    self.lista.append(i)

    def llamar(self):
        return self.lista



