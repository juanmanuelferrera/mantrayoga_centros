#!/bin/bash
# Convierte los PDF guardados desde cartel.html en PNG del tamaño exacto.
#
#   1080 px de ancho para el cuadrado y el story (Instagram)
#   150 dpi para el A4 (calidad de impresión)
#
# Uso: ./pdf-a-png.sh [carpeta]   (por defecto, la carpeta actual)

set -e
DIR="${1:-.}"
cd "$DIR"

shopt -s nullglob
hechos=0

for f in *.pdf; do
  base="${f%.pdf}"
  # tamaño de página en puntos, para saber qué formato es
  medidas=$(pdfinfo "$f" 2>/dev/null | awk '/Page size/{print $3, $5}')
  ancho=${medidas%% *}
  alto=${medidas##* }

  if [ -z "$ancho" ]; then
    echo "  saltado (no es un PDF legible): $f"
    continue
  fi

  # A4 son 595 x 842 puntos; el resto son los carteles de redes
  if [ "${ancho%.*}" -lt 620 ] && [ "${alto%.*}" -gt 800 ]; then
    pdftoppm -png -r 150 -singlefile "$f" "$base"
    echo "  A4 a 150 dpi   → $base.png"
  else
    pdftoppm -png -r 96 -singlefile "$f" "$base"
    echo "  1080 px        → $base.png"
  fi
  hechos=$((hechos+1))
done

if [ "$hechos" -eq 0 ]; then
  echo "No hay ningún PDF en $(pwd)"
else
  echo "Listo: $hechos archivo(s)."
fi
