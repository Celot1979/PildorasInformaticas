def setComparar(self):
        for l in range(len(self.lista_programa)):
            if not (self.lista_programa == self.lista_Usuario): #si el elemento l en la longitud de la lista no es igual en ambas lista , rompe
                print ("No has introduccido la lista correctamente. Se ha terminado el juego.")
                i = 3
                print("Programa terminado")
                break
            else:
                i = 1
                p= 2
                u=2
                while i <= 10:
                    
                    self.setPrograma(p)
                    self.getPrograma()
                    self.setUsuario(u)
                    self.getUsuario()
                    self.setComparar()
                    p += 1
                    u += 1
                    i += 1
                



#--------------------------------------------
i = 1
                p= 2
                u=2
                while i <= 10:
                    
                    self.setPrograma(p)
                    self.getPrograma()
                    self.setUsuario(u)
                    self.getUsuario()
                    self.setComparar()
                    p += 1
                    u += 1
                    i += 1