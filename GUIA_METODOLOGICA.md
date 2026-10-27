# Guía metodológica para los documentos clínicos

Este documento reúne todas las características solicitadas desde la primera versión de *Retinopatías* hasta su versión actual. Es la base obligatoria para elaborar el resto de los temas. *Retinopatías* (`1. RETINOPATÍAS/`) es el documento de referencia que la cumple.

---

## 1. Rol, objetivo y principio rector

- **Rol:** médico especialista del área, analista de documentación clínica y editor científico.
- **Objetivo:** convertir las fuentes del usuario en material fiable que sirva de dos formas: como **aprendizaje progresivo del razonamiento clínico**, leído de principio a fin, y como **documento de consulta**.
- **Contenido esperado:** el documento debe permitir comprender los mecanismos, reconocer las manifestaciones, interpretar los hallazgos, diagnosticar, clasificar la gravedad y fundamentar las decisiones terapéuticas.
- **Principio rector:** las fuentes del usuario deciden **qué** se estudia; la verificación externa decide **si es correcto**; la organización clínica decide **cómo** se presenta.
  - La exhaustividad no autoriza a añadir temas ajenos.
  - La claridad no justifica omitir datos.
  - La actualización no debe desplazar el contenido de estudio.
- **Prioridades, en este orden:**
  1. fidelidad documental;
  2. exactitud clínica verificada;
  3. exhaustividad;
  4. organización clínica;
  5. claridad causal;
  6. densidad sin redundancia;
  7. trazabilidad discreta.

## 2. Fuentes, verificación y corrección

### 2.1 Fuentes principales

- **Ubicación:** las fuentes están en `PDF_CONVERTED/N. TEMA.md`. Las imágenes están dentro de `PDF_CONVERTED/N. TEMA.pdf`; cada página contiene una imagen y el índice del PDF guarda su nombre original.
- **Lectura íntegra:** se examina todo, incluidos anexos, tablas, algoritmos, glosarios e imágenes.
- **Información dispersa:** se recupera aunque esté repartida entre documentos.
- **Elementos que se conservan:** definiciones, clasificaciones, criterios, valores, dosis, indicaciones, contraindicaciones y excepciones.
- **Inventario previo:** antes de redactar se hace un inventario interno de los subtemas.
- **Expansión proactiva:** se integra la información relacionada que las fuentes documentan, como los criterios diagnósticos o las complicaciones que condicionan un tratamiento. Nunca se introduce conocimiento ajeno.

### 2.2 Verificación externa (activada por defecto)

- **Finalidad:** comprobar, precisar o corregir. Nunca sirve para ampliar el temario.
- **Jerarquía de fuentes:**
  1. guías oficiales vigentes;
  2. consensos de sociedades;
  3. revisiones especializadas;
  4. revisiones sistemáticas y estudios de calidad;
  5. textos de referencia y fichas técnicas.
- **Contexto nacional:** se consideran las normas nacionales (guías IMSS y NOM) cuando el contexto lo requiere.
- **Qué se verifica:** definiciones, criterios, umbrales, dosis, vías, indicaciones, contraindicaciones, criterios quirúrgicos y recomendaciones posiblemente desactualizadas.
- **Correcciones con impacto:** toda corrección que cambie una conducta lleva una cita identificable.
- **Límites de la verificación:** se registran en `AUDITORIA.md`. En este entorno el acceso directo a webs está bloqueado y solo funciona el buscador. Por eso:
  - se citan las publicaciones primarias;
  - no se afirma haber leído un texto que no se leyó;
  - no se inventan DOI, páginas ni enlaces.

### 2.3 Tratamiento de errores

| Tipo | Acción |
|---|---|
| Error de sintaxis, ortografía o traducción | Se corrige directamente |
| Error de transcripción u OCR | Se restaura desde el original; si no es recuperable, se conserva la incertidumbre |
| Error médico verificable | Se corrige con una referencia externa y se cita |
| Información incompleta | Se busca primero en las demás fuentes; después, en las externas solo para precisar |
| Discrepancia entre fuentes | Se identifica si se debe a un contexto, una versión o una contradicción real; no se fabrican consensos |
| Recomendación desactualizada | Se contrasta con la vigente y se indica la conducta actual; la histórica pasa a un anexo |
| Dato no verificable | Se conserva sin inventar ni completar |

### 2.4 Datos que no se completan por suposición

- **Esquemas farmacológicos y dosis ausentes:** no se completan.
- **Algoritmos ilegibles:** no se reconstruyen.
- **Fotografías sin descripción en la fuente:** no se describen por inferencia. Se sustituyen por imágenes cuyo contenido esté descrito o sea verificable en las fuentes, o se omiten.

## 3. Organización modular

Se usan los módulos pertinentes, en el orden clínico más útil, y nunca para rellenar una estructura.

| Módulo | Contenido |
|---|---|
| A. Fundamentos | Definición, anatomía y fisiología necesarias para entender las alteraciones |
| B. Etiología y fisiopatología | Secuencia causal: desencadenante, cambio, progresión, alteración tisular, manifestación y complicación. Cada mecanismo se enlaza con el signo que produce |
| C. Clínica y semiología | Síntomas, signos, evolución y hallazgos de gravedad, cada uno con su mecanismo y significado |
| D. Clasificación | Todas las categorías y criterios exactos, con su implicación. No se mezclan sistemas; las equivalencias se marcan como aproximadas |
| E. Diagnóstico | Sospecha, exploración, estudios, criterios confirmatorios, gravedad y diferencial. Se distingue el cribado de la confirmación |
| F. Tratamiento | Para cada intervención: indicación, mecanismo, técnica o dosis y precauciones, en ese orden |
| G. Complicaciones, pronóstico y seguimiento | Por qué ocurren, cómo se detectan y qué conducta requieren |
| H. Integración | Algoritmo de decisiones, comparación entre entidades y criterios de referencia |

**Estructura fija de anexos (cuando aplique):**

1. **Atlas visual:** conjuntos extensos de fotografías estándar o de láminas.
2. **Tablas extensas de consulta:** equivalencias entre sistemas y plazos institucionales.
3. **Discrepancias normativas con implicación clínica:** tema, posición institucional, recomendación posterior verificada e implicación.
4. **Esquemas institucionales e históricos:** tablas, listas de verificación y algoritmos antiguos, conservados íntegros y señalados como no vigentes cuando corresponda.

**Jerarquía terapéutica:** el cuerpo del documento se construye sobre las recomendaciones **vigentes verificadas**. Las tablas y algoritmos históricos pasan al anexo y no compiten visualmente con la conducta actual. El texto, las tablas y el algoritmo deben representar el mismo contexto temporal.

## 4. Redacción médica explicativa de alta densidad

1. **Continuidad causal:** se usan oraciones completas con conectores precisos ("debido a", "lo que ocasiona", "por lo tanto", "cuando afecta"). No se encadenan conceptos ni se usan flechas.
2. **Jerarquía informativa:** primero el concepto o criterio, después el mecanismo o la justificación y al final la implicación clínica. No se presenta un valor o una clasificación sin explicar antes su finalidad.
3. **Formatos según la función:**
   - **Prosa:** para mecanismos, evolución y relaciones. Se cambia de párrafo cuando cambia el mecanismo o la decisión.
   - **Viñetas:** para criterios, categorías, indicaciones y conductas. Cada viñeta expresa una idea clínica completa; se usa un solo nivel, y el segundo solo cuando una subdivisión es imprescindible.
   - **Tablas:** solo para comparar o consultar, con celdas breves. Las explicaciones extensas van al texto inmediato.
4. **Sin redundancia funcional:** la primera aparición explica por completo; las siguientes solo recuperan lo necesario. En el tratamiento:
   - la tabla compara;
   - los apartados por intervención explican;
   - el algoritmo da únicamente la secuencia.
5. **Integración inmediata:** se evita obligar a consultar otros apartados para entender un concepto. Las remisiones internas se usan solo para ampliar.
6. **Valores con interpretación:** cada cifra lleva su significado clínico, sus unidades y sus condiciones.
7. **Afirmaciones prudentes:** se revisa cada "siempre", "nunca", "solo", "único", "no existe", "primera línea", "obligatorio" o "sin posibilidad". Se mantienen solo si son correctas y verificadas.
8. **Siglas:**
   - hay un glosario breve al inicio;
   - cada sección desarrolla los términos en su primera mención;
   - se limita la acumulación de siglas, y dentro de las tablas se escriben las categorías completas;
   - en los esquemas terapéuticos se identifica cada componente antes de usar su sigla.
9. **Estadísticas:** se conservan las que cambian la conducta (prevalencia que justifica el cribado, riesgo de progresión, beneficio terapéutico relevante, umbrales e intervalos). Se omiten tamaños muestrales, OR, RR, IC, valores p y datos históricos sin implicación práctica.
10. **Sin metacomentarios en el documento clínico:** no hay preámbulos, conclusiones genéricas, notas sobre el proceso, etiquetas como "[Nota de fuente]" o "[Complemento]", ni frases que anuncien lo que viene. El documento empieza con el contenido y termina con las referencias.
11. **Contraste normativo:** se distingue entre conocimiento establecido, criterio de una clasificación, recomendación institucional, conducta histórica y recomendación vigente. La aclaración es breve en el lugar pertinente y el detalle va al anexo de discrepancias.

## 5. Referencias y trazabilidad

- **Formato en el Markdown:** notas al pie de Markdown (`[^clave]`) al final de los párrafos, de los grupos de viñetas o de los títulos de tabla. Nunca van tras cada oración, en los encabezados ni como línea aislada.
- **Claves:** las fuentes del usuario usan `d1…dN` y las externas una clave descriptiva (`ada`, `aao`, `protS`…).
- **Bibliografía final:** las referencias aparecen completas al final, en estilo Vancouver, sin datos inventados.
- **En el PDF:** las notas se convierten en superíndices numerados por orden de aparición, sin duplicados, y la lista numerada va al final (la conversión la hace `herramientas/preparar_md.py`).

## 6. Imágenes, tablas y algoritmos

- **Imágenes:**
  - Se extraen las imágenes originales del PDF de cada tema con `herramientas/extraer_imagenes.py` y se guardan en `N. TEMA/assets/`, con nombres ASCII descriptivos y rutas relativas.
  - Se usa JPEG de calidad 92–93 para fotografías y PNG para esquemas y algoritmos.
- **Ubicación:** cada figura va junto al concepto que ilustra y lleva un pie breve, clínico y verificable.
  - No se usan imágenes sin pie descriptivo ni duplicados.
  - No se añaden flechas ni marcas.
  - Las láminas compuestas con texto incrustado ilegible se recortan en fotografías individuales sin alterar su contenido, y su texto pasa al pie.
- **Sustitución de imágenes sin descripción:** se buscan primero imágenes descritas en las demás fuentes del usuario. Si no las hay y el concepto se define por umbrales objetivos (por ejemplo, los patrones del RCTG), se genera un esquema con un script en `herramientas/`, construido solo con los valores de la definición citada. El pie dice que el esquema no reproduce un caso real, y la auditoría registra los parámetros usados.
- **Atlas:** los conjuntos extensos de fotografías van a un anexo de atlas en dos columnas, con remisiones desde el texto.
- **Tablas:** cada tabla lleva un título en negrita del tipo **"Tabla N. …"** que incluye sus referencias. Las celdas son breves, sin explicaciones fisiopatológicas extensas.
- **Algoritmos:**
  - Se conservan todos sus puntos de decisión y se verifica su lectura contra la imagen original.
  - No se añaden pasos.
  - Si un algoritmo histórico contradice la conducta vigente, se conserva en el anexo de esquemas históricos y el cuerpo recoge el algoritmo integrado actual.

## 7. Diseño editorial del PDF

Se aplica con `herramientas/estilo.css` y `herramientas/postprocesar_html.py`.

- **Texto principal:** 11,25 pt, con interlineado de 1,42.
- **Tablas:** 9,75 pt, con encabezado repetido en cada página; las tablas de hasta 14 filas no se parten.
- **Página:** formato carta, con márgenes de 18–19 mm y pie de página con el título y la numeración.
- **Títulos:** separación amplia antes de cada sección; los anexos y las referencias empiezan en página nueva.
- **Figuras:** de hasta 88 mm de alto. Las del atlas van en dos columnas: el pie de las fotografías estándar empieza por "Foto estándar".
- **Compilación:** `herramientas/compilar_pdf.sh "N. TEMA" "Título del pie"`.

## 8. Auditoría clínica final (fase independiente de la redacción)

Cada tema termina con una revisión separada que se registra en `N. TEMA/AUDITORIA.md`. La revisión comprueba:

1. **Afirmaciones absolutas:** todas se revisan.
2. **Contradicciones internas:** entre capítulos, tablas, algoritmos y figuras.
3. **Datos críticos:** criterios, dosis, contraindicaciones, indicaciones y umbrales se verifican uno por uno.
4. **Coherencia temporal:** el texto, las tablas y los algoritmos deben representar la misma conducta y el mismo momento normativo.
5. **Integridad técnica:** todas las notas están definidas y usadas, todas las imágenes existen y se usan, y no hay referencias aisladas.
6. **Legibilidad:** cada sección se entiende leída de forma consecutiva, sin consultar apartados anteriores para descifrar siglas o criterios.

El registro de auditoría recoge las correcciones con su fundamento, las afirmaciones reformuladas, las estadísticas suprimidas y los límites de la verificación.

## 9. Entregables y flujo de trabajo por tema

**Entregables:**

```
N. TEMA/
  N. TEMA.md        documento clínico editable
  N. TEMA.pdf       exportación con todas las figuras
  AUDITORIA.md      registro de verificación y cambios
  assets/           figuras con nombres descriptivos
```

**Flujo de trabajo:**

1. Limpiar la fuente para leerla: `python3 herramientas/limpiar_fuente.py "PDF_CONVERTED/N. TEMA.md" <salida>`.
2. Leer íntegramente la fuente limpia y elaborar el inventario de subtemas.
3. Extraer las imágenes y revisar las candidatas, con su pie de origen en el `.md` fuente.
4. Verificar externamente los datos críticos y las recomendaciones posiblemente desactualizadas.
5. Redactar el `.md` según las secciones 3 a 6.
6. Compilar el PDF y revisar visualmente varias páginas.
7. Hacer la auditoría y documentarla en `AUDITORIA.md`.
8. Hacer commit y push del tema y actualizar `PROGRESO.md`. En los temas largos, guardar también los avances parciales.

## 10. Lecciones aprendidas en Retinopatías

Son errores que deben vigilarse en todos los temas.

- **Afirmaciones absolutas heredadas de las fuentes:** por ejemplo, "su presencia indica presión normal" o "los corticoides son de primera línea en pseudofáquicos".
- **Errores anatómicos copiados de una fuente que contradicen otra sección:** por ejemplo, decir que las arteriolas carecen de capa media.
- **Afirmaciones sobre efectos adversos invertidas:** por ejemplo, que el láser "conserva" el campo visual periférico.
- **Umbrales que difieren entre guías:** se resuelven con el criterio original verificado y la discrepancia se explica.
- **Algoritmos de las fuentes leídos sin mirar la imagen:** produjeron dos errores de asignación de ramas, de modo que siempre se cotejan con la figura.
- **Recomendaciones históricas presentadas como conducta principal:** se corrigen con la estructura del anexo de esquemas históricos.
- **Listas de fármacos autorizados:** se desactualizan pronto y deben verificarse.
- **Situaciones de emergencia descritas sin contexto asistencial:** deben indicar el lugar de atención, la monitorización, el ritmo de tratamiento y la evaluación del daño agudo.

## 11. Lecciones aprendidas en RCTG

- **Reemplazos en bloque del archivo .md:** un recorte entre dos anclas eliminó dos secciones completas. Después de cada sustitución automática se comprueba la lista de encabezados (`grep -n "^#"`) antes de compilar.
- **Viñetas anidadas:** reaparecen al redactar listas de criterios. Antes de compilar se buscan con `grep -n -E "^  +[-*] "` y se convierten en un párrafo con encabezado en negrita seguido de un único nivel.
- **Boletines sustituidos:** se comprueba si el documento normativo de la fuente tiene una versión posterior (ACOG 2009 y 2010, sustituidos por la guía de 2025) y los cambios pasan al cuerpo y al anexo de discrepancias.
- **Advertencias regulatorias:** se citan con su alcance exacto. Por ejemplo, la advertencia de la FDA sobre la terbutalina se refiere al uso prolongado, no al uso hospitalario urgente.

## 12. Lecciones aprendidas en Propedéutica obstétrica y control prenatal

- **Páginas de guías convertidas en imagen:** el limpiador descarta por defecto los bloques OCR. Si la fuente tiene páginas enteras en imagen, se limpia con `--ocr 300` y se comprueba qué páginas faltan comparando la numeración de las imágenes con el texto. Las recomendaciones de páginas perdidas se recuperan de la cédula de recomendaciones clave de la GPC.
- **Orden de las imágenes extraídas:** el orden del PDF no es el orden lógico (las maniobras de Leopold salieron como 1.ª, 3.ª, 2.ª y 4.ª). Cada imagen se identifica por su contenido contra una descripción verificada.
- **Imágenes de tablas:** si una imagen de tabla está desalineada o contiene errores, se reconstruye como tabla Markdown con la correspondencia correcta y se registra en la auditoría.
- **Anchos de columna:** en las tablas con celdas largas, la línea separadora se escribe con guiones proporcionales al ancho deseado (por ejemplo `|------------|------------------|------------------------------------|`), porque pandoc reparte el ancho según esa línea.
- **Algoritmos:** las figuras cuyo pie empieza por "Algoritmo" se muestran a todo el ancho (clase `wide`), porque a menor tamaño su texto no se lee.
- **Normas oficiales con errores en apéndices:** las tablas normativas también se verifican (por ejemplo, el apéndice K de la NOM-007 mezcla las curvas de 75 g y de 100 g).
