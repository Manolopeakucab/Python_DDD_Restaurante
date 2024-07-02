from abc import ABC
from datetime import datetime

class DomainEvent(ABC):

  def __init__(self):

    self.occurred_at = datetime.utcnow()

class PubSub:
    """
    __init__: Inicializa una lista vacía de suscriptores.
    subscribe: Añade una función de suscriptor a la lista de suscriptores.
    publish: Llama a cada función suscriptora con el mensaje publicado.
    """
    def __init__(self):
        self.subscribers = []
    """
    callback: es una función que se pasa a otra función como un argumento, 
    que luego se invoca dentro de la función externa para completar algún 
    tipo de rutina o acción
    """
    def subscribe(self, callback):
        self.subscribers.append(callback)
        print(f"Subscribed: {callback}")

    def publish(self, message):
        for subscriber in self.subscribers:
            subscriber(message)
        print(f"Published: {message}")

