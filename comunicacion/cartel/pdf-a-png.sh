#!/bin/bash
# Convierte los PDF guardados desde cartel.html en PNG del tamaño exacto.
#
# El navegador imprime el cartel algo reducido y con margen blanco, porque
# Safari impone los márgenes mínimos de la impresora. Este script recorta ese
# margen y devuelve la imagen a su medida real:
#
#   cuadrado → 1080 × 1080
#   story    → 1080 × 1920
#   A4       → 1240 × 1754 (150 dpi)
#
# Uso: ./pdf-a-png.sh [carpeta]   (por defecto, la carpeta actual)

set -e
DIR="${1:-.}"
cd "$DIR"

command -v magick >/dev/null || { echo "Falta ImageMagick: brew install imagemagick"; exit 1; }

shopt -s nullglob
hechos=0

for f in *.pdf; do
  base="${f%.pdf}"
  tmp="/tmp/cartel-$$.png"

  # Se rasteriza en grande, se aplana sobre blanco y se recorta el margen.
  magick -density 300 "$f[0]" -background white -flatten \
         -fuzz 2% -trim +repage "$tmp"

  # La proporción de lo recortado dice qué formato es.
  read -r w h < <(magick identify -format "%w %h" "$tmp")
  ratio=$(echo "scale=4; $w / $h" | bc)

  if (( $(echo "$ratio > 0.90" | bc -l) )); then
    destino="1080x1080!"; etiqueta="cuadrado 1080×1080"
  elif (( $(echo "$ratio < 0.62" | bc -l) )); then
    destino="1080x1920!"; etiqueta="story 1080×1920"
  else
    destino="1240x1754!"; etiqueta="A4 a 150 dpi"
  fi

  magick "$tmp" -resize "$destino" -strip "$base.png"
  rm -f "$tmp"
  echo "  $etiqueta → $base.png"
  hechos=$((hechos+1))
done

if [ "$hechos" -eq 0 ]; then
  echo "No hay ningún PDF en $(pwd)"
else
  echo "Listo: $hechos archivo(s)."
fi
