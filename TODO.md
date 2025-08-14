# TODO — LPQM (Lenguaje de Proyección Cuántica Multidireccional)

Este archivo resume las tareas pendientes y en progreso del proyecto.

---

## 🔹 Tareas abiertas

### 1. Visualización del colapso y dispersión
- **Objetivo:** Mostrar gráficamente la transición onda → partícula (`→P`) y partícula → onda (`→W`).
- Opciones: Visualización ASCII o con librerías gráficas (`matplotlib`, `pygame`).
- Integrar con el simulador `simulator.py`.
- **Relacionado con Issue:** #1

---

### 2. Ampliar ejemplos en README
- Incluir explicación paso a paso del ejemplo actual (`examples/duality_basic.lpqm`).
- Agregar un ejemplo extra modificando parámetros de ruido y entorno.
- Incluir capturas de pantalla o GIFs del simulador en ejecución.
- **Relacionado con Issue:** #2

---

### 3. Módulo de “colapso condicionado”
- Crear funciones `→P_evento` y `→W_evento` que se activen por condiciones externas.
- Ejemplo: evento si `temperatura > X`.
- Integrar al simulador actual.
- **Relacionado con Issue:** #3

---

## 🔹 Ideas futuras
- Implementar gramática inicial de LPQM (parser básico).
- Agregar simulaciones con tablero geométrico de nodos y vibras.
- Configuración de ruido suave/agresivo parametrizable por espectro (1/f, blanco).
- Integrar visualización 2D interactiva.
- Publicar documentación más extensa en `docs/`.

---

## 🔹 Estado general
- Versión actual: **v0.1.0** (Prototipo inicial)
- Licencia: **Apache 2.0**
- Código de conducta: **Contributor Covenant v2.1**
- Última actualización: *(indicar fecha cuando actualices)*
