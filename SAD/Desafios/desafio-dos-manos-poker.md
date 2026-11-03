# RA15_DOS_MANOS_POKER

## ENUNCIADO

- Una primera página con un botón "Jugar". Al pulsarlo se pasa a una segunda pantalla donde se muestran las 2 manos de póker (5 cartas cada una), usando la baraja completa de 52 cartas (sus palos y valores); da igual que se repitan cartas entre las dos manos.
- Debajo de las manos, indicar cuál de las dos gana según la regla de comparación de cartas más altas descrita arriba.
- 2 manos de póker, 5 cartas en cada una, para dos jugadores. Las cartas deben ser aleatorias, y sí se pueden repetir.

Debajo habrá un `<textarea>` que dirá quién gana a la mano más alta: se comparan únicamente las cartas más altas de cada mano, una a una (de mayor a menor), sin tener en cuenta jugadas como pareja, doble pareja, trío, etc. Por ejemplo, la jugada `J 8 7 6 6` gana a la jugada `8 J 6 6 6`, ya que al ordenar ambas de mayor a menor y comparar carta a carta, la tercera carta más alta (7 frente a 6) decide la mano.

### Recursos de cartas de póker

```
https://magicomagico.com/gilbertron/recursos/NP.png
```

Valores que puede tomar N (índices): `A,K,Q,J,10,9,8,7,6,5,4,3,2`

Valores que puede tomar P (palos): `P,C,T,D`

Ejemplo para mostrar el as de corazones:

```
https://magicomagico.com/gilbertron/recursos/AC.png
```

### Se pide


- La implementación del PHP, subida al repositorio de GitHub, y además pantallazos de que se ve funcionando en Mint.

**FIN ENUNCIADO**

---

## DESAFÍO NCA

**Desafío Nº:** `RA15_DOS_MANOS_POKER`

# Dos manos de póker en PHP

Crear en PHP un juego que reparta 2 manos de póker de 5 cartas aleatorias cada una y determine cuál gana comparando únicamente las cartas más altas, una a una.

### Objetivos técnicos

- Representar una baraja completa de 52 cartas (13 valores × 4 palos) en PHP.
- Generar aleatoriamente 2 manos de 5 cartas cada una, permitiendo repeticiones entre y dentro de las manos.
- Implementar la lógica de comparación: ordenar cada mano de mayor a menor y comparar carta a carta, ignorando jugadas como pareja, doble pareja o trío.
- Construir el flujo de pantallas: página inicial con botón "Jugar" → pantalla de resultado con las 2 manos y el ganador.
- Subir la implementación al repositorio de GitHub.

### Módulos implicados

- (CFGS Administración de Sistemas Informáticos en Red – ASIR, módulo IAW)

### Resultados de aprendizaje

- **RA1.** Prepara el entorno de desarrollo y los servidores de aplicaciones Web instalando e integrando las funcionalidades necesarias.
- **RA5.** Genera documentos Web utilizando lenguajes de guiones de servidor.

### Elementos transversales / competencias

Digital, pensamiento lógico-algorítmico, autonomía, resolución de problemas

### Principios pedagógicos

Construcción del pensamiento, Conducta autorregulada, Autonomía

### Sesiones

Acogida 1 · Explorar 1 · Idear 1 · Materializar 3 · Cierre 1 — **Total: 7 sesiones en 7 días**

---

### Fases

**Acogida** — 1 sesión
- Presentación del desafío: un juego de cartas sencillo como excusa para trabajar aleatoriedad, arrays y comparación de datos en PHP.

Observación: se plantea como un reto corto y autocontenido, sin necesidad de base de datos ni backend complejo.

**Explorar** — 1 sesión
- Repasar generación de números/elementos aleatorios en PHP (`rand`, `array_rand`) y manejo de arrays — pond. 1
- Entender cómo ordenar un array de mayor a menor (`rsort`) y cómo pasar datos entre páginas (formularios, `GET`/`POST` o sesión) — pond. 2

Observación: apoyado en la teoría de referencia del módulo sobre sintaxis y arrays/cadenas en PHP.

**Idear** — 1 sesión
- Decidir cómo representar la baraja (valores y palos) y cómo generar cada mano de 5 cartas — pond. 1
- Diseñar el algoritmo de comparación carta a carta y el flujo de las 2 pantallas (inicial con botón "Jugar" y de resultado) — pond. 2

Observación: se piensa la estructura de datos y el algoritmo antes de escribir el código, individualmente o en pequeño grupo.

**Materializar** — 3 sesiones
- Construir la baraja completa de 52 cartas y la función que genera una mano aleatoria de 5 cartas (con repetición) — pond. 2
- Implementar la página inicial con el botón "Jugar" y el paso a la pantalla de resultado — pond. 2
- Implementar la lógica de comparación (ordenar cada mano y comparar carta a carta) y mostrar las cartas con sus imágenes — pond. 3
- Subir la implementación al repositorio de GitHub — pond. 1

Observación: es la fase central — se evalúa que la comparación de manos siga exactamente la regla de "solo cartas más altas", sin aplicar jugadas de pareja/trío.

**Cierre** — 1 sesión
- Puesta en común mostrando el juego funcionando y comentando casos límite (por ejemplo, empate total si las 5 cartas, ya ordenadas, coinciden una a una).

Observación: se revisan en grupo los resultados de varias partidas para comprobar que la regla de comparación se aplica correctamente.
