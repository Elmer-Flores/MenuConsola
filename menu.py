class Menu:
    
    def __init__(self, titulo, opciones, pregunta, tamanoFuente=True, saltosLinea=1, espaciosDerecha=1, estilosA="[",estilosB="]"):
        self.titulo = titulo
        self.opciones = opciones
        self.pregunta = pregunta
        self.tamanoFuente = tamanoFuente
        self.saltosLinea = saltosLinea
        self.espaciosDerecha =  espaciosDerecha
        self.estilosA = estilosA
        self.estilosB = estilosB

    def mostrarMenu(self):
        formatoTexto = self.dar_saltos_y_espacios()
        titulo = self.devolverTitulo()
        print(f"{formatoTexto}{titulo}")
        for indice in range(len(self.opciones)):
            estilo = f"{self.estilosA}{indice+1}{self.estilosB}"
            if self.tamanoFuente == True:
                opcion = f"{formatoTexto}{estilo}{self.opciones[indice]}".upper()
                print(opcion)
            else:
                opcion = f"{formatoTexto}{estilo}{self.opciones[indice]}"
                print(opcion)
        respuestaPregunta = ""
        if self.tamanoFuente == True:
            respuestaPregunta = input(f"{formatoTexto}{self.pregunta}: ".upper())
        else:
            respuestaPregunta = input(f"{formatoTexto}{self.pregunta}: ")
        respuestaFinal = self.obtenerDatoExacto(respuestaPregunta)
        return respuestaFinal

    def dar_saltos_y_espacios(self):
        saltos_de_linea = self.darFormato(self.saltosLinea, "\n")
        espacio_derecha = self.darFormato(self.espaciosDerecha, "\t")
        return f"{saltos_de_linea}{espacio_derecha}"

    def obtenerDatoExacto(self, valor):
        try:
            nuevoValor = 0
            if int(valor):
                nuevoValor = int(valor)
            return nuevoValor
        except ValueError as errorValor:
            print(self.mensajeError(errorValor))
            return valor
        except ValueError as errorTipo:
            print(self.mensajeError(errorTipo))
            return valor

    def devolverTitulo(self):
        if self.tamanoFuente == True:
            return f"{self.titulo}".upper()
        else:
            return f"{self.titulo}".title()

    def darFormato(self, cantidad, caracter=""):
        formato = ""
        for indice in range(cantidad):
            formato += f"{caracter}"
        return formato

    def limpiar(self):
        from os import system
        system("cls")

    def mensajeError(self, error):
        self.limpiar()
        saltos_de_linea = self.darFormato(self.saltosLinea, "\n")
        formatoTexto = self.dar_saltos_y_espacios()
        return f"{formatoTexto}(⌐■_■) Error: {error}\n\n{saltos_de_linea}"

    def mensajeSalir(self):
        import time
        self.limpiar()
        print(f"\n{self.dar_saltos_y_espacios()}( ﾟдﾟ)つ Bye Has salido de la aplicacion\n\n\n")
        time.sleep(1)
        self.limpiar()

    def mensajeOpcionInvavilitada(self, mensaje="Esta opcion no esta habilitada", estilo=""):
        if estilo == "":
            estilo = "┗( T﹏T )┛"
        mensajeDev = f"\n\n\t {estilo} {mensaje}\n\n"
        print(mensajeDev)


