class Estudiante(object):

    def __int__(self, codigo, nombre, apellido):
        self.codigo = codigo
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return "%s: %s, %s"
        (str(self.codigo), self.apellido, self.nombre)


class USTA(Estudiante):

    def __int__(self, codigo, nombre, apellido, padron):
        Estudiante.__int__(self, codigo, nombre, apellido)
        self.padron = padron


a = USTA("123456677", "Daniel", "Marcano", "987456132")
print(a)

def __str__(self):
    return " %d: %s, %s"
    (str(self.padron), self.apellido, self.nombre)

a = USTA("123456677", "Daniel", "Marcano", "987456132")