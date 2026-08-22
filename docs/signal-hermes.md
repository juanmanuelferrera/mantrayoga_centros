# Signal y Hermes

Cómo consultar y anotar cosas del proyecto desde el móvil.

## Consultar una ficha

Pídele a Hermes la ficha por el nombre del centro. Él lee el archivo de
`centros/fichas/`. El índice está en `centros/fichas/INDICE.md`.

> «Dame la ficha de Lloc de Yoga»
> «¿A qué hora abre Prana?»
> «¿Qué centros me quedan pendientes en Elche?»

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

## Fechas de visita: HyperFiler (gtd+h)

Las visitas con fecha van al calendario de **HyperFiler**, que es el sistema GTD.
Hay servidor MCP, así que se crean directamente:

- `hf_create_task` con `title`, `due_date` (YYYY-MM-DD), `due_time` y `notes`.
- `hf_list_tasks` para consultarlas, con filtros de estado, plantilla o fecha.

En las notas de la tarea va lo imprescindible para la visita y la ruta de la
ficha completa, para poder tirar del hilo desde el móvil.

**Nunca en Google Calendar.**

## Regla

Nada se manda al grupo sin que Juan Manuel lo confirme antes. Igual que con los
centros: se prepara, se enseña, y se manda cuando él dice.
