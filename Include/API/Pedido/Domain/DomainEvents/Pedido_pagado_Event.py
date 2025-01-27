from Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent
from Include.API.Pedido.Domain.ValueObjects.ID_Orden import ID_Orden
from Include.API.Pedido.Domain.ValueObjects.Total_Orden_VO import Total_Orden_VO

class Pedido_pagado_Event(DomainEvent):

    def __init__(self, id: ID_Orden , total: Total_Orden_VO):
        super().__init__()
        self.id = id
        self.total = total

    def create(self, id: ID_Orden , total: Total_Orden_VO )-> 'Pedido_pagado_Event':
        self.publish(self,'Pedido pagado')
        return Pedido_pagado_Event(id, total)