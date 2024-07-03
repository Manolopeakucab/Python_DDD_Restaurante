from Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from Include.API.Pedido.Domain.ValueObjects.ID_Orden import ID_Orden
from Include.API.Pedido.Domain.ValueObjects.Platos_VO import Platos_VO

class Pedido_Cocinado_Event(DomainEvent):
    
        def __init__(self, id: ID_Orden , cantidad_platos: Platos_VO):
            super().__init__()
            self.id = id
            self.cantidad_platos = cantidad_platos
    
        def create(self, id: ID_Orden , cantidad_platos: Platos_VO)-> 'Pedido_Cocinado_Event':
            self.publish(self,'Pedido en cocina')
            return Pedido_Cocinado_Event(id, cantidad_platos)