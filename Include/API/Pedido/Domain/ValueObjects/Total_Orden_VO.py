from Include.API.COMMON.Domain.valueObjects.Value_object import ValueObject

class Total_Orden_VO(ValueObject):
    def __init__(self, value: float):
        total = Total_Orden_VO.validate(value)
        if total is None:
            raise Exception("Total de la orden no puede ser negativo")
        super.__init__()
        self.value = value

    def equals(self, other: ValueObject) -> bool:
        return self.value == other.value    

    def validate(self, value: float):
        if value < 0:
            raise Exception("Total de la orden no puede ser negativo")

    def get(self) -> float:
        return self.value
    
    def create(self, value: float)-> 'Total_Orden_VO':
        return Total_Orden_VO(value)