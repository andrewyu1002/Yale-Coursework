# Description:
This project builds an end-to-end clinical data pipeline using the MIMIC-IV Demo dataset, a de-identified subset of the MIMIC-IV critical care database. It demonstrates the full workflow of setting up a relational database in the cloud, loading real-world healthcare data, querying it with SQL, and visualizing the results in Python.

# Skills Demonstrated:
- Provisioned an Azure SQL Database (MIMIC_IV_DEMO) to host the clinical tables.
- Imported four MIMIC-IV tables via Azure Data Studio's Import Wizard:
  - patients.csv
  - admissions.csv
  - diagnoses_icd.csv
  - d_icd_diagnoses.csv
- Configured a server-side firewall rule so the database could be securely accessed from an external client (Google Colab).
- Connected to the database from Python (via pymssql) and wrote a SQL query that joins the diagnosis and admissions tables to count the number of unique subjects (patients) per diagnosis, filtered to diagnoses with ≥20 subjects.
- Visualized the results with Matplotlib, producing both a pie chart and a bar chart of diagnosis frequency across subjects.