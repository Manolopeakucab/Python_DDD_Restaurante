from DDDAPI.Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class ID_Orden(ValueObject):
    
    id_orden:int;

    def __init__(self, id_orden:int):
        id_orden = ID_Orden.equals(id_orden)
        if id_orden is None:
            raise ValueError("El id de la orden no puede ser vacio")
        super().__init__()
        self.id_orden = id_orden

    def equals(self, other: 'ID_Orden') -> bool:
        return self.id_orden == other.id_orden
    
    def valid(self) -> bool:
        return len(self.id_orden) != 0
    
    def get_id_orden(self) -> int:
        return self.id_orden

    @staticmethod
    def create(id_orden: int) -> 'ID_Orden':
        return ID_Orden(id_orden)