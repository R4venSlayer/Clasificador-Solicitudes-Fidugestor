from ...infrastructure.models.models import AudGestionUsuariosLog, AudLoginUsuariosLog

class AudGestionUsuariosLogRepository():

    model = AudGestionUsuariosLog

    def create_audit_login_record(self, **kwargs) -> AudGestionUsuariosLog:
        """Crea un nuevo registro de trazabilidad sobre la gestión de usuarios que se realicen en el sistema"""
        return self.model.create(**kwargs)

class AudLoginUsuariosLogRepository():

    model = AudGestionUsuariosLog

    def create_audit_login_record(self, **kwargs) -> AudGestionUsuariosLog:
        """Crea un nuevo registro de trazabilidad sobre los inicios de sesión que se realicen en el sistema"""
        return self.model.create(**kwargs)
    
    



