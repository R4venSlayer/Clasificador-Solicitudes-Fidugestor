from ..infrastructure.repository.audit_repository import AudLoginUsuariosLogRepository, AudGestionUsuariosLogRepository

class AuditLoginUsuariosLogService():
    
    def __init__(self):
        self.aud_login_usuarios_log_repository = AudLoginUsuariosLogRepository()

    def create_audit_login_record(self, **kwargs):
        """Crea un nuevo registro de trazabilidad sobre los inicios de sesión que se realicen en el sistema"""
        return self.aud_login_usuarios_log_repository.create_record(**kwargs)

class AuditGestionUsuariosLogService():

    def __init__(self):
        self.aud_gestion_usuarios_log_repository = AudGestionUsuariosLogRepository()

    def create_audit_gestion_record(self, **kwargs):
        """Crea un nuevo registro de trazabilidad sobre la gestión de usuarios que se realicen en el sistema"""
        return self.aud_gestion_usuarios_log_repository.create_record(**kwargs)