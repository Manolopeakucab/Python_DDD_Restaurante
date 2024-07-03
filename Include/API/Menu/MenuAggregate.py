from Include.API.COMMON.Domain.aggregates.Aggregates import AggregateRoot
from Include.API.Menu.ValueObjects.ID_Menu_VO import Id_Menu_VO
from Include.API.Menu.ValueObjects.Nombre_VO import Nombre_Menu_VO
from Include.API.Menu.ValueObjects.Platos_VO import Platos_VO
from Include.API.Menu.DomainEvents.Menu_Created_Event import Menu_Created_Event
from Include.API.Menu.DomainEvents.Menu_Created_Event import Menu_Created_Event

class Menu(AggregateRoot):
    id: Id_Menu_VO
    nombre: Nombre_Menu_VO
    platos: Platos_VO

    def __init__(self, id: Id_Menu_VO, nombre: Nombre_Menu_VO, platos: Platos_VO):
        super().__init__()
        menu = Menu_Created_Event.create(id, nombre, platos)
        return menu
    
    def get_id(self) -> Id_Menu_VO:
        return self.id
    
    def get_nombre(self) -> Nombre_Menu_VO:
        return self.nombre
    
    def get_platos(self) -> Platos_VO:
        return self.platos
    
    @staticmethod
    async def create(id: Id_Menu_VO, nombre: Nombre_Menu_VO, platos: Platos_VO) -> 'Menu':
        return Menu(id, nombre, platos)
    
    