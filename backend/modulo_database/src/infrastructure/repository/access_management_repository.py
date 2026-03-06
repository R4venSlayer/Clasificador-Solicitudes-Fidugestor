import token

from ...infrastructure.models.models import RefreshTokens

class RefreshTokensRepository():

    model = RefreshTokens

    def create_record(self, **kwargs) -> RefreshTokens:
        """Crea un nuevo refresh token en la base de datos."""
        return self.model.create(**kwargs)
    
    def patch_refresh_token_revocado(self, id_usuario: str) -> RefreshTokens:
        """ Actualiza el campo de `revocado` a True de un refresh token existente. """

        token = self.model.objects.filter(id_usuario=id_usuario).order_by('fecha_hora_creacion').first()

        token.revocado = True
        token.save()

        return token
        
