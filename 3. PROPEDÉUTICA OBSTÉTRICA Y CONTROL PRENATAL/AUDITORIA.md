# Auditoría clínica correctiva: Propedéutica obstétrica y control prenatal

Registro de la fase de verificación aplicada a `3. PROPEDÉUTICA OBSTÉTRICA Y CONTROL PRENATAL.md`, separada de la redacción. El documento clínico no contiene comentarios sobre su elaboración; este archivo sirve solo para la trazabilidad.

## 1. Fuentes del usuario y su estado

| Clave | Fuente | Estado en la conversión a texto |
|---|---|---|
| d1 | Reglas de apoyo (Alfehld, Johnson-Toshach, McDonald, Naegele); material didáctico | Texto OCR muy degradado; las fórmulas se reconstruyeron con los ejemplos numéricos de las propias láminas, que son coherentes entre sí |
| d2 | Williams Obstetricia: definiciones y maniobras de Leopold | Solo ilustraciones, sin texto ni pies; las definiciones se tomaron de la GPC y de fuentes externas (sección 3) |
| d3 | GPC IMSS-028-22 (2022) | Varias páginas de evidencias y recomendaciones se perdieron en la conversión. Se recuperó el texto de las páginas convertidas en imagen con una nueva opción del limpiador (`--ocr`), y las recomendaciones de las páginas perdidas se tomaron de la cédula de verificación de recomendaciones clave |
| d4 | NOM-007-SSA2-2016 | Completa; se usaron las secciones 3, 5.1 a 5.4 y 5.11 y los apéndices A, C, D, E y K. Las secciones de parto, puerperio y recién nacido corresponden al tema de trabajo de parto |
| d5 | UpToDate, Prenatal care: Initial assessment (mayo de 2025) | Completa |

## 2. Errores de las fuentes corregidos

| # | Afirmación de la fuente | Corrección | Sección | Fundamento |
|---|---|---|---|---|
| 1 | NOM, apéndice K: la curva de 75 g incluye un valor a las 3 horas (140 mg/dL) | La curva de 75 g de la IADPSG tiene tres valores (ayuno, 1 y 2 horas); el valor de 140 mg/dL a las 3 horas pertenece a la curva de 100 g de Carpenter y Coustan | 6.3, anexo B | GPC (criterios IADPSG y Carpenter-Coustan); ACOG PB 190 |
| 2 | NOM, apéndice K: "126 mg/dL posprandial de 1 hora" diagnostica sin curva | Los criterios de diabetes manifiesta son glucosa en ayuno de 126 mg/dL o más, hemoglobina glucosilada de 6,5% o más o glucosa al azar de 200 mg/dL o más con síntomas | 6.3, anexo B | UpToDate (ADA/ACOG) |
| 3 | Carpenter y Coustan presentado en la GPC sin indicar cuántos valores se requieren | Se precisa que el diagnóstico requiere dos valores o más | 6.3 | ACOG PB 190 |
| 4 | GPC: "vacunar con DTaP" | DTaP es la formulación pediátrica; en el embarazo se usa Tdpa (formulación para adultos), y los CDC la indican en cada embarazo entre las semanas 27 y 36 | 7.6, anexo B | CDC 2024 |
| 5 | GPC: hierro intravenoso (carboximaltosa) como primera elección en la anemia ferropénica | El cuerpo presenta el hierro oral como primera línea en la mayoría de las guías y el intravenoso para indicaciones concretas; la postura de la GPC se conserva y se contrasta en el anexo B | 10.1, anexo B | ACOG PB 233 (2021); OMS 2016; síntesis de guías de manejo de la sangre del paciente |
| 6 | GPC: progestágenos ante parto pretérmino previo, sin matices | Se añade la retirada del caproato de 17-hidroxiprogesterona (FDA, 2023) y la indicación vigente de progesterona vaginal en el cérvix corto | 7.5, anexo B | Declaración de la SMFM 2023 |
| 7 | GPC: anemia "hemoglobina < 11 mg/dl" | Unidad corregida a g/dL | Tabla 5 | UpToDate |
| 8 | NOM, apéndice C: la tabla del índice de masa corporal está desalineada en la imagen (cada categoría aparece una fila más abajo) | Se reconstruye la tabla con la correspondencia correcta (menos de 18,5, bajo peso; 18,5 a 24,9, normal...) y se omite la imagen | Tabla 8 | Texto de la propia NOM ("un IMC bajo (<18.5) sugiere desnutrición...") |
| 9 | Curva de altura uterina de la NOM: el último valor del eje vertical aparece rotulado como 38 | Se conserva la imagen y el pie aclara que, por la progresión de 2 en 2, corresponde a 33 | 5.2 | Lectura de la escala de la propia figura |
| 10 | GPC: cuestionario "AUDIT-C" | El cuestionario reproducido tiene 10 preguntas: es el AUDIT completo; el AUDIT-C solo incluye las 3 primeras | Anexo A | Contenido de la propia tabla |
| 11 | GPC (algoritmo): reposo absoluto en cama en la amenaza de aborto | La revisión Cochrane no encontró evidencia suficiente de que el reposo prevenga el aborto; el algoritmo pasa al anexo C con esa precisión | 10.4, anexo C | Aleman et al., Cochrane CD003576 |
| 12 | Material de apoyo: la determinación del peso fetal ayuda a evaluar la desproporción cefalopélvica, "primera causa de operación cesárea" | Se omite la afirmación de causa principal, que no está respaldada por las demás fuentes | 5.3 | Revisión de afirmaciones absolutas |

## 3. Contenidos completados con fuentes externas

| Contenido | Motivo | Fuente |
|---|---|---|
| Umbrales para corregir la edad gestacional por ecografía (tabla 3) | La GPC solo da dos umbrales en su algoritmo | ACOG Committee Opinion 700 (2017) |
| Descripción de las cuatro maniobras de Leopold | La fuente de Williams no conserva texto | GLOWM, capítulo basado en Williams Obstetrics |
| Definiciones de actitud, punto de referencia y variedad de posición | La GPC solo define situación, presentación y posición | Fuentes docentes y Manual MSD, verificadas con el buscador |
| Ácido fólico de 4 mg tras un defecto del tubo neural | No figura en las fuentes | USPSTF 2009 (resume la postura de ACOG y AAFP) |
| Hierro de 30 a 60 mg diarios | La NOM solo indica prescribir hierro | OMS 2016 |
| Vacuna contra el virus sincitial respiratorio y momento de la Tdpa | No figuran o difieren | CDC 2024 |
| Inmunoglobulina anti-D a las 28 semanas | La NOM solo indica la dosis posparto | UpToDate; SOGC 2018 |
| Nitrofurantoína en el primer trimestre | El algoritmo de la GPC no la matiza | ACOG Committee Opinion 717 |
| Retirada de las categorías de riesgo por letras | La NOM las mantiene | FDA, Pregnancy and Lactation Labeling Rule (vigente desde 2015) |

## 4. Afirmaciones absolutas revisadas

| Afirmación que podía leerse como absoluta | Redacción final |
|---|---|
| "Se debe tratar la anemia" sin matiz | Se trata porque se asocia a bajo peso y parto pretérmino; suele deberse a deficiencia de hierro |
| Influenza: vacuna que "protege a la madre y al recién nacido" | "Su seguridad y eficacia están demostradas", como en la GPC |
| Altura uterina: "la altura en centímetros coincide con las semanas" | "Suele coincidir aproximadamente después de las 24 semanas"; las reglas se presentan como aproximaciones |
| Maniobras de Leopold como método de diagnóstico de la presentación | Se informan su precisión, sus límites y la confirmación del encajamiento por tacto vaginal |
| Altura uterina fuera de los percentiles 10 a 90 como sinónimo de patología | Altura anormal significa investigar y consultar con el especialista, no diagnosticar |

## 5. Estadísticas suprimidas por no modificar la conducta

- Riesgos relativos e intervalos de confianza de los metaanálisis sobre programas educativos, tabaquismo, enfermedad periodontal, anemia, tricomoniasis, calambres, estreñimiento y várices; se conservan sus conclusiones.
- Cifras de cobertura de la atención prenatal en México y en el mundo (ENADID 2018, OMS).
- Razones de momios de los predictores ecográficos de aborto, salvo la regla práctica del descenso de la frecuencia cardiaca embrionaria.
- Datos de consanguinidad (probabilidades de portadores entre primos) y de la cohorte de rotura prematura de membranas.
- Calificaciones AGREE II de las guías revisadas por la GPC y su protocolo de búsqueda.

## 6. Imágenes

### Imágenes conservadas

| Archivo | Origen | Descripción verificable |
|---|---|---|
| `pp_actitud_cefalicas.jpg` | d2 (Williams), página 1 | Figura de Williams "Longitudinal lie. Cephalic presentation. Differences in attitude of the fetal body in (A) vertex, (B) sinciput, (C) brow, and (D) face presentations", confirmada por una reproducción docente de la figura |
| `pp_maniobras_leopold.jpg` | d2 (Williams), página 3; cuatro dibujos reunidos en una lámina sin modificar su contenido | Cada dibujo muestra la posición de manos descrita para cada maniobra en el texto verificado (manos en el fondo; palmas a los lados; una mano sobre la sínfisis; explorador mirando a los pies). El orden de extracción del PDF (2, 3, 4, 5) no coincide con el de las maniobras, por lo que se reordenaron según su contenido: primera (0003-02), segunda (0003-04), tercera (0003-03) y cuarta (0003-05) |
| `pp_curva_afu_nom.png` | d4, apéndice A | Título en la propia imagen y fuente en el texto de la NOM (Fescina y colaboradores, CLAP) |
| `pp_algoritmo_edad_gestacional.png` | d3, anexo de diagramas de flujo | Título "Diagnóstico de embarazo" en la GPC; contenido verificado contra ACOG 700 |
| `pp_algoritmo_vomitos_sangrado.png` y `pp_algoritmo_anemia_infecciones.png` | d3, anexo de diagramas de flujo | Título "Complicaciones menores en el embarazo" en la GPC; se ubican en el anexo C con la lectura actual |

### Imágenes omitidas

- **Williams, presentaciones y posiciones sin pie** (páginas 2 y 3: vértice en distintas variedades, presentaciones de cara en vista pélvica, presentación pélvica y situación transversa): sin leyenda, la variedad exacta (derecha o izquierda, anterior o posterior) no puede asignarse con certeza, porque depende de la perspectiva del dibujo. Se omitieron y la estática fetal se explica en texto.
- **Material de apoyo (d1):** ilustraciones decorativas sin contenido clínico.
- **NOM:** tabla del índice de masa corporal desalineada (se reconstruyó como tabla), gráfica de peso al nacer y escalas neonatales (corresponden al tema de trabajo de parto y recién nacido).
- **UpToDate:** algoritmos de hemoglobinopatías, sífilis y hepatitis B, con títulos perdidos y orientados a la práctica de Estados Unidos; su contenido esencial está en la tabla 5.
- **GPC:** páginas de evidencias convertidas en imagen; su texto se recuperó por OCR y se integró en el cuerpo.

## 7. Diseño

- Los algoritmos de la GPC se muestran a todo el ancho de la página (nueva clase `wide` en `herramientas/postprocesar_html.py`).
- Las tablas con celdas largas reciben anchos relativos de columna desde la línea separadora del Markdown, para que la columna de interpretación no quede estrecha.
- La tabla de factores de riesgo integra las tres listas de la GPC (introducción, cuadro 4 y factores modificables) para no repetirlas.

## 8. Limitaciones de la verificación

- El entorno impidió abrir directamente las webs de ACOG, CDC, OMS, FDA y PubMed. La verificación se hizo con los resúmenes del buscador web, que remiten a las publicaciones primarias citadas.
- La **regla de Alfehld** ((altura uterina + 4) / 4 = meses) no se encontró en ninguna fuente externa; se conserva como regla de la fuente de apoyo, presentada como aproximación.
- Los factores de la **regla de McDonald** (× 8/7 y × 2/7) y la constante de la **regla de Johnson-Toshach** (12 sin encajar, 11 encajada) solo se confirmaron en fuentes docentes, no en guías.
- La recomendación de hierro oral de primera línea de ACOG PB 233 se confirmó a través de síntesis secundarias, no del texto completo.
- El momento de la Tdpa en el esquema nacional mexicano vigente no se pudo confirmar con un documento oficial reciente; el cuerpo remite al esquema nacional y cita a la GPC y a los CDC.
- Las páginas perdidas de la GPC pueden contener recomendaciones (por ejemplo, sobre calcio o ejercicio) que no figuran en la cédula de recomendaciones clave y, por tanto, no se incluyeron.
