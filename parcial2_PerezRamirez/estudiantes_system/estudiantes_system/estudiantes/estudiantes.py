from conexionBD import cursor, conexion

class Estudiantes:
    def __init__(self, nombre, nota):
        self._nombre = nombre
        self._nota = nota

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre

    @property
    def nota(self):
        return self._nota

    @nota.setter
    def nota(self, nota):
        self._nota = nota

    def insertar(self):
        try:
            cursor.execute("INSERT INTO estudiante VALUES (NULL, %s, %s)", (self._nombre, self._nota))
            conexion.commit()
            return True
        except Exception as e:
            conexion.rollback()  # Revierte la transacción si falla
            print(f"Error al insertar: {e}")
            return False

    @staticmethod
    def consultar():
        try:
            cursor.execute("SELECT * FROM estudiante")
            return cursor.fetchall()
        except Exception as e:
            print(f"Error al consultar: {e}")
            return []

    @staticmethod
    def eliminar(id):
        try:
            cursor.execute("DELETE FROM estudiante WHERE id = %s", (id,))
            conexion.commit()
            return True
        except Exception as e:
            conexion.rollback()
            print(f"Error al eliminar: {e}")
            return False

    def actualizar(self, id):
        try:
            cursor.execute("UPDATE estudiante SET nombre = %s, nota = %s WHERE id = %s", (self._nombre, self._nota, id))
            conexion.commit()
            return True
        except Exception as e:
            conexion.rollback()
            print(f"Error al actualizar: {e}")
            return False