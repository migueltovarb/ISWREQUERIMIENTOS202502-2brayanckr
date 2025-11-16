import csv
import os
import time

# -------------------------------
# Clase que representa una función de cine
# -------------------------------
class Funcion:
    def __init__(self, codigo, pelicula, hora, precio):
        self.codigo = codigo
        self.pelicula = pelicula
        self.hora = hora
        self.precio = float(precio)


# -------------------------------
# Clase principal del sistema MovieTime
# -------------------------------
class MovieTime:
    def __init__(self):
        self.funciones = []
        self.ventas = []
        self.archivo_funciones = "funciones.csv"
        self.archivo_ventas = "ventas.csv"
        self.cargar_datos()

    # -------------------------------
    # Cargar funciones y ventas desde archivos
    # -------------------------------
    def cargar_datos(self):
        if os.path.exists(self.archivo_funciones):
            with open(self.archivo_funciones, newline='', encoding='utf-8') as f:
                lector = csv.reader(f)
                for fila in lector:
                    if fila:  # evitar líneas vacías
                        codigo, pelicula, hora, precio = fila
                        self.funciones.append(Funcion(codigo, pelicula, hora, precio))

        if os.path.exists(self.archivo_ventas):
            with open(self.archivo_ventas, newline='', encoding='utf-8') as f:
                lector = csv.reader(f)
                for fila in lector:
                    if fila:
                        self.ventas.append(fila)

    # -------------------------------
    # Registrar una nueva función
    # -------------------------------
    def registrar_funcion(self):
        codigo = input("Ingrese código de la función: ")
        pelicula = input("Ingrese nombre de la película: ")
        hora = input("Ingrese hora de la función: ")
        precio = input("Ingrese precio del boleto: ")

        self.funciones.append(Funcion(codigo, pelicula, hora, precio))
        print("✅ Función registrada correctamente.\n")

    # -------------------------------
    # Listar funciones
    # -------------------------------
    def listar_funciones(self):
        if not self.funciones:
            print("No hay funciones registradas.\n")
        else:
            print("\n--- FUNCIONES DISPONIBLES ---")
            for f in self.funciones:
                print(f"Código: {f.codigo} | Película: {f.pelicula} | Hora: {f.hora} | Precio: ${f.precio}")
            print("------------------------------\n")

    # -------------------------------
    # Vender boletos
    # -------------------------------
    def vender_boletos(self):
        codigo = input("Ingrese el código de la función: ")
        funcion = None
        for f in self.funciones:
            if f.codigo == codigo:
                funcion = f
                break

        if funcion is None:
            print("❌ Error: la función no existe.\n")
            return

        try:
            cantidad = int(input("Ingrese la cantidad de boletos: "))
            if cantidad <= 0:
                print("❌ Error: número inválido de boletos.\n")
                return
        except ValueError:
            print("❌ Error: debe ingresar un número válido.\n")
            return

        total = funcion.precio * cantidad
        print(f"Total a pagar: ${total:.2f}")
        self.ventas.append([funcion.codigo, funcion.pelicula, cantidad, total])
        print("✅ Venta registrada con éxito.\n")

    # -------------------------------
    # Resumen de ventas
    # -------------------------------
    def resumen_ventas(self):
        total_boletos = 0
        total_dinero = 0

        for venta in self.ventas:
            total_boletos += int(venta[2])
            total_dinero += float(venta[3])

        print("\n--- RESUMEN DE VENTAS DEL DÍA ---")
        print(f"Boletos vendidos: {total_boletos}")
        print(f"Dinero recaudado: ${total_dinero:.2f}")
        print("---------------------------------\n")

    # -------------------------------
    # Menú principal
    # -------------------------------
    def menu(self):
        while True:
            print("===== CINE MOVIETIME =====")
            print("1. Registrar nueva función")
            print("2. Listar funciones")
            print("3. Vender boletos")
            print("4. Ver resumen de ventas")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")

            if opcion == "1":
                self.registrar_funcion()
            elif opcion == "2":
                self.listar_funciones()
            elif opcion == "3":
                self.vender_boletos()
            elif opcion == "4":
                self.resumen_ventas()
            elif opcion == "5":
                print("Saliendo del sistema...")
                time.sleep(1.5)
                break
            else:
                print("❌ Opción no válida. Intente de nuevo.\n")
            time.sleep(1.5)


# -------------------------------
# Programa principal
# -------------------------------
if __name__ == "__main__":
    app = MovieTime()
    app.menu()
