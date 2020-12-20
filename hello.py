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
sheet = client.open("siswa").sheet1

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
print(type(list_of_hashes))
df = pd.DataFrame(list_of_hashes, columns=namaIndex)
totalValue = df.shape[0]
print(totalValue)

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
    jk1 = (len(df[df["X1_Jenis_Kelamin"].str.contains("Laki_laki_1")])) / totalValue
    jk2 = (len(df[df["X1_Jenis_Kelamin"].str.contains("Perempuan_2")])) / totalValue

X1_Jenis_Kelamin = DiscreteDistribution({"1_Laki_laki": jk1, "2_Perempuan": jk2})

# X2 Nilai Rerata
if (
    len(df[df["X2_Nilai_Rerata"].str.contains("C_1")]) == 0
    or len(df[df["X2_Nilai_Rerata"].str.contains("B_2")]) == 0
):
    nilai1 = (len(df[df["X2_Nilai_Rerata"].str.contains("C_1")]) + 1) / (totalValue + 2)
    nilai2 = (len(df[df["X2_Nilai_Rerata"].str.contains("B_2")]) + 1) / (totalValue + 2)
else:
    nilai1 = (len(df[df["X2_Nilai_Rerata"].str.contains("C_1")])) / totalValue
    nilai2 = (len(df[df["X2_Nilai_Rerata"].str.contains("B_2")])) / totalValue

X2_Nilai_Rerata = DiscreteDistribution({"1_C": nilai1, "2_B": nilai2})

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

X5_Mengalami_Broken_Home = DiscreteDistribution({"0_Tidak": broken1, "1_Iya": broken2})

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
    jarak1 = (len(df[df["X6_Jarak_Sekolah"].str.contains("Dekat_1")])) / totalValue
    jarak2 = (len(df[df["X6_Jarak_Sekolah"].str.contains("Sedang_2")])) / totalValue
    jarak3 = (len(df[df["X6_Jarak_Sekolah"].str.contains("Jauh_3")])) / totalValue

X6_Jarak_Sekolah = DiscreteDistribution(
    {"1_Dekat": jarak1, "2_Sedang": jarak2, "3_Jauh": jarak3}
)

# X8 Pendidikan Ibu
if (
    len(df[df["X8_Pendidikan_Ibu"].str.contains("Yang_Lainnya_1")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("SD_2")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("SMP_3")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("SMA_4")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("D1_D4_5")]) == 0
    or len(df[df["X8_Pendidikan_Ibu"].str.contains("6_S1_S3")]) == 0
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
    pdkIbu1 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("SD_2")])) / totalValue
    pdkIbu2 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("SMP_3")])) / totalValue
    pdkIbu3 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("SMA_4")])) / totalValue
    pdkIbu4 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("D1_D4_5")])) / totalValue
    pdkIbu5 = (len(df[df["X8_Pendidikan_Ibu"].str.contains("S1_S3_6")])) / totalValue

X8_Pendidikan_Ibu = DiscreteDistribution(
    {
        "1_Yang_Lainnya": pdkIbu0,
        "2_SD": pdkIbu1,
        "3_SMP": pdkIbu2,
        "4_SMA": pdkIbu3,
        "5_D1_D4": pdkIbu4,
        "6_S1_S3": pdkIbu5,
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
    phsIbu1 = (len(df[df["X10_Penghasilan_Ibu"].str.contains("Rendah_2")])) / totalValue
    phsIbu2 = (len(df[df["X10_Penghasilan_Ibu"].str.contains("Sedang_3")])) / totalValue
    phsIbu3 = (len(df[df["X10_Penghasilan_Ibu"].str.contains("Tinggi_4")])) / totalValue

X10_Penghasilan_Ibu = DiscreteDistribution(
    {
        "1_Tidak_Bekerja": phsIbu0,
        "2_Rendah": phsIbu1,
        "3_Sedang": phsIbu2,
        "4_Tinggi": phsIbu3,
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
        ["1_Laki_laki", "1_Tidak_Bekerja", "0_Tidak", data1],
        ["1_Laki_laki", "1_Tidak_Bekerja", "1_Iya", data2],
        ["1_Laki_laki", "2_Rendah", "0_Tidak", data3],
        ["1_Laki_laki", "2_Rendah", "1_Iya", data4],
        ["1_Laki_laki", "3_Sedang", "0_Tidak", data5],
        ["1_Laki_laki", "3_Sedang", "1_Iya", data6],
        ["1_Laki_laki", "4_Tinggi", "0_Tidak", data7],
        ["1_Laki_laki", "4_Tinggi", "1_Iya", data8],
        ["2_Perempuan", "1_Tidak_Bekerja", "0_Tidak", data11],
        ["2_Perempuan", "1_Tidak_Bekerja", "1_Iya", data12],
        ["2_Perempuan", "2_Rendah", "0_Tidak", data13],
        ["2_Perempuan", "2_Rendah", "1_Iya", data14],
        ["2_Perempuan", "3_Sedang", "0_Tidak", data15],
        ["2_Perempuan", "3_Sedang", "1_Iya", data16],
        ["2_Perempuan", "4_Tinggi", "0_Tidak", data17],
        ["2_Perempuan", "4_Tinggi", "1_Iya", data18],
    ],
    [X1_Jenis_Kelamin, X10_Penghasilan_Ibu],
)

# X7 Pendidikan Ayah
hitung1 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung2 = df[
    (df["X8_Pendidikan_Ibu"] == "Yang_Lainnya_1") & (df["X7_Pendidikan_Ayah"] == "SD_2")
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
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
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
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung12 = df[
    (df["X8_Pendidikan_Ibu"] == "SD_2") & (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung13 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung14 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung15 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung16 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung17 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung18 = df[
    (df["X8_Pendidikan_Ibu"] == "SMP_3") & (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung19 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung20 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung21 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung22 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung23 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung24 = df[
    (df["X8_Pendidikan_Ibu"] == "SMA_4") & (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung25 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung26 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung27 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung28 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung29 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung30 = df[
    (df["X8_Pendidikan_Ibu"] == "D1_D4_5") & (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
].shape[0]

hitung31 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6")
    & (df["X7_Pendidikan_Ayah"] == "Yang_Lainnya_1")
].shape[0]
hitung32 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (df["X7_Pendidikan_Ayah"] == "SD_2")
].shape[0]
hitung33 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (df["X7_Pendidikan_Ayah"] == "SMP_3")
].shape[0]
hitung34 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (df["X7_Pendidikan_Ayah"] == "SMA_4")
].shape[0]
hitung35 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
].shape[0]
hitung36 = df[
    (df["X8_Pendidikan_Ibu"] == "S1_S3_6") & (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
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
        ["1_Yang_Lainnya", "1_Yang_Lainnya", data1],
        ["1_Yang_Lainnya", "2_SD", data2],
        ["1_Yang_Lainnya", "3_SMP", data3],
        ["1_Yang_Lainnya", "4_SMA", data4],
        ["1_Yang_Lainnya", "5_D1_D4", data5],
        ["1_Yang_Lainnya", "6_S1_S3", data6],
        ["2_SD", "1_Yang_Lainnya", data7],
        ["2_SD", "2_SD", data8],
        ["2_SD", "3_SMP", data9],
        ["2_SD", "4_SMA", data10],
        ["2_SD", "5_D1_D4", data11],
        ["2_SD", "6_S1_S3", data12],
        ["3_SMP", "1_Yang_Lainnya", data13],
        ["3_SMP", "2_SD", data14],
        ["3_SMP", "3_SMP", data15],
        ["3_SMP", "4_SMA", data16],
        ["3_SMP", "5_D1_D4", data17],
        ["3_SMP", "6_S1_S3", data18],
        ["4_SMA", "1_Yang_Lainnya", data19],
        ["4_SMA", "2_SD", data20],
        ["4_SMA", "3_SMP", data21],
        ["4_SMA", "4_SMA", data22],
        ["4_SMA", "5_D1_D4", data23],
        ["4_SMA", "6_S1_S3", data24],
        ["5_D1_D4", "1_Yang_Lainnya", data25],
        ["5_D1_D4", "2_SD", data26],
        ["5_D1_D4", "3_SMP", data27],
        ["5_D1_D4", "4_SMA", data28],
        ["5_D1_D4", "5_D1_D4", data29],
        ["5_D1_D4", "6_S1_S3", data30],
        ["6_S1_S3", "1_Yang_Lainnya", data31],
        ["6_S1_S3", "2_SD", data32],
        ["6_S1_S3", "3_SMP", data33],
        ["6_S1_S3", "4_SMA", data34],
        ["6_S1_S3", "5_D1_D4", data35],
        ["6_S1_S3", "6_S1_S3", data36],
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
    (df["X7_Pendidikan_Ayah"] == "SD_2") & (df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung7 = df[
    (df["X7_Pendidikan_Ayah"] == "SD_2") & (df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung8 = df[
    (df["X7_Pendidikan_Ayah"] == "SD_2") & (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung9 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung10 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3") & (df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung11 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3") & (df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung12 = df[
    (df["X7_Pendidikan_Ayah"] == "SMP_3") & (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung13 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung14 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4") & (df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung15 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4") & (df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung16 = df[
    (df["X7_Pendidikan_Ayah"] == "SMA_4") & (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung17 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung18 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5") & (df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung19 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5") & (df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung20 = df[
    (df["X7_Pendidikan_Ayah"] == "D1_D4_5") & (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
].shape[0]

hitung21 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6")
    & (df["X9_Penghasilan_Ayah"] == "Tidak_Bekerja_1")
].shape[0]
hitung22 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6") & (df["X9_Penghasilan_Ayah"] == "Rendah_2")
].shape[0]
hitung23 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6") & (df["X9_Penghasilan_Ayah"] == "Sedang_3")
].shape[0]
hitung24 = df[
    (df["X7_Pendidikan_Ayah"] == "S1_S3_6") & (df["X9_Penghasilan_Ayah"] == "Tinggi_4")
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
        ["1_Yang_Lainnya", "1_Tidak_Bekerja", data1],
        ["1_Yang_Lainnya", "2_Rendah", data2],
        ["1_Yang_Lainnya", "3_Sedang", data3],
        ["1_Yang_Lainnya", "4_Tinggi", data4],
        ["2_SD", "1_Tidak_Bekerja", data5],
        ["2_SD", "2_Rendah", data6],
        ["2_SD", "3_Sedang", data7],
        ["2_SD", "4_Tinggi", data8],
        ["3_SMP", "1_Tidak_Bekerja", data9],
        ["3_SMP", "2_Rendah", data10],
        ["3_SMP", "3_Sedang", data11],
        ["3_SMP", "4_Tinggi", data12],
        ["4_SMA", "1_Tidak_Bekerja", data13],
        ["4_SMA", "2_Rendah", data14],
        ["4_SMA", "3_Sedang", data15],
        ["4_SMA", "4_Tinggi", data16],
        ["5_D1_D4", "1_Tidak_Bekerja", data17],
        ["5_D1_D4", "2_Rendah", data18],
        ["5_D1_D4", "3_Sedang", data19],
        ["5_D1_D4", "4_Tinggi", data20],
        ["6_S1_S3", "1_Tidak_Bekerja", data21],
        ["6_S1_S3", "2_Rendah", data22],
        ["6_S1_S3", "3_Sedang", data23],
        ["6_S1_S3", "4_Tinggi", data24],
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
        ["1_Dekat", "0_Tidak", "0_Tidak", "0_Tidak", data1],
        ["1_Dekat", "0_Tidak", "0_Tidak", "1_Iya", data2],
        ["1_Dekat", "0_Tidak", "1_Iya", "0_Tidak", data3],
        ["1_Dekat", "0_Tidak", "1_Iya", "1_Iya", data4],
        ["1_Dekat", "1_Iya", "0_Tidak", "0_Tidak", data5],
        ["1_Dekat", "1_Iya", "0_Tidak", "1_Iya", data6],
        ["1_Dekat", "1_Iya", "1_Iya", "0_Tidak", data7],
        ["1_Dekat", "1_Iya", "1_Iya", "1_Iya", data8],
        ["2_Sedang", "0_Tidak", "0_Tidak", "0_Tidak", data9],
        ["2_Sedang", "0_Tidak", "0_Tidak", "1_Iya", data10],
        ["2_Sedang", "0_Tidak", "1_Iya", "0_Tidak", data11],
        ["2_Sedang", "0_Tidak", "1_Iya", "1_Iya", data12],
        ["2_Sedang", "1_Iya", "0_Tidak", "0_Tidak", data13],
        ["2_Sedang", "1_Iya", "0_Tidak", "1_Iya", data14],
        ["2_Sedang", "1_Iya", "1_Iya", "0_Tidak", data15],
        ["2_Sedang", "1_Iya", "1_Iya", "1_Iya", data16],
        ["3_Jauh", "0_Tidak", "0_Tidak", "0_Tidak", data17],
        ["3_Jauh", "0_Tidak", "0_Tidak", "1_Iya", data18],
        ["3_Jauh", "0_Tidak", "1_Iya", "0_Tidak", data19],
        ["3_Jauh", "0_Tidak", "1_Iya", "1_Iya", data20],
        ["3_Jauh", "1_Iya", "0_Tidak", "0_Tidak", data21],
        ["3_Jauh", "1_Iya", "0_Tidak", "1_Iya", data22],
        ["3_Jauh", "1_Iya", "1_Iya", "0_Tidak", data23],
        ["3_Jauh", "1_Iya", "1_Iya", "1_Iya", data24],
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
        ["1_Tidak_Bekerja", "1_C", "0_Tidak", "0_Tidak", data1],
        ["1_Tidak_Bekerja", "1_C", "0_Tidak", "1_Iya", data2],
        ["1_Tidak_Bekerja", "1_C", "1_Iya", "0_Tidak", data3],
        ["1_Tidak_Bekerja", "1_C", "1_Iya", "1_Iya", data4],
        ["1_Tidak_Bekerja", "2_B", "0_Tidak", "0_Tidak", data5],
        ["1_Tidak_Bekerja", "2_B", "0_Tidak", "1_Iya", data6],
        ["1_Tidak_Bekerja", "2_B", "1_Iya", "0_Tidak", data7],
        ["1_Tidak_Bekerja", "2_B", "1_Iya", "1_Iya", data8],
        ["2_Rendah", "1_C", "0_Tidak", "0_Tidak", data9],
        ["2_Rendah", "1_C", "0_Tidak", "1_Iya", data10],
        ["2_Rendah", "1_C", "1_Iya", "0_Tidak", data11],
        ["2_Rendah", "1_C", "1_Iya", "1_Iya", data12],
        ["2_Rendah", "2_B", "0_Tidak", "0_Tidak", data13],
        ["2_Rendah", "2_B", "0_Tidak", "1_Iya", data14],
        ["2_Rendah", "2_B", "1_Iya", "0_Tidak", data15],
        ["2_Rendah", "2_B", "1_Iya", "1_Iya", data16],
        ["3_Sedang", "1_C", "0_Tidak", "0_Tidak", data17],
        ["3_Sedang", "1_C", "0_Tidak", "1_Iya", data18],
        ["3_Sedang", "1_C", "1_Iya", "0_Tidak", data19],
        ["3_Sedang", "1_C", "1_Iya", "1_Iya", data20],
        ["3_Sedang", "2_B", "0_Tidak", "0_Tidak", data21],
        ["3_Sedang", "2_B", "0_Tidak", "1_Iya", data22],
        ["3_Sedang", "2_B", "1_Iya", "0_Tidak", data23],
        ["3_Sedang", "2_B", "1_Iya", "1_Iya", data24],
        ["4_Tinggi", "1_C", "0_Tidak", "0_Tidak", data25],
        ["4_Tinggi", "1_C", "0_Tidak", "1_Iya", data26],
        ["4_Tinggi", "1_C", "1_Iya", "0_Tidak", data27],
        ["4_Tinggi", "1_C", "1_Iya", "1_Iya", data28],
        ["4_Tinggi", "2_B", "0_Tidak", "0_Tidak", data29],
        ["4_Tinggi", "2_B", "0_Tidak", "1_Iya", data30],
        ["4_Tinggi", "2_B", "1_Iya", "0_Tidak", data31],
        ["4_Tinggi", "2_B", "1_Iya", "1_Iya", data32],
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


import streamlit as st
import numpy as np

st.title("Sistem Prediksi Putus Sekolah")

st.write("Sistem Prediksi Siswa Putus Sekolah SMA Islam Al Wahid Kepung")

dataset_name = st.sidebar.selectbox(
    "Pilih Menu", ("Tentang Sistem", "Prediksi Perorangan", "Prediksi Berkelompok")
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


if dataset_name == "Tentang Sistem":
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
        "Kemampuan sistem prediksi dapat terus diperbarui dengan cara mengakses spreadsheet yang sudah disediakan pada tautan berikut : https://docs.google.com/spreadsheets/d/1-_ouhVDZD9OO-Wm3PK_aclvIvZLiy2K_C66k81tbvIQ/edit?usp=sharing"
    )
    st.write("Silakan gunakan akun email sekolahan yang sudah didaftarkan")
    st.text("")
    st.write("Terima kasih, semoga bermanfaat. 😊👨‍🎓👩‍🎓")
elif dataset_name == "Prediksi Perorangan":
    X1_Jenis_Kelamin = st.selectbox(
        "Pilih Jenis Kelamin", ("1_Laki_laki", "2_Perempuan")
    )
    X2_Nilai_Rerata = st.selectbox("Pilih Nilai Rata-rata", ("1_C", "2_B"))
    X3_Mengikuti_Ekstrakurikuler = st.selectbox(
        "Pilih Ekstrakurikuler", ("0_Tidak", "1_Iya")
    )
    X4_Ikut_Bekerja = st.selectbox("Pilih Ikut Bekerja", ("0_Tidak", "1_Iya"))
    X5_Mengalami_Broken_Home = st.selectbox("Pilih Broken Home", ("0_Tidak", "1_Iya"))
    X6_Jarak_Sekolah = st.selectbox(
        "Pilih Broken Home", ("1_Dekat", "2_Sedang", "3_Jauh")
    )
    X7_Pendidikan_Ayah = st.selectbox(
        "Pilih Pendidikan Ayah",
        ("1_Yang_Lainnya", "2_SD", "3_SMP", "4_SMA", "5_D1_D4", "6_S1_S3"),
    )

    X8_Pendidikan_Ibu = st.selectbox(
        "Pilih Pendidikan Ibu",
        ("1_Yang_Lainnya", "2_SD", "3_SMP", "4_SMA", "5_D1_D4", "6_S1_S3"),
    )
    X9_Penghasilan_Ayah = st.selectbox(
        "Pilih Penghasilan Ayah",
        ("1_Tidak_Bekerja", "2_Rendah", "3_Sedang", "4_Tinggi"),
    )
    X10_Penghasilan_Ibu = st.selectbox(
        "Pilih Penghasilan Ibu", ("1_Tidak_Bekerja", "2_Rendah", "3_Sedang", "4_Tinggi")
    )
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
        if df.iloc[:, -1:].Class_Putus.item() == "1_Iya":
            st.write("Iya")
            st.warning(
                "Siswa tersebut berpotensi untuk putus sekolah. Lebih baik untuk lebih diperhatikan lagi ya! 🙏🧐"
            )
        else:
            st.write("Tidak")
            st.success(
                "Siswa tersebut tidak berpotensi untuk putus sekolah. Namun lebih baik untuk tetap diperhatikan ya! 👩‍🎓👨‍🎓"
            )
else:
    st.write("Pastikan anda tidak melebihi batas masukkan yakni 30 baris per percobaan")
    x = st.text_area("Data Siswa")
    dataSiswa1 = x
    df = pd
    x = x.split()
    if st.button("Prediksi Siswa"):
        if len(x) > 300:
            st.write("Mohon maaf, jumlah data melebihi maksimal masukkan (30 data)")
            totalData = int(len(x) / 10)
            st.write("Jumlah yang anda masukkan", totalData, "baris data")
        else:
            if len(x) == 10:
                group1 = list()
                for i in range(len(x) + 1):
                    if i == 10:
                        group1.append(None)
                    else:
                        group1.append(x[i])
                dfResult = network.predict([group1])
                df = pd.DataFrame(dfResult, columns=namaIndex)
                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 20:
                group1 = list()
                group2 = list()
                for i in range(len(x) + 1):
                    if i < 10:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i < 20:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                dfResult = network.predict([group1, group2])
                df = pd.DataFrame(dfResult, columns=namaIndex)
                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 30:
                group1 = list()
                group2 = list()
                group3 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                dfResult = network.predict([group1, group2, group3])
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 40:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                dfResult = network.predict([group1, group2, group3, group4])
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 50:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                dfResult = network.predict([group1, group2, group3, group4, group5])
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 60:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                dfResult = network.predict(
                    [group1, group2, group3, group4, group5, group6]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 70:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                dfResult = network.predict(
                    [group1, group2, group3, group4, group5, group6, group7]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 80:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                dfResult = network.predict(
                    [group1, group2, group3, group4, group5, group6, group7, group8]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 90:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 100:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 110:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 120:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 130:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 140:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 150:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 160:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 170:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)

                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 180:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)

                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 190:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 200:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 210:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 220:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 230:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 240:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                group24 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                    if i >= 230 and i <= 239:
                        group24.append(x[i])
                    if i == 239:
                        group24.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                        group24,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 250:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                group24 = list()
                group25 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                    if i >= 230 and i <= 239:
                        group24.append(x[i])
                    if i == 239:
                        group24.append(None)
                    if i >= 240 and i <= 249:
                        group25.append(x[i])
                    if i == 249:
                        group25.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                        group24,
                        group25,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 260:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                group24 = list()
                group25 = list()
                group25 = list()
                group26 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                    if i >= 230 and i <= 239:
                        group24.append(x[i])
                    if i == 239:
                        group24.append(None)
                    if i >= 240 and i <= 249:
                        group25.append(x[i])
                    if i == 249:
                        group25.append(None)
                    if i >= 250 and i <= 259:
                        group26.append(x[i])
                    if i == 259:
                        group26.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                        group24,
                        group25,
                        group26,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 270:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                group24 = list()
                group25 = list()
                group25 = list()
                group26 = list()
                group27 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                    if i >= 230 and i <= 239:
                        group24.append(x[i])
                    if i == 239:
                        group24.append(None)
                    if i >= 240 and i <= 249:
                        group25.append(x[i])
                    if i == 249:
                        group25.append(None)
                    if i >= 250 and i <= 259:
                        group26.append(x[i])
                    if i == 259:
                        group26.append(None)
                    if i >= 260 and i <= 269:
                        group27.append(x[i])
                    if i == 269:
                        group27.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                        group24,
                        group25,
                        group26,
                        group27,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 280:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                group24 = list()
                group25 = list()
                group25 = list()
                group26 = list()
                group27 = list()
                group28 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                    if i >= 230 and i <= 239:
                        group24.append(x[i])
                    if i == 239:
                        group24.append(None)
                    if i >= 240 and i <= 249:
                        group25.append(x[i])
                    if i == 249:
                        group25.append(None)
                    if i >= 250 and i <= 259:
                        group26.append(x[i])
                    if i == 259:
                        group26.append(None)
                    if i >= 260 and i <= 269:
                        group27.append(x[i])
                    if i == 269:
                        group27.append(None)
                    if i >= 270 and i <= 279:
                        group28.append(x[i])
                    if i == 279:
                        group28.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                        group24,
                        group25,
                        group26,
                        group27,
                        group28,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 290:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                group24 = list()
                group25 = list()
                group25 = list()
                group26 = list()
                group27 = list()
                group28 = list()
                group29 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                    if i >= 230 and i <= 239:
                        group24.append(x[i])
                    if i == 239:
                        group24.append(None)
                    if i >= 240 and i <= 249:
                        group25.append(x[i])
                    if i == 249:
                        group25.append(None)
                    if i >= 250 and i <= 259:
                        group26.append(x[i])
                    if i == 259:
                        group26.append(None)
                    if i >= 260 and i <= 269:
                        group27.append(x[i])
                    if i == 269:
                        group27.append(None)
                    if i >= 270 and i <= 279:
                        group28.append(x[i])
                    if i == 279:
                        group28.append(None)
                    if i >= 280 and i <= 289:
                        group29.append(x[i])
                    if i == 289:
                        group29.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                        group24,
                        group25,
                        group26,
                        group27,
                        group28,
                        group29,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)

                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
            if len(x) == 300:
                group1 = list()
                group2 = list()
                group3 = list()
                group4 = list()
                group5 = list()
                group6 = list()
                group7 = list()
                group8 = list()
                group9 = list()
                group10 = list()
                group11 = list()
                group12 = list()
                group13 = list()
                group14 = list()
                group15 = list()
                group16 = list()
                group17 = list()
                group18 = list()
                group19 = list()
                group20 = list()
                group21 = list()
                group22 = list()
                group23 = list()
                group24 = list()
                group25 = list()
                group25 = list()
                group26 = list()
                group27 = list()
                group28 = list()
                group29 = list()
                group30 = list()
                for i in range(len(x) + 1):
                    if i <= 9:
                        group1.append(x[i])
                    if i == 9:
                        group1.append(None)
                    if i >= 10 and i <= 19:
                        group2.append(x[i])
                    if i == 19:
                        group2.append(None)
                    if i >= 20 and i <= 29:
                        group3.append(x[i])
                    if i == 29:
                        group3.append(None)
                    if i >= 30 and i <= 39:
                        group4.append(x[i])
                    if i == 39:
                        group4.append(None)
                    if i >= 40 and i <= 49:
                        group5.append(x[i])
                    if i == 49:
                        group5.append(None)
                    if i >= 50 and i <= 59:
                        group6.append(x[i])
                    if i == 59:
                        group6.append(None)
                    if i >= 60 and i <= 69:
                        group7.append(x[i])
                    if i == 69:
                        group7.append(None)
                    if i >= 70 and i <= 79:
                        group8.append(x[i])
                    if i == 79:
                        group8.append(None)
                    if i >= 80 and i <= 89:
                        group9.append(x[i])
                    if i == 89:
                        group9.append(None)
                    if i >= 90 and i <= 99:
                        group10.append(x[i])
                    if i == 99:
                        group10.append(None)
                    if i >= 100 and i <= 109:
                        group11.append(x[i])
                    if i == 109:
                        group11.append(None)
                    if i >= 110 and i <= 119:
                        group12.append(x[i])
                    if i == 119:
                        group12.append(None)
                    if i >= 120 and i <= 129:
                        group13.append(x[i])
                    if i == 129:
                        group13.append(None)
                    if i >= 130 and i <= 139:
                        group14.append(x[i])
                    if i == 139:
                        group14.append(None)
                    if i >= 140 and i <= 149:
                        group15.append(x[i])
                    if i == 149:
                        group15.append(None)
                    if i >= 150 and i <= 159:
                        group16.append(x[i])
                    if i == 159:
                        group16.append(None)
                    if i >= 160 and i <= 169:
                        group17.append(x[i])
                    if i == 169:
                        group17.append(None)
                    if i >= 170 and i <= 179:
                        group18.append(x[i])
                    if i == 179:
                        group18.append(None)
                    if i >= 180 and i <= 189:
                        group19.append(x[i])
                    if i == 189:
                        group19.append(None)
                    if i >= 190 and i <= 199:
                        group20.append(x[i])
                    if i == 199:
                        group20.append(None)
                    if i >= 200 and i <= 209:
                        group21.append(x[i])
                    if i == 209:
                        group21.append(None)
                    if i >= 210 and i <= 219:
                        group22.append(x[i])
                    if i == 219:
                        group22.append(None)
                    if i >= 220 and i <= 229:
                        group23.append(x[i])
                    if i == 229:
                        group23.append(None)
                    if i >= 230 and i <= 239:
                        group24.append(x[i])
                    if i == 239:
                        group24.append(None)
                    if i >= 240 and i <= 249:
                        group25.append(x[i])
                    if i == 249:
                        group25.append(None)
                    if i >= 250 and i <= 259:
                        group26.append(x[i])
                    if i == 259:
                        group26.append(None)
                    if i >= 260 and i <= 269:
                        group27.append(x[i])
                    if i == 269:
                        group27.append(None)
                    if i >= 270 and i <= 279:
                        group28.append(x[i])
                    if i == 279:
                        group28.append(None)
                    if i >= 280 and i <= 289:
                        group29.append(x[i])
                    if i == 289:
                        group29.append(None)
                    if i >= 290 and i <= 299:
                        group30.append(x[i])
                    if i == 299:
                        group30.append(None)
                dfResult = network.predict(
                    [
                        group1,
                        group2,
                        group3,
                        group4,
                        group5,
                        group6,
                        group7,
                        group8,
                        group9,
                        group10,
                        group11,
                        group12,
                        group13,
                        group14,
                        group15,
                        group16,
                        group17,
                        group18,
                        group19,
                        group20,
                        group21,
                        group22,
                        group23,
                        group24,
                        group25,
                        group26,
                        group27,
                        group28,
                        group29,
                        group30,
                    ]
                )
                df = pd.DataFrame(dfResult, columns=namaIndex)
                st.markdown(get_table_download_link(df), unsafe_allow_html=True)
                st.write(df)
