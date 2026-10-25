from coches import cochesBD, coches

class App:
    def __init__(self):
        self.main()

    def borrarPantalla(self):
        print("\033c")

    def esperarTecla(self):
        input("Espere porfavor... ")

    def menu_acciones(self, tipo):
        print(f"\n\t\t\t...::: Menu de {tipo} :::... \n")
        opcion = input("\n\t 1.- Agregar \n\t 2.- Borrar \n\t 3.- Modificar \n\t 4.- Mostrar \n\t 5.- Salir \n\t\t Elige una opcion: ").strip()
        return opcion

    def respuesta_sql(self, respuesta):
        if respuesta:
            input("\n\t Accion Realizada con Exito \n")
        else:
            input("\n\t Opcion invalida! Oprima cualquier tecla para continuar... \n")

    def datos_coche(self, tipo):
        self.borrarPantalla()
        print(f"\n\t ...Ingresar los datos del {tipo}...")
        cochesitos = {}
        cochesitos['marca'] = input("Marca: ").upper().strip()
        cochesitos['color'] = input("Color: ").upper().strip()
        cochesitos['modelo'] = input("Modelo: ").upper().strip()
        cochesitos['velocidad'] = input("Velocidad (km/h) ").strip()
        cochesitos['potencia'] = input("Potencia (Hp): ").strip()
        cochesitos['asientos'] = input("# de Asientos: ").strip()
        return cochesitos

    def menu_coches(self):
       opcion = True
       while opcion:
          self.borrarPantalla()
          opcion = self.menu_acciones("Coches")

          match opcion:
            case '1':
                cochesitos = self.datos_coche("Coche")      
                coche1 = cochesBD.cochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                respuesta = coche1.insertar()
                self.respuesta_sql(respuesta)
                del coche1

            case "2":
                self.borrarPantalla()
                id = input("Ingresa el ID del coche a eliminar: ").strip()
                
                # metodo estatico que llama directo desde la clase
                respuesta = cochesBD.cochesBD.eliminar(id)
                self.respuesta_sql(respuesta)

            case "3":
                id = input("Ingresa el ID del coche a actualizar: ").strip()
                cochesitos = self.datos_coche("Coche")      
                coche1 = cochesBD.cochesBD(cochesitos['marca'], cochesitos['color'], cochesitos['modelo'], cochesitos['velocidad'], cochesitos['potencia'], cochesitos['asientos'])
                respuesta = coche1.actualizar(id)
                self.respuesta_sql(respuesta)
                del coche1
                
            case "4":
                self.borrarPantalla()
                # metodo estatico que llama directo desde la clase
                registros = cochesBD.cochesBD.consultar()
                if len(registros) > 0:
                    numero_coches = 1
                    for fila in registros:
                        print(f"Coche #{numero_coches}\n\t ID: {fila[0]}\n\t marca: {fila[1]}\n\t color: {fila[2]}\n\t modelos: {fila[3]}\n\t velocidad: {fila[4]}\n\t potencia: {fila[5]}\n\t # de asientos: {fila[6]}\n\t")
                        numero_coches += 1
                        self.esperarTecla()
                else:
                    print("\n\n\t ¡No existen datos que mostrar por el momento ...!")
                    self.esperarTecla()

            case "5":
                opcion = False
            case _:
                input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ... ")

    def main(self):
        opcion = True
        while opcion:
            self.borrarPantalla()
            opcion = input("\n\t\t\t...:: M E N U   P R I N C I P A L ::...\n\n\t 1.- Coches \n\t 2.- Salir \n \t\t Elige una opcion: ").strip().lower()
            match opcion:
                case "1":
                    self.borrarPantalla()
                    self.menu_coches()
                case "2":
                    self.borrarPantalla()
                    input("Saliendo del sistema... ")
                    opcion = False
                case _:
                    input("\n\t ... Opcion invalida, vuelve a intentarlo por favor ... ")


if __name__ == "__main__":
    app = App()