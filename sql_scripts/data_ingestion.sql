-- Ingesta de datos en la tabla ´cat_tipo_documento_identidad´   

INSERT INTO dbo.cat_tipo_documento_identidad (abreviacion, descripcion)
VALUES
('CC', 'Cédula de ciudadanía'),
('CE', 'Cédula de extranjería'),
('TI', 'Tarjeta de identidad'),
('RC', 'Registro civil'),
('PA', 'Pasaporte'),
('PEP', 'Permiso especial de permanencia'),
('NIT', 'Número de identificación tributaria'),
('CD', 'Carné diplomático');


-- Ingesta de datos en la tabla ´cat_tipo_base_principal´   

INSERT INTO dbo.cat_tipo_base_principal (nombre_base_principal)
VALUES
('tutelas'),
('solicitudes fidugestor')


-- Ingesta de datos en la tabla ´cat_etapa_validacion´

INSERT INTO dbo.cat_etapa_validacion (nombre_etapa)
VALUES
('regla 1 - base pensional'),
('regla 2 - base accion grupo'),
('regla 3 - base fallo judicial'),
('regla 4 - base pension gracia'),
('regla 5 - fecha fuera de rango - fecha vinculación'),
('regla 6 - fecha fuera de rango - fecha estatus pensional'),
('regla 7 - smlmv fuera de rango - mesada');


-- Ingesta de datos en la tabla ´cat_tipo_fuente_archivo´

INSERT INTO dbo.cat_tipo_fuente_archivo(nombre_archivo)
VALUES
('base principal'),
('base accion grupo'),
('base fallo judicial'),
('base pension gracia'),
('base pension - fecha vinculacion'),
('base pension - fecha status')


-- Ingesta de datos en la tabla ´cat_tipo_operacion_gestion_usuario´

INSERT INTO dbo.cat_tipo_operacion_gestion_usuario(nombre_operacion)
VALUES
('agregar usuario'),
('modificar usuario'),
('activar usuario'),
('inactivar usuario'),
('modificar contraseña')

-- Ingesta de datos en la tabla ´roles´

INSERT INTO dbo.roles (id_rol, nombre_rol)
VALUES
(1, 'Administrador'),
(2, 'Analista')

-- Ingesta de datos en la tabla ´permisos´ 

INSERT INTO dbo.permisos(id_permiso, nombre_permiso)
VALUES
(1, 'user_manager'),
(2, 'load_information'),
(3, 'check_log_auditing'),
(4, 'execute_process'),
(5, 'check_historical')

-- Ingesta de datos en la tabla ´roles_permisos´ 

INSERT INTO dbo.permisos(id_rol, id_permiso)
VALUES
(1, 'user_manager'),
(2, 'load_information'),
(3, 'check_log_auditing'),
(4, 'execute_process'),
(5, 'check_historical')
