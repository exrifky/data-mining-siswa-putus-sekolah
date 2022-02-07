# Final Project Application Testing

Data Visualization GDS\
https://datastudio.google.com/s/tX4QBZ666ZU

Testing using Amazon Web Service\
\
-*bayes-17e255d53554.json* --> For web service purposes between AWS and Google Spreadsheet\
-Python source code *ok.py* is the final source code\
-*requirements.txt* is useful for listing the libraries used\
-*setup.sh* for streamlit installation\
-*sma.png* logo on streamlit main display\

# Hasil Penelitian #
**Problem**\
-The related high school has problems due to the large number of students who have to drop out of school\
-Impacts on schools include a decrease in financial assistance from the government, the number of study groups, and the existence of dependents on students\

**Solution**\
-Early prediction to prevent the student from deciding to drop out of school\

**Dataset**\
-Dataset contains academic and non-academic values \
-Datasets were collected primary (questionnaire) and secondary (student data)\
-The amount of data is 77 rows with 18 rows for dropout students\
-The list of features include
| *Fitur* | *Istilah*  |
| :---:   | :-: |
| *Jenis_Kelamin* | X1 |
| *Nilai_Rerata* | X2 |
| *Mengikuti_Ekstrakurikuler* | X3 |
| *Ikut_Bekerja* | X4 |
| *Mengalami_Broken_Home* | X5 |
| *Jarak_Sekolah* | X6  |
| *Pendidikan_Ayah* | X7 |
| *Pendidikan_Ibu* | X8  |
| *Penghasilan_Ayah* | X9 |
| *Penghasilan_Ibu* | X10 |
| *Penghasilan_Ibu* | *class* |

**Methodology**\
-Using Bayesian Network (BN) for the main model\
-BN can help see the most dominant features in the case of dropout students\
-Utilizing Amazon Web Service for hosting, so that it can be accessed online\
![alt text](https://i.ibb.co/pfSk5p4/Group-65.png)\

**Result**\
-Pendidikan_Ayah (X9), Nilai_Rerata (X2), and Mengikuti_Ekstrakurikuler (X3) are the main factors for dropping out of school
![alt text](https://i.ibb.co/h9FNP07/Bayesian-Networks-Modelling-5.png)\
-The results of the Bayesian Network model are as follows
| *Accuracy* | *Precision*  | *Recall*  | *F1-Score*  | *AUC*  |
| :---: | :-: | :-: | :-: | :-: |
| 0.935 | 0.100 | 0.722 | 0.839 | 0.938 |

**Limitation**\
-Limitations from research using datasets that do not have a balanced distribution, so that future research can use resampling\
-Optimization of BN structure creation such as using PSO
