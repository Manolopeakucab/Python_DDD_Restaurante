from abc import ABC
from typing import List
from DDDAPI.Include.API.COMMON.Domain.domainevents.Domain_Event import DomainEvent 

class AggregateRoot(ABC):

    __events: List[DomainEvent] = []

    def add_domain_event(self, event: DomainEvent) -> None:
 
        self._events.append(event)

    def get_uncommitted_events(self) -> List[DomainEvent]:

        return self._events  

    def clear_events(self) -> None:

        self._events = []



