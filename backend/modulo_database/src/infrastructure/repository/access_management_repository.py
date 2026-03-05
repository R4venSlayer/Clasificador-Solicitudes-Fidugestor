from ...infrastructure.models.models import RefreshTokens

class RefreshTokensRepository():

    model = RefreshTokens

    def create_refresh_token(self, **kwargs) -> RefreshTokens:
        """Crea un nuevo refresh token en la base de datos."""
        return self.model.create(**kwargs)
    
    def patch_refresh_token_revocado(self, id_usuario: str, revocado_value:bool) -> RefreshTokens:
        """ Actualiza el campo de `revocado` de un refresh token existente. """
        return self.model.objects(id_usuario=id_usuario).update({"revocado": revocado_value})
        
