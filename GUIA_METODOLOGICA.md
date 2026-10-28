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
6. Comprobar la integridad con `python3 herramientas/verificar_tema.py "N. TEMA"` (notas, imágenes, viñetas anidadas, flechas, remisiones a secciones y numeración de tablas), compilar el PDF y revisar visualmente varias páginas (`herramientas/hojas_contacto.py` genera hojas de contacto).
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

## 13. Lecciones aprendidas en Enfermedades hipertensivas del embarazo

- **Algoritmos vectoriales de las GPC:** no se extraen como imagen (solo salen fragmentos de pocos cientos de píxeles). No se reconstruyen; se transcriben únicamente los recuadros que el OCR deja legibles, se señala en el anexo que el algoritmo está incompleto y la secuencia vigente va en la sección de integración.
- **Páginas perdidas en revisiones extensas:** se comprueba la continuidad de la numeración de páginas del artículo en la fuente limpia; si faltan páginas, no se completa su contenido y se registra en la auditoría.
- **Cuadros de las GPC copiados de otras guías:** pueden introducir errores al traducir (la preeclampsia sobreagregada "antes" de la semana 20, las "complicaciones adversas o severas", la PA colocada en la fila del sistema nervioso). Se cotejan con la guía original de la que proceden y con el texto de la propia GPC.
- **Contradicciones entre la tabla de evidencias y la cédula de una misma GPC:** se elige la cifra coherente con el resto de la conducta y se registra la contradicción en la auditoría.
- **Fichas del cuadro básico:** son generales y pueden contradecir el uso obstétrico (dilución del sulfato de magnesio, contraindicaciones); se transcriben en el anexo con una nota de lectura y el cuerpo sigue el esquema obstétrico.
- **Mecanismos y justificaciones propias:** al redactar es fácil añadir explicaciones fisiológicas o farmacológicas ciertas pero ausentes en las fuentes (mecanismo del ácido acetilsalicílico, distensión de la cápsula de Glisson). Antes de compilar se relee cada "porque" y se retira el que no esté respaldado por una fuente citada.

## 14. Lecciones aprendidas en Aborto

- **Tablas muy anchas:** una tabla de 12 columnas hizo que el navegador redujera toda la página (el PDF bajó de 55 a 29 páginas con letra pequeña). Si el número de páginas o el tamaño de letra cambian sin motivo, se busca la tabla más ancha y se reorganiza (por ejemplo, filas por categoría y una columna con la lista de elementos).
- **Listas de contraindicaciones institucionales:** pueden mezclar contraindicaciones verdaderas, precauciones y condiciones distintas en una misma frase ("trastorno hemorrágico (porfiria hereditaria)"). Se cotejan con la ficha técnica del fármaco y con una guía especializada, y se presenta la clasificación verificada junto a la de la fuente.
- **Apuntes del usuario anotados:** los subrayados y resaltados tapan texto y producen imágenes que solo contienen líneas; esas imágenes se descartan y el texto oculto no se completa.
- **Contenido legal:** cambia más rápido que el clínico. Se buscan las resoluciones judiciales y reformas posteriores a la norma de la fuente; si las cifras publicadas difieren (número de entidades), se cita la fuente más completa, se registra la diferencia en la auditoría y se indica consultar la ley vigente.
- **Listas numeradas:** el margen izquierdo de `estilo.css` cortaba la primera cifra de las referencias 10 en adelante; se amplió. Los temas compilados antes del cambio deben recompilarse.

## 15. Lecciones aprendidas en Hemorragia de la segunda mitad del embarazo

- **Temas con varias guías:** cuando un tema reúne guías de distintos años, se fija primero cuál es la más reciente en cada punto (el ácido tranexámico pasó de "sin recomendación" en 2017 a recomendado en 2021) y se busca si alguna guía internacional posterior cambió la conducta (la OMS 2023 en la medición de la pérdida).
- **Tablas de la evidencia a la recomendación (GRADE):** conservan el tipo de recomendación, pero no su texto. Si se pierden las páginas de recomendaciones, el texto se recupera de la cédula de verificación y no se reconstruye a partir del tipo.
- **Cifras de subgrupos o de poblaciones especiales:** un efecto llamativo puede proceder de un subgrupo (la albúmina del estudio SAFE en la sepsis grave) o de una población seleccionada (el riesgo de acretismo por número de cesáreas en mujeres con placenta previa). Se coteja con el estudio original antes de usarlo y se precisa la población.
- **Unidades y diluciones:** se recalculan las diluciones y los ritmos de infusión, y se revisan las unidades de tiempo y de calibre ("mL/kg/minuto" por "por hora", "mUI/mL" por "mUI/min", "14 fr" por "14 G").
- **Ediciones de tablas clásicas:** la tabla numérica del choque del ATLS corresponde a la 9.ª edición; la 10.ª la sustituyó por tendencias. Se cita la edición de la que procede la tabla reproducida.
- **Esquemas generados:** la letra debe tener al menos 10 puntos en la figura, porque al ajustarse al ancho de la página se reduce casi a la mitad; se revisa cada esquema en la página compilada.
- **Remisiones a figuras:** la compilación no numera las figuras, de modo que no se escriben remisiones del tipo "(figura 1)". `herramientas/verificar_tema.py` ahora detecta estas remisiones y las que apuntan a tablas o secciones inexistentes, también en plural.

## 16. Lecciones aprendidas en Trabajo de parto

- **Fuentes de otros temas:** una norma que está entre las fuentes de otro tema (la NOM-007 en el tema 3) se usa cuando regula el tema actual; se cita como fuente del usuario e indicando de qué tema procede.
- **Unidades de las tablas:** se comprueban sumando o integrando los valores contra los totales que da la misma fuente (el cuadro de dilatación rotulado "cm/h" solo cuadraba como horas por centímetro).
- **Figuras repartidas entre páginas:** cuando la conversión divide una figura en dos imágenes, se unen calculando la alineación por la continuidad de los bordes y se comprueba la unión a simple vista.
- **Figuras altas:** con la altura máxima de 88 mm, una figura vertical con muchos paneles queda ilegible; se divide en láminas por filas, cada una con su pie.
- **Normas obligatorias frente a guías:** cuando la NOM y la GPC difieren (partograma, frecuencia de los tactos y de los signos vitales), el cuerpo presenta ambas y aclara que la NOM es de cumplimiento obligatorio.

## 17. Lecciones aprendidas en Cáncer cervicouterino

- **Figuras perdidas que el texto describe:** si la fuente explica una figura perdida con detalle (paneles, convención de colores o tramas), se genera el esquema con esa misma convención y el pie dice que sustituye a la figura de la fuente y que no reproduce un caso real.
- **Clasificaciones superadas que organizan el tratamiento:** cuando una guía trata por etapas de una clasificación anterior (FIGO 2009), el cuerpo describe la clasificación vigente, explica la equivalencia entre ambas y conserva el tratamiento con las etapas de la guía; la tabla antigua pasa al anexo C.
- **Cifras de ensayos citados:** se comprueba el orden de las comparaciones contra el ensayo original (la GPC invertía los resultados de Peters) y la interpretación de los indicadores de exactitud (una especificidad presentada como valor predictivo negativo).
- **Estimados incoherentes:** si un riesgo relativo no cabe en su intervalo, se informan solo las proporciones absolutas y se registra el error en la auditoría.
- **Letra de los esquemas anchos:** un esquema de cuatro paneles en fila se reduce al 82% del ancho de la página; con 12 puntos quedaba por debajo de 7 en el PDF, de modo que se usan 15 puntos.

## 18. Lecciones aprendidas en Cáncer de mama

- **Figuras de exploración con pie impreso:** cuando la fuente muestra dibujos de técnica con su pie dentro de la imagen, se recortan las franjas de texto de la página, se conserva el pie impreso como identificación y se agrupan en láminas por maniobra; se omiten los duplicados (el mismo dibujo con otro pie) y los dibujos sin rótulo.
- **Algoritmos conservados como fragmentos de texto:** solo se reconstruyen en prosa los pasos que se leen sin ambigüedad, y se dice cuál algoritmo se omitió y por qué.
- **Normas frente a guías en el tamizaje:** si la GPC propone varios intervalos que no coinciden entre sí, el cuerpo los presenta y adopta la NOM de cumplimiento obligatorio, con la guía internacional más reciente como referencia.
- **Cifras de metanálisis citadas como "veces":** se comprueba si la fuente original da riesgos relativos o incidencias; la GPC presentaba como "1,2 veces" una incidencia del 1,2%.
- **Afirmaciones atribuidas a sociedades:** se coteja lo que la GPC atribuye a una sociedad (la ACS) con la guía de esa sociedad.

## 19. Lecciones aprendidas en Choque anafiláctico y RCP

- **Fuentes que son resúmenes de una guía mayor:** cuando la fuente del usuario resume una guía (los Aspectos destacados de la AHA), se comprueba si la guía completa se actualizó después (AHA 2025) y las diferencias van al anexo B, sin reescribir el cuerpo con la versión no verificada en su texto original.
- **Fuentes que cubren solo parte del tema:** si la fuente trata el diagnóstico y no el tratamiento, el tratamiento se completa con guías internacionales y se declara en la auditoría, no en el cuerpo.
- **Límite de búsquedas:** lo que no se pudo verificar en línea se registra expresamente en la auditoría como no comprobado.
- **Figuras divididas en fragmentos que no encajan:** si la alineación no es segura, la figura se transcribe en el texto en lugar de componerla.
- **Ramas de otros autores en la misma rama de trabajo:** antes de subir, si el envío se rechaza, se revisan los commits remotos y se integran con un merge cuando no tocan los mismos archivos.

## 20. Guías prácticas para la ECOE

Las guías ECOE son un segundo entregable por tema, distinto del documento clínico. Preparan una estación de consulta de primer o segundo nivel, de pregrado, que parte de un caso clínico. Se estudian en dos días, de modo que se organizan para la eficiencia sin perder exhaustividad. Siguen vigentes todas las reglas de redacción de la sección 4: oraciones completas, sin flechas, sin viñetas anidadas, sin metacomentarios y con referencias en notas al pie.

**Fuentes y prioridad.**

- **La rúbrica decide qué se califica.** Está en `RUBRICAS/RUBRICAS_ECOE_VI.pdf` e incluye las prácticas 1, 4, 8, 9 y 11 y la de RCP intrahospitalaria. Se cita como fuente (`rub`).
- **El documento clínico del tema y sus fuentes aportan el contenido.** Lo que la rúbrica pide y las fuentes no contienen se verifica externamente.
- **Lo que no se usa como referencia:** las guías ECOE elaboradas en otras sesiones.
- **Qué se desarrolla y qué no:** se desarrolla por completo lo que la rúbrica califica y lo que decide la conducta en primer y segundo nivel (diagnóstico, escalas y clasificaciones, estudios, tratamiento y referencia). Lo especializado se nombra en una frase en la sección de segundo plano.

**Estructura.**

1. La estación y su rúbrica: tabla con cada criterio, la respuesta esperada y la sección que lo resuelve; reglas de acreditación y criterios eliminatorios, con su consecuencia aritmética.
2. Secuencia de la consulta en el orden de la rúbrica.
3. Interrogatorio y exploración, con tablas de "qué se pregunta" y "para qué sirve".
4. Conceptos que se preguntan de forma directa, cada uno con la frase de respuesta.
5. Clasificaciones completas, recitables en el orden en que se dicen.
6. Estudios, tratamiento, prevención y referencia, con la utilidad de cada estudio.
7. Casos para ensayar en voz alta y preguntas directas con respuesta modelo.
8. Lista de respuestas de la rúbrica que conviene precisar: la respuesta que califica la rúbrica, su precisión vigente y cómo decir ambas en una frase.
9. Contenido de segundo plano y plan de estudio de dos días.

**Tablas.** En las guías ECOE solo se usa la tabla de criterios de la rúbrica (una por estación). El resto de la información (siglas, criterios, escalas, fármacos, precisiones, plan de estudio) va en párrafos o en listas de un solo nivel. Una tabla adicional solo se admite si da una ventaja imposible de obtener con otro formato, y la auditoría registra el motivo.

**Archivos.** Los archivos van en `N. TEMA/ECOE/`: la guía (`GUIA_ECOE_<TEMA>.md`), su PDF, `AUDITORIA_ECOE.md` y `assets/` para las figuras nuevas. Las figuras del tema se reutilizan con rutas `../assets/`.

**Herramientas.**

- Se compila con `herramientas/compilar_pdf.sh "N. TEMA/ECOE" "<pie>" GUIA_ECOE_<TEMA>`.
- Se verifica con `python3 herramientas/verificar_tema.py "N. TEMA/ECOE" GUIA_ECOE_<TEMA>.md`.
- Una figura ancha se marca con `{.ancho}` después de la imagen para que ocupe todo el ancho de la página.

### 20.1 Lecciones aprendidas en la guía ECOE de cáncer cervicouterino

- **Criterios eliminatorios:** se calcula su peso. En la práctica 9, no saber Bethesda deja como máximo 9 de los 11 puntos necesarios, por lo que la guía le da prioridad en el plan de estudio.
- **Respuestas de la rúbrica superadas:** no se corrigen en silencio. La rúbrica pedía la vacuna bivalente o tetravalente en dos o tres dosis, y el tratamiento quirúrgico de una "IB2" que solo es quirúrgica con la FIGO 2018. Se enseña a decir la respuesta esperada y, en la misma frase, la precisión vigente.
- **Referencias sin autor identificado:** se citan por institución o por título, sin completar autores. Un borrador inventó un autor para la triple toma; se detectó al revisar las referencias y se sustituyó.
- **Notas que agrupan varias fuentes sin datos editoriales:** no se admiten. Se separan en referencias identificables o se retiran.
- **Imágenes que la estación muestra y no se pueden verificar** (el frotis de carcinoma epidermoide): se sustituyen por una tabla de rasgos y una respuesta modelo.
- **Figuras con muchos paneles:** con 15 puntos y 10 pulgadas de ancho, la letra quedaba en unos 8,6 puntos al 82% del ancho de la página; con la clase `ancho` sube a unos 10,5.
- **Navegación del PDF:** con `ENLACES=1` antes de `compilar_pdf.sh` se añaden índice, marcadores, enlaces a secciones y tablas, regreso de cada referencia a su primera cita y un botón "Índice" en cada página (`enlaces_html.py` y `boton_indice.py`). Un botón de "regresar al último sitio" no funciona en Vista Previa de Mac, que no ejecuta esas acciones; ahí se usa Cmd + [.

### 20.2 Lecciones aprendidas en la guía ECOE de cervicovaginitis

- **Fechas de la rúbrica:** se recalculan siempre. La FPP de la rúbrica (07/03/2024) sale de contar 280 días e incluye el 29 de febrero; la regla de Naegele da el 8 de marzo. La guía enseña a decir ambas.
- **Temas añadidos a la rúbrica:** solo se añaden los que hacen falta para cumplir un criterio (datos de alarma, cálculo obstétrico) o para no dañar a la paciente (tratamientos vigentes en el embarazo). Se registran en la auditoría con su motivo.
- **Tratamientos de la rúbrica sin respaldo en guías** (nitrofurazona): se transcriben como respuesta de la rúbrica y se dice expresamente que no figuran en las guías revisadas, sin inventar un esquema alternativo.
- **Factores de riesgo de la rúbrica con evidencia débil:** se conservan en la tabla con una columna de respaldo, para que el alumno empiece por los sólidos.
- **Secciones que repiten tablas:** se eliminan antes de compilar.

### 20.3 Lecciones aprendidas en la guía ECOE de trabajo de parto

- **Estaciones de procedimiento:** la guía se organiza por bloques de la técnica (preparación estéril, campo, expulsivo, alumbramiento y cierre). Cada paso se escribe como una acción que se anuncia en voz alta, porque el evaluador califica lo que ve y lo que oye.
- **Pasos sin fuente clínica verificable** (asepsia "en calzoncillo", orden de los campos): se transcriben de la rúbrica y se citan como tal, sin inventar un respaldo.
- **Fuentes docentes de menor jerarquía** (manuales universitarios, revistas de enfermería): se aceptan para técnicas que las guías no describen, se citan sin autor si no se identifica y la auditoría registra su nivel.
- **Criterios que se solapan** (la oxitocina aparece en los criterios 13 y 18): la guía propone una forma de anunciarlos que cumpla ambos sin duplicar la dosis.

### 20.4 Lecciones aprendidas en la guía ECOE de choque anafiláctico y RCP

- **Se cuentan los criterios de la rúbrica:** la de choque anafiláctico numera 13 pero omite el 7, lo que reduce el margen real a dos criterios. Se informa al alumno.
- **Errores de dosis en la rúbrica:** se corrigen de forma explícita y visible ("0,5 mg/kg" en lugar de 0,5 mg), porque repetirlos sería peligroso.
- **Prácticas con varias estaciones:** si una práctica de la rúbrica tiene más de una estación y el tema las cubre, la guía las reúne y la respuesta final lo dice.
- **Tablas:** a petición del usuario, la guía se rehízo sin tablas salvo las de la rúbrica. Las escalas (Glasgow) y las listas de fármacos se leen bien como listas de un solo nivel con el puntaje o la dosis en la misma línea.
- **Revisión de completitud:** antes de dar una guía por terminada se revisa también lo que la rúbrica no pide pero la práctica exige. En esta guía faltaban el diagnóstico diferencial y la monitorización continua.

### 20.5 Lecciones aprendidas al rehacer la guía ECOE de cáncer cervicouterino

- **Clasificaciones largas sin tabla:** una clasificación que se recita (Bethesda) se presenta como lista numerada en el orden en que se dice; una con jerarquía (FIGO) se divide en bloques, cada uno con un párrafo en negritas para la etapa y una lista de un solo nivel para sus subetapas. Así no hacen falta viñetas anidadas.
- **Lista de completitud de una estación de consulta:** diagnóstico diferencial del síntoma principal, conducta en el nivel de atención de la estación (aquí, las lesiones precursoras), criterios completos de referencia y la urgencia que puede presentar la misma paciente (aquí, el sangrado activo). Cada añadido se integra también en la secuencia de la consulta, en un caso y en las preguntas directas.

### 20.6 Pasar de tabla a texto

Convertir una tabla en texto no es copiar sus celdas en una lista. Cada celda breve se completa hasta formar una oración que diga qué es, qué se pregunta o qué se hace, y para qué sirve. Al hacerlo aparecen los huecos que el formato escondía: dosis que la tabla daba solo como duración, términos sin definir, cifras sin unidad o sin la regla que las aplica (por ejemplo, "basta un valor alterado"), y comparaciones cuyo motivo no se explicaba. Esos huecos se completan con las fuentes y la auditoría los registra como aclaraciones.
