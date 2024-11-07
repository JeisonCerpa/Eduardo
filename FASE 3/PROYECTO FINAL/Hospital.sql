CREATE TABLE `historia_clinica` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `fecha` timestamp,
  `diagnostico` text,
  `tratamiento` text,
  `observaciones` text,
  `prescripciones` text
);

CREATE TABLE `pacientes` (
  `documento` text PRIMARY KEY,
  `tipo_documento` text,
  `nombre` text,
  `apellido` text,
  `fecha_nacimiento` date,
  `genero` text,
  `direccion` text,
  `telefono` text,
  `email` text,
  `historial_medico_id` bigint
);

CREATE TABLE `roles` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `nombre` text UNIQUE,
  `descripcion` text
);

CREATE TABLE `horarios` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `dia_semana` text,
  `hora_inicio` time,
  `hora_fin` time
);

CREATE TABLE `medicos` (
  `cedula` text PRIMARY KEY,
  `nombre` text,
  `apellido` text,
  `especialidad` text,
  `telefono` text,
  `email` text,
  `horario_id` bigint
);

CREATE TABLE `enfermeros` (
  `cedula` text PRIMARY KEY,
  `nombre` text,
  `apellido` text,
  `telefono` text,
  `email` text,
  `horario_id` bigint
);

CREATE TABLE `personal_administrativo` (
  `cedula` text PRIMARY KEY,
  `nombre` text,
  `apellido` text,
  `telefono` text,
  `email` text,
  `puesto` text,
  `horario_id` bigint
);

CREATE TABLE `citas` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `paciente_documento` text,
  `medico_cedula` text,
  `fecha` timestamp,
  `motivo` text,
  `estado` text
);

CREATE TABLE `medicamentos` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `nombre` text,
  `descripcion` text,
  `cantidad` int,
  `fecha_vencimiento` date
);

CREATE TABLE `inventarios` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `medicamento_id` bigint,
  `cantidad` int,
  `fecha_actualizacion` timestamp
);

CREATE TABLE `usuarios` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `email` text UNIQUE,
  `contraseña` text,
  `rol_id` bigint,
  `persona_documento` text
);

CREATE TABLE `tipo_habitaciones` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `nombre` text UNIQUE,
  `descripcion` text
);

CREATE TABLE `habitaciones` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `numero` text,
  `tipo_id` bigint,
  `estado` text,
  `piso` int
);

CREATE TABLE `equipos` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `nombre` text,
  `descripcion` text,
  `cantidad` int,
  `estado` text,
  `ubicacion` text
);

CREATE TABLE `turnos` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `horario_id` bigint,
  `medico_cedula` text,
  `enfermero_cedula` text,
  `fecha` timestamp
);

CREATE TABLE `ingresos` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `paciente_documento` text,
  `fecha_ingreso` timestamp,
  `motivo` text,
  `habitacion_id` bigint
);

CREATE TABLE `egresos` (
  `id` bigint PRIMARY KEY AUTO_INCREMENT,
  `paciente_documento` text,
  `fecha_egreso` timestamp,
  `motivo` text,
  `habitacion_id` bigint
);

ALTER TABLE `pacientes` ADD FOREIGN KEY (`historial_medico_id`) REFERENCES `historia_clinica` (`id`);

ALTER TABLE `medicos` ADD FOREIGN KEY (`horario_id`) REFERENCES `horarios` (`id`);

ALTER TABLE `enfermeros` ADD FOREIGN KEY (`horario_id`) REFERENCES `horarios` (`id`);

ALTER TABLE `personal_administrativo` ADD FOREIGN KEY (`horario_id`) REFERENCES `horarios` (`id`);

ALTER TABLE `citas` ADD FOREIGN KEY (`paciente_documento`) REFERENCES `pacientes` (`documento`);

ALTER TABLE `citas` ADD FOREIGN KEY (`medico_cedula`) REFERENCES `medicos` (`cedula`);

ALTER TABLE `inventarios` ADD FOREIGN KEY (`medicamento_id`) REFERENCES `medicamentos` (`id`);

ALTER TABLE `usuarios` ADD FOREIGN KEY (`rol_id`) REFERENCES `roles` (`id`);

ALTER TABLE `usuarios` ADD FOREIGN KEY (`persona_documento`) REFERENCES `pacientes` (`documento`);

ALTER TABLE `habitaciones` ADD FOREIGN KEY (`tipo_id`) REFERENCES `tipo_habitaciones` (`id`);

ALTER TABLE `turnos` ADD FOREIGN KEY (`horario_id`) REFERENCES `horarios` (`id`);

ALTER TABLE `turnos` ADD FOREIGN KEY (`medico_cedula`) REFERENCES `medicos` (`cedula`);

ALTER TABLE `turnos` ADD FOREIGN KEY (`enfermero_cedula`) REFERENCES `enfermeros` (`cedula`);

ALTER TABLE `ingresos` ADD FOREIGN KEY (`paciente_documento`) REFERENCES `pacientes` (`documento`);

ALTER TABLE `ingresos` ADD FOREIGN KEY (`habitacion_id`) REFERENCES `habitaciones` (`id`);

ALTER TABLE `egresos` ADD FOREIGN KEY (`paciente_documento`) REFERENCES `pacientes` (`documento`);

ALTER TABLE `egresos` ADD FOREIGN KEY (`habitacion_id`) REFERENCES `habitaciones` (`id`);
