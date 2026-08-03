# Description:
This project builds an end-to-end pipeline that connects a biomedical ontology to a real clinical database in order to profile disease cohorts. It integrates the Human Disease Ontology (DOID), accessed through the EBI Ontology Lookup Service (OLS) REST API, with the MIMIC-IV critical care database hosted on Google BigQuery.

For three disease groups — Kidney Disease, Lung Disease, and Liver Disease — the pipeline:
1. Queries the OLS API for all hierarchical descendant terms under each disease group's root DOID.
2. Extracts each term's DOID identifier and, where available, its mapped ICD-10-CM code from the ontology's cross-reference annotations (terms without an ICD-10 mapping are skipped).
3. Writes the results to a tab-delimited lookup file (Group, Term, DOID, ICD10Code).
4. Loads that file into BigQuery as a reference table.
5. Joins the reference table against physionet-data.mimiciv_hosp.diagnoses_icd to count unique patients per disease group.
6. Extends the join to the patients and admissions tables to pull demographic attributes (gender, race).
7. Visualizes the resulting demographic breakdowns per disease group as grouped bar charts using matplotlib/seaborn.

# Skills Demonstrated
- REST API integration: Paginated GET requests to an external ontology web service (OLS), parsing nested JSON responses and extracting cross-database references.
- Ontology/terminology mapping: Working with hierarchical biomedical ontologies (DOID) and mapping concepts to clinical coding systems (ICD-10-CM).
- Data engineering / ETL: Structuring scraped API data into a clean tabular format and loading it into a cloud data warehouse (BigQuery).
- SQL & data warehousing: Writing multi-table JOIN queries (CTEs, aggregation, GROUP BY) against a large real-world clinical database (MIMIC-IV, tens of millions of records).
- Cloud platform usage: Authenticating and querying Google BigQuery from a Python/Colab environment.
- Healthcare/clinical data analysis: Cohort identification and demographic stratification using real de-identified EHR data, a core skill for health informatics and clinical data science roles.
- Data visualization: Communicating cohort demographic distributions clearly using grouped bar charts.