# Progreso de los documentos clínicos

La metodología está en `GUIA_METODOLOGICA.md`. Este registro se actualiza en cada commit para poder retomar el trabajo si se interrumpe.

| # | Tema | Estado | Notas |
|---|---|---|---|
| 1 | Retinopatías | Completo | Documento de referencia. Las fotos ETDRS 2B y 3, sin descripción en la fuente, se sustituyeron por retinografías descritas en AMF 2018 |
| 2 | RCTG | Completo | Nueve trazados sin título en la fuente se sustituyeron por cuatro esquemas generados con las definiciones del NICHD (`herramientas/esquemas_rctg.py`) |
| 3 | Propedéutica obstétrica y control prenatal | Completo | 44 páginas. La conversión perdió páginas de la GPC; se recuperaron con OCR y con la cédula de recomendaciones clave. Las ilustraciones de Williams sin pie se identificaron por su contenido (actitud y Leopold) o se omitieron (variedades de posición) |
| 4 | Cervicovaginitis | Completo | 17 páginas. La GRR de 2014 tiene varios esquemas superados; el cuerpo usa los CDC 2021 y la GPC de candidosis 2019, y las diferencias van al anexo A. Se añadió la cervicitis por gonococo, ausente en las fuentes |
| 5 | Enfermedades hipertensivas del embarazo | Completo | 45 páginas. El cuerpo sigue la ACOG 2019-2021 y la AHA 2025; la metildopa de primera línea, las metas de la GPC y la suspensión del ácido acetilsalicílico a las 36 semanas pasan al anexo B. Se corrigieron errores de los cuadros de las GPC (plaquetas, "LDL", preeclampsia sobreagregada). Figuras: dos de Countouris 2025; los algoritmos vectoriales de las GPC no se reconstruyeron |
| 6 | Aborto | Completo | 55 páginas. El cuerpo sigue el Lineamiento de 2022, la OMS 2022 y la ACOG; las medidas sin respaldo de la GPC de amenaza de aborto (multivitamínicos, tocolíticos, reposo absoluto, caproato de hidroxiprogesterona) y los criterios del IMSS de 2009 pasan a los anexos B y C. Se reclasificaron las contraindicaciones del aborto con medicamentos y se actualizó el marco legal (Suprema Corte 2023). Figuras: esquema de tipos de aborto, algoritmo ecográfico, equipo de AMEU, saco persistente y flujograma del Lineamiento; cuatro ultrasonidos sin pie se omitieron |
| 7 | Hemorragia de la segunda mitad del embarazo | Completo | 50 páginas. Integra cinco fuentes: GPC de choque hemorrágico (IMSS 2017), Lineamiento de triage y Código Mater (2016), GPC de anomalías de la inserción placentaria (2019), GPC de ruptura uterina (2017) y GPC de hemorragia posparto (2021). El ácido tranexámico sigue la GPC de 2021 y la OMS 2017 (la GPC de 2017 no lo recomendaba); se añadieron la medición objetiva y el paquete de la OMS 2023, los momentos de nacimiento del ACOG 831 y un apartado breve de desprendimiento con fuentes externas. Figuras: dos esquemas generados de inserción placentaria y acretismo (`herramientas/esquemas_placenta.py`) y el algoritmo histórico de ruptura uterina; las páginas de evidencias en imagen se omitieron |
| 8 | Trabajo de parto | Pendiente | |
| 9 | Cáncer cervicouterino | Pendiente | |
| 10 | Cáncer de mama | Pendiente | |
| 11 | Choque anafiláctico y RCPIH (ACLS) | Pendiente | |
