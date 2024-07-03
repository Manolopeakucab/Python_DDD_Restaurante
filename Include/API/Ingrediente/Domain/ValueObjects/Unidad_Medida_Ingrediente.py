from Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class Unidad_medida_ingrediente_VO(ValueObject):
    medida: int

    def __init__(self, medida:str):
        medida = Unidad_medida_ingrediente_VO.valid(medida);
        if medida is None:
            raise ValueError("La medidas del ingrediente no puede ser vacio")
        self._medida = medida

    def equals(self, other: 'Unidad_medida_ingrediente_VO') -> bool:
        return self._medida== other._medida
    
    def valid(self) -> bool:
        return len(self.medida) > 0
    
    def get_value(self) -> str:
        return self
    
    staticmethod
    def create(nombre: str) -> 'Unidad_medida_ingrediente_VO':
        return Unidad_medida_ingrediente_VO(nombre)