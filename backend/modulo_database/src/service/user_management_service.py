from ..infrastructure.repository.user_management_repository import UsuariosRepository

class UsuarioService():

    def __init__(self):
        self.usuarios_repository = UsuariosRepository()

    def get_usuario_by_id(self, id_usuario: str):
        """Obtiene un usuario por su ID."""
        return self.usuarios_repository.get_usuario_by_id(id_usuario)
    
    def get_all_usuarios(self) -> list:
        """Obtiene todos los usuarios registrados en la base de datos."""
        return self.usuarios_repository.get_all_users()
    
    def patch_usuario(self, id_usuario: str, **kwargs):
        """Actualiza parcialmente un usuario existente."""
        return self.usuarios_repository.patch_user(id_usuario, **kwargs)