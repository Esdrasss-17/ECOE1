# Auditoría: Guía práctica ECOE de cáncer de mama

Registro de la verificación aplicada a `GUIA_ECOE_CANCER_MAMA.md`. La guía no contiene comentarios sobre su elaboración; este archivo sirve solo para la trazabilidad.

## 1. Fuentes y criterio de selección

- **rub:** el documento `RUBRICAS/RUBRICAS_ECOE_VI.pdf` solo contiene las prácticas 1, 4, 8, 9 y 11; no hay rúbrica de cáncer de mama. Se usó como patrón la práctica 9 (cáncer cervicouterino), que es la otra estación oncológica de consulta: presentación, historia con énfasis en los AGO, padecimiento con signos vitales, exploración en orden, síntomas, factores de riesgo, vías de diseminación, prueba diagnóstica, estudios por sospecha de metástasis, clasificación completa, carcinoma in situ, estadificación, interpretación de un resultado, tratamiento según la etapa y prevención.
- **d1, d2 y claves del tema 10:** GPC S-001-08 (primer nivel, 2017), GPC IMSS-232-09 (tratamiento, 2017), NOM-041 y las externas ya verificadas del documento clínico `10. CÁNCER DE MAMA.md` (INEGI 2025, USPSTF 2024, ACS 2015, AJCC 8.ª, ASCO/CAP 2018, St. Gallen 2013, ACOSOG Z0011, EBCTCG 2015 y ASCO 2020). En las referencias con más de tres autores se dejaron los tres primeros y "et al.".
- **Externas nuevas (revisión de completitud):** AFP 2012 y 2019 (secreción por el pezón y mastalgia), clasificación de la OMS de 2019 (nomenclatura del carcinoma invasor de tipo no especial) y protocolo SPIKES (comunicación de malas noticias).
- No se usaron guías ni repasos creados en otras sesiones.

## 2. Diseño sin rúbrica

La sección 1.1 presenta una lista de verificación propuesta de 16 pasos, numerada y declarada como no oficial, construida con el patrón de la práctica 9 (metodología, sección 20.7). La clasificación BI-RADS ocupa el lugar de Bethesda como clasificación que se dice completa. La sección de precisiones de la rúbrica se sustituye por las diferencias entre fuentes (sección 14), tomadas del anexo B del documento del tema 10. Las tablas del documento de origen (factores de riesgo, BI-RADS, criterios de referencia, subtipos, Van Nuys, tratamiento adyuvante y TNM) se pasaron a listas de un nivel; la tabla del tratamiento adyuvante se resumió por subtipo, conservando los umbrales de tamaño y de ganglios.

## 3. Revisión de completitud

Además de lo que la estación calificaría con el patrón de la práctica 9, se incluyeron: el interrogatorio dirigido del nódulo, la piel, el pezón, la axila y los síntomas de metástasis; la técnica completa de exploración con sus figuras; la forma de describir un hallazgo; la enseñanza de la autoexploración; el diagnóstico diferencial (lesiones benignas, secreción por el pezón, mastalgia y cáncer inflamatorio frente a mastitis); la imagen según la edad; los criterios de referencia con plazos; la interpretación de un informe de patología con el subtipo; el cáncer de mama en el embarazo; la comunicación de malas noticias y el seguimiento.

## 4. Datos verificados externamente

- **AFP 2012 (Salzman, Fleegle, Tully):** criterios de secreción patológica (espontánea, sanguinolenta, unilateral o con masa) y su referencia; galactorrea con prolactina y TSH; dolor focal con ultrasonido antes de los 30 años y con mastografía desde los 30; paracetamol y antiinflamatorios. Verificado con el resumen de la página de la AAFP.
- **AFP 2019 (Salzman, Collins, Hersh):** la mayoría de los síntomas son benignos; imagen en casi toda mujer con masa palpable; la mastalgia rara vez se debe a cáncer. Verificado con el resumen de la página de la AAFP.
- **OMS 2019:** la nomenclatura "carcinoma invasor de tipo no especial" se confirmó con la guía de informe del ICCR, que remite a la 5.ª edición. El orden de frecuencia (tipo no especial y después lobulillar) se confirmó con fuentes secundarias de patología; la guía no da porcentajes porque las cifras varían entre fuentes (76 a 79% y alrededor de 10 a 13%).
- **SPIKES:** registro bibliográfico confirmado (Oncologist. 2000;5(4):302-311; PMID 10964998). Los seis pasos se tomaron del resumen y de fuentes secundarias; no se leyó el texto completo.
- **ACOG 164 (enfermedad mamaria benigna):** se confirmó su registro, pero no se pudo leer su contenido, por lo que no se cita.

## 5. Razonamiento sin fuente específica

- La forma de describir un hallazgo por mama, cuadrante y distancia al pezón (sección 3.6) es la convención clínica habitual; las características que se describen son las de los datos de sospecha de la GPC.
- La definición de carcinoma in situ como el que no atraviesa la membrana basal es un concepto general de patología.
- La advertencia de pensar en el cáncer inflamatorio ante un cuadro parecido a una mastitis fuera de la lactancia o que no se resuelve aplica la descripción del cáncer inflamatorio de la GPC de tratamiento.
- En el caso 2, el fibroadenoma se presenta como "un diagnóstico probable", sin cifra, y se insiste en que la exploración no basta.

## 6. Imágenes

- `assets/ecoe_cm_categorias_T.png`: generada con `herramientas/esquemas_ecoe_mama.py` con las definiciones del TNM que transcribe la GPC (regla a escala de las categorías T por tamaño y recuadro de T4). Una primera versión con círculos a escala se descartó porque los círculos tapaban la regla. Se muestra a todo el ancho.
- Del tema 10, por ruta relativa (`../assets/`): las cinco figuras de exploración y autoexploración de la GPC S-001-08.

## 7. Formato

- El PDF tiene 27 páginas y se compiló con `ENLACES=1` (índice en la página 2, 63 marcadores).
- La guía no tiene tablas, viñetas anidadas ni flechas; el verificador no encontró notas sin definir o sin usar ni remisiones rotas.

## 8. Limitaciones de la verificación

- El acceso directo a las webs está bloqueado; las externas nuevas se verificaron con resúmenes y fuentes secundarias.
- Las cifras del documento del tema 10 se tomaron de su versión auditada, sin volver a consultar las fuentes primarias.

## Versión 2 (`GUIA_ECOE2_CANCER_MAMA.md`)

- **Motivo:** la versión 1 se centraba en el diagnóstico y la referencia y omitía datos del documento del tema 10: TRH y estilo de vida, indicaciones completas de RM y ultrasonido, la referencia de la masa no palpable, la mastectomía bilateral y el ganglio centinela en el CDIS, los detalles de la axila y de la RT, las histologías favorables, los factores de alto riesgo en la premenopausia, la respuesta patológica completa y la hormonoterapia neoadyuvante, la evaluación y el dolor en la enfermedad metastásica, el detalle del embarazo, de Paget y del hombre, los estudios ante síntomas en el seguimiento, las categorías N y pN y las dosis del cuadro básico. Sus cinco casos no cubrían el riesgo promedio, el alto riesgo, la TRH, el CDIS, cada subtipo, la enfermedad inflamatoria, la metastásica, el tamoxifeno con sangrado, Paget ni el hombre. La versión 2 los incorpora y tiene catorce casos.
- **Límite de contenido:** no sale de los temas del documento .md. Se retiró el protocolo SPIKES, porque la comunicación de malas noticias no es un tema del documento; la sección 13 usa lo que dicen las GPC (informar con claridad, consentimiento informado). El diferencial de la secreción y la mastalgia (AFP 2012 y 2019) y la nomenclatura histológica (OMS 2019) se conservan porque se añadieron al documento general (secciones 1.1 y 5.1), que ya trataba la secreción, el dolor focal y los tipos histológicos.
- **Formato:** 31 páginas con `ENLACES=1`, sin tablas; el verificador no encontró errores. La versión 1 se conserva.
