import base64
import numpy as np
import streamlit as st
import pandas as pd
from pomegranate import *
import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]
creds = ServiceAccountCredentials.from_json_keyfile_name(
    "bayes-17e255d53554.json", scope
)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Data SMAS Islam Al Wahid").sheet1

namaIndex = [
    "X1_Jenis_Kelamin",
    "X2_Nilai_Rerata",
    "X3_Mengikuti_Ekstrakurikuler",
    "X4_Ikut_Bekerja",
    "X5_Mengalami_Broken_Home",
    "X6_Jarak_Sekolah",
    "X7_Pendidikan_Ayah",
    "X8_Pendidikan_Ibu",
    "X9_Penghasilan_Ayah",
    "X10_Penghasilan_Ibu",
    "Class_Putus",
]

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()
df = pd.DataFrame(list_of_hashes, columns=namaIndex)
totalValue = df.shape[0]

# X1 Jenis Kelamin
if (
    len(df[df["X1_Jenis_Kelamin"].str.contains("Laki_laki_1")]) == 0
    or len(df[df["X1_Jenis_Kelamin"].str.contains("Perempuan_2")]) == 0
):
    jk1 = (len(df[df["X1_Jenis_Kelamin"].str.contains("Laki_laki_1")]) + 1) / (
        totalValue + 2
    )
    jk2 = (len(df[df["X1_Jenis_Kelamin"].str.contains("Perempuan_2")]) + 1) / (
        totalValue + 2
    )
else:
    jk1 = (
        len(df[df["X1_Jenis_Kelamin"].str.contains("Laki_laki_1")])) / totalValue
    jk2 = (
        len(df[df["X1_Jenis_Kelamin"].str.contains("Perempuan_2")])) / totalValue

X1_Jenis_Kelamin = DiscreteDistribution(
    {"Laki_laki_1": jk1, "Perempuan_2": jk2})

# X2 Nilai Rerata
if (
    len(df[df["X2_Nilai_Rerata"].str.contains("C_1")]) == 0
    or len(df[df["X2_Nilai_Rerata"].str.contains("B_2")]) == 0
):
    nilai1 = (
        len(df[df["X2_Nilai_Rerata"].str.contains("C_1")]) + 1) / (totalValue + 2)
    nilai2 = (
        len(df[df["X2_Nilai_Rerata"].str.contains("B_2")]) + 1) / (totalValue + 2)
else:
    nilai1 = (len(df[df["X2_Nilai_Rerata"].str.contains("C_1")])) / totalValue
    nilai2 = (len(df[df["X2_Nilai_Rerata"].str.contains("B_2")])) / totalValue

X2_Nilai_Rerata = DiscreteDistribution({"C_1": nilai1, "B_2": nilai2})

# X5 Mengalami Broken Home
if (
    len(df[df["X5_Mengalami_Broken_Home"].str.contains("Tidak_0")]) == 0
    or len(df[df["X5_Mengalami_Broken_Home"].str.contains("Iya_1")]) == 0
):
    broken1 = (len(df[df["X5_Mengalami_Broken_Home"].str.contains("Tidak_0")]) + 1) / (
        totalValue + 2
    )
    broken2 = (len(df[df["X5_Mengalami_Broken_Home"].str.contains("Iya_1")]) + 1) / (
        totalValue + 2
    )
else:
    broken1 = (
        len(df[df["X5_Mengalami_Broken_Home"].str.contains("Tidak_0")])
    ) / totalValue
    broken2 = (
        len(df[df["X5_Mengalami_Broken_Home"].str.contains("Iya_1")])
    ) / totalValue

X5_Mengalami_Broken_Home = DiscreteDistribution(
    {"Tidak_0": broken1, "Iya_1": broken2})

# X6 Jarak Sekolah
if (
    len(df[df["X6_Jarak_Sekolah"].str.contains("Dekat_1")]) == 0
    or len(df[df["X6_Jarak_Sekolah"].str.contains("Sedang_2")]) == 0
    or len(df[df["X6_Jarak_Sekolah"].str.contains("Jauh_3")]) == 0
):
    jarak1 = (len(df[df["X6_Jarak_Sekolah"].str.contains("Dekat_1")]) + 1) / (
        totalValue + 3
    )
    jarak2 = (len(df[df["X6_Jarak_Sekolah"].str.contains("Sedang_2")]) + 1) / (
        totalValue + 3
    )
    jarak3 = (len(df[df["X6_Jarak_Sekolah"].str.contains("Jauh_3")]) + 1) / (
        totalValue + 3
    )
else:
    jarak1 = (
        len(df[df["X6_Jarak_Sekolah"].str.contains("Dekat_1")])) / totalValue
    jarak2 = (
        len(df[df["X6_Jarak_Sekolah"].str.contains("Sedang_2")])) / totalValue
    jarak3 = (
        len(df[df["X6_Jarak_Sekolah"].str.contains("Jauh_3")])) / totalValue

X6_Jarak_Sekolah = DiscreteDistribution(
    {"Dekat_1": jarak1, "Sedang_2": jarak2, "Jauh_3": jarak3}
)

# X8 Pendidikan Ibu
if (
    len(df[df["X8_Pendidikan_Ibu"].str.contains("Yang_Lainnya_1")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("SD_2")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("SMP_3")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("SMA_4")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("D1_D4_5")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("S1_S3_6")]) == 0
):
    pdkIbu0 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("Yang_Lainnya_1")]) + 1) / (
        totalValue + 6
    )
    pdkIbu1 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("SD_2")]) + 1) / (
        totalValue + 6
    )
    pdkIbu2 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("SMP_3")]) + 1) / (
        totalValue + 6
    )
    pdkIbu3 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("SMA_4")]) + 1) / (
        totalValue + 6
    )
    pdkIbu4 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("D1_D4_5")]) + 1) / (
        totalValue + 6
    )
    pdkIbu5 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("S1_S3_6")]) + 1) / (
        totalValue + 6
    )
else:
    pdkIbu0 = (
        len(df[df["X8_Pendidikan_Ibu"].str.contains("Yang_Lainnya_1")])
    ) / totalValue
    pdkIbu1 = (
        len(df[df["X8_Pendidikan_Ibu"].str.contains("SD_2")])) / totalValue
    pdkIbu2 = (
        len(df[df["X8_Pendidikan_Ibu"].str.contains("SMP_3")])) / totalValue
    pdkIbu3 = (
        len(df[df["X8_Pendidikan_Ibu"].str.contains("SMA_4")])) / totalValue
    pdkIbu4 = (
        len(df[df["X8_Pendidikan_Ibu"].str.contains("D1_D4_5")])) / totalValue
    pdkIbu5 = (
        len(df[df["X8_Pendidikan_Ibu"].str.contains("S1_S3_6")])) / totalValue

X8_Pendidikan_Ibu = DiscreteDistribution(
    {
        "Yang_Lainnya_1": pdkIbu0,
        "SD_2": pdkIbu1,
        "SMP_3": pdkIbu2,
        "SMA_4": pdkIbu3,
        "D1_D4_5": pdkIbu4,
        "S1_S3_6": pdkIbu5,
    }
)

# X10 Penghasilan Ibu
if (
    len(df[df["X10_Penghasilan_Ibu"].str.contains("Tidak_Bekerja_1")]) == 0
    or len(df[df["X10_Penghasilan_Ibu"].str.contains("Rendah_2")]) == 0
    or len(df[df["X10_Penghasilan_Ibu"].str.contains("Sedang_3")]) == 0
    or len(df[df["X10_Penghasilan_Ibu"].str.contains("Tinggi_4")]) == 0
):
    phsIbu0 = (
        len(df[df["X10_Penghasilan_Ibu"].str.contains("Tidak_Bekerja_1")]) + 1
    ) / (totalValue + 4)
    phsIbu1 = (len(df[df["X10_Penghasilan_Ibu"].str.contains("Rendah_2")]) + 1) / (
        totalValue + 4
    )
    phsIbu2 = (len(df[df["X10_Penghasilan_Ibu"].str.contains("Sedang_3")]) + 1) / (
        totalValue + 4
    )
    phsIbu3 = (len(df[df["X10_Penghasilan_Ibu"].str.contains("Tinggi_4")]) + 1) / (
        totalValue + 4
    )
else:
    phsIbu0 = (
        len(df[df["X10_Penghasilan_Ibu"].str.contains("Tidak_Bekerja_1")])
    ) / totalValue
    phsIbu1 = (
        len(df[df["X10_Penghasilan_Ibu"].str.contains("Rendah_2")])) / totalValue
    phsIbu2 = (
        len(df[df["X10_Penghasilan_Ibu"].str.contains("Sedang_3")])) / totalValue
    phsIbu3 = (
        len(df[df["X10_Penghasilan_Ibu"].str.contains("Tinggi_4")])) / totalValue

X10_Penghasilan_Ibu = DiscreteDistribution(
    {
        "Tidak_Bekerja_1": phsIbu0,
        "Rendah_2": phsIbu1,
        "Sedang_3": phsIbu2,
        "Tinggi_4": phsIbu3,
    }
)

# X4 Ikut Bekerja
hitung1 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Tidak_Bekerja_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung2 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Tidak_Bekerja_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]
hitung3 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Rendah_2")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung4 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Rendah_2")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]
hitung5 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Sedang_3")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung6 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Sedang_3")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]
hitung7 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Tinggi_4")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung8 = df[
    (df["X1_Jenis_Kelamin"] == "Laki_laki_1")
    & (df["X10_Penghasilan_Ibu"] == "Tinggi_4")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]
#
hitung11 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Tidak_Bekerja_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung12 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Tidak_Bekerja_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]
hitung13 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Rendah_2")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung14 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Rendah_2")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]
hitung15 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Sedang_3")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung16 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Sedang_3")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]
hitung17 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Tinggi_4")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
].shape[0]
hitung18 = df[
    (df["X1_Jenis_Kelamin"] == "Perempuan_2")
    & (df["X10_Penghasilan_Ibu"] == "Tinggi_4")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
].shape[0]

if hitung1 == 0 or hitung2 == 0:
    hitung1 += 1
    hitung2 += 1
if hitung3 == 0 or hitung4 == 0:
    hitung3 += 1
    hitung4 += 1

if hitung5 == 0 or hitung6 == 0:
    hitung5 += 1
    hitung6 += 1

if hitung7 == 0 or hitung8 == 0:
    hitung7 += 1
    hitung8 += 1

if hitung11 == 0 or hitung12 == 0:
    hitung11 += 1
    hitung12 += 1

if hitung13 == 0 or hitung14 == 0:
    hitung13 += 1
    hitung14 += 1

if hitung15 == 0 or hitung16 == 0:
    hitung15 += 1
    hitung16 += 1

if hitung17 == 0 or hitung18 == 0:
    hitung17 += 1
    hitung18 += 1

data1 = hitung1 / (hitung1 + hitung2)
data2 = hitung2 / (hitung1 + hitung2)
data3 = hitung3 / (hitung3 + hitung4)
data4 = hitung4 / (hitung3 + hitung4)
data5 = hitung5 / (hitung5 + hitung6)
data6 = hitung6 / (hitung5 + hitung6)
data7 = hitung7 / (hitung7 + hitung8)
data8 = hitung8 / (hitung7 + hitung8)
data11 = hitung11 / (hitung11 + hitung12)
data12 = hitung12 / (hitung11 + hitung12)
data13 = hitung13 / (hitung13 + hitung14)
data14 = hitung14 / (hitung13 + hitung14)
data15 = hitung15 / (hitung15 + hitung16)
data16 = hitung16 / (hitung15 + hitung16)
data17 = hitung17 / (hitung17 + hitung18)
data18 = hitung18 / (hitung17 + hitung18)

# Input CPT
X4_Ikut_Bekerja = ConditionalProbabilityTable(
    [
        ["Laki_laki_1", "Tidak_Bekerja_1", "Tidak_0", data1],
        ["Laki_laki_1", "Tidak_Bekerja_1", "Iya_1", data2],
        ["Laki_laki_1", "Rendah_2", "Tidak_0", data3],
        ["Laki_laki_1", "Rendah_2", "Iya_1", data4],
        ["Laki_laki_1", "Sedang_3", "Tidak_0", data5],
        ["Laki_laki_1", "Sedang_3", "Iya_1", data6],
        ["Laki_laki_1", "Tinggi_4", "Tidak_0", data7],
        ["Laki_laki_1", "Tinggi_4", "Iya_1", data8],
        ["Perempuan_2", "Tidak_Bekerja_1", "Tidak_0", data11],
        ["Perempuan_2", "Tidak_Bekerja_1", "Iya_1", data12],
        ["Perempuan_2", "Rendah_2", "Tidak_0", data13],
        ["Perempuan_2", "Rendah_2", "Iya_1", data14],
        ["Perempuan_2", "Sedang_3", "Tidak_0", data15],
        ["Perempuan_2", "Sedang_3", "Iya_1", data16],
        ["Perempuan_2", "Tinggi_4", "Tidak_0", data17],
        ["Perempuan_2", "Tinggi_4", "Iya_1", data18],
    ],
    [X1_Jenis_Kelamin, X10_Penghasilan_Ibu],
)

# X7 Pendidikan Ayah
hitung1 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung2 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1") & (
        df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung3 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1")
    & (df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung4 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1")
    & (df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung5 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1")
    & (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung6 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1")
    & (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung7 = df[
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (
        df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung8 = df[
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung9 = df[
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung10 = df[
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung11 = df[
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (
        df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung12 = df[
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (
        df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung13 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung14 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung15 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (
        df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung16 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (
        df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung17 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (
        df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung18 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (
        df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung19 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung20 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung21 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (
        df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung22 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (
        df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung23 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (
        df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung24 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (
        df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung25 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung26 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (
        df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung27 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (
        df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung28 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (
        df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung29 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (
        df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung30 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (
        df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung31 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung32 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (
        df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung33 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (
        df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung34 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (
        df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung35 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (
        df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung36 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (
        df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

if (
    hitung1 == 0
    or hitung2 == 0
    or hitung3 == 0
    or hitung4 == 0
    or hitung5 == 0
    or hitung6 == 0
):
    hitung1 += 1
    hitung2 += 1
    hitung3 += 1
    hitung4 += 1
    hitung5 += 1
    hitung6 += 1

if (
    hitung7 == 0
    or hitung8 == 0
    or hitung9 == 0
    or hitung10 == 0
    or hitung11 == 0
    or hitung12 == 0
):
    hitung7 += 1
    hitung8 += 1
    hitung9 += 1
    hitung10 += 1
    hitung11 += 1
    hitung12 += 1

if (
    hitung13 == 0
    or hitung14 == 0
    or hitung15 == 0
    or hitung16 == 0
    or hitung17 == 0
    or hitung18 == 0
):
    hitung13 += 1
    hitung14 += 1
    hitung15 += 1
    hitung16 += 1
    hitung17 += 1
    hitung18 += 1

if (
    hitung19 == 0
    or hitung20 == 0
    or hitung21 == 0
    or hitung22 == 0
    or hitung23 == 0
    or hitung24 == 0
):
    hitung19 += 1
    hitung20 += 1
    hitung21 += 1
    hitung22 += 1
    hitung23 += 1
    hitung24 += 1

if (
    hitung25 == 0
    or hitung26 == 0
    or hitung27 == 0
    or hitung28 == 0
    or hitung29 == 0
    or hitung30 == 0
):
    hitung25 += 1
    hitung26 += 1
    hitung27 += 1
    hitung28 += 1
    hitung29 += 1
    hitung30 += 1

if (
    hitung31 == 0
    or hitung32 == 0
    or hitung33 == 0
    or hitung34 == 0
    or hitung35 == 0
    or hitung36 == 0
):
    hitung31 += 1
    hitung32 += 1
    hitung33 += 1
    hitung34 += 1
    hitung35 += 1
    hitung36 += 1

pembagi1 = hitung1 + hitung2 + hitung3 + hitung4 + hitung5 + hitung6
pembagi2 = hitung7 + hitung8 + hitung9 + hitung10 + hitung11 + hitung12
pembagi3 = hitung13 + hitung14 + hitung15 + hitung16 + hitung17 + hitung18
pembagi4 = hitung19 + hitung20 + hitung21 + hitung22 + hitung23 + hitung24
pembagi5 = hitung25 + hitung26 + hitung27 + hitung28 + hitung29 + hitung30
pembagi6 = hitung31 + hitung32 + hitung33 + hitung34 + hitung3 + hitung36

data1 = hitung1 / pembagi1
data2 = hitung2 / pembagi1
data3 = hitung3 / pembagi1
data4 = hitung4 / pembagi1
data5 = hitung5 / pembagi1
data6 = hitung6 / pembagi1
data7 = hitung7 / pembagi2
data8 = hitung8 / pembagi2
data9 = hitung9 / pembagi2
data10 = hitung10 / pembagi2
data11 = hitung11 / pembagi2
data12 = hitung12 / pembagi2
data13 = hitung13 / pembagi3
data14 = hitung14 / pembagi3
data15 = hitung15 / pembagi3
data16 = hitung16 / pembagi3
data17 = hitung17 / pembagi3
data18 = hitung18 / pembagi3
data19 = hitung19 / pembagi4
data20 = hitung20 / pembagi4
data21 = hitung21 / pembagi4
data22 = hitung22 / pembagi4
data23 = hitung23 / pembagi4
data24 = hitung24 / pembagi4
data25 = hitung25 / pembagi5
data26 = hitung26 / pembagi5
data27 = hitung27 / pembagi5
data28 = hitung28 / pembagi5
data29 = hitung29 / pembagi5
data30 = hitung30 / pembagi5
data31 = hitung31 / pembagi6
data32 = hitung32 / pembagi6
data33 = hitung33 / pembagi6
data34 = hitung34 / pembagi6
data35 = hitung35 / pembagi6
data36 = hitung36 / pembagi6

# Input CPT
X7_Pendidikan_Ayah = ConditionalProbabilityTable(
    [
        ["Yang_Lainnya_1", "Yang_Lainnya_1", data1],
        ["Yang_Lainnya_1", "SD_2", data2],
        ["Yang_Lainnya_1", "SMP_3", data3],
        ["Yang_Lainnya_1", "SMA_4", data4],
        ["Yang_Lainnya_1", "D1_D4_5", data5],
        ["Yang_Lainnya_1", "S1_S3_6", data6],
        ["SD_2", "Yang_Lainnya_1", data7],
        ["SD_2", "SD_2", data8],
        ["SD_2", "SMP_3", data9],
        ["SD_2", "SMA_4", data10],
        ["SD_2", "D1_D4_5", data11],
        ["SD_2", "S1_S3_6", data12],
        ["SMP_3", "Yang_Lainnya_1", data13],
        ["SMP_3", "SD_2", data14],
        ["SMP_3", "SMP_3", data15],
        ["SMP_3", "SMA_4", data16],
        ["SMP_3", "D1_D4_5", data17],
        ["SMP_3", "S1_S3_6", data18],
        ["SMA_4", "Yang_Lainnya_1", data19],
        ["SMA_4", "SD_2", data20],
        ["SMA_4", "SMP_3", data21],
        ["SMA_4", "SMA_4", data22],
        ["SMA_4", "D1_D4_5", data23],
        ["SMA_4", "S1_S3_6", data24],
        ["D1_D4_5", "Yang_Lainnya_1", data25],
        ["D1_D4_5", "SD_2", data26],
        ["D1_D4_5", "SMP_3", data27],
        ["D1_D4_5", "SMA_4", data28],
        ["D1_D4_5", "D1_D4_5", data29],
        ["D1_D4_5", "S1_S3_6", data30],
        ["S1_S3_6", "Yang_Lainnya_1", data31],
        ["S1_S3_6", "SD_2", data32],
        ["S1_S3_6", "SMP_3", data33],
        ["S1_S3_6", "SMA_4", data34],
        ["S1_S3_6", "D1_D4_5", data35],
        ["S1_S3_6", "S1_S3_6", data36],
    ],
    [X8_Pendidikan_Ibu],
)

# X9 Penghasilan Ayah
hitung1 = df[
    (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung2 = df[
    (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
    & (df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung3 = df[
    (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
    & (df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung4 = df[
    (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
    & (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung5 = df[
    (df["X7_Pendidikan_Ayah"] == "SD_2")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung6 = df[
    (df["X7_Pendidikan_Ayah"] == "SD_2") & (
        df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung7 = df[
    (df["X7_Pendidikan_Ayah"] == "SD_2") & (
        df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung8 = df[
    (df["X7_Pendidikan_Ayah"] == "SD_2") & (
        df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung9 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung10 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3") & (
        df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung11 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3") & (
        df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung12 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3") & (
        df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung13 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung14 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4") & (
        df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung15 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4") & (
        df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung16 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4") & (
        df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung17 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung18 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5") & (
        df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung19 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5") & (
        df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung20 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5") & (
        df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung21 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung22 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6") & (
        df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung23 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6") & (
        df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung24 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6") & (
        df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

if hitung1 == 0 or hitung2 == 0 or hitung3 == 0 or hitung4 == 0:
    hitung1 += 1
    hitung2 += 1
    hitung3 += 1
    hitung4 += 1

if hitung5 == 0 or hitung6 == 0 or hitung7 == 0 or hitung8 == 0:
    hitung5 += 1
    hitung6 += 1
    hitung7 += 1
    hitung8 += 1

if hitung9 == 0 or hitung10 == 0 or hitung11 == 0 or hitung12 == 0:
    hitung9 += 1
    hitung10 += 1
    hitung11 += 1
    hitung12 += 1

if hitung13 == 0 or hitung14 == 0 or hitung15 == 0 or hitung16 == 0:
    hitung13 += 1
    hitung14 += 1
    hitung15 += 1
    hitung16 += 1

if hitung17 == 0 or hitung18 == 0 or hitung19 == 0 or hitung20 == 0:
    hitung17 += 1
    hitung18 += 1
    hitung19 += 1
    hitung20 += 1

if hitung21 == 0 or hitung22 == 0 or hitung23 == 0 or hitung24 == 0:
    hitung21 += 1
    hitung22 += 1
    hitung23 += 1
    hitung24 += 1

pembagi1 = hitung1 + hitung2 + hitung3 + hitung4
pembagi2 = hitung5 + hitung6 + hitung7 + hitung8
pembagi3 = hitung9 + hitung10 + hitung11 + hitung12
pembagi4 = hitung13 + hitung14 + hitung15 + hitung16
pembagi5 = hitung17 + hitung18 + hitung19 + hitung20
pembagi6 = hitung21 + hitung22 + hitung23 + hitung24

data1 = hitung1 / pembagi1
data2 = hitung2 / pembagi1
data3 = hitung3 / pembagi1
data4 = hitung4 / pembagi1
data5 = hitung5 / pembagi2
data6 = hitung6 / pembagi2
data7 = hitung7 / pembagi2
data8 = hitung8 / pembagi2
data9 = hitung9 / pembagi3
data10 = hitung10 / pembagi3
data11 = hitung11 / pembagi3
data12 = hitung12 / pembagi3
data13 = hitung13 / pembagi4
data14 = hitung14 / pembagi4
data15 = hitung15 / pembagi4
data16 = hitung16 / pembagi4
data17 = hitung17 / pembagi5
data18 = hitung18 / pembagi5
data19 = hitung19 / pembagi5
data20 = hitung20 / pembagi5
data21 = hitung21 / pembagi6
data22 = hitung22 / pembagi6
data23 = hitung23 / pembagi6
data24 = hitung24 / pembagi6

# Input CPT
X9_Penghasilan_Ayah = ConditionalProbabilityTable(
    [
        ["Yang_Lainnya_1", "Tidak_Bekerja_1", data1],
        ["Yang_Lainnya_1", "Rendah_2", data2],
        ["Yang_Lainnya_1", "Sedang_3", data3],
        ["Yang_Lainnya_1", "Tinggi_4", data4],
        ["SD_2", "Tidak_Bekerja_1", data5],
        ["SD_2", "Rendah_2", data6],
        ["SD_2", "Sedang_3", data7],
        ["SD_2", "Tinggi_4", data8],
        ["SMP_3", "Tidak_Bekerja_1", data9],
        ["SMP_3", "Rendah_2", data10],
        ["SMP_3", "Sedang_3", data11],
        ["SMP_3", "Tinggi_4", data12],
        ["SMA_4", "Tidak_Bekerja_1", data13],
        ["SMA_4", "Rendah_2", data14],
        ["SMA_4", "Sedang_3", data15],
        ["SMA_4", "Tinggi_4", data16],
        ["D1_D4_5", "Tidak_Bekerja_1", data17],
        ["D1_D4_5", "Rendah_2", data18],
        ["D1_D4_5", "Sedang_3", data19],
        ["D1_D4_5", "Tinggi_4", data20],
        ["S1_S3_6", "Tidak_Bekerja_1", data21],
        ["S1_S3_6", "Rendah_2", data22],
        ["S1_S3_6", "Sedang_3", data23],
        ["S1_S3_6", "Tinggi_4", data24],
    ],
    [X7_Pendidikan_Ayah],
)

# X3 Mengikuti Ekstrakurikuler
hitung1 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung2 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung3 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung4 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung5 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung6 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung7 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung8 = df[
    (df["X6_Jarak_Sekolah"] == "Dekat_1")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
#
hitung9 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung10 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung11 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung12 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung13 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung14 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung15 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung16 = df[
    (df["X6_Jarak_Sekolah"] == "Sedang_2")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
#
hitung17 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung18 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung19 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung20 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Tidak_0")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung21 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung22 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Tidak_0")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]
hitung23 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
].shape[0]
hitung24 = df[
    (df["X6_Jarak_Sekolah"] == "Jauh_3")
    & (df["X5_Mengalami_Broken_Home"] == "Iya_1")
    & (df["X4_Ikut_Bekerja"] == "Iya_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
].shape[0]

if hitung1 == 0 or hitung2 == 0:
    hitung1 += 1
    hitung2 += 1
if hitung3 == 0 or hitung4 == 0:
    hitung3 += 1
    hitung4 += 1
if hitung5 == 0 or hitung6 == 0:
    hitung5 += 1
    hitung6 += 1
if hitung7 == 0 or hitung8 == 0:
    hitung7 += 1
    hitung8 += 1
if hitung9 == 0 or hitung10 == 0:
    hitung9 += 1
    hitung10 += 1
if hitung11 == 0 or hitung12 == 0:
    hitung11 += 1
    hitung12 += 1
if hitung13 == 0 or hitung14 == 0:
    hitung13 += 1
    hitung14 += 1
if hitung15 == 0 or hitung16 == 0:
    hitung15 += 1
    hitung16 += 1
if hitung17 == 0 or hitung18 == 0:
    hitung17 += 1
    hitung18 += 1
if hitung19 == 0 or hitung20 == 0:
    hitung19 += 1
    hitung20 += 1
if hitung21 == 0 or hitung22 == 0:
    hitung21 += 1
    hitung22 += 1
if hitung23 == 0 or hitung24 == 0:
    hitung23 += 1
    hitung24 += 1

data1 = hitung1 / (hitung1 + hitung2)
data2 = hitung2 / (hitung1 + hitung2)
data3 = hitung3 / (hitung3 + hitung4)
data4 = hitung4 / (hitung3 + hitung4)
data5 = hitung5 / (hitung5 + hitung6)
data6 = hitung6 / (hitung5 + hitung6)
data7 = hitung7 / (hitung7 + hitung8)
data8 = hitung8 / (hitung7 + hitung8)
data9 = hitung9 / (hitung9 + hitung10)
data10 = hitung10 / (hitung9 + hitung10)
data11 = hitung11 / (hitung11 + hitung12)
data12 = hitung12 / (hitung11 + hitung12)
data13 = hitung13 / (hitung13 + hitung14)
data14 = hitung14 / (hitung13 + hitung14)
data15 = hitung15 / (hitung15 + hitung16)
data16 = hitung16 / (hitung15 + hitung16)
data17 = hitung17 / (hitung17 + hitung18)
data18 = hitung18 / (hitung17 + hitung18)
data19 = hitung19 / (hitung19 + hitung20)
data20 = hitung20 / (hitung19 + hitung20)
data21 = hitung21 / (hitung21 + hitung22)
data22 = hitung22 / (hitung21 + hitung22)
data23 = hitung23 / (hitung23 + hitung24)
data24 = hitung24 / (hitung23 + hitung24)

# Input CPT
X3_Mengikuti_Ekstrakurikuler = ConditionalProbabilityTable(
    [
        ["Dekat_1", "Tidak_0", "Tidak_0", "Tidak_0", data1],
        ["Dekat_1", "Tidak_0", "Tidak_0", "Iya_1", data2],
        ["Dekat_1", "Tidak_0", "Iya_1", "Tidak_0", data3],
        ["Dekat_1", "Tidak_0", "Iya_1", "Iya_1", data4],
        ["Dekat_1", "Iya_1", "Tidak_0", "Tidak_0", data5],
        ["Dekat_1", "Iya_1", "Tidak_0", "Iya_1", data6],
        ["Dekat_1", "Iya_1", "Iya_1", "Tidak_0", data7],
        ["Dekat_1", "Iya_1", "Iya_1", "Iya_1", data8],
        ["Sedang_2", "Tidak_0", "Tidak_0", "Tidak_0", data9],
        ["Sedang_2", "Tidak_0", "Tidak_0", "Iya_1", data10],
        ["Sedang_2", "Tidak_0", "Iya_1", "Tidak_0", data11],
        ["Sedang_2", "Tidak_0", "Iya_1", "Iya_1", data12],
        ["Sedang_2", "Iya_1", "Tidak_0", "Tidak_0", data13],
        ["Sedang_2", "Iya_1", "Tidak_0", "Iya_1", data14],
        ["Sedang_2", "Iya_1", "Iya_1", "Tidak_0", data15],
        ["Sedang_2", "Iya_1", "Iya_1", "Iya_1", data16],
        ["Jauh_3", "Tidak_0", "Tidak_0", "Tidak_0", data17],
        ["Jauh_3", "Tidak_0", "Tidak_0", "Iya_1", data18],
        ["Jauh_3", "Tidak_0", "Iya_1", "Tidak_0", data19],
        ["Jauh_3", "Tidak_0", "Iya_1", "Iya_1", data20],
        ["Jauh_3", "Iya_1", "Tidak_0", "Tidak_0", data21],
        ["Jauh_3", "Iya_1", "Tidak_0", "Iya_1", data22],
        ["Jauh_3", "Iya_1", "Iya_1", "Tidak_0", data23],
        ["Jauh_3", "Iya_1", "Iya_1", "Iya_1", data24],
    ],
    [X6_Jarak_Sekolah, X5_Mengalami_Broken_Home, X4_Ikut_Bekerja],
)

# Class Putus
hitung1 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung2 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung3 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung4 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung5 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung6 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung7 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung8 = df[
    (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
#
hitung9 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung10 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung11 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung12 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung13 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung14 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung15 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung16 = df[
    (df["X9_Penghasilan_Ayah"] == "Rendah_2")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
#
hitung17 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung18 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung19 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung20 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung21 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung22 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung23 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung24 = df[
    (df["X9_Penghasilan_Ayah"] == "Sedang_3")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
#
hitung25 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung26 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung27 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung28 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "C_1")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung29 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung30 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Tidak_0")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]
hitung31 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Tidak_0")
].shape[0]
hitung32 = df[
    (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
    & (df["X2_Nilai_Rerata"] == "B_2")
    & (df["X3_Mengikuti_Ekstrakurikuler"] == "Iya_1")
    & (df["Class_Putus"] == "Iya_1")
].shape[0]

if hitung1 == 0 or hitung2 == 0:
    hitung1 += 1
    hitung2 += 1
if hitung3 == 0 or hitung4 == 0:
    hitung3 += 1
    hitung4 += 1
if hitung5 == 0 or hitung6 == 0:
    hitung5 += 1
    hitung6 += 1
if hitung7 == 0 or hitung8 == 0:
    hitung7 += 1
    hitung8 += 1
if hitung9 == 0 or hitung10 == 0:
    hitung9 += 1
    hitung10 += 1
if hitung11 == 0 or hitung12 == 0:
    hitung11 += 1
    hitung12 += 1
if hitung13 == 0 or hitung14 == 0:
    hitung13 += 1
    hitung14 += 1
if hitung15 == 0 or hitung16 == 0:
    hitung15 += 1
    hitung16 += 1
if hitung17 == 0 or hitung18 == 0:
    hitung17 += 1
    hitung18 += 1
if hitung19 == 0 or hitung20 == 0:
    hitung19 += 1
    hitung20 += 1
if hitung21 == 0 or hitung22 == 0:
    hitung21 += 1
    hitung22 += 1
if hitung23 == 0 or hitung24 == 0:
    hitung23 += 1
    hitung24 += 1
if hitung25 == 0 or hitung26 == 0:
    hitung25 += 1
    hitung26 += 1
if hitung27 == 0 or hitung28 == 0:
    hitung27 += 1
    hitung28 += 1
if hitung29 == 0 or hitung30 == 0:
    hitung29 += 1
    hitung30 += 1
if hitung31 == 0 or hitung32 == 0:
    hitung31 += 1
    hitung32 += 1

data1 = hitung1 / (hitung1 + hitung2)
data2 = hitung2 / (hitung1 + hitung2)
data3 = hitung3 / (hitung3 + hitung4)
data4 = hitung4 / (hitung3 + hitung4)
data5 = hitung5 / (hitung5 + hitung6)
data6 = hitung6 / (hitung5 + hitung6)
data7 = hitung7 / (hitung7 + hitung8)
data8 = hitung8 / (hitung7 + hitung8)
data9 = hitung9 / (hitung9 + hitung10)
data10 = hitung10 / (hitung9 + hitung10)
data11 = hitung11 / (hitung11 + hitung12)
data12 = hitung12 / (hitung11 + hitung12)
data13 = hitung13 / (hitung13 + hitung14)
data14 = hitung14 / (hitung13 + hitung14)
data15 = hitung15 / (hitung15 + hitung16)
data16 = hitung16 / (hitung15 + hitung16)
data17 = hitung17 / (hitung17 + hitung18)
data18 = hitung18 / (hitung17 + hitung18)
data19 = hitung19 / (hitung19 + hitung20)
data20 = hitung20 / (hitung19 + hitung20)
data21 = hitung21 / (hitung21 + hitung22)
data22 = hitung22 / (hitung21 + hitung22)
data23 = hitung23 / (hitung23 + hitung24)
data24 = hitung24 / (hitung23 + hitung24)
data25 = hitung25 / (hitung25 + hitung26)
data26 = hitung26 / (hitung25 + hitung26)
data27 = hitung27 / (hitung27 + hitung28)
data28 = hitung28 / (hitung27 + hitung28)
data29 = hitung29 / (hitung29 + hitung30)
data30 = hitung30 / (hitung29 + hitung30)
data31 = hitung31 / (hitung31 + hitung32)
data32 = hitung32 / (hitung31 + hitung32)

# Input CPT
Class_Putus = ConditionalProbabilityTable(
    [
        ["Tidak_Bekerja_1", "C_1", "Tidak_0", "Tidak_0", data1],
        ["Tidak_Bekerja_1", "C_1", "Tidak_0", "Iya_1", data2],
        ["Tidak_Bekerja_1", "C_1", "Iya_1", "Tidak_0", data3],
        ["Tidak_Bekerja_1", "C_1", "Iya_1", "Iya_1", data4],
        ["Tidak_Bekerja_1", "B_2", "Tidak_0", "Tidak_0", data5],
        ["Tidak_Bekerja_1", "B_2", "Tidak_0", "Iya_1", data6],
        ["Tidak_Bekerja_1", "B_2", "Iya_1", "Tidak_0", data7],
        ["Tidak_Bekerja_1", "B_2", "Iya_1", "Iya_1", data8],
        ["Rendah_2", "C_1", "Tidak_0", "Tidak_0", data9],
        ["Rendah_2", "C_1", "Tidak_0", "Iya_1", data10],
        ["Rendah_2", "C_1", "Iya_1", "Tidak_0", data11],
        ["Rendah_2", "C_1", "Iya_1", "Iya_1", data12],
        ["Rendah_2", "B_2", "Tidak_0", "Tidak_0", data13],
        ["Rendah_2", "B_2", "Tidak_0", "Iya_1", data14],
        ["Rendah_2", "B_2", "Iya_1", "Tidak_0", data15],
        ["Rendah_2", "B_2", "Iya_1", "Iya_1", data16],
        ["Sedang_3", "C_1", "Tidak_0", "Tidak_0", data17],
        ["Sedang_3", "C_1", "Tidak_0", "Iya_1", data18],
        ["Sedang_3", "C_1", "Iya_1", "Tidak_0", data19],
        ["Sedang_3", "C_1", "Iya_1", "Iya_1", data20],
        ["Sedang_3", "B_2", "Tidak_0", "Tidak_0", data21],
        ["Sedang_3", "B_2", "Tidak_0", "Iya_1", data22],
        ["Sedang_3", "B_2", "Iya_1", "Tidak_0", data23],
        ["Sedang_3", "B_2", "Iya_1", "Iya_1", data24],
        ["Tinggi_4", "C_1", "Tidak_0", "Tidak_0", data25],
        ["Tinggi_4", "C_1", "Tidak_0", "Iya_1", data26],
        ["Tinggi_4", "C_1", "Iya_1", "Tidak_0", data27],
        ["Tinggi_4", "C_1", "Iya_1", "Iya_1", data28],
        ["Tinggi_4", "B_2", "Tidak_0", "Tidak_0", data29],
        ["Tinggi_4", "B_2", "Tidak_0", "Iya_1", data30],
        ["Tinggi_4", "B_2", "Iya_1", "Tidak_0", data31],
        ["Tinggi_4", "B_2", "Iya_1", "Iya_1", data32],
    ],
    [X9_Penghasilan_Ayah, X2_Nilai_Rerata, X3_Mengikuti_Ekstrakurikuler],
)

# Bayesian Network Modeling
d1 = State(X1_Jenis_Kelamin, name="X1_Jenis_Kelamin")
d2 = State(X2_Nilai_Rerata, name="X2_Nilai_Rerata")
d3 = State(X3_Mengikuti_Ekstrakurikuler, name="X3_Mengikuti_Ekstrakurikuler")
d4 = State(X4_Ikut_Bekerja, name="X4_Ikut_Bekerja")
d5 = State(X5_Mengalami_Broken_Home, name="X5_Mengalami_Broken_Home")
d6 = State(X6_Jarak_Sekolah, name="X6_Jarak_Sekolah")
d7 = State(X7_Pendidikan_Ayah, name="X7_Pendidikan_Ayah")
d8 = State(X8_Pendidikan_Ibu, name="X8_Pendidikan_Ibu")
d9 = State(X9_Penghasilan_Ayah, name="X9_Penghasilan_Ayah")
d10 = State(X10_Penghasilan_Ibu, name="X10_Penghasilan_Ibu")
d11 = State(Class_Putus, name="Class_Putus")

# Membentuk Bayesian Network
network = BayesianNetwork("Sistem Prediksi Siswa Putus Sekolah")
network.add_states(d1, d2, d3, d4, d5, d6, d7, d8, d9, d10, d11)
network.add_edge(d8, d7)
network.add_edge(d7, d9)
network.add_edge(d10, d4)
network.add_edge(d1, d4)
network.add_edge(d6, d3)
network.add_edge(d5, d3)
network.add_edge(d4, d3)
network.add_edge(d9, d11)
network.add_edge(d2, d11)
network.add_edge(d3, d11)
network.bake()

namaIndex = [
    "X1_Jenis_Kelamin",
    "X2_Nilai_Rerata",
    "X3_Mengikuti_Ekstrakurikuler",
    "X4_Ikut_Bekerja",
    "X5_Mengalami_Broken_Home",
    "X6_Jarak_Sekolah",
    "X7_Pendidikan_Ayah",
    "X8_Pendidikan_Ibu",
    "X9_Penghasilan_Ayah",
    "X10_Penghasilan_Ibu",
    "Class_Putus",
]


st.title("Sistem Prediksi Putus Sekolah")

st.write("Sistem Prediksi Siswa Putus Sekolah SMA Islam Al Wahid Kepung")
url = "https://i.ibb.co/RSXmDD8/sma.png"
st.sidebar.image("sma.png", width=None)
dataset_name = st.sidebar.selectbox(
    "Pilih Menu", ("Tentang Sistem", "Prediksi Perorangan",
                   "Prediksi Berkelompok")
)

st.write(f"## {dataset_name}")


def get_table_download_link(df):
    """Generates a link allowing the data in a given panda dataframe to be downloaded
    in:  dataframe
    out: href string
    """
    csv = df.to_csv(index=False)
    b64 = base64.b64encode(
        csv.encode()
    ).decode()  # some strings <-> bytes conversions necessary here
    return f'<a href="data:file/csv;base64,{b64}" download="prediksiSiswa.csv">Unduh file .csv</a>'

# untuk mengembalikan hasil prediksi

# melakukan prediksi pada kelomppok


def predict_kelompok(datFrame, group):
    dfResult = network.predict([group])
    datFrame = datFrame.append(dfResult, ignore_index=True)
    return datFrame

# untuk memulai mengambil data dari teks dan memanggil fungsi predict_kelompok


def ambil_dataKelompok(jumlahData, data):
    df_marks = pd.DataFrame()
    group = list()
    for i in range(jumlahData):
        if (i % 10 == 0):
            batas = i
        if (i >= batas and i <= batas+9):
            if (data[i] == 'None'):
                data[i] = None
            group.append(data[i])
        if (i == batas+9):
            group.append(None)
            df_marks = predict_kelompok(df_marks, group)
            group = list()
    st.markdown(get_table_download_link(
                df_marks), unsafe_allow_html=True)
    # memberi nama pada DataFrame columns
    df_marks.columns = ['X1_Jenis_Kelamin', 'X2_Nilai_Rerata', 'X3_Mengikuti_Ekstrakurikuler',
                        'X4_Ikut_Bekerja', 'X5_Mengalami_Broken_Home', 'X6_Jarak_Sekolah',
                        'X7_Pendidikan_Ayah', 'X8_Pendidikan_Ibu', 'X9_Penghasilan_Ayah',
                        'X10_Penghasilan_Ibu', 'Class_Putus', ]
    st.write(df_marks)

# menampilkan menu tentang sistem


def tentang_sistem():
    st.write(
        "Sistem prediksi merupakan sebuah sistem yang digunakan untuk melakukan prediksi siswa yang berpotensi mengalami putus sekolah khususnya di SMA Islam Al Wahid."
    )
    st.write("Atribut yang digunakan antara lain")
    st.write("1. Jenis Kelamin")
    st.write("2. Nilai Rerata")
    st.write("3. Ketertarika Mengikuti Ekstrakurikuler")
    st.write("4. Ikut Bekerja")
    st.write("5. Mengalami Masalah Keluarga")
    st.write("6. Jarak ke Sekolah")
    st.write("7. Pendidikan Terakhir Ayah")
    st.write("8. Pendidikan Terakhir Ibu")
    st.write("9. Penghasilan Ayah")
    st.write("10. Penghasilan Ibu")
    st.text("")
    st.write(
        "Kemampuan sistem prediksi dapat terus diperbarui dengan cara mengakses spreadsheet yang sudah disediakan pada tautan berikut : https://docs.google.com/spreadsheets/d/1HOut-jWjztfhhjNY0mrbv2t-Xj9wqe1VrFhaHUwEIQo/edit?usp=sharing"
    )
    st.write("Silakan perbarui data pada sheet dengan nama \"Data Untuk Model\""
             )
    st.write("Silakan gunakan akun email sekolah yang sudah didaftarkan")
    st.text("")
    st.write("Terima kasih, semoga bermanfaat. 😊👨‍🎓👩‍🎓")

# menampilkan menu prediksi perorangan


def prediksi_perorangan():
    st.write("Prosedur Percobaan Prediksi 📑")
    st.write("1. Isilah semua data yang telah tersedia dengan benar")
    st.write("2. Tekan tombol \"Prediksi Siswa\"")
    st.write(
        "Note: jika tidak mempunyai informasi yang lengkap maka dapat memilih \"None\"")
    X1_Jenis_Kelamin = st.selectbox(
        "Pilih Jenis Kelamin", ("None", "Laki_laki_1", "Perempuan_2")
    )
    if (X1_Jenis_Kelamin == "None"):
        X1_Jenis_Kelamin = None
    X2_Nilai_Rerata = st.selectbox(
        "Pilih Nilai Rata-rata", ("None", "C_1", "B_2"))
    if (X2_Nilai_Rerata == "None"):
        X2_Nilai_Rerata = None
    X3_Mengikuti_Ekstrakurikuler = st.selectbox(
        "Pilih Ekstrakurikuler", ("None", "Tidak_0", "Iya_1")
    )
    if (X3_Mengikuti_Ekstrakurikuler == "None"):
        X3_Mengikuti_Ekstrakurikuler = None
    X4_Ikut_Bekerja = st.selectbox(
        "Pilih Ikut Bekerja", ("None", "Tidak_0", "Iya_1"))
    if (X4_Ikut_Bekerja == "None"):
        X4_Ikut_Bekerja = None
    X5_Mengalami_Broken_Home = st.selectbox(
        "Pilih Broken Home", ("None", "Tidak_0", "Iya_1"))
    if(X5_Mengalami_Broken_Home == "None"):
        X5_Mengalami_Broken_Home = None
    X6_Jarak_Sekolah = st.selectbox(
        "Pilih Broken Home", ("None", "Dekat_1", "Sedang_2", "Jauh_3")
    )
    if (X6_Jarak_Sekolah == "None"):
        X6_Jarak_Sekolah = None
    X7_Pendidikan_Ayah = st.selectbox(
        "Pilih Pendidikan Ayah",
        ("None", "Yang_Lainnya_1", "SD_2", "SMP_3", "SMA_4", "D1_D4_5", "S1_S3_6"),
    )
    if(X7_Pendidikan_Ayah == "None"):
        X7_Pendidikan_Ayah = None
    X8_Pendidikan_Ibu = st.selectbox(
        "Pilih Pendidikan Ibu",
        ("None", "Yang_Lainnya_1", "SD_2", "SMP_3", "SMA_4", "D1_D4_5", "S1_S3_6"),
    )
    if(X8_Pendidikan_Ibu == "None"):
        X8_Pendidikan_Ibu = None
    X9_Penghasilan_Ayah = st.selectbox(
        "Pilih Penghasilan Ayah",
        ("None", "Tidak_Bekerja_1", "Rendah_2", "Sedang_3", "Tinggi_4"),
    )
    if(X9_Penghasilan_Ayah == "None"):
        X9_Penghasilan_Ayah = None
    X10_Penghasilan_Ibu = st.selectbox(
        "Pilih Penghasilan Ibu", ("None", "Tidak_Bekerja_1",
                                  "Rendah_2", "Sedang_3", "Tinggi_4")
    )
    if(X10_Penghasilan_Ibu == "None"):
        X10_Penghasilan_Ibu = None
    if st.button("Prediksi Siswa"):
        dfResult = network.predict(
            [
                [
                    X1_Jenis_Kelamin,
                    X2_Nilai_Rerata,
                    X3_Mengikuti_Ekstrakurikuler,
                    X4_Ikut_Bekerja,
                    X5_Mengalami_Broken_Home,
                    X6_Jarak_Sekolah,
                    X7_Pendidikan_Ayah,
                    X8_Pendidikan_Ibu,
                    X9_Penghasilan_Ayah,
                    X10_Penghasilan_Ibu,
                    None,
                ]
            ]
        )
        df = pd.DataFrame(dfResult, columns=namaIndex)
        st.write(df)
        if df.iloc[:, -1:].Class_Putus.item() == "Iya_1":
            st.write("Iya")
            st.warning(
                "Siswa tersebut berpotensi untuk putus sekolah. Lebih baik untuk lebih diperhatikan lagi ya! 🙏🧐"
            )
        else:
            st.write("Tidak")
            st.success(
                "Siswa tersebut tidak berpotensi untuk putus sekolah. Namun lebih baik untuk tetap diperhatikan ya! 👩‍🎓👨‍🎓"
            )

# menampilkan menu prediksi kelompok


def prediksi_Kelompok():
    st.write("Prosedur Percobaan Prediksi 📑")
    st.write("1. Buka https://docs.google.com/spreadsheets/d/1HOut-jWjztfhhjNY0mrbv2t-Xj9wqe1VrFhaHUwEIQo/edit?usp=sharing dengan akun SMA Al Wahid")
    st.write("2. Pilih sheet dengan nama \"Template Prediksi\"")
    st.write("3. Silakan merubah data sesuai kebutuhan")
    st.write("4. Copy syntax yang muncul pada kolom L dengan jumlah menyesuaikan data")
    st.write("5. Kemudian paste/tempel pada kolom yang barada di bawah ini 👇")
    st.write(
        "Note: jika tidak mempunyai informasi yang lengkap maka dapat memilih \"None\"")
    x = st.text_area("Data Siswa", height=300)
    df = pd
    x = x.split()
    if st.button("Prediksi Siswa"):
        ambil_dataKelompok(len(x), x)


if dataset_name == "Tentang Sistem":
    tentang_sistem()
elif dataset_name == "Prediksi Perorangan":
    prediksi_perorangan()
else:
    prediksi_Kelompok()
