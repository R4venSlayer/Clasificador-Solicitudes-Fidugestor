CREATE DATABASE SolicitudesFidugestor

USE SolicitudesFidugestor

CREATE TABLE "usuarios" (
  "id_usuario" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "tipo_documento_identidad" integer NOT NULL,
  "num_documento_identidad" varchar(255) NOT NULL,
  "primer_nombre" varchar(255) NOT NULL,
  "segundo_nombre" varchar(255),
  "primer_apellido" varchar(255) NOT NULL,
  "segundo_apellido" varchar(255),
  "email_usuario" varchar(255) NOT NULL,
  "nombre_usuario" varchar(255) NOT NULL,
  "password_usuario" varchar(255) NOT NULL,
  "codigo_seguridad" varchar(255) NOT NULL,
  "id_rol" integer NOT NULL,
  "es_activo" bit NOT NULL
);

CREATE TABLE "refresh_tokens" (
  "id_refresh_token" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_usuario" UNIQUEIDENTIFIER NOT NULL,
  "token_hash" varchar(255) NOT NULL,
  "fecha_hora_expiracion" datetime2 NOT NULL,
  "revocado" bit NOT NULL
);

CREATE TABLE "permisos" (
  "id_permiso" integer  PRIMARY KEY NOT NULL,
  "nombre_permiso" varchar(255) NOT NULL
);

CREATE TABLE "roles" (
  "id_rol" integer  PRIMARY KEY NOT NULL,
  "nombre_rol" varchar(255) NOT NULL
);

CREATE TABLE "roles_permisos" (
  "id_rol_permiso" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_rol" integer NOT NULL,
  "id_permiso" integer NOT NULL
);

CREATE TABLE "aud_log_descarga" (
  "id_descarga" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "id_usuario_descarga" UNIQUEIDENTIFIER NOT NULL,
  "fecha_hora_descarga" datetime2 NOT NULL,
  "hash_archivo" varchar(255) NOT NULL,
  "total_registros" integer
);

CREATE TABLE "aud_gestion_usuarios_log" (
  "id_operacion" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_tipo_operacion" integer NOT NULL,
  "id_usuario_responsable" UNIQUEIDENTIFIER NOT NULL,
  "id_usuario_afectado" UNIQUEIDENTIFIER NOT NULL,
  "fecha_hora_operacion" datetime2 NOT NULL
);

CREATE TABLE "aud_login_usuarios_log" (
  "id_sesion_login" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_usuario_login" UNIQUEIDENTIFIER NOT NULL,
  "fecha_hora_login" datetime2 NOT NULL
);

CREATE TABLE "aud_log_carga" (
  "id_aud_carga" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_tipo_archivo" integer NOT NULL,
  "nombre_fuente" varchar(255) NOT NULL,
  "id_usuario_responsable" UNIQUEIDENTIFIER NOT NULL,
  "fecha_hora_carga" datetime2 NOT NULL,
  "hash_archivo" varchar(255) NOT NULL,
  "total_registros" integer
);

CREATE TABLE "cat_tipo_operacion_gestion_usuario" (
  "id_tipo_operacion" integer  PRIMARY KEY NOT NULL IDENTITY,
  "nombre_operacion" varchar(255)
);

CREATE TABLE "cat_tipo_documento_identidad" (
  "id_tipo" integer  PRIMARY KEY NOT NULL IDENTITY,
  "abreviacion" varchar(255) NOT NULL,
  "descripcio" varchar(255) NOT NULL
);

CREATE TABLE "cat_tipo_fuente_archivo" (
  "id_fuente" integer  PRIMARY KEY NOT NULL IDENTITY,
  "nombre_archivo" varchar(255)
);

CREATE TABLE "cat_tipo_base_principal" (
  "id_base_principal" integer  PRIMARY KEY NOT NULL IDENTITY,
  "nombre_base_principal" varchar(255) NOT NULL
);

CREATE TABLE "cat_etapa_validacion" (
  "id_etapa_validacion" integer  PRIMARY KEY NOT NULL IDENTITY,
  "nombre_etapa" varchar(255)
);

CREATE TABLE "lote_datasets" (
  "id_lote" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_aud_carga" UNIQUEIDENTIFIER
);

CREATE TABLE "base_principal" (
  "id_registro" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "id_tipo_base_principal" integer NOT NULL,
  "radicado" varchar(255),
  "proceso" varchar(255),
  "nombreAccionante" varchar(255),
  "numDocumentoAccionante" varchar(255),
  "tipoDocumentoRemitente" varchar(255),
  "emailRemitente" varchar(255)
);

CREATE TABLE "base_accion_grupo" (
  "id_registro" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "numDocumentoUsuario" varchar(255)
);

CREATE TABLE "base_fallo_judicial" (
  "id_registro" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "radicadoCasomDocumentoUsuario" varchar(255),
  "nombreCaso" varchar(255),
  "numDocumentoDemandante" varchar(255),
  "jurisdiccionCaso" varchar(255),
  "estadoProceso" varchar(255)
);

CREATE TABLE "base_pension_gracia" (
  "id_registro" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "numDocumentoPensionado" varchar(255)
);

CREATE TABLE "base_pension_fecha_status" (
  "id_registro" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "numDocumentoPensionado" varchar(255),
  "fechaStatus" datetime2
);

CREATE TABLE "base_pension_fecha_vinculacion" (
  "id_registro" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "numDocumentoPensionado" varchar(255),
  "fechaVinculacion" datetime2,
  "mesada" decimal,
  "regimenPension" varchar(255)
);

CREATE TABLE "historical_output_datasets" (
  "id_output_record" UNIQUEIDENTIFIER  PRIMARY KEY NOT NULL,
  "id_lote" UNIQUEIDENTIFIER NOT NULL,
  "radicado" varchar(255),
  "proceso" varchar(255),
  "nombre_accionante" varchar(255),
  "num_documento_accionante" varchar(255),
  "tipo_documento_accionante" varchar(255),
  "num_documento_pensionado" varchar(255),
  "fecha_vinculacion" datetime2,
  "fecha_status" datetime2,
  "mesada" decimal,
  "regimen_pension" varchar(255),
  "num_documento_usuario_accion_grupo" varchar(255),
  "num_documento_usuario_fallo_judicial" varchar(255),
  "radicado_caso" varchar(255),
  "nombre_caso" varchar(255),
  "jurisdiccion_caso" varchar(255),
  "estado_proceso" varchar(255),
  "num_documento_usuario_pension_gracia" varchar(255),
  "id_etapa_validacion" integer,
  "tiene_derecho" bit,
  "fecha_ejecucion_validacion" datetime2
);

ALTER TABLE "aud_log_carga" ADD CONSTRAINT "fk_tipoFuenteArchivo_id_fuente_LogCargaAuditoria" FOREIGN KEY ("id_tipo_archivo") REFERENCES "cat_tipo_fuente_archivo" ("id_fuente") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "aud_log_carga" ADD CONSTRAINT "fk_Usuarios_idUsuario_LogCarga" FOREIGN KEY ("id_usuario_responsable") REFERENCES "usuarios" ("id_usuario") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "usuarios" ADD CONSTRAINT "fk_tipoDocumentoIdentidadCatalogo_idTipo_Usuarios" FOREIGN KEY ("tipo_documento_identidad") REFERENCES "cat_tipo_documento_identidad" ("id_tipo") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "aud_gestion_usuarios_log" ADD CONSTRAINT "fk_cat_tipo_operacion_gestion_usuario_id_operacion_aud_gestion_usuarios_log" FOREIGN KEY ("id_tipo_operacion") REFERENCES "cat_tipo_operacion_gestion_usuario" ("id_tipo_operacion") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "refresh_tokens" ADD CONSTRAINT "fk_refresh_tokens_id_usuario_usuarios" FOREIGN KEY ("id_usuario") REFERENCES "usuarios" ("id_usuario") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "roles_permisos" ADD CONSTRAINT "fk_permisos_id_permiso_roles_permisos" FOREIGN KEY ("id_permiso") REFERENCES "permisos" ("id_permiso") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "roles_permisos" ADD CONSTRAINT "fk_roles_id_rol_roles_permisos" FOREIGN KEY ("id_rol") REFERENCES "roles" ("id_rol") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "usuarios" ADD CONSTRAINT "fk_usuarios_id_rol_roles" FOREIGN KEY ("id_rol") REFERENCES "roles" ("id_rol") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "aud_login_usuarios_log" ADD CONSTRAINT "fk_aud_login_usuarios_log_id_usuario_login_usuarios" FOREIGN KEY ("id_usuario_login") REFERENCES "usuarios" ("id_usuario") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "aud_log_descarga" ADD CONSTRAINT "fk_usuarios_id_usuario_aud_log_descarga" FOREIGN KEY ("id_usuario_descarga") REFERENCES "usuarios" ("id_usuario") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "base_principal" ADD CONSTRAINT "fk_cat_tipo_base_principal_id_base_principal_base_principal" FOREIGN KEY ("id_tipo_base_principal") REFERENCES "cat_tipo_base_principal" ("id_base_principal") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "base_principal" ADD CONSTRAINT "fk_lote_datasets_id_lote_base_principal" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "base_accion_grupo" ADD CONSTRAINT "fk_lote_datasets_id_lote_base_accion_grupo" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "base_fallo_judicial" ADD CONSTRAINT "fk_lote_datasets_id_lote_base_fallo_judicial" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "base_pension_gracia" ADD CONSTRAINT "fk_lote_datasets_id_lote_base_pension_gracia" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "base_pension_fecha_status" ADD CONSTRAINT "fk_lote_datasets_id_lote_base_pension_fecha_status" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "base_pension_fecha_vinculacion" ADD CONSTRAINT "fk_lote_datasets_id_lote_base_pension_fecha_vinculacion" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "lote_datasets" ADD CONSTRAINT "fk_lote_datasets_id_aud_carga_aud_log_carga" FOREIGN KEY ("id_aud_carga") REFERENCES "aud_log_carga" ("id_aud_carga") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "historical_output_datasets" ADD CONSTRAINT "fk_lote_datasets_id_lote_historical_output_datasets" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "historical_output_datasets" ADD CONSTRAINT "fk_cat_etapa_validacion_id_etapa_validacion_historical_output_datasets" FOREIGN KEY ("id_etapa_validacion") REFERENCES "cat_etapa_validacion" ("id_etapa_validacion") ON DELETE NO ACTION ON UPDATE NO ACTION;

ALTER TABLE "aud_log_descarga" ADD CONSTRAINT "fk_lote_datasets_id_lote_aud_log_descarga" FOREIGN KEY ("id_lote") REFERENCES "lote_datasets" ("id_lote") ON DELETE NO ACTION ON UPDATE NO ACTION;
