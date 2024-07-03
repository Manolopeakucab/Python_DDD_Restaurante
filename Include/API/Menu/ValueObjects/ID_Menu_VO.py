from Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class Id_Menu_VO(ValueObject):
    def __init__(self, id: str):
        super().__init__()
        self.id = id

    def equals(self, other: 'Id_Menu_VO') -> bool:
        return self.id == other.id

    def valid(self) -> bool:
        return self.id != 0

    def get_id(self) -> str:
        return self

    @staticmethod
    def create(id: str) -> 'Id_Menu_VO':
        return Id_Menu_VO(id)