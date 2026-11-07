##Clase abstracta base para las entidades de Software FJ##

from abc import ABC , abstractmethod 

class Entidad(ABC):
  ##Define la estructura comun de las entidades del sistema##

  @abstractmethod
  def describir(self):
    #exige que cada entidad implemente su propia descripcion##
    pass
