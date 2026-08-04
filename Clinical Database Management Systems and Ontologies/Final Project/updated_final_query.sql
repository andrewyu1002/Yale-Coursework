-- 1. Identify Sepsis Patients
WITH sepsis AS (
  SELECT DISTINCT subject_id, hadm_id
  FROM `physionet-data.mimiciv_3_1_hosp.diagnoses_icd`
  WHERE (icd_version = 9 AND icd_code IN ('99591','99592','78552'))
     OR (icd_version = 10 AND (icd_code LIKE 'A40%' OR icd_code LIKE 'A41%' OR icd_code LIKE 'R652%'))
),

-- 2. PaO2 measurements (numeric only)
pao2 AS (
  SELECT subject_id, hadm_id, charttime, valuenum AS pao2
  FROM `physionet-data.mimiciv_3_1_hosp.labevents`
  WHERE itemid = 50821 AND valuenum IS NOT NULL
),

-- 3. FiO2 measurements (ICU numeric only)
fio2 AS (
  SELECT subject_id, hadm_id, stay_id, charttime, valuenum AS fio2
  FROM `physionet-data.mimiciv_3_1_icu.chartevents`
  WHERE itemid = 223835 AND valuenum IS NOT NULL AND valuenum > 0
),

-- 4. Attach ICU stay_id and first_careunit to PaO2
pao2_with_stay AS (
  SELECT
    p.subject_id,
    p.hadm_id,
    icu.stay_id,
    icu.first_careunit,
    p.charttime,
    p.pao2
  FROM pao2 p
  JOIN `physionet-data.mimiciv_3_1_icu.icustays` icu
    ON p.subject_id = icu.subject_id
   AND p.hadm_id = icu.hadm_id
   AND p.charttime BETWEEN icu.intime AND icu.outtime
),

-- 5. Compute PF ratio for each matched PaO2/FiO2 within ±30 min
pf_ratio AS (
  SELECT
    p.subject_id,
    p.hadm_id,
    p.stay_id,
    p.first_careunit,
    p.charttime,
    ROUND(p.pao2 / (f.fio2 / 100), 2) AS pf_ratio_numeric
  FROM pao2_with_stay p
  JOIN fio2 f
    ON p.hadm_id = f.hadm_id
   AND p.stay_id = f.stay_id
   AND ABS(TIMESTAMP_DIFF(p.charttime, f.charttime, MINUTE)) <= 30
),

-- 6. Mortality info
mortality AS (
  SELECT
    subject_id,
    hadm_id,
    CASE WHEN deathtime IS NOT NULL THEN 1 ELSE 0 END AS inhospital_death
  FROM `physionet-data.mimiciv_3_1_hosp.admissions`
),

-- 7. Ventilation info
vent AS (
  SELECT
    stay_id,
    starttime,
    endtime,
    ventilation_status
  FROM `physionet-data.mimiciv_3_1_derived.ventilation`
),

-- 8. Compute min PF ratio per stay and its timestamp
min_pf AS (
  SELECT
    subject_id,
    hadm_id,
    stay_id,
    first_careunit,
    MIN(pf_ratio_numeric) AS min_pf_ratio,
    ARRAY_AGG(charttime ORDER BY pf_ratio_numeric ASC LIMIT 1)[OFFSET(0)] AS min_pf_time
  FROM pf_ratio
  GROUP BY subject_id, hadm_id, stay_id, first_careunit
),

-- 9. Compute ARDS severity from min PF ratio
severity_final AS (
  SELECT
    *,
    CASE
      WHEN min_pf_ratio < 100 THEN 'Severe'
      WHEN min_pf_ratio BETWEEN 100 AND 200 THEN 'Moderate'
      WHEN min_pf_ratio BETWEEN 200 AND 300 THEN 'Mild'
      ELSE 'No ARDS'
    END AS ards_severity
  FROM min_pf
),

-- 10. Attach first ventilation event after min PF
vent_after_min_pf AS (
  SELECT
    sf.*,
    v.first_vent.starttime AS vent_starttime,
    v.first_vent.endtime AS vent_endtime,
    v.first_vent.ventilation_status
  FROM severity_final sf
  LEFT JOIN (
    SELECT
      sf2.stay_id,
      sf2.min_pf_time,
      ARRAY_AGG(STRUCT(v.starttime, v.endtime, v.ventilation_status)
                ORDER BY v.starttime ASC LIMIT 1)[OFFSET(0)] AS first_vent
    FROM vent v
    JOIN severity_final sf2
      ON v.stay_id = sf2.stay_id
     AND v.starttime >= sf2.min_pf_time
    GROUP BY sf2.stay_id, sf2.min_pf_time
  ) v
  ON sf.stay_id = v.stay_id
)

-- 11. Final output
SELECT
  s.subject_id,
  s.hadm_id,
  vpmf.stay_id,
  vpmf.first_careunit,
  vpmf.min_pf_ratio,
  vpmf.ards_severity,
  m.inhospital_death,
  vpmf.vent_starttime,
  vpmf.vent_endtime,
  vpmf.ventilation_status
FROM sepsis s
JOIN vent_after_min_pf vpmf
  ON s.hadm_id = vpmf.hadm_id
JOIN mortality m
  ON s.hadm_id = m.hadm_id
ORDER BY s.subject_id, s.hadm_id, vpmf.stay_id;