# Auditoría clínica correctiva: Registro cardiotocográfico intraparto

Registro de la fase de verificación aplicada a `2. RCTG.md`, separada de la redacción. El documento clínico no contiene comentarios sobre su elaboración; este archivo sirve solo para la trazabilidad.

## 1. Fuentes del usuario y su vigencia

| Clave | Fuente | Vigencia |
|---|---|---|
| d1 | UpToDate, Macones: manejo de los registros de categoría I, II y III (literatura hasta mayo de 2025) | Vigente; base de la conducta |
| d2 | UpToDate, Miller: visión general de la monitorización intraparto (literatura hasta mayo de 2025) | Vigente; base de la fisiología, las definiciones y las pruebas auxiliares |
| d3 | ACOG, boletín de práctica 106 (2009) | Sustituido por la guía de práctica clínica n.º 10 de la ACOG (2025); se conserva para la nomenclatura del NICHD, que no cambió |

## 2. Recomendaciones actualizadas o corregidas

| # | Afirmación de la fuente | Corrección | Sección | Fundamento |
|---|---|---|---|---|
| 1 | Oxígeno materno entre las medidas iniciales ante un registro anormal (ACOG 2009) | No se administra de forma sistemática a la parturienta con saturación normal; se reserva para la hipoxemia materna | 8, anexo A | ACOG CPG n.º 10 (2025), recomendación fuerte; ensayos aleatorizados resumidos en d1 |
| 2 | Boletines 106 y 116 como documentos de referencia | Sustituidos por la guía n.º 10 (2025), que mantiene el sistema de tres categorías | 4.1, anexo A | ACOG 2025 |
| 3 | Análisis del segmento ST, pulsioximetría fetal e interpretación computarizada como técnicas en estudio | La ACOG 2025 desaconseja su uso sistemático y que la interpretación dependa principalmente del ordenador | 7.2, anexo A | ACOG 2025 |
| 4 | Sistema de cinco niveles mencionado como propuesta | La ACOG 2025 lo recoge en un apéndice como complemento; la conducta sigue basándose en las tres categorías | 4.3, anexo A | ACOG 2025 |
| 5 | Terbutalina 250 µg subcutánea sin advertencias | Se añaden el uso fuera de indicación y la advertencia de la FDA contra el uso de más de 48 a 72 horas y la tocolisis de mantenimiento. La FDA reconoce el uso hospitalario en situaciones urgentes, al que no se dirige la advertencia | 8, anexo A | Comunicación de seguridad de la FDA, 2011 |

## 3. Discrepancias entre fuentes que se mantienen visibles

- **Frecuencia de la auscultación intermitente sin factores de riesgo:**
  - la ACOG de 2009 indica cada 15 minutos en la fase activa y cada 5 en el segundo periodo;
  - UpToDate indica cada 30 y cada 15 minutos.
  Ambas se exponen en la tabla 1 y en el anexo A, y la conducta remite al protocolo institucional dentro de esos rangos.
- **Umbrales de la FIGO frente a los del NICHD:** la bradicardia y la variabilidad normal tienen límites distintos (por debajo de 100 frente a 110 lpm; de 5 a 25 frente a 6 a 25 lpm). La tabla 4 conserva los de la FIGO y el anexo A advierte que no deben mezclarse.

## 4. Afirmaciones absolutas revisadas

| Afirmación que podía leerse como absoluta | Redacción final |
|---|---|
| La estimulación del cuero cabelludo, "siempre disponible" | "Puede realizarse en cualquier sala de partos" |
| La aceleración tras la estimulación "garantiza" la ausencia de acidemia | Se mantiene "casi siempre garantiza", como en la fuente, junto con la probabilidad: pH menor de 7,20 en menos del 10% si hay aceleración y en el 50% si no la hay |
| La variabilidad mínima o ausente "indica" acidemia | Predice mal la acidemia por sí sola; se enumeran las causas no hipóxicas |
| Un registro intraparto normal "excluye" la lesión prenatal | No la excluye (sección 5) |

Los demás términos absolutos que conserva el texto ("todos" en los criterios de categoría I, "siempre" para precisar si la taquisistolia se acompaña de deceleraciones) proceden de las definiciones del NICHD y de la ACOG y no se modificaron.

## 5. Estadísticas suprimidas por no modificar la conducta

- Razones de momios e intervalos de confianza del metaanálisis de tocolisis aguda frente a cesárea urgente. Se conserva la conclusión: mejoró el equilibrio ácido-base y redujo los ingresos en cuidados intensivos, con beneficio real incierto.
- Razones de verosimilitud de la estimulación digital del cuero cabelludo. Se conserva la probabilidad de pH menor de 7,20 con y sin aceleración.
- Diferencia media del intervalo hasta el parto en ese mismo metaanálisis.

## 6. Imágenes

### Imágenes conservadas

| Archivo | Origen | Descripción verificable |
|---|---|---|
| `rctg_desaceleracion_tardia.jpg` | d2, gráfico 96977 | Título de la fuente: "Late deceleration" |
| `rctg_tardias_recurrentes.jpg` | d2, gráfico 96980 | Título de la fuente: "Recurrent late decelerations" |
| `rctg_tardia_profunda.jpg` | d2, gráfico 96978 | Título de la fuente: "Deep late deceleration" |
| `rctg_posiciones_reanimacion.png` | d1, página 29 | Rótulos de la propia imagen: "All-fours position" y "Knee-chest position" |

### Imágenes sin descripción y su sustitución

Nueve trazados de d1 y d2 (páginas 23, 24, 26 y 27 de d1; 33, 38, 39, 40 y 48 de d2) perdieron su título en la conversión a PDF; la página solo contiene la imagen. El texto cita los trazados por número ("waveform 1" a "waveform 11", "2A" a "2C"), pero el orden de las imágenes no permite asignar cada número con certeza; por ejemplo, varias imágenes se repiten en d1 y en d2, que numeran los trazados de forma distinta. Por eso se retiraron. El logotipo de la ACOG (d3, página 1) también se omitió, porque no tiene contenido clínico.

En su lugar se añadieron cuatro esquemas, generados con `herramientas/esquemas_rctg.py` a partir de los umbrales de la tabla 2 (definiciones del NICHD). Cada pie indica que el esquema no reproduce un registro real.

| Esquema | Parámetros con los que se construyó |
|---|---|
| `rctg_esquema_variabilidad.png` | Amplitud de pico a valle: ausente, cercana a 0; mínima, unos 4 lpm; moderada, unos 15 lpm; marcada, unos 38 lpm |
| `rctg_esquema_temprana_tardia.png` | Contracción de 80 segundos con pico en el segundo 90. Temprana: inicio con la contracción y nadir en su pico, 40 segundos desde el inicio. Tardía: inicio a los 80 segundos, nadir a los 125 y recuperación después del final de la contracción. Ambas son graduales (30 segundos o más hasta el nadir) |
| `rctg_esquema_variable_prolongada.png` | Variable: 12 segundos hasta el nadir (brusca), 55 lpm de profundidad, 52 segundos de duración y hombros previos y posteriores. Prolongada: 50 lpm durante 3,5 minutos |
| `rctg_esquema_sinusoidal.png` | 4 ciclos por minuto y amplitud de 10 lpm de pico a valle; el pie recuerda que la definición exige 20 minutos o más |

## 7. Diseño

- Las viñetas anidadas (actividad uterina, situaciones que simulan hipoxia, ejemplos de categoría II, bolo intravenoso y terbutalina) se convirtieron en párrafos con encabezado en negrita seguidos de un único nivel de viñetas.
- Las tablas llevan un pie numerado con sus referencias. En el PDF, el encabezado se repite en cada página y las tablas cortas no se parten.

## 8. Limitaciones de la verificación

- El entorno impidió abrir directamente las webs de la ACOG, la FDA y PubMed. La verificación se hizo con los resúmenes del buscador web, que remiten a las publicaciones primarias citadas.
- No pudo leerse el texto completo de la guía n.º 10 de la ACOG (2025). Solo se incorporan las recomendaciones confirmadas en los resúmenes (oxígeno, sistema de cinco niveles, análisis del segmento ST, pulsioximetría e interpretación computarizada); la conducta detallada por patrón procede de d1.
- Las dosis de nitroglicerina y terbutalina proceden de d1 y d3; no se contrastaron con las fichas técnicas.
