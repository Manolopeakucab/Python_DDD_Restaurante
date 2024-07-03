from Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from Include.API.Pedido.Domain.ValueObjects.ID_Orden import ID_Orden

class Pedido_Enviado_Event(DomainEvent):
    
    def __init__(self, id: ID_Orden):
        super().__init__()
        self.id = id

    def create(self, id: ID_Orden)-> 'Pedido_Enviado_Event':
        self(self, 'Transportando el pedido')
        return Pedido_Enviado_Event(id)