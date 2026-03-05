
from ...infrastructure.models.models import Usuarios

class UsuariosRepository():
    
    model = Usuarios

    def create_user(self, **kwargs) -> Usuarios:
        """Crea un nuevo usuario en la base de datos."""
        return self.model.create(**kwargs)

    def get_user_by_id(self, id_usuario: str) -> Usuarios:
        """Obtiene un usuario por su ID."""
        return self.model.get_by_id(id_usuario)
    
    def patch_user(self, id_usuario: str, **kwargs) -> Usuarios:
        """Actualiza parcialmente un usuario existente."""
        return self.model.objects(id_usuario=id_usuario).update(**kwargs)