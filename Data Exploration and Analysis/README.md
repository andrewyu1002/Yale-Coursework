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

# Homework 4
## Description:
This project is an R Markdown analysis exploring core inferential statistics concepts through hands-on programming and simulation. It combines custom iterative algorithms, Monte Carlo simulation of sampling distributions, and bootstrap resampling methods to analyze real-world environmental and economic datasets. The work demonstrates the ability to translate statistical theory into working code, validate theoretical results against simulated data, and communicate findings clearly through visualizations and written interpretation.

## Skills Demonstrated:
Programming & Data Wrangling: Writing custom for loops to generate sequences (Tribonacci numbers) and compute column-wise summary statistics across a dataframe. Reading and cleaning external CSV data directly from URLs. Vectorized computation using apply()/tapply() for row- and group-wise summary statistics.
Statistical Simulation: Simulating sampling distributions via repeated random sampling from theoretical distributions. Empirically validating the Central Limit Theorem by comparing simulated standard errors to theoretical predictions. Comparing the behavior of sample means, medians, and variances under repeated sampling.
Bootstrap Resampling & Inference: Constructing bootstrap resampling procedures from scratch to estimate confidence intervals for differences in means. Comparing bootstrap confidence intervals to parametric (t-test based) confidence intervals. Applying log transformations to address skewed data and improve normality assumptions.
Hypothesis Testing: Conducting and interpreting two-sample t-tests at custom significance levels. Assessing statistical significance using both p-values and confidence intervals. Evaluating distributional assumptions using normal quantile plots.
Data Visualization: Building histograms, boxplots, and overlaid density plots with custom colors, line types, and legends in base R. Designing multi-distribution comparison plots to visualize how parameters affect distribution shape.

# Homework 5
## Description:
An R-based data analysis project examining two independent datasets: runner performance from the New Haven Road Race 5K across the 2017 and 2018 race years, and global measles vaccination rates from 2016 to 2024 in relation to national income levels. The project builds a reusable data-cleaning function to standardize raw race-timing data, merges cross-year records to identify repeat participants and measure individual performance changes, and applies bootstrap resampling and permutation testing to evaluate whether vaccination rate changes differ significantly between high- and low-income countries. 

## Skills Demonstrated:
Custom Function Development (R): Wrote a reusable cleanNHData() function to standardize and clean raw datasets, including handling missing values, deriving new variables from existing fields, and converting inconsistently formatted time strings using conditional logic.
Data Wrangling & Cleaning: Deduplicated records, filtered missing/invalid observations, and reshaped raw CSV data into analysis-ready formats using base R (subset, logical indexing, substr()).
Data Merging & Integration: Combined multiple datasets across years using merge(), intersect(), and %in% to construct matched longitudinal records for repeat observations.
Exploratory Data Analysis: Produced summary statistics, histograms, and side-by-side boxplots to visualize distributions and compare subgroups.
Statistical Inference: Constructed bootstrap confidence intervals and conducted permutation (randomization) hypothesis tests to assess differences in medians/means between groups without relying on parametric assumptions.
Hypothesis Testing & Interpretation: Framed null and alternative hypotheses, selected appropriate significance thresholds, and drew data-supported conclusions from simulation-based test results.
Data Visualization: Created labeled histograms and boxplots with reference lines using R base graphics to communicate statistical findings clearly.

# Homework 6
## Description
This project applies correlation analysis techniques in R to three real-world datasets: road race finishing times, World Bank CO2 emissions/energy use data, and a class survey dataset. The analysis includes custom statistical functions for permutation testing, bootstrap resampling for confidence intervals, and data cleaning of messy real-world variables.

## Skills Demonstrated
Statistical Inference: Permutation testing and bootstrap resampling to construct confidence intervals and evaluate significance of correlation coefficients.
Data Cleaning & Wrangling: Handling inconsistent/messy data (out-of-range values, mixed text/numeric fields, missing data) using base R and regular expressions.
Exploratory Data Analysis: Identifying and interpreting outliers, assessing distribution shape and skewness, and evaluating the appropriateness of statistical measures given data characteristics.
Data Visualization: Custom scatterplots, histograms, jittered plots, and frequency-scaled bubble plots using base R graphics; correlation matrix visualization with corrplot and PerformanceAnalytics.
Custom Function Development: Writing reusable R functions (myCor(), permCor(), cleanIt()) to standardize analysis workflows.
Log Transformation: Applying and interpreting log transformations to normalize skewed distributions and improve correlation analysis.