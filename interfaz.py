import requests
class api:
    #Se definen como variable de instancia ambas url's utilizadas
    def __init__(self):
        self.url_login = "https://codigo-alfa.cl/Api/setLogin"
        self.url_get = "https://codigo-alfa.cl/Api/getClaves"
    
    #metodo para consumir Api Login , retorna lista contiene codigo de status y hash asignado a la sesion
    def sesion(self,rut,contraseña):
        Lista = []
        parametros={"Rut":rut, "Pass":contraseña}
        req = requests.api.post(self.url_login,data=parametros).json()
        Lista.append(req['status']);Lista.append(req['hash'])
        return Lista
    
    #metodo para consumir api login , retorna lista que contiene los tres hashe a desencriptar
    def enc(self):
        Lista = []
        req = requests.api.post(self.url_get).json()
        for i in range(0,3):
            Lista.append(req['hash'][i])
        return Lista
            
