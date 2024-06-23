from COMMON.Domain.valueObjects import ValueObject

class Plato_Pasos_VO(ValueObject):
    
    pasos = []

    def __init__(self, nombre):
        nombre = Plato_Pasos_VO.equals(nombre)
        if nombre is None:
            raise ValueError("Una receta tiene que tener mas de cero pasos")
        super().__init__()
        self.nombre = nombre

    def equals(self, other: 'Plato_Pasos_VO') -> bool:
        return self.pasos == other.pasos
    
    def valid(self) -> bool:
        return len(self.pasos) > 0