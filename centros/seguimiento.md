# Seguimiento de centros

El CSV es la base de datos. Aquí va lo que pasa con cada uno.

## Estados

Siguen la secuencia de `comunicacion/secuencia-contacto.md`.

| Estado | Qué significa |
|---|---|
| `pendiente` | Aún no contactado |
| `preparado` | Texto listo y datos comprobados, pero **sin enviar todavía** |
| `visita directa` | Se entra sin escribir antes, porque no hay canal o no compensa |
| `enviado` | Paso 1: email o mensaje enviado de verdad (día 0) |
| `visitado` | Paso 2: te pasaste por el centro |
| `revisita` | Fuiste y no estaba quien decide. Hay que volver en otra franja |
| `cerrando` | Han mostrado interés; se está pactando el día |
| `fecha` | Hay fecha cerrada para el primer taller |
| `activo` | Taller mensual funcionando |
| `pausado` | Estuvo activo y ahora no |
| `no` | Dijeron que no. Reabrir a los 6 meses |
| `sin respuesta` | Email y dos visitas sin resultado. Reabrir a los 6 meses |

## Prioridades

- **A** — Ya hacen meditación, kundalini, sivananda o talleres. La puerta está
  medio abierta. Empezar por estos.
- **B** — Centro generalista, receptivo, sin encaje obvio pero sin barrera.
- **C** — Perfil fitness o encaje dudoso. Al final de la cola.

## Regla de ritmo

No más de cinco contactos nuevos por semana. Si contestan tres a la vez y no
tienes agenda, quedas mal.

## Bitácora

Una línea por movimiento. Lo último arriba. **Aquí se anota todo**: lo que se
manda, lo que contestan, lo que se ve al pasar por delante y lo que te cuenta
alguien. Si no está escrito, a los tres centros ya no te acuerdas.

| Fecha | Centro | Qué pasó | Siguiente paso |
|---|---|---|---|
| 22-ago-26 | Lloc de Yoga Alicante | Decidido entrar **sin escribir antes**. No tienen email público. Horario localizado: solo lunes a jueves, 17:30-21:30 | Visita en frío, martes o miércoles a las 17:35. Ficha en `proxima-visita.md` |
| 22-ago-26 | Yoga Espacio Vital | **Confirmado enviado** por Juan Manuel | Visitar entre el 26 y el 29 de agosto |
| 22-ago-26 | Yoga Espacio Vital | Email del paso 1 enviado a yogaespaciovital@gmail.com. Sin adjunto, con nombre de contacto genérico porque no publican ninguno | Visitar entre el 26 y el 29 de agosto |
| 22-ago-26 | Yoga Espacio Vital | Datos verificados en su web: el directorio daba mal el email (info@…) y el teléfono (617…). Los correctos son yogaespaciovital@gmail.com y 647 83 34 70 | — |

### Regla de la bitácora

Un centro pasa a `enviado` **solo cuando Juan Manuel confirma que lo ha
mandado**, nunca al preparar el texto. Mientras tanto se queda en `preparado`.
La cuenta de enviados tiene que ser real o no sirve de nada.

### Lo que hemos aprendido hasta ahora

- **Los datos de los directorios fallan.** El primer centro que comprobamos
  tenía mal el email y el teléfono. Comprueba siempre en su web antes de
  escribir; si no, el primer contacto se pierde sin que te enteres.
- **Casi ningún centro publica el nombre de quien lo lleva.** Se saluda con un
  «Hola, buenas» y se pregunta el nombre en la visita.
- **Muchos no publican horario de clases.** Como el horario es lo que decide
  cuándo presentarse, cuando no esté hay que mirarlo en su Instagram o llamar
  y preguntar solo eso, sin contar nada más.

## Aviso sobre los datos del CSV

Los teléfonos y direcciones vienen de directorios públicos y algunos están
desactualizados (hay centros con dos teléfonos distintos según la fuente).
**Antes de llamar, comprueba el dato en la web o el Instagram del propio
centro.** Llamar a un número que ya no es suyo quema el primer contacto.

## Las fichas

Hay **una ficha por centro** en `centros/fichas/`, con sus datos, sus notas y el
guion de la visita. Se generan desde el CSV:

```
python3 centros/generar-fichas.py
```

**El CSV es la única fuente de verdad.** No edites una ficha a mano: se borran y
se regeneran enteras cada vez. Edita el CSV y vuelve a ejecutar el script.

**Para consultarlas desde Signal**, pídele a Hermes la ficha por el nombre del
centro y él lee el archivo de esa carpeta. El índice está en
`centros/fichas/INDICE.md`.

## Estado de la investigación

45 centros localizados. Reparto:

| Localidad | Centros |
|---|---|
| Alicante ciudad | 17 |
| Elche | 18 |
| Benidorm | 5 |
| Santa Pola | 2 |
| San Juan de Alicante | 2 |
| l'Alfàs del Pi | 1 |

Por prioridad: 11 de A, 21 de B, 13 de C.

Con 11 centros de prioridad A ya hay más de los 6-8 que caben en la Fase A. No
hace falta buscar más para empezar.

## El correo hay que buscarlo

El CSV trae email de solo 7 de los 45 centros, y esos siete vienen de un
directorio, con la misma advertencia que los teléfonos: **compruébalo en su web
antes de escribir**.

Para el resto hay dos caminos, y el segundo suele ser mejor:

- **Buscar el correo en su web**, en la página de contacto o en el pie.
- **Escribir por Instagram**, que en un estudio pequeño lo lee antes el dueño
  que el buzón de info@. El texto está en `comunicacion/whatsapp.md`.

Tres de los cinco centros de prioridad A de Alicante ciudad (Dayananda, Lloc de
Yoga y Sadhana) no tienen web localizada: con esos se va por Instagram
directamente, o se entra sin avisar.

## Nota sobre Benidorm

Son 45 minutos de coche cada trayecto. No compensa un solo taller. Si entran
dos o más centros de Benidorm, se agrupan el mismo día. Si solo entra uno, va al
final de la cola.

## Pendiente de investigar (más adelante)

Solo si hiciera falta ampliar por encima de 45:

- El Campello
- Mutxamel
- San Vicente del Raspeig
- Villajoyosa
- Asociaciones de vecinos y centros culturales con sala libre
