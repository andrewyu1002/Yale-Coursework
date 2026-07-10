# Description:
This project analyzed a publicly available personal germline genome (science journalist Carl Zimmer's genome) to identify and characterize the most biologically significant genetic variants on chromosome 22. Starting from a raw VCF file, a Python pipeline was built to filter chromosome-specific variants, annotate them with the Ensembl Variant Effect Predictor (VEP), and rank genes using two independent prioritization strategies: raw mutational burden (variant count per gene) and a custom weighted impact-severity score (based on HIGH/MODERATE/LOW/MODIFIER consequence categories). The top-ranked genes were then cross-referenced against the GTEx tissue expression database and primary literature to connect each gene's expression pattern to its known biological function and disease associations. 

# Skills Demonstrated:
## Bioinformatics pipeline development
Parsed and processed large-scale VCF files using cyvcf2 and pandas in Python.
## Variant annotation
Configured and applied Ensembl VEP to annotate variants with gene symbols, predicted consequence, and impact severity.
## Custom scoring & algorithm design
Designed and implemented a weighted scoring system to rank genes by cumulative variant impact, going beyond simple mutation counts to prioritize functionally relevant targets.
## Comparative data analysis
Cross-validated two independent gene-prioritization methods and reconciled overlapping/divergent results.
## Public genomic database research
Queried and interpreted tissue-specific expression data from the GTEx Portal to support functional hypotheses.
## Scientific literature review & synthesis
Reviewed peer-reviewed publications to connect quantitative genomic findings to established gene function and disease biology.
## Scientific communication
Co-authored a formal written report and delivered a data-driven presentation summarizing methodology, results, and biological implications to a technical audience.
## Collaborative research
Worked within an interdisciplinary team combining programming and non-programming contributors.