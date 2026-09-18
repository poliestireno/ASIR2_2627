# RA1_ATTACK_SIMULATION

## ENUNCIADO

Simulación de ataques en Kali Linux

*(a la vez que su realización ir documentando en github con los pantallazos explicados más relevantes)*

### 1.- Creación de diccionarios con PYDICTOR Y DYMERGE

Vamos a trabajar con la herramienta Pydictor, que permite la creación de diccionarios para fuerza bruta. Sus principales características son las siguientes:

- Pydictor se utiliza para crear diccionarios para fuerza bruta.
- Esta herramienta crea la lista de palabras tanto en palabras normales como en diferentes tipos de cifrado, como el cifrado base64.
- Pydictor está escrito en Python.
- Hay dos métodos para romper la contraseña usando esta herramienta:
  - crear una lista de palabras normales.
  - crear la lista de palabras en formato base64.

Instala las herramientas Pydictor y Dymerge y crea dos diccionarios de palabras con Pydictor: uno con números y otro con una lista de palabras con letras en mayúsculas.

Fusiona los dos diccionarios anteriores en uno solo llamado `diccionarion` con la herramienta Dymerge.

### ¡Al ataque!

Utilizaremos la herramienta Hydra para simular 2 ataques por fuerza bruta con `diccionarion`:

### 2.- Utilizar diccionarion con Hydra para simular un ataque de fuerza bruta en SSH

- Instalar OpenSSH.
- Iniciar y configurar el servidor SSH en Kali Purple.
- Crear un usuario que simule ser el objetivo de tus pruebas.
- Conectar al servidor SSH desde tu sistema.
- Simular un ataque de fuerza bruta utilizando Hydra y `diccionarion`.
- Revisar los logs del sistema para analizar los intentos de conexión.
- Analizar los resultados y estudiar cómo mitigar ataques similares en entornos reales.

### 3.- Utilizar diccionarion con Hydra para simular un ataque de fuerza bruta con HTTP (formulario web)

- Instalar y configurar [DVWA](https://github.com/digininja/DVWA) como una aplicación web vulnerable en tu servidor Apache local.
- Identificar los detalles del formulario de login para poder construir el ataque.
- Usar Hydra para realizar un ataque de fuerza bruta, utilizando `diccionarion`.
- Analizar los resultados y estudiar cómo mitigar ataques similares en entornos reales.

---

## DESAFÍO NCA

**Desafío Nº:** `RA1_ATTACK_SIMULATION`

# Simulación de ataques en Kali Linux

Simular ataques reales de fuerza bruta en un entorno controlado, generando tus propios diccionarios y atacando un servicio SSH y un formulario web, documentando todo en GitHub.

### Objetivos técnicos

- Generar diccionarios de contraseñas propios con Pydictor y fusionarlos con Dymerge.
- Simular un ataque de fuerza bruta con Hydra contra un servicio SSH.
- Simular un ataque de fuerza bruta con Hydra contra un formulario de login web (DVWA).
- Documentar el proceso completo en GitHub con capturas explicadas.

### Módulos implicados

- (CFGS Administración de Sistemas Informáticos en Red – ASIR, módulo SAD)

### Resultados de aprendizaje

- **RA1.** Adopta pautas y prácticas de tratamiento seguro de la información, reconociendo las vulnerabilidades de un sistema informático y la necesidad de asegurarlo.

### Elementos transversales / competencias

Digital, autonomía, pensamiento analítico, ética profesional (uso responsable de herramientas ofensivas)

### Principios pedagógicos

Construcción del pensamiento, Conducta autorregulada, Autonomía

### Sesiones

Acogida 1 · Explorar 1 · Idear 1 · Materializar 4 · Cierre 1 — **Total: 8 sesiones en 8 días**

---

### Fases

**Acogida** — 1 sesión
- Presentación del desafío: qué es un ataque de fuerza bruta/diccionario y por qué conviene entenderlo también desde el lado defensivo.

Observación: se plantea como un ejercicio de Red Team en un laboratorio propio y aislado (Kali Linux) — nunca contra sistemas de terceros.

**Explorar** — 1 sesión
- Repasar qué son los ataques por diccionario y por fuerza bruta — pond. 1
- Entender qué hacen Pydictor, Dymerge y Hydra, y cómo funcionan SSH y la autenticación por formulario HTTP — pond. 2

Observación: apoyado en la teoría de referencia del módulo sobre diccionarios y fuerza bruta con Hydra.

**Idear** — 1 sesión
- Decidir qué diccionarios generar (números, mayúsculas) y con qué criterios de longitud y juego de caracteres — pond. 1
- Planificar cómo montar cada ataque: usuario objetivo en SSH, y cómo identificar el mensaje de fallo del formulario de DVWA — pond. 2

Observación: se piensa la estrategia antes de tocar la terminal, individualmente o en pequeño grupo.

**Materializar** — 4 sesiones
- Instalar Pydictor y Dymerge; crear los dos diccionarios y fusionarlos en `diccionarion` — pond. 2
- Instalar y configurar OpenSSH, crear el usuario objetivo, lanzar el ataque con Hydra y revisar los logs de conexión — pond. 3
- Instalar y configurar DVWA sobre Apache, identificar el formulario de login, y lanzar el ataque con Hydra — pond. 3
- Documentar cada paso en GitHub con capturas explicadas — pond. 2

Observación: es la fase central — se evalúa la ejecución técnica y la calidad de la documentación.

**Cierre** — 1 sesión
- Analizar los resultados de ambos ataques y explicar cómo se mitigarían en un entorno real.

Observación: puesta en común en clase de las medidas de mitigación propuestas por cada alumno o equipo.
