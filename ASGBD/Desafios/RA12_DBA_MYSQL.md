# RA12_DBA_MYSQL

## ENUNCIADO

Eres un DBA (administrador de bases de datos) de una consultora informática y tienes que configurar la base de datos MySQL/MariaDB de 3 empresas en función de sus necesidades.

Estos son los 15 parámetros de MySQL que deberías configurar:

```
innodb_buffer_pool_size
innodb_log_file_size
max_connections
query_cache_size
table_open_cache
tmp_table_size
max_heap_table_size
innodb_flush_log_at_trx_commit
log_bin
slow_query_log
slow_query_log_file
long_query_time
bind-address
innodb_file_per_table
performance_schema
```

Se han encontrado extractos de entrevistas para cada una de las 3 empresas. Se pide la configuración y el porqué de los valores de los parámetros. Preséntalo en formato tabla:

```
Parámetro|valor|porqué
```

Extractos de entrevistas:

- Entrevista 1
- Entrevista 2
- Entrevista 3

*(los enlaces originales a las entrevistas no se capturaron en esta extracción — consulta el documento original del desafío para su contenido.)*

Además, indica en qué ficheros de tu instalación MySQL tendrías que modificar para configurar los 15 parámetros, y haz 3 pantallazos con ellos modificados en tu propia instalación.

Haz pruebas en el servidor MySQL del XAMPP y pon pantallazos y explicaciones de cada caso.

Realízalo en lenguaje Markdown en el repositorio ASGBD y entrega en TutoZ el enlace al repositorio.

**FIN ENUNCIADO**

---

## DESAFÍO NCA

**Desafío Nº:** `RA12_DBA_MYSQL`

# El DBA de la consultora: MySQL a medida de 3 empresas

Configurar, como DBA externo, los mismos 15 parámetros de MySQL/MariaDB de tres formas distintas — una por empresa — justificando cada valor a partir de lo que cuenta cada cliente en su entrevista.

### Objetivos técnicos

- Interpretar necesidades de negocio (extractos de entrevista) y traducirlas a parámetros técnicos concretos de MySQL/MariaDB.
- Configurar y justificar los 15 parámetros de rendimiento/comportamiento del servidor, para 3 perfiles de empresa distintos.
- Localizar en qué ficheros de la instalación (my.ini/my.cnf) se aplica cada parámetro, y aplicarlos en un entorno propio.
- Probar la configuración sobre el servidor MySQL de XAMPP y documentar el resultado con capturas.

### Módulos implicados

- (CFGS Administración de Sistemas Informáticos en Red – ASIR, módulo ASGBD)

### Resultados de aprendizaje

- **RA1.** Implanta sistemas gestores de bases de datos analizando sus características y ajustándose a los requerimientos del sistema.
- **RA2.** Configura el sistema gestor de bases de datos interpretando las especificaciones técnicas y los requisitos de explotación.

### Elementos transversales / competencias

Análisis de requisitos, toma de decisiones justificada, documentación técnica, pensamiento analítico

### Principios pedagógicos

Aprendizaje basado en problemas, Construcción del pensamiento, Autonomía

### Sesiones

Acogida 1 · Explorar 2 · Idear 1 · Materializar 4 · Cierre 1 — **Total: 9 sesiones en 9 días**

---

### Fases

**Acogida** — 1 sesión
- Presentación del rol: eres el DBA externo de una consultora, y cada empresa cliente tiene necesidades de rendimiento distintas que vas a tener que traducir a configuración real.

Observación: se plantea como caso de consultoría — no hay una única respuesta correcta, sino una justificada.

**Explorar** — 2 sesiones
- Estudiar qué hace cada uno de los 15 parámetros (buffer pool, caché de consultas, logging, límites de conexión, InnoDB por tabla, performance_schema...) y qué efecto tiene subirlo o bajarlo — pond. 3
- Localizar en qué archivo de configuración de MySQL/MariaDB (my.ini en Windows, my.cnf en Linux) vive cada parámetro, y cómo se recarga el servicio tras modificarlo — pond. 2

Observación: apoyado en la teoría de referencia del módulo sobre administración de MySQL/MariaDB.

**Idear** — 1 sesión
- Leer los tres extractos de entrevista y anotar, empresa por empresa, qué pistas de negocio (tráfico esperado, tipo de consultas, tolerancia a caídas, necesidad de auditoría...) apuntan a qué parámetro — pond. 2
- Diseñar la tabla `Parámetro | valor | porqué` que se rellenará en la fase siguiente, una por empresa — pond. 1

Observación: es planificación sobre papel — decidir el razonamiento antes de tocar ningún fichero de configuración.

**Materializar** — 4 sesiones
- Rellenar las 3 tablas (una por empresa) con el valor de cada uno de los 15 parámetros y su justificación a partir de la entrevista — pond. 3
- Aplicar la configuración en la propia instalación y capturar 3 pantallazos de los ficheros ya modificados — pond. 2
- Probar la configuración sobre el servidor MySQL de XAMPP, con pantallazos y explicación de cada prueba — pond. 3
- Documentar todo el proceso en Markdown, en el repositorio ASGBD — pond. 2

Observación: es la fase central — se evalúa tanto la coherencia de la configuración con cada entrevista como la evidencia de que de verdad se ha probado.

**Cierre** — 1 sesión
- Presentar las 3 configuraciones y explicar qué parámetro marcó la mayor diferencia entre empresas y por qué.

Observación: puesta en común en clase comparando cómo cada alumno interpretó las mismas entrevistas.
