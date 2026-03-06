from ..infrastructure.repository.access_management_repository import RefreshTokensRepository

class RefreshTokenService():

    def __init__(self):
        self.refresh_tokens_repository = RefreshTokensRepository()

    def create_refresh_token(self, **kwargs):
        """Crea un nuevo refresh token en la base de datos."""
        return self.refresh_tokens_repository.create_record(**kwargs)
    
    def patch_refresh_token_revocado(self, id_usuario: str):
        """ Actualiza el campo de `revocado` de un refresh token existente. """
        return self.refresh_tokens_repository.patch_refresh_token_revocado(id_usuario)
    