# Signal y Hermes

Cómo consultar y anotar cosas del proyecto desde el móvil.

## Consultar una ficha

Pídele a Hermes la ficha por el nombre. Hay dos carpetas y él lee de las dos:

- **Centros:** `centros/fichas/` · índice en `centros/fichas/INDICE.md`
- **Personas conocidas:** `contactos/fichas/` · índice en `contactos/fichas/INDICE.md`

> «Dame la ficha de Lloc de Yoga»
> «¿A qué hora abre Prana?»
> «¿Qué centros me quedan pendientes en Elche?»
> «Dame la ficha de Natasha»

## Mandar un mensaje al grupo Personal

**Cuenta:** `+34687357660`
**Grupo Personal:** `51E6ktm1z/GJUqDL8kJzztdi2RLXnonqy13f0jsZNGs=`

### Ojo: hay un daemon corriendo

Hay un `signal-cli daemon` escuchando en `127.0.0.1:8080` que mantiene la cuenta
bloqueada. **Cualquier `signal-cli` lanzado por separado se queda colgado para
siempre**, sin error y sin salida. No es que vaya lento: es que espera un
bloqueo que no se va a soltar.

Todo va por el JSON-RPC del daemon:

```bash
curl -s -X POST http://127.0.0.1:8080/api/v1/rpc \
  -H 'Content-Type: application/json' \
  -d '{"jsonrpc":"2.0","method":"send",
       "params":{"account":"+34687357660",
                 "groupId":"51E6ktm1z/GJUqDL8kJzztdi2RLXnonqy13f0jsZNGs=",
                 "message":"texto"},
       "id":1}'
```

Para listar grupos, el mismo `curl` con `"method":"listGroups"` y solo
`account` en los parámetros.

## Fechas de visita: GTD+H

Las visitas con fecha van al **GTD+H**, que es el sistema de tareas de Juan
Manuel. Cuando dice «ponlo en Signal», se refiere a esto.

**Archivo:** `~/Library/CloudStorage/Dropbox/Kavya/Horario/gtd-r-308dac3a.md`,
sección `## CALENDAR`.

**Formato:** `- [ ] texto — mar 25 - 17:35`. Día abreviado en español, fecha al
final, hora detrás con guion.

Las reglas completas están en el skill de Hermes `gtph-jaganat`. Léelo antes de
editar el archivo, y edita de forma atómica: leer una vez, escribir una vez.

**Nunca HyperFiler** (ni sus herramientas MCP) **ni Google Calendar.**

## Regla

Nada se manda al grupo sin que Juan Manuel lo confirme antes. Igual que con los
centros: se prepara, se enseña, y se manda cuando él dice.
