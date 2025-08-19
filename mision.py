import re

class Mision:
    def __init__(self, mensaje, m1, m2, m3):
        self.__mensaje_original = mensaje
        self.__mensaje = mensaje  # Se trabajará sobre esta copia
        self.__instrucciones = [m1, m2, m3]
        self.__funciones = []

    def aplicar_misiones(self):
        try:
            for instruccion in self.__instrucciones:
                instruccion = instruccion.lower().strip()

                if "espacios al inicio" in instruccion:
                    self.__mensaje = self.__mensaje.lstrip()
                    self.__funciones.append("lstrip")

                elif "guiones por espacios" in instruccion:
                    self.__mensaje = self.__mensaje.replace("-", " ")
                    self.__funciones.append("replace")

                elif "caracteres especiales al final" in instruccion:
                    self.__mensaje = re.sub(r"[^\w\sáéíóúÁÉÍÓÚñÑ]+$", "", self.__mensaje)
                    self.__funciones.append("regex_sub_final")

                elif "caracteres especiales al inicio" in instruccion:
                    self.__mensaje = re.sub(r"^[^\w\sáéíóúÁÉÍÓÚñÑ]+", "", self.__mensaje)
                    self.__funciones.append("regex_sub_inicio")

                elif "espacios dobles" in instruccion:
                    self.__mensaje = re.sub(r"\s{2,}", " ", self.__mensaje)
                    self.__funciones.append("regex_doble_espacio")

                elif "capitalizaci" in instruccion:
                    self.__mensaje = self.__mensaje.title()
                    self.__funciones.append("title")

                elif "punto final" in instruccion:
                    self.__mensaje = self.__mensaje.rstrip()
                    if not self.__mensaje.endswith("."):
                        self.__mensaje += "."
                    self.__funciones.append("verificar_punto")

            return self.__mensaje, self.__funciones

        except Exception as e:
            raise ValueError(f"Error al aplicar las misiones: {e}")