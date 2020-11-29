# Heart-Disease---Search-for-risk-factors

# Introduction
Data science is at the forefront in medicine. The classical area of heart disease diagnosis is a critical process step. The analysed dataset contains a range of symptoms and as the a result variable if the condition is malignent or benign.

# Objectives
The target is to analyse the data and generate a model which predicts based on the input variables if the condition of the patient is malignent or benign. Items to investigate:

Age distibution of the patients
Chest pain vs. diagnosis - gender comparison
Precision of prediction algorithm
Approach
Data import
Data cleaning and preparation
Modelling
Evaluation
Data
The Cleveland database was provided by in Kaggle.

# Creators:

Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation: Robert Detrano, M.D., Ph.D. Donor:
David W. Aha (aha '@' ics.uci.edu) (714) 856-8779

# PARAMETERS
age
sex
chest pain type (4 values)
resting blood pressure
serum cholestoral in mg/dl
fasting blood sugar > 120 mg/dl
resting electrocardiographic results (values 0,1,2)
maximum heart rate achieved
exercise induced angina
oldpeak = ST depression induced by exercise relative to rest
the slope of the peak exercise ST segment
number of major vessels (0-3) colored by flourosopy
thal: 3 = normal; 6 = fixed defect; 7 = reversable defect

All details are contained in the notebook.

# Evaluation
Age distibution of the patients
![Age_Dist](C:\Users\demhumm\Documents\MH\Data\Heart-Disease---Search-for-risk-factors\age_dist.png)
age distribution

The mean of the patients' age is end 50 with a peak at round about 60.

Chest pain vs. diagnosis - gender comparison

cp_diagnosis_gender

Males (flag 1) show an increase of chest pain (cp) while at the same time the likelyhood of a serious condition drops. For woman (flag 0) is the trend reversed.



# References and links
Dataset in [Kaggle](https://www.kaggle.com/ronitf/heart-disease-uci).


