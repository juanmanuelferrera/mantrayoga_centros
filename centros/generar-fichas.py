#!/usr/bin/env python3
"""Genera una ficha por centro a partir del CSV, en centros/fichas/.

Se regenera entera cada vez, así que el CSV es la única fuente de verdad:
edita el CSV y vuelve a ejecutar esto. Nunca edites una ficha a mano.

Uso:  python3 centros/generar-fichas.py
"""
import csv, io, os, re, unicodedata

BASE = os.path.dirname(os.path.abspath(__file__))
CSV = os.path.join(BASE, 'centros-alicante.csv')
DIR = os.path.join(BASE, 'fichas')

def slug(t):
    t = unicodedata.normalize('NFKD', t).encode('ascii', 'ignore').decode()
    return re.sub(r'-+', '-', re.sub(r'[^a-z0-9]+', '-', t.lower())).strip('-')

PRIORIDAD = {
    'A': 'A — ya hacen meditación, kundalini o talleres. La puerta está medio abierta.',
    'B': 'B — centro generalista, receptivo, sin encaje obvio pero sin barrera.',
    'C': 'C — perfil fitness o encaje dudoso. Al final de la cola.',
}

PLAYBOOK = """
## Cuándo ir

Quince o veinte minutos **antes** de una clase de tarde, o justo **después** de
una de mañana. Hay alguien en recepción y el profesor anda por allí.

Nunca en mitad de una clase. Nunca lunes a primera ni viernes a última.

Mira su horario en la web o el Instagram antes de salir de casa.

## Qué llevas

- Dos copias del dossier impreso, con el nombre del centro y el de la persona
  escritos a mano en la esquina.
- Una hoja del alumno de muestra.
- Nada más. Sin instrumentos.

## Cómo entras

Si escribiste antes:

> "Hola, buenas. Soy Juan Manuel, escribí hace unos días sobre un taller de
> mantra yoga. ¿Está [nombre]? Si es mal momento vuelvo otro día, sin problema."

Si entras en frío:

> "Hola, buenas. Soy Juan Manuel, doy talleres de mantra yoga. ¿Quién lleva el
> centro? Si es mal momento vuelvo otro día, sin problema."

Ofrecer irte tú antes de que te lo digan es lo que baja la guardia.

## Lo que preguntas en los dos primeros minutos

1. ¿Cuánto lleváis abiertos?
2. ¿Qué clase os funciona mejor?
3. **¿Qué franja os cuesta más llenar?** — la respuesta es el hueco que
   propones tú después.

## Cómo cierras

Nunca «¿te interesa?». Siempre por el día, y fijo:

> "Lo que mejor funciona es un día fijo del mes, siempre el mismo, para que la
> gente se lo aprenda. ¿El segundo jueves a las siete os iría?"

Si dice que se lo piensa: "¿Te llamo el [día concreto]?". Fecha concreta o no
hay seguimiento.

Si dice que no: "Sin problema, gracias por el rato." Se anota y se cierra.

## Si no está quien decide

Deja el dossier con su nombre escrito, di cuándo vuelves y vete. **No cuentes
el taller a quien no puede decir que sí.**
"""

def ficha(r):
    L = []
    L.append('# %s' % r['nombre'])
    L.append('')
    L.append('**%s** · prioridad %s · estado `%s`' % (r['localidad'], r['prioridad'], r['estado']))
    L.append('')
    L.append('| | |')
    L.append('|---|---|')
    L.append('| Dirección | %s |' % (r['direccion'] or '—'))
    L.append('| Teléfono | %s |' % (r['telefono'] or '—'))
    L.append('| Email | %s |' % (r['email'] or '—'))
    L.append('| Web | %s |' % (r['web'] or '—'))
    L.append('| Instagram | %s |' % (r['instagram'] or '—'))
    L.append('| Estilo | %s |' % (r['estilo'] or '—'))
    L.append('')
    if not r['telefono'] and not r['email'] and not r['web']:
        L.append('> Sin teléfono, email ni web localizados. La vía es Instagram, '
                 'o presentarse directamente.')
        L.append('')
    L.append('**Prioridad %s.** %s' % (r['prioridad'], PRIORIDAD.get(r['prioridad'], '')))
    L.append('')
    if r['notas']:
        L.append('## Notas de este centro')
        L.append('')
        L.append(r['notas'])
        L.append('')
    L.append('> Los datos que vienen de directorios fallan a menudo: el primer '
             'centro que comprobamos tenía mal el email y el teléfono. '
             'Compruébalos en su web antes de escribir o llamar.')
    L.append(PLAYBOOK)
    L.append('---')
    L.append('')
    L.append('*Generado desde `centros-alicante.csv`. No editar a mano: '
             'edita el CSV y ejecuta `python3 centros/generar-fichas.py`.*')
    return '\n'.join(L) + '\n'

os.makedirs(DIR, exist_ok=True)
for f in os.listdir(DIR):
    if f.endswith('.md'):
        os.remove(os.path.join(DIR, f))

filas = list(csv.DictReader(io.open(CSV, encoding='utf-8'), delimiter=';'))
indice = ['# Fichas de centros', '',
          'Una ficha por centro, generadas desde `centros-alicante.csv`.', '',
          'Para consultarlas desde Signal, pídele a Hermes la ficha por el nombre '
          'del centro: él lee el archivo de esta carpeta.', '',
          '| Centro | Localidad | Prioridad | Estado | Ficha |', '|---|---|---|---|---|']

for r in sorted(filas, key=lambda x: (x['prioridad'], x['localidad'], x['nombre'])):
    s = slug(r['nombre'])
    io.open(os.path.join(DIR, s + '.md'), 'w', encoding='utf-8').write(ficha(r))
    indice.append('| %s | %s | %s | `%s` | `fichas/%s.md` |'
                  % (r['nombre'], r['localidad'], r['prioridad'], r['estado'], s))

io.open(os.path.join(DIR, 'INDICE.md'), 'w', encoding='utf-8').write('\n'.join(indice) + '\n')
print('%d fichas generadas en %s' % (len(filas), DIR))
