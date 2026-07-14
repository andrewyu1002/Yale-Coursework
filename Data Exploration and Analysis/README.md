# Homework 1
## Description:
This project demonstrates foundational data analysis skills in R using a real-world World Bank dataset covering economic and social indicators across countries. The work includes importing and inspecting data, subsetting and summarizing it, generating custom visualizations, working with nested list structures, and outlining a data-cleaning strategy for a large, messy, multi-year civic dataset.

## Skills Demonstrated:
Data Import & Inspection: Loaded external CSV data directly from a URL into R; inspected structure, dimensions, variable names, and data types.
Data Wrangling: Subset and filtered data based on conditional logic.
Descriptive Statistics: Generated and manipulated summary statistics, including indexing and rounding numeric output.
Data Visualization: Built customized scatterplots and multi-variable boxplots in base R, including titles, axis labels, custom colors, and plot symbols to effectively communicate relationships in the data.
R Data Structures: Worked with nested lists, distinguishing between list-based and vector-based subsetting ([ ] vs [[ ]]).
R Syntax & Best Practices: Refactored code to follow clean, readable R coding conventions.
RMarkdown Authoring: Produced a reproducible, formatted technical document combining code, output, and narrative text using RMarkdown (knit to HTML/PDF/Word).
Analytical Problem-Solving: Designed a step-by-step data-cleaning and exploratory-analysis plan (pseudocode) for a large, messy, multi-department municipal dataset with missing and inconsistent data.

# Homework 2
## Description:
This project explores a large, real-world OKCupid dating profile dataset using R. The dataset was originally published in an academic study by Kirkegaard and Bjerrekaer and includes demographic information, dating profile responses, and psychometric scale scores. The analysis covers the full data science workflow on messy, high-dimensional survey data.

## Skills Demonstrated:
Data Import & Formats: Reading Parquet files (arrow package) and delimited CSVs into R data frames; working with column-oriented data storage.
Exploratory Data Analysis: Profiling dataset dimensions, variable names, and data types; identifying and quantifying missing data across rows and columns.
Data Cleaning & Feature Engineering: Writing custom parsing functions to convert inconsistent, free-text categorical data (e.g., income ranges) into clean numeric variables.
String Manipulation: Using grepl(), gsub(), strsplit(), and substr() for pattern matching, text cleaning, and field extraction.
Data Wrangling: Filtering, subsetting, and combining logical conditions with %in% and substr(); building one-way and two-way contingency tables.
Statistical Summarization: Computing summary statistics, standard deviations, and group-wise comparisons.
Data Visualization: Creating and formatting histograms, horizontal and grouped bar plots, and scatterplots in base R; customizing labels, colors, legends, margins, and text annotations for readability.

# Homework 3
## Description:
This project demonstrates end-to-end data cleaning and statistical analysis in R, using a real-world, messy survey dataset (open-ended "favorite food" responses from ~200+ respondents). The work spans three areas: manipulating nested list/matrix data structures, simulating and visualizing probability distributions, and cleaning unstructured text survey data into a coherent categorical variable ready for analysis. 

## Skills Demonstrated:
Data structure manipulation: Indexing and subsetting nested lists, matrices, and vectors in R using [], [[]], and [,] notation; applying functions across matrix dimensions with apply().
Text/data cleaning: Standardizing messy, free-text survey data through case normalization, whitespace and punctuation removal, and regular expressions (gsub(), sub()) to consolidate inconsistent entries into standardized categories.
Pattern matching & regex: Writing and iterating regular expressions to detect and unify string variants.
Categorical data aggregation: Building custom mapping logic and iterative loops to recode and consolidate low-frequency categories into broader groupings, including a rule-based "miscellaneous" catch-all.
Programmatic workflow design: Writing loops to apply repeated transformations across a vector of search terms rather than hardcoding each case individually.
Statistical simulation: Generating random samples from binomial distributions (rbinom()) and assessing normal approximation conditions (np > 10, n(1−p) > 10).
Data visualization: Creating normal quantile plots (qqPlot()) and customized horizontal bar charts (barplot()) with formatted labels, margins, colors, and titles.