from Include.API.COMMON.Domain.valueObjects import Value_object;

class Id_Almacen_VO(Value_object):

    id_almacen:str;

    def __init__(self, id_almacen: str):
        id_almacen = Id_Almacen_VO.valid(id_almacen);
        if id_almacen is None:
            raise ValueError("El id del almacen tiene que ser un UUID valido")
        self._id_almacen = id_almacen

    def equals(self, other: 'Id_Almacen_VO') -> bool:
        return self._id_almacen == other._id_almacen
    
    def valid(self) -> bool:
        return self._id_almacen != None
    
    def get_value(self) -> int:
        return self
    
    staticmethod
    def create(id_almacen: int) -> 'Id_Almacen_VO':
        return Id_Almacen_VO(id_almacen)