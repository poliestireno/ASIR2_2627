# RA34_DBA_SQLITE

## ENUNCIADO

Eres el DBA (administrador) de una base de datos SQLite para una pequeña aplicación de gestión de frutas en dispositivos móviles. Tendrás que configurar correctamente la base de datos, optimizar su rendimiento, realizar backups/restauraciones y garantizar la seguridad de los datos almacenados.

Log de consultas de referencia (para el apartado de optimización): https://drive.google.com/file/d/1RToxJsbzJo_mOdjcGh6ff2DMFP7RsQAA/view

### Finalidad

1. Gestionar y configurar el entorno de la base de datos SQLite.
2. Optimizar el rendimiento de la base de datos a través de diferentes técnicas de ajuste.
3. Implementar copias de seguridad y restauración.
4. Aplicar técnicas de seguridad para proteger los datos sensibles.

### Requisitos del entorno

- Instalación de SQLite: asegúrate de tener SQLite instalado en tu entorno de trabajo. Puedes verificarlo con `sqlite3 --version`.
- Crea una base de datos llamada `frutitas.db` que almacenará la información de mandarinas, melocotones y caquis.

### 1. Configuración de la base de datos (2 puntos)

#### 1.1. Creación de tablas y estructura

Crea las siguientes tablas básicas con las restricciones adecuadas:

- **Mandarinas**:
  - `id_mandarina` (INTEGER, PK, AUTOINCREMENT): identificador único para cada mandarina.
  - `color` (TEXT, NOT NULL): color de la mandarina.
  - `tipo` (TEXT, NOT NULL): tipo de mandarina.
  - `size` (TEXT, NOT NULL): tamaño de la mandarina.
  - `fecha_recogida` (DATE, NOT NULL): fecha en la que se recogió la mandarina.
- **Melocotones**:
  - `id_melocoton` (INTEGER, PK, AUTOINCREMENT): identificador único para cada melocotón.
  - `tipo` (TEXT, NOT NULL): tipo de melocotón.
  - `suavidad` (BOOLEAN, NOT NULL): indica si el melocotón es suave (1) o no (0).
- **Caquis**:
  - `id_caqui` (INTEGER, PK, AUTOINCREMENT): identificador único para cada caqui.
  - `id_mandarina` (INTEGER, FK, NOT NULL): relacionado con `id_mandarina` en la tabla mandarinas.
  - `id_melocoton` (INTEGER, FK, NOT NULL): relacionado con `id_melocoton` en la tabla melocotones.
  - `color` (TEXT, NOT NULL): color del caqui.
  - `pedunculo` (BOOLEAN, NOT NULL): indica si el caqui tiene pedúnculo (1) o no (0).
  - `tiempo_maduracion` (INTEGER, NOT NULL): tiempo de maduración en días.

#### 1.2. Tamaño y más

Justifica cuánto ocupa la base de datos en disco. ¿En qué momento aumenta de tamaño si se mete más info? ¿Cómo harías algo para optimizar eso?

### 2. Optimización del rendimiento y mantenimiento (5 puntos)

Se ha encontrado un trozo de log de consultas a la base de datos durante el día 27 de octubre de 2024 (enlace arriba). Se pide qué optimizaciones realizarías y por qué, para mejorar la base de datos en función de la información que te ofrece el log, y justifícalo.

**PISTA:** utiliza `EXPLAIN QUERY PLAN` y revisa todos los pragmas de SQLite.

### 3. Copias de seguridad y restauración (2.5 puntos)

#### 3.1. Realización de una copia de seguridad con el nombre `frutitas_bonitas_bonitas.db`

#### 3.2. Realiza la restauración desde la copia de seguridad

#### 3.3. Automatización de backups

Crea un script para backups automáticos que se ejecute todos los días a las 23:59:59.

### 4. Preguntas sin ChatGPT ni IAs (0.5 puntos)

- ¿Cómo impactan los cambios en el PRAGMA en el rendimiento y la seguridad de la base de datos?
- ¿Qué mecanismos adicionales usarías para proteger una base de datos SQLite en un entorno de producción?
- ¿Qué diferencia existe entre los modos de journaling como DELETE, TRUNCATE y WAL en SQLite?

**FIN ENUNCIADO**

---

## DESAFÍO NCA

**Desafío Nº:** `RA34_DBA_SQLITE`

# El DBA de las frutitas: SQLite a punto para el móvil

Administrar de extremo a extremo una base de datos SQLite para una app móvil de gestión de frutas: crearla, afinarla a partir de un log real de consultas, protegerla con copias de seguridad automáticas y justificar las decisiones de seguridad.

### Objetivos técnicos

- Crear y configurar la base de datos `frutitas.db` con sus tablas, claves foráneas y restricciones, y razonar sobre su tamaño en disco y su crecimiento.
- Analizar un log de consultas reales y decidir optimizaciones justificadas (índices, `EXPLAIN QUERY PLAN`, PRAGMAs, `VACUUM`).
- Realizar una copia de seguridad, restaurarla y automatizarla con un script que se ejecute a diario a las 23:59:59.
- Explicar cómo los PRAGMAs, los modos de journaling y otros mecanismos afectan al rendimiento y a la seguridad de los datos.

### Módulos implicados

- (CFGS Administración de Sistemas Informáticos en Red – ASIR, módulo ASGBD)

### Resultados de aprendizaje

- **RA3.** Implanta métodos de control de acceso utilizando asistentes, herramientas gráficas y comandos del lenguaje del sistema gestor.
- **RA4.** Automatiza tareas de administración del gestor describiéndolas y utilizando guiones de sentencias.

### Elementos transversales / competencias

Seguridad de la información, análisis de datos, automatización de tareas, documentación técnica, pensamiento crítico

### Principios pedagógicos

Aprendizaje basado en problemas, Construcción del pensamiento, Autonomía

### Sesiones

Acogida 1 · Explorar 1 · Idear 1 · Materializar 3 · Cierre 1 — **Total: 7 sesiones en 7 días**

---

### Fases

**Acogida** — 1 sesión
- Presentación del desafío: eres el DBA de una app móvil de frutas, con una base de datos pequeña pero que debe ser rápida, estar protegida y poder recuperarse si algo falla.

Observación: se plantea como caso de administración real en un entorno ligero (móvil), donde SQLite no tiene servidor ni usuarios y la seguridad hay que buscarla por otras vías.

**Explorar** — 1 sesión
- Repasar cómo guarda SQLite los datos (fichero único, páginas, crecimiento y `VACUUM`) y la herramienta `sqlite3` — pond. 2
- Estudiar `EXPLAIN QUERY PLAN`, los índices y los PRAGMAs principales (`journal_mode`, `synchronous`, `cache_size`, `foreign_keys`, `auto_vacuum`...) — pond. 3
- Conocer las vías de copia de seguridad (`.backup`, `.dump`, copia del fichero) y cómo programar tareas diarias (`cron`) — pond. 2

Observación: son los anclajes de las cuatro partes del desafío (estructura, rendimiento, backups y seguridad); se trabaja con el `sqlite3` de la propia máquina.

**Idear** — 1 sesión
- Leer el log de consultas e identificar qué tablas y columnas se consultan más y de qué forma (filtros, ordenaciones, uniones) para decidir dónde harían falta índices o ajustes — pond. 2
- Planificar la estrategia de copias de seguridad (qué método, dónde se guarda, cómo se nombra, cómo se restaura) y la lista de PRAGMAs y medidas de seguridad que se valorarán — pond. 1

Observación: es diseño sobre papel; no se toca la base de datos hasta tener claro qué se va a optimizar y por qué.

**Materializar** — 3 sesiones
- Crear `frutitas.db` con las tres tablas, sus claves y restricciones, y justificar cuánto ocupa en disco, cuándo crece y cómo reducirlo — pond. 3
- Aplicar y justificar las optimizaciones derivadas del log (índices, PRAGMAs, mantenimiento), comprobando el antes y el después con `EXPLAIN QUERY PLAN` — pond. 5
- Hacer la copia `frutitas_bonitas_bonitas.db`, restaurar desde ella y comprobar que los datos son correctos — pond. 3
- Escribir el script de backup automático y programarlo para que se ejecute todos los días a las 23:59:59 — pond. 3
- Responder por escrito, sin ayuda de IAs, a las tres preguntas sobre PRAGMAs, protección en producción y modos de journaling — pond. 1

Observación: es la fase central y la que concentra el peso de la nota; se evalúa que cada decisión (sobre todo las de optimización) esté justificada con evidencia y no solo ejecutada.

**Cierre** — 1 sesión
- Puesta en común: presentar las optimizaciones elegidas, la estrategia de backups y las respuestas de seguridad, y comparar con las decisiones del resto de la clase.

Observación: sirve para ver que distintas optimizaciones pueden ser válidas para el mismo log si están bien justificadas.
