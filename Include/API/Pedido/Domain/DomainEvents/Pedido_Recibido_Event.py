from Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from Include.API.Pedido.Domain.ValueObjects.ID_Orden import ID_Orden
from Include.API.Pedido.Domain.ValueObjects.Total_Orden_VO import Total_Orden_VO
from Include.API.Pedido.Domain.ValueObjects.Direccion_Pedido_VO import Direccion_Pedido_VO
from Include.API.Pedido.Domain.ValueObjects.Platos_VO import Platos_VO

class Pedido_pagado_Event(DomainEvent):

    def __init__(self, id: ID_Orden , total: Total_Orden_VO , direccion: Direccion_Pedido_VO , cantidad_platos: Platos_VO ):
        super().__init__()
        self.id = id
        self.total = total
        self.direccion = direccion
        self.cantidad_platos = cantidad_platos

    def create(self, id: ID_Orden , total: Total_Orden_VO , direccion: Direccion_Pedido_VO , cantidad_platos: Platos_VO)-> 'Pedido_pagado_Event':
        self.publish(self,'Pedido recibido por el cliente')
        return Pedido_pagado_Event(id, total, direccion, cantidad_platos)