# Cartel

**El productor de carteles es un archivo de este repo:**
`comunicacion/cartel/cartel.html`. Ábrelo con doble clic en el navegador.

Rellenas los campos y salen los tres formatos a la vez. No necesita internet
(salvo para las tipografías), no depende de ningún servicio y funcionará igual
dentro de cinco años.

Hay además una copia publicada en
https://claude.ai/code/artifact/24fc66da-d47d-49f9-bd61-d96e08a50402 para verla
desde el móvil, pero **los botones de guardar solo funcionan bien en el archivo
local**: la página publicada bloquea las descargas.

Y hay una versión LaTeX en `cartel/cartel.tex` para PDF vectorial.

## Cómo sacar los carteles

**Usa la versión LaTeX.** Es la que da los archivos definitivos, con el tamaño
exacto y sin depender del navegador.

1. Abre `comunicacion/cartel/cartel.tex` y rellena los campos de arriba: tema,
   día de la semana, número, mes, hora, centro, dirección, canal (`tel`, `wa` o
   `tg`), número, contacto, posición fija y, si lo tienes, la ruta al logo.
2. Ejecuta `./build.sh` en esa carpeta.
3. Salen seis archivos: PDF y PNG de los tres formatos.

| Archivo | Para qué |
|---|---|
| `cartel-a4.pdf` | Imprimir y colgar. Fondo claro, llena la hoja, una sola página |
| `cartel-cuadrado.png` | Feed de Instagram. 1080 × 1080, fondo oscuro |
| `cartel-story.png` | Stories. 1080 × 1920, fondo oscuro |

Para cambiar el fondo de un formato, edita la llamada correspondiente en
`build.sh` (`claro` u `oscuro`).

### La versión HTML

`cartel.html` sigue ahí y es más cómoda para probar textos y ver los tres
formatos a la vez en vivo. Pero **no la uses para generar los archivos
finales**: Safari no permite controlar los márgenes de impresión ni desactivar
sus cabeceras desde el documento, así que el resultado depende de ajustes del
diálogo y sale distinto en cada impresora. Sirve para decidir; LaTeX, para
producir.

## El logo del centro

El productor tiene un campo para subir el logo del centro. **Úsalo siempre.**

Va **arriba del todo, encima del título**, y no al pie. La razón no es de
cortesía: la sala es suya y nosotros no tenemos local propio, así que dónde se
hace el taller es información principal, no un crédito. Además, con su marca
arriba el cartel deja de ser tuyo y pasa a ser suyo, y un centro publica mucho
más lo que siente propio.

Hay un control de tamaño porque los logos no se comportan igual: un wordmark
ancho necesita menos altura que una marca cuadrada. Ajústalo hasta que pese lo
mismo que el título sin taparlo.

Pídeselo en la visita, junto con la posición fija: "¿me pasas vuestro logo en
PNG y os hago el cartel?". Es una petición mínima que además les compromete un
poco más.

**Si su logo es oscuro y el cartel va en fondo oscuro**, el botón *Aclarar logo*
lo invierte. Si queda mal, pasa el cartel entero a fondo claro: es preferible un
cartel claro con su logo bien que uno oscuro con su logo hecho un borrón.

## Reglas de diseño

- Sobrio. Nada de mandalas, lotos, siluetas en posición de loto al atardecer ni
  degradados morados.
- El nombre del centro tan visible como el título. Es su cartel también.
- La palabra **gratuito** tiene que verse desde lejos.
- Una foto real de gente cantando en círculo, o ninguna. Nada de banco de
  imágenes.
- Sin logos grandes. El de Centros de Bhakti yoga, pequeño y abajo.
- Que se lea en el móvil a tamaño miniatura. Si no se lee, hay demasiado texto.

## Nota

"Plazas limitadas" no es un truco: en una sala de yoga caben 25 o 30 y conviene
que el centro lleve control. Además hace que la gente reserve, y quien reserva
viene.
