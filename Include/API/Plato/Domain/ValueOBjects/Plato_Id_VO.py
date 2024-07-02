from DDDAPI.Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class Id_Plato_VO(ValueObject):
    
    id_plato:str;

    def __init__(self, id_plato:str):
        id_plato = Id_Plato_VO.equals(id_plato)
        if id_plato is None:
            raise ValueError("El id del plato no puede ser vacio")
        super().__init__()
        self.id_plato = id_plato

    def equals(self, other: 'Id_Plato_VO') -> bool:
        return self.id_plato == other.id_plato
    
    def valid(self) -> bool:
        return len(self.id_plato) != 0
    
    def get_id(self) -> str:
        return self.id_plato

    @staticmethod
    def create(id_plato: str) -> 'Id_Plato_VO':
        return Id_Plato_VO(id_plato)