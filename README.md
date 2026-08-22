# Mantra Yoga en centros de yoga de Alicante

Material de trabajo para llevar un taller de mantra yoga de 1 hora a los
centros de yoga de Alicante y comarca. Gratuito para el centro, a donativo,
repetido de forma regular en cada sitio.

Proyecto de **Centros de Bhakti yoga** (entidad no lucrativa, CIF G-76660679,
bhaktiyoga.es).

## Qué hay aquí

| Carpeta | Para qué |
|---|---|
| `docs/` | Estrategia, fases y registro de métricas |
| `dossier/` | El PDF que se envía a los centros |
| `programa/` | El guion del taller: formato fijo y los ocho temas |
| `centros/` | Lista de centros, ficha de cada uno, calendario perpetuo y bitácora |
| `centros/fichas/` | **Una ficha por centro**, generada desde el CSV. Consultable desde Signal con Hermes |
| `contactos/` | **Gente conocida**, con una ficha por persona. No son centros y se les escribe distinto |
| `comunicacion/` | Email, WhatsApp, llamada, objeciones, cartel, Instagram |
| `comunicacion/personas-conocidas.md` | Mensajes para gente que ya conoces, que se escribe distinto |

## Enlaces

| Qué | Dónde |
|---|---|
| Productor de carteles | `comunicacion/cartel/` — edita `cartel.tex` y ejecuta `./build.sh` |
| Copia en línea del productor | https://claude.ai/code/artifact/24fc66da-d47d-49f9-bd61-d96e08a50402 |
| Repositorio | https://github.com/juanmanuelferrera/mantrayoga_centros |
| Web de la entidad | https://bhaktiyoga.es |

## Cómo se usa

1. Abre `centros/centros-alicante.csv` y elige los de prioridad A.
2. Sigue `comunicacion/secuencia-contacto.md`: mandas el email con el material
   anunciando que te pasarás, y a los cuatro o cinco días te presentas en el
   centro. El email prepara la visita; la visita es la que cierra.
3. En la visita cierras una **posición fija** del mes (ver
   `centros/calendario.md`): el segundo jueves, el primer martes. No una fecha
   suelta. Cuando está cerrada, mándale al centro el cartel y el texto de
   Instagram ya hechos.
4. Da el taller siguiendo `programa/formato-taller.md` y el tema de
   `programa/repertorio.md`.
5. Anota lo que pasó en `docs/metricas.md` y actualiza `centros/seguimiento.md`.

## Regla de oro

No se abren centros nuevos mientras los abiertos no se sostengan dos meses
seguidos. Primero que funcione, luego que crezca.
