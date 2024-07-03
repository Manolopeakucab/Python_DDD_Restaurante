from Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class Estados_Orden_VO(ValueObject):
    
    estado:str;

    def __init__(self, estado:str):
        estado = Estados_Orden_VO.equals(estado)
        if estado is None:
            raise ValueError("El estado no puede ser vacio")
        super().__init__()
        self.estado = estado

    def equals(self, other: 'Estados_Orden_VO') -> bool:
        return self.estado == other.estado
    
    def valid(self) -> bool:
        return len(self.estado) != 0
    
    def get_estado(self) -> str:
        return self.estado

    @staticmethod
    def create(estado: str) -> 'Estados_Orden_VO':
        return Estados_Orden_VO(estado)