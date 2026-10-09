# RA12_USERS_MYSQL

## ENUNCIADO

Realiza en MySQL/MariaDB en Kali Linux la gestión completa de usuarios y permisos sobre una base de datos de red social.

Teoría de referencia (pública): `teoria-administracion-mysql.html`.

### Esquema inicial: base de datos `red_social`

| usuario | grupo | comentario |
|---|---|---|
| PK id_usuario (INT) | PK id_grupo (INT) | PK id_comentario (INT) |
| nombre (VARCHAR) | nombre_grupo (VARCHAR) | FK usuario_id (INT) |
| email (VARCHAR) | FK creador_id (INT) | FK grupo_id (INT) |
| fecha_registro (DATE) | fecha_creacion (DATE) | texto (TEXT) |

#### Relaciones (claves foráneas)

- **USUARIO ← GRUPO** (1 a N): `GRUPO.creador_id` referencia a `USUARIO.id_usuario`. Un usuario crea muchos grupos, pero un grupo tiene solo un creador.
- **USUARIO ← COMENTARIO** (1 a N): `COMENTARIO.usuario_id` referencia a `USUARIO.id_usuario`. Un usuario escribe muchos comentarios.
- **GRUPO ← COMENTARIO** (1 a N): `COMENTARIO.grupo_id` referencia a `GRUPO.id_grupo`. Un grupo contiene muchos comentarios.

Para cada ejercicio, presenta evidencia de pantallazo con comando y resultado, y lo que se considere necesario.

### Ejercicios

1. Indica el nombre de las tablas que aparecen en tu base de datos mysql.
2. Crea el usuario "Bego" con contraseña "Beglña" para que pueda acceder desde localhost.
3. Crea el usuario "Mati" con contraseña "aMti90" para que pueda acceder desde el dominio lasalleinstitucion.es.
4. Crea el usuario "Mifli" con contraseña "lopol45" para que pueda acceder desde el dominio lasalleinstitucion.es.
5. Muestra los usuarios creados (los que están en la tabla `user` de la base de datos mysql). Indica la sentencia que has utilizado para mostrar esos usuarios.
6. Muestra el usuario con el que te has logado, utilizando para ello una función. Indica la sentencia que has utilizado para ello.
7. Cambia la contraseña de Mati, de manera que la nueva contraseña sea "minuevacontraseña". Indica la sentencia que has utilizado para ello.
8. Muestra los privilegios del usuario Bego. Indica la sentencia que has utilizado para ello.
9. Muestra los privilegios del usuario con el que te has logado. Indica la sentencia que has utilizado para ello.
10. Concede permisos al usuario Bego de lectura y actualización sobre la tabla usuario.
11. Conéctate como Bego y lanza una sentencia select y otra update sobre la tabla usuario. Lanza también una sentencia delete. Muestra las sentencias y sus efectos sobre la base de datos de la red social.
12. Concede permisos al usuario Mati de borrado sobre la tabla grupo.
13. Crea el usuario Crispula con contraseña "rosita" para que pueda acceder desde el dominio lasalleinstitucion.es y con permiso de lectura, actualización y borrado sobre las tablas usuario, grupo y comentario. Concede además permisos a Crispula para que pueda conceder sus permisos a otros usuarios.
14. Conéctate con el usuario Crispula.
15. Inserta un registro en la tabla comentario. Actualiza un registro de la tabla grupo. Muestra las sentencias y su resultado al ejecutarlas sobre la base de datos de la red social.
16. Concede permiso de borrado sobre la tabla usuario a Bego. Muestra la sentencia utilizada y el resultado de su ejecución.
17. Concede permiso de lectura y actualización sobre la tabla grupo a Mati. Muestra la sentencia utilizada y el resultado de su ejecución.
18. Vuelve a conectarte con tu usuario de mysql.
19. Concede permisos totales sobre todas las tablas de la base de datos de la red social a Mifli. Muestra la sentencia utilizada y el resultado de su ejecución.
20. Quítale permisos de borrado sobre todas las tablas de la base de datos de la red social a Mifli. Muestra la sentencia utilizada y el resultado de su ejecución.
21. Muestra los usuarios creados y sus privilegios (los que están en la tabla user de la base de datos mysql). Indica la sentencia que has utilizado para mostrar esos usuarios.
22. Cambia la contraseña del usuario Mifli modificando directamente la tabla user. Indica la sentencia que has utilizado para ello.
23. ¿Has necesitado hacer FLUSH PRIVILEGES después de la sentencia anterior? Explica el porqué y para qué sirve FLUSH PRIVILEGES.
24. ¿Puedo utilizar la función PASSWORD con GRANT? Justifica tu respuesta.
25. Elimina el usuario Mifli. Muestra la sentencia utilizada y el resultado de su ejecución.

### Entrega

Presentar en lenguaje Markdown en vuestro repositorio de GitHub.

**FIN ENUNCIADO**

---

## DESAFÍO NCA

**Desafío Nº:** `RA12_USERS_MYSQL`

# Usuarios y permisos en MySQL: administrar el acceso a una red social

Gestionar de extremo a extremo los usuarios, contraseñas y privilegios de una base de datos MySQL/MariaDB para una red social, sobre Kali Linux.

### Objetivos técnicos

- Crear usuarios MySQL con distintos orígenes de conexión (localhost, dominio) y gestionar sus contraseñas.
- Consultar los usuarios y privilegios existentes en las tablas de sistema de MySQL (`mysql.user`).
- Conceder y revocar privilegios granulares (SELECT, UPDATE, DELETE, todos los permisos) sobre tablas concretas de una base de datos.
- Delegar la capacidad de conceder permisos a otros usuarios (GRANT OPTION).
- Modificar directamente la tabla `user` y entender el papel de FLUSH PRIVILEGES.
- Verificar cada operación conectándose como el usuario afectado y comprobando el efecto real de sus permisos.

### Módulos implicados

- (CFGS Administración de Sistemas Informáticos en Red – ASIR, módulo ASGBD)

### Resultados de aprendizaje

- **RA1.** Implanta sistemas gestores de bases de datos analizando sus características y ajustándose a los requerimientos del sistema.
- **RA2.** Configura el sistema gestor de bases de datos interpretando las especificaciones técnicas y los requisitos de explotación.

### Elementos transversales / competencias

Seguridad de la información, rigor en la ejecución de comandos, documentación técnica, verificación experimental

### Principios pedagógicos

Aprendizaje por la práctica, Construcción del pensamiento, Autonomía

### Sesiones

Acogida 1 · Explorar 1 · Idear 1 · Materializar 3 · Cierre 1 — **Total: 7 sesiones en 7 días**

---

### Fases

**Acogida** — 1 sesión
- Presentación del desafío: te conviertes en el administrador de la base de datos de una red social, y vas a controlar quién puede ver, cambiar o borrar qué, usuario por usuario.

Observación: enmarca el desafío como gestión de seguridad de acceso, no solo como sintaxis SQL.

**Explorar** — 1 sesión
- Repasar el modelo de usuarios de MySQL/MariaDB: la tabla `user`, el formato `'usuario'@'host'`, y los comandos `CREATE USER`, `SHOW GRANTS`, `CURRENT_USER()` — pond. 2
- Repasar el sistema de privilegios (`GRANT`/`REVOKE`, niveles sobre base de datos/tabla, `GRANT OPTION`) y para qué sirve `FLUSH PRIVILEGES` — pond. 2

Observación: apoyado en la teoría de referencia del módulo sobre administración de MySQL/MariaDB.

**Idear** — 1 sesión
- A partir del esquema de la base de datos `red_social` (usuario, grupo, comentario), planificar qué usuario necesita qué permiso sobre qué tabla, y desde qué origen de conexión (localhost o dominio) — pond. 2
- Planificar el orden de las pruebas de verificación: qué usuario se conecta, qué sentencia ejecuta y qué resultado se espera en cada caso — pond. 1

Observación: se diseña el mapa de usuarios/permisos antes de ejecutar ninguna sentencia.

**Materializar** — 3 sesiones
- Crear los usuarios Bego, Mati y Mifli con sus contraseñas y orígenes de conexión, y comprobar su existencia en la tabla `user` — pond. 2
- Conceder y verificar permisos progresivos sobre `usuario`, `grupo` y `comentario` (lectura, actualización, borrado, permisos totales) para cada usuario, conectándose como ellos para comprobar el efecto — pond. 4
- Crear el usuario Crispula con permisos múltiples y capacidad de conceder sus propios permisos a otros, y usarlo para insertar/actualizar registros — pond. 3
- Cambiar contraseñas (con sentencia dedicada y modificando directamente la tabla `user`), revocar permisos y eliminar un usuario, documentando cada sentencia y su resultado con pantallazos — pond. 3

Observación: es la fase central — se evalúa que cada sentencia SQL sea correcta y que la evidencia (pantallazo + comentario) demuestre que el permiso realmente funciona o se ha revocado.

**Cierre** — 1 sesión
- Puesta en común: responder a las preguntas de reflexión (¿hace falta FLUSH PRIVILEGES tras modificar la tabla user a mano? ¿se puede usar PASSWORD con GRANT?) y comparar con el resto de la clase.

Observación: cierre centrado en consolidar el porqué de cada comando, no solo en haberlo ejecutado.
