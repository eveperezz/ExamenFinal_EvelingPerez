import pyodbc
from lector_json import LectorJSON
from mision import Mision

def consultar_mensaje(pk):
    try:
        with pyodbc.connect(
            "DRIVER={SQL Server};SERVER=EV\\SQLEXPRESS;DATABASE=ExamenFinal;Trusted_Connection=yes;"
        ) as conn:
            cursor = conn.cursor()
            cursor.execute(
                "SELECT mensaje, mision_1, mision_2, mision_3 FROM estudiante WHERE id = ?", pk
            )
            resultado = cursor.fetchone()

        if resultado:
            return resultado[0], resultado[1], resultado[2], resultado[3]
        else:
            raise ValueError("Registro no encontrado en la base de datos.")
    except Exception as e:
        raise ValueError(f"Error al consultar la base de datos: {e}")

if __name__ == "__main__":
    lector = LectorJSON("examen.json")
    lector.leer_json()

    bd, consecutivo = lector.filtrar_por_nombre("3V3L1NG @N13LK@")
    pk = lector.calcular_pk(consecutivo)

    print(f" PK calculado: {pk}")

    mensaje, m1, m2, m3 = consultar_mensaje(pk)
    mision = Mision(mensaje, m1, m2, m3)
    frase_final, funciones = mision.aplicar_misiones()

    print(f"\n Frase corregida: {frase_final}")
    print(f" Funciones utilizadas: {funciones}")
    