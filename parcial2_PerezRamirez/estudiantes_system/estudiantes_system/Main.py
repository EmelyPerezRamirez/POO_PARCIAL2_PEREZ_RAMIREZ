from estudiantes import estudiantes

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("Oprima tecla ")

    def menu_acciones(self, tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
        opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n\t\t Elige una opcion: ").strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            input("\n\t Accion Realizada con Exito! \n")
        else:
            input("\n\t Opcion invalida! Oprima cualquier tecla para continuar...  \n")

    def datos_estudiante(self, tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresar los datos del {tipo}...")
        estudiantitos = {}
        estudiantitos['nombre'] = input("Nombre: ").upper().strip()
        estudiantitos['nota'] = input("Calificacion: ").strip()
        return estudiantitos

    def menu_estudiantes(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = self.menu_acciones("Estudiantes")
            match opcion:
                case '1':
                    estudiantitos = self.datos_estudiante("Estudiante")      
                    estudiante1 = estudiantes.Estudiantes(estudiantitos['nombre'], estudiantitos['nota'])
                    respuesta = estudiante1.insertar()
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case "2":
                    self.borrarPantalla()
                    id = input("Ingresa el ID del estudiante a eliminar: ").strip()
                    # Método estático: se llama directamente desde la clase sin instanciar
                    respuesta = estudiantes.Estudiantes.eliminar(id)
                    self.respuesta_sql(respuesta)

                case "3":
                    id = input("Ingresa el ID del estudiante a actualizar: ").strip()
                    estudiantitos = self.datos_estudiante("Estudiante")      
                    estudiante1 = estudiantes.Estudiantes(estudiantitos['nombre'], estudiantitos['nota'])
                    respuesta = estudiante1.actualizar(id)
                    self.respuesta_sql(respuesta)
                    del estudiante1

                case "4":
                    self.borrarPantalla()
                    # Método estático: se llama directamente desde la clase
                    registros = estudiantes.Estudiantes.consultar()
                    if len(registros) > 0:
                        numero_estudiantes = 1
                        for fila in registros:
                            print(f"Estudiante #{numero_estudiantes}\n\t ID: {fila[0]}\n\t nombre: {fila[1]}\n\t calificacion: {fila[2]}\n")
                            numero_estudiantes += 1
                        self.esperarTecla()
                    else:
                        print("\n\n\t ¡No existen datos que mostrar por el momento ...!")
                        self.esperarTecla()

                case "5":
                    opcion = False
                case _:
                    input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ...") 

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = input("\n\t\t\t...:: M E N U   P R I N C I P A L ::...\n\n\t 1.- Estudiantes \n\t 2.- Salir \n \t\t Elige una opcion: ").strip().lower()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_estudiantes()
                case "2":
                    self.borrarPantalla()
                    input("Saliendo del sistema... ")
                    opcion = False
                case _:
                    input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ... ")

if __name__ == "__main__":
    app = App()