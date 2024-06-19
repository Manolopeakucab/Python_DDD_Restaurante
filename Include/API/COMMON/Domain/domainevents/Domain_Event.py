from abc import ABC
from datetime import datetime

class DomainEvent(ABC):

  def __init__(self):

    self.occurred_at = datetime.utcnow()

