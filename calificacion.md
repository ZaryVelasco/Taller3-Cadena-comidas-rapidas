# Taller3-Cadena-comidas-rapidas — Semana 3, Pista A: "El modelo milagroso" 🏢📊

Repo: [github.com/ZaryVelasco/Taller3-Cadena-comidas-rapidas](https://github.com/ZaryVelasco/Taller3-Cadena-comidas-rapidas)
Autores: Juan Felipe Sanchez · Nicolas Sotelo · Zary Velasco

Rúbrica: El contrato funciona contra el conjunto oculto (30% · 1.5 pts) · Honestidad metodológica (20% · 1.0 pt) · Calidad del pipeline (30% · 1.5 pts) · Auditoría + Git (20% · 1.0 pt). Escala final: 0–5. Sin bonus esta semana.

**Nota final: 4.15 / 5.0**

| Contrato vs. oculto | Honestidad metodológica | Calidad del pipeline | Auditoría + Git |
|---|---|---|---|
| 1.5 / 1.5 | 1.0 / 1.0 | 0.95 / 1.5 | 0.7 / 1.0 |

---

### 1. El contrato funciona contra el conjunto oculto — 1.5 / 1.5 ✅
Corrí `python src/predict.py <oculto_features.csv> <salida.csv>` (60 fechas futuras) con Python 3.11 (documentan compatibilidad ≥3.11, desarrollado en 3.14.3). Sin crash, salida idéntica en dos corridas, exactamente `fecha, prediccion` en un rango razonable. El contrato exacto que pide el enunciado funciona.

### 2. Honestidad metodológica — 1.0 / 1.0 ✅
`python src/validar.py` reproduce exactamente lo que dice el README:

```
Entrenado con 158 días, validado con los 40 siguientes
MAE honesto (validación temporal): 10.1 almuerzos
```

Split estrictamente cronológico, sin aleatoriedad, y `validar.py`/`predict.py` construyen las features de forma idéntica y consistente (misma referencia temporal, mismo modelo) — no hay riesgo de que el número reportado no represente lo que hace el contrato real. La metodología en sí es honesta; el MAE más alto que otros modelos revisados esta semana no viene de un problema de honestidad, sino de una decisión de features (ver punto 3).

### 3. Calidad del pipeline — 0.95 / 1.5 ⚠️
**Bien:** `ColumnTransformer` correcto (numéricas escaladas, categórica con `OneHotEncoder`, binaria passthrough). La referencia temporal (`inicio`) se calcula una sola vez y se reutiliza en entrenamiento y predicción, evitando la fuga sutil de la feature de tendencia. Generaron y revisaron la gráfica de la serie completa antes de decidir features, tal como sugiere el enunciado.

**Se bajó nota por:**
- **`llovio` fue excluida del modelo por completo**, pese a ser una de las 6 columnas que el contrato garantiza como entrada. Revisando `src/entrenar.py` (el script original, conservado sin modificar): `llovio` aparece ahí como una feature más, sin ningún comentario que la señale como sospechosa — a diferencia de `ingreso_dia`, que sí tiene la pista explícita ("el ingreso del dia ayuda MUCHISIMO al modelo"). Es decir, el propio material del taller trata `llovio` como legítima; se trata de información de pronóstico (se sabe la noche anterior), no de un dato que se conoce solo al cierre del día. Esta exclusión probablemente explica buena parte de la diferencia entre el MAE de este modelo y el de modelos que sí la usan. **(-0.35)**
- `predict.py` no valida el número de argumentos ni las columnas del CSV de entrada — con datos mal formados, el error sería un traceback crudo (`IndexError`/`KeyError`) en vez de un mensaje claro. **(-0.1)**
- `grafica_6_meses()` guarda la imagen en una ruta relativa (`"Image/grafica_demanda.png"`), no anclada a la ubicación del módulo — solo funciona si `validar.py` se ejecuta desde la raíz del repositorio. **(-0.1)**

### 4. Auditoría + Git — 0.7 / 1.0 ⚠️
**Auditoría:** identifican correctamente las 3 trampas reales (fuga de `ingreso_dia`, escalado antes del split, split aleatorio), con buena explicación de cada una. Sin embargo, la Trampa 1 mezcla la fuga real (`ingreso_dia`) con la exclusión incorrecta de `llovio`, presentando ambas como si fueran del mismo tipo de problema — reduce la precisión de un análisis que, por lo demás, identifica bien las tres trampas oficiales.

**Git:** 10 commits de tres autores (más los de inicialización de la plantilla) a lo largo de varios días, pero la mayoría de los mensajes son genéricos por fase (`Fase 1`, `Fase 2`, `Fase 2`, `Fase 2_creación validar.py`, `Fase 3 - Predict`) sin detalle de qué cambió puntualmente en cada uno.

### Resumen para el equipo
La arquitectura del pipeline y la validación temporal están bien resueltas, y el contrato corre perfecto contra datos nuevos. El punto más importante para revisar antes de la sustentación: `llovio` sí es una feature legítima según el propio `entrenar.py` original (no tiene la marca de sospecha que sí tiene `ingreso_dia`) — inclúyanla y midan de nuevo el MAE honesto, probablemente mejore. También conviene agregar validación de argumentos/columnas a `predict.py` y anclar la ruta de la gráfica a la ubicación del módulo en vez del directorio de trabajo. Para la defensa, tengan clara la distinción entre las 3 trampas oficiales (que sí identificaron bien) y esta decisión adicional sobre `llovio`, que es un tema aparte.
