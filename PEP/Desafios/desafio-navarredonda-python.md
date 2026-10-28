# RA12_NAVARREDONDA_PYTHON

## ENUNCIADO

Simulador de Entradas a Parque de Atracciones de Navarredonda.

### Enunciado

Realiza un programa en Python que calcule el precio de una entrada en función de **7 parámetros** y **12 reglas de modificación**. Al final, imprime el precio con caracteres (arte ASCII) — si el precio final fuera 15, podría verse así:

```
d888     888888888
d8888    888
 888     888
 888     8888888b.
 888          "Y88b
 888             888
 888     Y88b  d88P
8888888   "Y8888P"
```

El **precio base** de la entrada es de **€45.00**.

### Datos de entrada

El usuario introduce 7 informaciones, excepto 2 que se indican aparte:

1. Edad del visitante (número entero).
2. Tipo de día (cadena: `'laboral'` o `'fin de semana'`).
3. Tipo de grupo (cadena: `'familiar'`, `'colegio'` o `'individual'`).
4. Residencia (cadena: `'madrid'` o `'otra provincia'`).
5. Día de la semana (cadena: `'lunes'` a `'domingo'`) — **no la introduce el usuario**, se toma automáticamente del sistema (fecha actual).
6. Es socio del club (cadena: `'si'` o `'no'`) — **no la introduce el usuario**, el 80% de las veces será socio (aleatorio).
7. Altura en metros (flotante, ejemplo: `1.55`).

### Reglas de modificación de tarifa

El precio final se define con las siguientes reglas, teniendo en cuenta la **prioridad**: más prioridad la 1, menos prioridad la 12. Se aplica la primera regla que se cumpla, de arriba a abajo.

| Prioridad | Condición | Ajuste de tarifa |
| --- | --- | --- |
| 1 | Es socio del club **y** la edad es mayor de 65 años. | Entrada gratuita (€0.00). |
| 2 | Es socio del club **y** reside en Madrid. | Descuento del 50%. |
| 3 | La altura es inferior a 1.20 m **o** la edad es menor de 4 años. | Descuento del 45%. |
| 4 | El grupo es `'colegio'` **y** la entrada es un lunes o viernes. | Descuento del 35%. |
| 5 | El día de la semana es jueves **y** el tipo de día es laboral. | Descuento del 30% (día del estudiante/promoción). |
| 6 | El visitante es menor de 18 años **y** la entrada es un día laboral. | Descuento del 25%. |
| 7 | El grupo es `'familiar'` **y** reside en `'otra provincia'`. | Descuento del 20%. |
| 8 | La edad está entre 18 y 25 años (joven) **y** no es socio. | Descuento del 10%. |
| 9 | La entrada es un sábado o domingo **y** el grupo es `'familiar'`. | Recargo del 5%. |
| 10 | El día de la semana es miércoles **y** no reside en Madrid. | Recargo del 10%. |
| 11 | La entrada es en fin de semana **y** el grupo es `'individual'` **y** reside en `'otra provincia'`. | Recargo fijo de €8.00. |
| 12 | Ninguna de las anteriores se cumple. | Tarifa base (€45.00). |

### Entrega

Todo en git:

- Código fuente comentado.
- Vídeo de 1 min comentando con tu voz lo que hace el código y su ejecución.

### Rúbrica

| Apartado | Puntos |
| --- | --- |
| Entrada (7 informaciones de inicio) | 10 |
| Reglas (12 reglas) | 10 |
| Salida (formato caracteres) | 10 |

**FIN ENUNCIADO**

---

## DESAFÍO NCA

**Desafío Nº:** `RA12_NAVARREDONDA_PYTHON`

# El precio de la entrada: un simulador de tarifas para el parque de Navarredonda

Programar en Python un simulador que calcule el precio de una entrada a partir de 7 datos de entrada y 12 reglas de descuento o recargo aplicadas por estricto orden de prioridad, con el resultado final dibujado en arte ASCII.

### Objetivos técnicos

- Capturar y validar 7 datos de entrada de distinto tipo (entero, cadena, flotante), incluyendo 2 que se obtienen automáticamente, sin pedirlos al usuario.
- Encadenar 12 reglas condicionales aplicadas por prioridad, aplicando únicamente la primera que se cumpla.
- Obtener el día de la semana a partir de la fecha actual del sistema.
- Generar un valor aleatorio con una probabilidad concreta (80%), no equiprobable.
- Mostrar el precio final como arte ASCII, dígito a dígito.
- Comentar el código y documentar su funcionamiento con un vídeo de un minuto.

### Módulos implicados

- (CFGS Administración de Sistemas Informáticos en Red – ASIR, módulo PEP)

### Resultados de aprendizaje

- **RA1.** Reconoce la estructura de un programa informático, identificando y relacionando los elementos propios del lenguaje de programación utilizado.
- **RA2.** Escribe y depura código, analizando y utilizando las estructuras de control del lenguaje.

### Elementos transversales / competencias

Lógica condicional, precisión en el orden de prioridad, manejo de fechas y aleatoriedad, presentación de resultados, documentación en vídeo

### Principios pedagógicos

Aprendizaje por proyectos, Construcción del pensamiento, Autonomía

### Sesiones

Acogida 1 · Explorar 1 · Idear 1 · Materializar 3 · Cierre 1 — **Total: 7 sesiones en 7 días**

---

### Fases

**Acogida** — 1 sesión
- Presentación del desafío: programar el sistema de tarifas de un parque de atracciones, donde el precio final depende de hasta 12 reglas distintas aplicadas en un orden estricto de prioridad.

Observación: se plantea como un caso realista de lógica de negocio con reglas que compiten entre sí, no solo como ejercicio de sintaxis.

**Explorar** — 1 sesión
- Repasar cómo pedir y validar datos de distinto tipo por teclado (`input()`, conversión a `int`/`float`) y cómo encadenar condiciones con `if`/`elif`/`else` — pond. 2
- Repasar cómo obtener la fecha y el día de la semana actuales del sistema, y cómo generar un valor aleatorio con una probabilidad concreta (no 50/50) — pond. 2

Observación: apoyado en la teoría de referencia del módulo sobre estructuras de control y de datos.

**Idear** — 1 sesión
- Diseñar la estructura de los datos de entrada: qué variable, de qué tipo, y cuáles introduce el usuario frente a las que se calculan solas — pond. 1
- Repasar las 12 reglas una a una e identificar qué condiciones se solapan entre sí, confirmando que el orden de prioridad evita aplicar dos reglas a la vez sobre un mismo caso — pond. 2
- Bocetar en papel cómo se va a dibujar el precio final en arte ASCII, dígito a dígito — pond. 1

Observación: lo más importante aquí es detectar de antemano los solapamientos entre reglas, antes de escribir ningún condicional.

**Materializar** — 3 sesiones
- Programar la captura y validación de los 7 datos de entrada, incluyendo el cálculo automático del día de la semana y el sorteo de si el visitante es socio — pond. 2
- Implementar la cadena completa de las 12 reglas de modificación de tarifa, respetando estrictamente el orden de prioridad — pond. 4
- Generar la salida del precio final en arte ASCII — pond. 2
- Comentar el código y grabar el vídeo de un minuto explicando con la voz qué hace y cómo se ejecuta — pond. 2

Observación: es la fase central — se evalúa que la prioridad de las reglas se respete exactamente (por ejemplo, que no se aplique la regla 7 cuando también se cumple la 3) y que la salida en ASCII sea legible.

**Cierre** — 1 sesión
- Puesta en común probando entre compañeros casos límite que cumplen varias reglas a la vez, y comprobando que cada programa aplica siempre la de mayor prioridad.

Observación: cierre centrado en el orden de prioridad de las reglas, que es el punto donde más errores suelen aparecer.
