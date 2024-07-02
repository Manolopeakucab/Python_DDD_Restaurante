from DDDAPI.Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class Direccion_Pedido_VO(ValueObject):
    
    direccion:str;

    def __init__(self, direccion:str):
        direccion = Direccion_Pedido_VO.equals(direccion)
        if direccion is None:
            raise ValueError("La direccion no puede ser vacia")
        super().__init__()
        self.direccion = direccion

    def equals(self, other: 'Direccion_Pedido_VO') -> bool:
        return self.direccion == other.direccion
    
    def valid(self) -> bool:
        return len(self.direccion) != 0
    
    def get_direccion(self) -> str:
        return self.direccion

    @staticmethod
    def create(direccion: str) -> 'Direccion_Pedido_VO':
        return Direccion_Pedido_VO(direccion)