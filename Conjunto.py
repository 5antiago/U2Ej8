
class conjunto:
    __conjunto = list

    def __init__(self, con=[]):
        self.__conjunto = con
    def __str__(self):
        return str(self.__conjunto)

    def agregar(self, elemento):
        if type(elemento) == int:
            if elemento in self.__conjunto:
                return False
            else:
                self.__conjunto.append(elemento)
                return True
    def get(self):
        return self.__conjunto
    def cant(self):
        return len(self.__conjunto)
    def __add__(self, otro):
        aux = self.__conjunto.copy()
        if type(otro) == conjunto:
            for i  in otro.get():
                if i not in self.__conjunto:
                   aux.append(i)
            return conjunto(aux)
    def __sub__(self, otro):
        aux = self.__conjunto.copy()
        if type(otro) == conjunto:
            for i in otro.get():
                if i in self.__conjunto:
                    aux.pop(aux.index(i))
            return conjunto(aux)
    def __eq__(self, otro):
        if otro.cant() == len(self.__conjunto):
            bandera = True
            for i in otro.get():
                if i not in self.__conjunto:
                    bandera = False
            return bandera
        else:
            return False
