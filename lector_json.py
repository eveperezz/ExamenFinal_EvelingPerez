import json

class LectorJSON:
    def __init__(self, ruta):
        self.__ruta = ruta
        self.__datos = []

    def leer_json(self):
        try:
            with open(self.__ruta, 'r', encoding='utf-8') as f:
                contenido = json.load(f)
                if "estudiantes" not in contenido:
                    raise ValueError("La clave 'estudiantes' no se encuentra en el archivo JSON.")
                self.__datos = contenido["estudiantes"]
                print(f" {len(self.__datos)} estudiantes cargados correctamente.")
        except Exception as e:
            raise ValueError(f"Error al leer el archivo JSON: {e}")

    def mostrar_estudiantes(self):
        print(" Lista de estudiantes:")
        for est in self.__datos:
            print(est)

    def filtrar_por_nombre(self, nombre):
        nombre = nombre.strip()
        coincidencias = [est for est in self.__datos if est["nombre"].strip() == nombre]

        if not coincidencias:
            raise ValueError(f" Nombre '{nombre}' no encontrado en el archivo JSON.")

        est = coincidencias[0]  # Se toma el primero si hay duplicados
        print(f" Estudiante encontrado: {nombre}")
        return est["bd"], est["consecutivo"]

    def calcular_pk(self, consecutivo):
        pk = (consecutivo % 42) + 1
        print(f" PK calculado a partir del consecutivo {consecutivo}: {pk}")
        return pk