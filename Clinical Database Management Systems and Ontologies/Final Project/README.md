# Description:
This project was completed as the final assignment for Yale University's BIS638: Clinical Database Management Systems and Ontologies. Working with a team of four, we used the MIMIC-IV critical care database to study Acute Respiratory Distress Syndrome (ARDS) in septic ICU patients, covering three areas: (1) demographic/behavioral risk factors for ARDS, (2) the association between ARDS severity and in-hospital mortality, and (3) 48-hour oxygenation trajectories and their link to outcomes.

My contribution was the stratified analysis of ARDS severity and in-hospital mortality across ICU types and demographic subgroups. The code in this repository reflects that portion of the work only; the demographic modeling and trajectory-clustering code were completed by other team members and are not included here.

# Repo Contents:
- updated_final_query.sql: BigQuery SQL that builds the analytic cohort from MIMIC-IV. Identifies septic admissions via ICD-9/10 codes, extracts paired PaO₂/FiO₂ measurements from lab and chart events, computes the minimum PF ratio per ICU stay, classifies ARDS severity using Berlin criteria thresholds, and joins in-hospital mortality and ventilation status.
- expanded_query_results.Rmd: R Markdown notebook that consumes the SQL query output and performs the stratified analysis, including the distribution of minimum PF ratio by mortality outcome, a summary table of ARDS severity vs. in-hospital death rate, a cross-tabulation of severity × ventilation status × mortality, and a horizontal stacked bar chart of survival by ICU care unit type.

# Analysis Summary:
- Built a cohort of septic ICU admissions and computed each patient's worst (minimum) PaO₂/FiO₂ ratio to classify ARDS severity per the Berlin criteria (Severe <100, Moderate 100–200, Mild 200–300, No ARDS >300).
- Found a clear mortality gradient by severity: 49.7% (Severe) vs. 38.1% (Moderate) vs. 30.9% (Mild) vs. 25.1% (No ARDS), reinforcing the prognostic value of the Berlin classification in this cohort.
- Cross-tabulated severity with mechanical ventilation status, showing that receiving ventilation support was associated with lower in-hospital death percentages across every severity stratum.
- Compared survival across 13 distinct ICU care unit types and found no meaningful difference in outcome by unit, suggesting patient-level severity was a stronger driver of mortality than unit of care.

# Skills Demonstrated:
- SQL for clinical data engineering: Multi-CTE BigQuery query design over a large relational EHR database (MIMIC-IV), including time-windowed joins (matching PaO₂/FiO₂ readings within a ±30 minute window), array aggregation to find first/nearest events, and combining diagnosis, lab, chart, and admissions tables into an analysis-ready cohort.
- Clinical domain translation: Operationalizing a published clinical scoring system (Berlin ARDS criteria) into reproducible code logic.
- Statistical/exploratory data analysis in R: Aggregation, cross-tabulation, and summary table generation (base R aggregate, tapply, table, prop.table) for stratified outcome analysis.
- Data visualization: Custom base-R visualizations (grouped boxplots, annotated horizontal stacked bar charts) built for clarity and clinical interpretability rather than default plotting output.
- Reproducible research practices: Literate programming via R Markdown, documenting analytic decisions and caveats (e.g., outlier handling, differences between admission-level vs. stay-level aggregation) inline with the code.
- Collaborative, modular team analytics: Worked from a shared SQL-derived dataset alongside teammates handling separate modeling (Random Forest classifier) and trajectory-clustering (k-means) workstreams, and integrated results into a unified team report and presentation.

# Team: Nat Chairuengjitjaras, Vincent Angelo, Andrew Yu, Mengyao Wang