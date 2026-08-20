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

## Cómo guardar un cartel

1. Abre `cartel/cartel.html` en el navegador y rellena los campos.
2. Pulsa **Guardar cuadrado**, **Guardar story** o **Guardar A4**.
3. En el diálogo elige **PDF → Guardar como PDF**, y marca **Print
   backgrounds** en la sección de Safari (si no, no imprime los fondos).
4. Guarda los PDF en una carpeta y ejecuta `pdf-a-png.sh` dentro de ella.

### Por qué el rodeo

Una página web no puede generar un PNG de esto por sí sola sin librerías
externas. Y Safari **no respeta `@page { margin: 0 }`**: aplica siempre los
márgenes mínimos de la impresora, así que un cartel del tamaño exacto del papel
no cabe, se corta por la derecha y lo que sobra cae en una segunda hoja.

Por eso el cartel se imprime algo reducido y con margen blanco alrededor. Ese
margen lo recorta `pdf-a-png.sh`, que además devuelve la imagen a su medida
real: 1080×1080 el cuadrado, 1080×1920 el story y 1240×1754 el A4 (150 dpi).

Necesita ImageMagick: `brew install imagemagick`.

Se lo mandas al centro el mismo día que dice que sí. Cuanto menos tenga que
hacer el centro, más lo publica.

Formatos que hay que entregar:
- **Cuadrado 1080x1080** para el feed de Instagram.
- **Vertical 1080x1920** para stories.
- **A4 vertical** para imprimir y colgar en la puerta y el vestuario.

---

## Texto del cartel

**MANTRA YOGA**

*Aprende a cantar los mantras clásicos en sánscrito*

[DÍA] [FECHA] · [HORA]
[NOMBRE DEL CENTRO]

Una hora. Cada mes, un tema distinto.
No hace falta experiencia ni saber sánscrito.

**Gratuito**

Plazas limitadas · Reserva en [contacto del centro]

---

## Variante para los meses siguientes

Debajo del título, en pequeño:

*Tema de este mes: [tema]*

Sirve para que quien ya vino sepa que no repite. Es la línea que trae de vuelta
a los repetidores, así que no la quites.

---

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
