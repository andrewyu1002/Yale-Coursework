# Description
This report was written for Yale University's Introduction to Health Informatics course. For this project, we were tasked to form a research question and perform analysis using data from the All of Us Research Program.

# Skills Demonstrated:
## Data Engineering & ETL
Built case/control cohorts (16,460 eczema patients; 413K+ population) from the All of Us Controlled Tier database (OMOP-based EHR data). Designed ETL pipeline to unmelt longitudinal survey data and aggregate high-frequency wearable (Fitbit) time-series data into person-level summary statistics. Engineered missing-data strategy treating nulls as informative categorical flags rather than discarding records.
## Machine Learning
Trained a Random Forest classifier (scikit-learn) with class-balancing to handle severe label imbalance. Performed feature importance ranking and dimensionality reduction (20+ features → top 20) with minimal accuracy loss. Conducted ablation testing to isolate the predictive contribution of specific feature groups.
## Algorithmic Fairness & Bias Auditing
Evaluated cross-population generalizability by training on one demographic subgroup (White) and testing on another (Black). Used confusion matrices to quantify false positive/negative rate disparities across populations.
## Data Visualization & Communication
Produced confusion matrix heatmaps and feature-importance tables to present model performance clearly. Translated technical ML results into health-equity insights for a non-technical/policy audience.
## Domain & Policy Analysis
Addressed data privacy, HIPAA-adjacent considerations, and algorithmic bias in the context of a clinical decision-support tool.