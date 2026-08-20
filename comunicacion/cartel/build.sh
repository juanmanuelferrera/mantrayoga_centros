#!/bin/bash
# Genera el cartel en los tres formatos.
# Uso: ./build.sh   (desde comunicacion/cartel/)
set -e
cd "$(dirname "$0")"

for f in a4 cuadrado story; do
  xelatex -interaction=nonstopmode -halt-on-error \
    "\def\FORMATO{$f}\input{cartel.tex}" > /dev/null
  mv cartel.pdf "cartel-$f.pdf"
done

# Versiones PNG para redes (1080 px de ancho exactos)
pdftoppm -png -r 72 -singlefile cartel-cuadrado.pdf cartel-cuadrado
pdftoppm -png -r 72 -singlefile cartel-story.pdf    cartel-story

rm -f cartel.aux cartel.log
echo "Listo:"
ls -1 cartel-*.pdf cartel-*.png
