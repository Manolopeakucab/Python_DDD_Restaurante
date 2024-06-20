from abc import ABC, abstractmethod
from typing import Generic, TypeVar

T = TypeVar('T')

class ValueObject(ABC,Generic[T]):
    @abstractmethod
    def equals(self,other: 'ValueObject')-> bool:
        pass
    
    @abstractmethod
    def valid(self)->bool:
        pass
    
    
    def get_value(self) -> T:
        return self
