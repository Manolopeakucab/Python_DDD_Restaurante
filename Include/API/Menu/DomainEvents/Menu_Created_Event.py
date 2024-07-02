from DDDAPI.Include.API.COMMON.Domain.domainevents.Domain_Event import Domain_Event
from DDDAPI.Include.API.Menu.ValueObjects.Nombre_VO import Nombre_Menu_VO
from DDDAPI.Include.API.Menu.ValueObjects.ID_Menu_VO import Id_Menu_VO
from DDDAPI.Include.API.Menu.ValueObjects.Platos_VO import Platos_VO

class Menu_Created_Event(Domain_Event):

    def __init__(self, id: Id_Menu_VO, nombre: Nombre_Menu_VO, platos: Platos_VO ):
        super().__init__()
        self.id = id
        self.nombre = nombre
        self.platos = platos

    @staticmethod
    def create(self,id: Id_Menu_VO, nombre: Nombre_Menu_VO, platos: Platos_VO) -> 'Menu_Created_Event':
        self.publish(self,'Menu creado')
        return Menu_Created_Event(id, nombre, platos)