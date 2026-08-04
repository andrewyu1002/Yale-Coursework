DROP TABLE IF EXISTS 	cbb6380-final-project.5790_analysis.CBB5790_FinalProject;
CREATE TABLE 	cbb6380-final-project.5790_analysis.CBB5790_FinalProject AS
SELECT DISTINCT
  icu.subject_id,
  icu.hadm_id,
  icu.stay_id,
  a.insurance,
  a.language,
  a.marital_status,
  a.race,
  p.anchor_age,
  p.gender,
  d.icd_code,
  d.icd_version,
  icu.first_careunit,
  icu.los AS icu_length_of_stay,
  a.hospital_expire_flag AS outcome_death, 

  -- Renal-Specific Lab Results
  labs.creatinine_min,
  labs.creatinine_max, 
  labs.bun_min,        
  labs.bun_max,
  labs.potassium_min,
  labs.potassium_max,
  labs.bicarbonate_min,
  labs.bicarbonate_max,
  labs.sodium_min,
  labs.sodium_max,

  -- Vital Signs
  vitals.mbp_min,    
  -- Changed mbp_avg to mbp_mean since I believe that's the correct notation  
  vitals.mbp_mean,
  vitals.mbp_max, 
  vitals.heart_rate_max,
  vitals.heart_rate_min,
  
  -- Urine Output & AKI Staging (Adding these since you joined the tables)
  uo.urineoutput AS urineoutput_24hr,
  -- Changed aki_stage_kdigo to just aki_stage. I assume this is the correct one
  kdigo.aki_stage AS kdigo_stage

FROM `physionet-data.mimiciv_3_1_icu.icustays` AS icu
JOIN `physionet-data.mimiciv_3_1_hosp.admissions` AS a
  ON icu.hadm_id = a.hadm_id
JOIN `physionet-data.mimiciv_3_1_hosp.patients` AS p
  ON icu.subject_id = p.subject_id
JOIN `physionet-data.mimiciv_3_1_hosp.diagnoses_icd` AS d
  ON a.hadm_id = d.hadm_id

-- Derived tables usually don't have the version number in the official PhysioNet DB
LEFT JOIN `physionet-data.mimiciv_3_1_derived.first_day_lab` AS labs
  ON icu.stay_id = labs.stay_id
LEFT JOIN `physionet-data.mimiciv_3_1_derived.first_day_vitalsign` AS vitals
  ON icu.stay_id = vitals.stay_id
LEFT JOIN `physionet-data.mimiciv_3_1_derived.first_day_urine_output` AS uo
  ON icu.stay_id = uo.stay_id
LEFT JOIN `physionet-data.mimiciv_3_1_derived.kdigo_stages` AS kdigo
  ON icu.stay_id = kdigo.stay_id

WHERE d.icd_code IN (
  '5845', '5846', '5847', '5848', '5849', 
  'N17', 'N170', 'N171', 'N172', 'N178', 'N179'
)



