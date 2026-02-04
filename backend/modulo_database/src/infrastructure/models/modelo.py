
from django.db import models


class Baseacciongrupo(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    numdocumentousuario = models.CharField(db_column='numDocumentoUsuario', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idarchivo = models.ForeignKey('Gestorarchivo', models.DO_NOTHING, db_column='idArchivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaseAccionGrupo'


class Basefallojudicial(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    radicadocaso = models.CharField(db_column='radicadoCaso', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombrecaso = models.CharField(db_column='nombreCaso', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    numdocumentodemandante = models.CharField(db_column='numDocumentoDemandante', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    nombredemandante = models.CharField(db_column='nombreDemandante', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    jurisdiccioncaso = models.CharField(db_column='jurisdiccionCaso', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    estadoproceso = models.CharField(db_column='estadoProceso', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idarchivo = models.ForeignKey('Gestorarchivo', models.DO_NOTHING, db_column='idArchivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaseFalloJudicial'


class Baseinicial(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    radicado = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    proceso = models.CharField(max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)
    id_tipo_base_inicial = models.ForeignKey('Tipobaseinicial', models.DO_NOTHING, db_column='idTipoBaseInicial')  # Field name made lowercase.
    nombre_accionante = models.CharField(db_column='nombreAccionante', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    num_documento_accionante = models.CharField(db_column='numDocumentoAccionante', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    tipo_documento_accionante = models.CharField(db_column='tipoDocumentoAccionante', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    email_accionante = models.CharField(db_column='emailAccionante', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    id_archivo = models.ForeignKey('Gestorarchivo', models.DO_NOTHING, db_column='idArchivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BaseInicial'


class Basepensiongracia(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    numdocumentopensionado = models.CharField(db_column='numDocumentoPensionado', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idarchivo = models.ForeignKey('Gestorarchivo', models.DO_NOTHING, db_column='idArchivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BasePensionGracia'


class Basepensionadosfecstatus(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    numdocumentopensionado = models.CharField(db_column='numDocumentoPensionado', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechastatus = models.DateTimeField(db_column='fechaStatus', blank=True, null=True)  # Field name made lowercase.
    idarchivo = models.ForeignKey('Gestorarchivo', models.DO_NOTHING, db_column='idArchivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BasePensionadosFecStatus'


class Basepensionadosfecvinculacion(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    numdocumentopensionado = models.CharField(db_column='numDocumentoPensionado', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    fechavinculacion = models.DateTimeField(db_column='fechaVinculacion', blank=True, null=True)  # Field name made lowercase.
    mesada = models.DecimalField(max_digits=18, decimal_places=2, blank=True, null=True)
    regimenpension = models.CharField(db_column='regimenPension', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS', blank=True, null=True)  # Field name made lowercase.
    idarchivo = models.ForeignKey('Gestorarchivo', models.DO_NOTHING, db_column='idArchivo')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'BasePensionadosFecVinculacion'


class Gestorarchivo(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    nombre_archivo = models.CharField(db_column='nombreArchivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    ruta_archivo = models.CharField(db_column='rutaArchivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.
    id_tipo_archivo = models.ForeignKey('Tipoarchivo', models.DO_NOTHING, db_column='idTipoArchivo')  # Field name made lowercase.
    id_lote_gestor_archivo = models.ForeignKey('Lotegestorarchivo', models.DO_NOTHING, db_column='idLoteGestorArchivo')  # Field name made lowercase.
    procesado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'GestorArchivo'


class Lotegestorarchivo(models.Model):
    id = models.CharField(primary_key=True, max_length=36)
    id_usuario_quien_carga = models.CharField(db_column='idUsuarioQuienCarga', max_length=36, blank=True, null=True)  # Field name made lowercase.
    fecha_hora_carga = models.DateTimeField(db_column='fechaHoraCarga', blank=True, null=True)  # Field name made lowercase.
    procesado = models.BooleanField()

    class Meta:
        managed = False
        db_table = 'LoteGestorArchivo'

class Tipoarchivo(models.Model):
    nombre_tipo_archivo = models.CharField(db_column='nombreTipoArchivo', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoArchivo'


class Tipobaseinicial(models.Model):
    id = models.IntegerField(primary_key=True)
    nombre_base_inicial = models.CharField(db_column='nombreBaseInicial', max_length=255, db_collation='SQL_Latin1_General_CP1_CI_AS')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'TipoBaseInicial'
