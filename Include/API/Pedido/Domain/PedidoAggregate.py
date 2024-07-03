from Include.API.COMMON.Domain.aggregates.Aggregates import Aggregates
from Include.API.Pedido.Domain.ValueObjects.ID_Orden import ID_Orden
from Include.API.Pedido.Domain.ValueObjects.Total_Orden_VO import Total_Orden_VO
from Include.API.Pedido.Domain.ValueObjects.Direccion_Pedido_VO import Direccion_Pedido_VO
from Include.API.Pedido.Domain.ValueObjects.Estados_Orden_VO import Estados_Orden_VO
from Include.API.Pedido.Domain.ValueObjects.Platos_VO import Platos_VO

from Include.API.Pedido.Domain.DomainEvents.Pedido_Enviado_Event import Pedido_Enviado_Event
from Include.API.Pedido.Domain.DomainEvents.Pedido_pagado_Event import Pedido_pagado_Event
from Include.API.Pedido.Domain.DomainEvents.Pedido_Recibido_Event import Pedido_Recibido_Event
from Include.API.Pedido.Domain.DomainEvents.Pedido_Cocinado_Event import Pedido_Cocinado_Event

class PedidoAggregate(Aggregates):
    def __init__(self, id: ID_Orden, total: Total_Orden_VO, direccion: Direccion_Pedido_VO, estado: Estados_Orden_VO, cantidad_platos: Platos_VO):
        self.id = id
        self.total = total
        self.direccion = direccion
        self.estado = estado
        self.cantidad_platos = cantidad_platos
    
    def get_id(self) -> ID_Orden:
        return self.id
    
    def get_total(self) -> Total_Orden_VO:
        return self.total
    
    def get_direccion(self) -> Direccion_Pedido_VO:
        return self.direccion
    
    def get_estado(self) -> Estados_Orden_VO:
        return self.estado
    
    def get_cantidad_platos(self) -> Platos_VO:
        return self.cantidad_platos
    
    @staticmethod
    async def create(id: ID_Orden, total: Total_Orden_VO, direccion: Direccion_Pedido_VO, estado: Estados_Orden_VO, cantidad_platos: Platos_VO) -> 'PedidoAggregate':
        return PedidoAggregate(id, total, direccion, estado, cantidad_platos)
    
    async def pagar(self) -> Pedido_pagado_Event:
        return Pedido_pagado_Event.create(self.id, self.total, self.direccion, self.cantidad_platos)
    
    async def enviar(self) -> Pedido_Enviado_Event:
        return Pedido_Enviado_Event.create(self.id, self.total, self.direccion, self.cantidad_platos)
    
    async def recibido(self) -> Pedido_Recibido_Event:
        return Pedido_Recibido_Event.create(self.id, self.total, self.direccion, self.cantidad_platos)