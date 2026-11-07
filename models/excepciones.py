##Excepciones personalizadas del sistema Software FJ.##

class ErrorsistemaFJ(Exception):
  ## Representa un error general de nuestra aplicación ##
  pass

class 
DatosInvalidosError(ErrorSistemaFJ):
  ## indica que un dato no cumple las validaciones##
  pass

class
ParametroFaltanteError(ErrorSistemaFJ):
  ##indica que no se proporciono un dato obligatorio##
  pass

class
OperaciónNoPermitidaError(ErrorSistemaFJ):
  ##Indica que una accion no esta permitida##
  pass
  
class
ServicioNoDisponibleError(ErrorSistemaFJ):
  ##indica que el servicio solicitado no esta disponible##
  pass

class
ReservaInvalidaError(ErrorSistemaFJ):
  ##indica que una reserva no cumple las condiciones necesarias##
  pass

class
CalculoInconsistenteError(ErrorSistemaFJ):
  ##indica que un calculo de costo produjo un resultado invalido##


  
