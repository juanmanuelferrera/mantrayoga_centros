#!/bin/bash
# Genera el cartel en los tres formatos, en PDF y en PNG del tamaño exacto.
# Uso: ./build.sh
set -e
cd "$(dirname "$0")"

compila () {   # $1 formato   $2 fondo
  xelatex -interaction=nonstopmode -halt-on-error \
    "\def\FORMATO{$1}\def\FONDO{$2}\input{cartel.tex}" > /dev/null
  mv cartel.pdf "cartel-$1.pdf"
}

compila a4       claro
compila cuadrado oscuro
compila story    oscuro

pdftoppm -png -r 72 -singlefile cartel-cuadrado.pdf cartel-cuadrado
pdftoppm -png -r 72 -singlefile cartel-story.pdf    cartel-story
pdftoppm -png -r 150 -singlefile cartel-a4.pdf      cartel-a4

rm -f cartel.aux cartel.log
echo "Listo:"
ls -1 cartel-*.pdf cartel-*.png
