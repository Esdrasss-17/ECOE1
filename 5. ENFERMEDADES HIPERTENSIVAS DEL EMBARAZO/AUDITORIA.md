# Auditoría clínica correctiva: Enfermedades hipertensivas del embarazo

Registro de la fase de verificación aplicada a `5. ENFERMEDADES HIPERTENSIVAS DEL EMBARAZO.md`, separada de la redacción. El documento clínico no contiene comentarios sobre su elaboración; este archivo sirve solo para la trazabilidad.

## 1. Fuentes del usuario y su vigencia

| Clave | Fuente | Vigencia |
|---|---|---|
| d1 | Countouris M, et al. Hypertension in pregnancy and postpartum. Circulation 2025 (revisión de la AHA) | Vigente; base de la farmacología, los umbrales, el puerperio y el seguimiento cardiovascular |
| d2 | IMSS, GPC Detección, diagnóstico y tratamiento de enfermedades hipertensivas del embarazo (2017) | Parcialmente superada: metildopa de primera línea, suspensión del ácido acetilsalicílico a las 36 semanas y varios errores en su tabla de clasificación |
| d3 | IMSS, GPC S-020-08 Prevención, diagnóstico y tratamiento de la preeclampsia en segundo y tercer nivel (2017) | Vigente en lo esencial; sus metas de presión y algunas tablas proceden de la guía canadiense de 2014 |
| d4 | Luna D, et al. Hipertensión y embarazo: revisión de la literatura. Rev Med Clin Condes 2023 | Vigente; aporta fisiopatología, biomarcadores, HELLP, toxicidad del magnesio y conducta expectante |

**Páginas perdidas en la conversión.** De d1 faltan las páginas 498 y 499 (medición domiciliaria posparto y parte del riesgo cardiovascular), y el inicio del apartado de anticoncepción está truncado; no se completaron por suposición. De d2, la página 24 (evidencias sobre el ácido acetilsalicílico) es una imagen sin texto legible; su contenido se cubrió con d3 y la página 25. De d3, la página 31 (tratamiento no farmacológico) es ilegible; las demás páginas convertidas en imagen se recuperaron con OCR (`limpiar_fuente.py --ocr 300`) y se cotejaron con las imágenes.

## 2. Errores de las fuentes corregidos

| # | Afirmación de la fuente | Corrección | Sección | Fundamento |
|---|---|---|---|---|
| 1 | d2 (tabla de clasificación): preeclampsia con datos de severidad con "plaquetas menores a 150 000" | Menos de 100 000/µL | 3.3 | d3, d4, ACOG 2020 |
| 2 | d2: "elevación de las lipoproteínas de baja densidad (LDL)" como dato de severidad | Deshidrogenasa láctica (DHL) | 3.3, 3.4 | d3 y d4; error de sigla |
| 3 | d2: preeclampsia con "creatinina sérica elevada (>30 mg/mmol)" | El valor de 30 mg/mmol corresponde al cociente proteína/creatinina urinario de la guía británica, no a la creatinina sérica; el cuerpo usa los cocientes en mg/mg | 3.2, 5.1 | d3; NICE |
| 4 | d3 (cuadro 1): la preeclampsia sobreagregada se define por criterios "antes de la semana 20" | Después de la semana 20 | 3.1 | Guía canadiense de 2014, de la que procede el cuadro; d2 omite el error |
| 5 | d3 (cuadro 1): preeclampsia con datos de severidad "con una o más complicaciones adversas o severas" | Con una o más complicaciones severas; las condiciones adversas solo aumentan el riesgo | 3.3 | Texto de d3 (sección 3.4) y d2 |
| 6 | d3 (cuadro 8): la PA de 160/110 mm Hg se coloca en la fila del sistema nervioso central; DHL "mayor de 600 UI/ml" | La PA se presenta como fila propia; la unidad es UI/L | Tabla 4 | d4; error de maquetación y de unidad |
| 7 | d4: cociente proteína/creatinina "≥ 0,3 mg/dL" | 0,3 mg/mg (cociente adimensional en mg de proteína por mg de creatinina) | 3.2 | ACOG 2020; d3 |
| 8 | d4: ácido acetilsalicílico "82 mg" según la ACOG | 81 mg | 4.3 | ACOG 2018 y USPSTF 2021 |
| 9 | d2 (cuadro de la prueba sin estrés): línea de base normal de 120 a 160 lpm y "≤2 aceleraciones" en las pruebas atípica y anormal | 110 a 160 lpm; menos de 2 aceleraciones (2 o más definen la prueba normal en la misma tabla) | Anexo A.3 | Guía canadiense de vigilancia fetal (tabla adaptada de su versión de 2018) |
| 10 | d1: contraindicación absoluta de los anticonceptivos combinados con PA mayor de 160/110 mm Hg | Categoría 4 de los criterios de Estados Unidos con PAS de 160 o más o PAD de 100 o más; categoría 3 con 140-159/90-99 | 9.4, anexo B | US MEC 2024 |
| 11 | d3: "Glosario": hipertensión enmascarada con 130/85 mm Hg fuera del consultorio | Se usa el umbral de 135/85 mm Hg de los cuadros de ambas GPC | 3.1 | d2 y d3 (cuadros 1 y 2) |

## 3. Contradicciones internas de las fuentes resueltas

| Contradicción | Resolución |
|---|---|
| d2 recomienda iniciar el tratamiento con PAD persistentemente mayor de 90 mm Hg, pero su tabla por grados no trata la hipertensión de 140/90 a 149/99 | Ambas posiciones se presentan como institucionales en el anexo B y C.1; el cuerpo usa las guías vigentes (tabla 6) |
| d2 propone una meta menor de 130/80 mm Hg en la hipertensión crónica y, en su tabla, PAD de 80 a 100 y PAS menor de 150 | Se registran en el anexo B; el cuerpo usa la meta del CHAP (menos de 140/90) |
| d3 indica el seguimiento ambulatorio de la preeclampsia sin datos de severidad "antes de 38 semanas" en la tabla de evidencias y "antes de 37 semanas" en la cédula | Se usa 37 semanas, coherente con el nacimiento recomendado a las 37 semanas |
| d3 fija la recurrencia de la convulsión en 5 minutos (texto) o 10 minutos (cuadro 12) | El cuerpo usa 5 minutos; el cuadro se transcribe íntegro en el anexo C.4 |
| d3 recomienda corticosteroides para el HELLP "no de rutina" y a la vez transcribe el protocolo de Mississippi | El cuerpo sigue la recomendación; el protocolo pasa al anexo C.5 |
| d3 considera la PA de 160/110 condición adversa (cuadro 2) y complicación severa (cuadro 8) | Se explica en la sección 3.3 junto con la posición de la ACOG |

## 4. Contenidos completados o precisados con fuentes externas

| Contenido | Fuente |
|---|---|
| Criterios de preeclampsia y de datos de severidad, tira reactiva de 2+, cociente de 0,3 | ACOG, boletín 222 (2020) |
| Esquemas escalonados de labetalol, hidralazina y nifedipino; meta de 140-150/90-100 mm Hg; consulta ante la falta de respuesta | ACOG, opinión 767 (2019) |
| Carga de 4 a 6 g en 20 a 30 minutos y mantenimiento de 1 a 2 g por hora | ACOG 2020 (confirmado con protocolos estatales que lo reproducen) |
| Momento del nacimiento en la hipertensión crónica según el grado de control | ACOG, opinión 831 (2021) |
| Indicación, dosis y duración del ácido acetilsalicílico | ACOG 743 (2018) y USPSTF (2021) |
| Calcio de 1,5 a 2 g en tres tomas, separado del hierro | OMS (2018) |
| Clasificación de Mississippi del HELLP (los criterios diagnósticos del cuerpo proceden de d4 y coinciden con los de Tennessee) | Haram et al., 2009 |
| Puntos de corte del cociente sFlt-1/PlGF | Zeisler et al., 2016 (PROGNOSIS) y d4 |
| Umbrales de plaquetas para el bloqueo neuroaxial y verificación en 6 horas en el HELLP | Consenso de la SOAP (2021) |
| Corticosteroides en el pretérmino tardío | SMFM, consulta 58 (2021) |
| Ausencia de más efectos graves al combinar nifedipino y sulfato de magnesio | Magee et al., 2005 |
| Antiinflamatorios no esteroideos preferibles a los opioides en el puerperio | ACOG 2020 |
| Existencia de un registro sanitario mexicano de labetalol inyectable | Vademécum México (registro 205M2021 SSA) |
| Criterios de elegibilidad de los anticonceptivos combinados en la hipertensión | US MEC 2024 |

## 5. Afirmaciones absolutas revisadas

| Afirmación de la fuente | Redacción final |
|---|---|
| d3: "Toda paciente con preeclampsia severa independientemente de la edad debe considerarse el nacimiento en breve" | Se mantiene que el nacimiento es el tratamiento definitivo, con el manejo expectante antes de las 34 semanas en pacientes estables y en tercer nivel (d3, d4, ACOG) |
| d3 (glosario): la preeclampsia con datos de severidad "indica el parto, independientemente de la edad gestacional" | Igual que la anterior; se precisa la conducta por edad gestacional en la tabla 9 |
| d2: "Labetalol no está disponible en México" | Se fecha (GPC de 2017) y se añade el registro sanitario posterior |
| d1: "Aspirin use during pregnancy is safe ... and thus universally recommended" | Se limita a su indicación por factores de riesgo, que es la recomendación de la misma fuente y de las guías |
| d3: la única resolución del HELLP es la interrupción del embarazo | Se conserva, porque coincide con todas las fuentes |
| Redacción propia inicial sobre el mecanismo del ácido acetilsalicílico y la distensión de la cápsula de Glisson | Se retiró por no figurar en las fuentes; se sustituyó por el momento de inicio (d3) y por la isquemia y necrosis hepáticas (d4) |

## 6. Estadísticas suprimidas por no modificar la conducta

- Riesgos relativos de cada factor de riesgo (cuadros 1 y 6 de las GPC y cuadro 18 de hipertensión posparto); se conservan los factores sin cifras.
- Sensibilidad, especificidad, razones de verosimilitud y valores predictivos de los modelos de predicción, del Doppler y de la tira reactiva, salvo el rango de sensibilidad de la tira, que explica por qué se confirma con un método cuantitativo.
- Riesgos relativos e intervalos de confianza del calcio, de la vitamina D, del ácido acetilsalicílico, del sulfato de magnesio y de los betabloqueadores.
- Tasas de mortalidad por etnia, incidencias mundiales de muertes maternas y perinatales, y la mortalidad fetal por cada 1000 en la preeclampsia y en cada resultado del perfil biofísico.
- Número necesario a tratar del CHAP y detalles de los ensayos (tamaño muestral, cohortes de derivación).

## 7. Imágenes

| Archivo | Origen | Descripción verificable |
|---|---|---|
| `ehe_presion_embarazo_puerperio.png` | d1, página 491 (figura 1 de la revisión) | Esquema rotulado (presión arterial, resistencia vascular sistémica, volumen sanguíneo, trimestres y puerperio temprano y tardío). El pie describe solo lo rotulado y lo que explica el texto de d1; se recortó el margen blanco derecho sin alterar el contenido. No se encontró el pie original |
| `ehe_seguimiento_posparto.png` | d1, figura 2 ("Postpartum Management Timeline after HDP") | El texto de d1 remite a ella como figura 2; el pie traduce sus rótulos |

**Imágenes omitidas.**

- Las 14 imágenes de d2 y las 19 de d3 son páginas de evidencias y recomendaciones convertidas en imagen (o fragmentos de ellas); su texto se recuperó por OCR y se integró en el cuerpo. Las páginas 24 de d2 y 31 de d3 son ilegibles.
- Los algoritmos de ambas GPC no se extrajeron como imagen (solo fragmentos de 440 × 276 y 228 × 226 píxeles). No se reconstruyeron; del algoritmo 6 de d3 solo se transcribió su recuadro legible de criterios de estabilización (anexo C.8).
- Figuras 3 a 5 de d1 (modelos de clínicas posparto, lista de verificación de la visita y prioridades de investigación): la lista de verificación se transcribió al español en la sección 9.4; las otras dos son organizativas y no clínicas.
- La imagen de d4 es el logotipo de la revista.

No se generaron esquemas propios, porque las tablas cubren los conceptos definidos por umbrales.

## 8. Limitaciones de la verificación

- No pudo abrirse el texto completo de los documentos de la ACOG; los esquemas de la opinión 767 se verificaron con protocolos institucionales que la reproducen. Los pasos del labetalol (20, 40 y 80 mg cada 10 minutos) y de la hidralazina (5 a 10 mg y después 10 mg a los 20 minutos) coinciden en varias fuentes; los del nifedipino (10, 20 y 20 mg cada 20 minutos) solo se confirmaron parcialmente. La meta de 140-150/90-100 mm Hg aparece en un protocolo basado en la opinión 767, mientras otro resumen cita 140-160 mm Hg de PAS.
- Los intervalos de nacimiento de la opinión 831 se confirmaron con un resumen secundario que tiene una errata en el intervalo de la hipertensión de difícil control; se usó 36 0/7 a 37 6/7 semanas.
- Las concentraciones de toxicidad del magnesio (7, 10 y 25 mEq/L) proceden de d4 y de una referencia obstétrica; la ficha del fabricante describe la pérdida de reflejos al acercarse a 10 mEq/L. La GPC no indica las unidades de su objetivo de 5 a 7.
- La duración de la hidralazina intravenosa (45 minutos) y los tiempos de acción del cuadro 11 de d3 se transcriben sin verificar.
- La mención de las mujeres de raza negra entre los factores de riesgo moderado sigue a la ACOG y la USPSTF, que la atribuyen a determinantes sociales.
- La afirmación de que el manejo expectante está contraindicado antes de la viabilidad se tomó de una revisión que enumera las contraindicaciones definidas por la ACOG.
- La disponibilidad real del labetalol en las unidades mexicanas no pudo comprobarse; solo se documentó un registro sanitario.
