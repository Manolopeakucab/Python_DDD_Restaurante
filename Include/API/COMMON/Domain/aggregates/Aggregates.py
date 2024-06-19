from abc import ABC
from typing import List
from domainevents.Domain_Event import DomainEvent  # Assuming "domainevent.py" is in the same directory

class AggregateRoot(ABC):

    __events: List[DomainEvent] = []

    def add_domain_event(self, event: DomainEvent) -> None:
 
        self._events.append(event)

    def get_uncommitted_events(self) -> List[DomainEvent]:

        return self._events  # Return a copy to avoid modifying internal state

    def clear_events(self) -> None:

        self._events = []


