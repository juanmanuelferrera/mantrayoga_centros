#!/usr/bin/env python3
"""Genera una ficha por contacto a partir de contactos.csv, en contactos/fichas/.

Mismo criterio que las fichas de centros: el CSV es la única fuente de verdad,
las fichas se borran y se regeneran enteras. No editarlas a mano.

Uso:  python3 contactos/generar-fichas.py
"""
import csv, io, os, re, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, 'contactos.csv')
DIR = os.path.join(BASE, 'fichas')

def slug(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', t.lower())).strip('-')

REGLAS = """
## Cómo se le escribe a un conocido

**Cambia el tono y cambia lo que pides.** A un centro se le pide la sala. A un
conocido, dos cosas mucho más pequeñas: permiso para avisarle, y un nombre.

- **Uno a uno, con su nombre.** Nunca a un grupo: un reenvío se nota y no lo
  contesta nadie.
- **Una sola petición pequeña.** «¿Te aviso cuando tenga fecha?» se contesta en
  cinco segundos. «¿Vienes?» a un taller que aún no existe, no.
- **«Dime el nombre y ya me presento yo.»** Le quita de encima el papel de
  intermediario, y por eso contesta mucha más gente.
- **El dossier depende.** Si decide sobre una sala, mándaselo. Si vendría como
  alumno, no: le sonará a que le colocas algo.
- **Si no contesta, no insistas.** Con un conocido el seguimiento cuesta más de
  lo que da. Se saca en la siguiente conversación que tengáis por otro motivo.

Textos completos en `comunicacion/personas-conocidas.md`.
"""

def ficha(r):
    L = ['# %s' % r['nombre'], '']
    L.append('**Contacto**%s · estado `%s`' %
             (' · ' + r['localidad'] if r['localidad'] else '', r['estado']))
    L.append('')
    L.append('| | |')
    L.append('|---|---|')
    L.append('| Canal | %s |' % (r['canal'] or '—'))
    L.append('| Dónde lo tienes | %s |' % (r['contacto'] or '—'))
    L.append('| ¿Decide sobre una sala? | %s |' % (r['decide_sala'] or '—'))
    L.append('')
    L.append('## De qué os conocéis')
    L.append('')
    L.append(r['relacion'] or '—')
    L.append('')
    L.append('**Ábrele por ahí.** Es lo que convierte el mensaje en una '
             'conversación en vez de en un anuncio.')
    L.append('')
    if r['notas']:
        L.append('## Notas')
        L.append('')
        L.append(r['notas'])
        L.append('')
    L.append(REGLAS)
    L.append('---')
    L.append('')
    L.append('*Generado desde `contactos.csv`. No editar a mano: edita el CSV y '
             'ejecuta `python3 contactos/generar-fichas.py`.*')
    return '\n'.join(L) + '\n'

os.makedirs(DIR, exist_ok=True)
for f in os.listdir(DIR):
    if f.endswith('.md'):
        os.remove(os.path.join(DIR, f))

filas = list(csv.DictReader(io.open(CSV, encoding='utf-8'), delimiter=';'))
idx = ['# Contactos', '',
       'Gente conocida, no centros. Se les escribe distinto: ver '
       '`comunicacion/personas-conocidas.md`.', '',
       'Para consultarlas desde Signal, pídele a Hermes la ficha por el nombre.', '',
       '| Nombre | Canal | ¿Decide sala? | Estado | Ficha |', '|---|---|---|---|---|']
for r in sorted(filas, key=lambda x: x['nombre']):
    s = slug(r['nombre'])
    io.open(os.path.join(DIR, s + '.md'), 'w', encoding='utf-8').write(ficha(r))
    idx.append('| %s | %s | %s | `%s` | `contactos/fichas/%s.md` |'
               % (r['nombre'], r['canal'], r['decide_sala'], r['estado'], s))
io.open(os.path.join(DIR, 'INDICE.md'), 'w', encoding='utf-8').write('\n'.join(idx) + '\n')
print('%d fichas de contacto generadas' % len(filas))
