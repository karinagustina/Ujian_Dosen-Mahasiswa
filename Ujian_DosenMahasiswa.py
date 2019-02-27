# Ujian_Dosen & Mahasiswa
# Soal 3.2

import pymongo
import matplotlib.pyplot as plt
import pandas as pd

# Mengakses Database Kampus dari MongoDB
url = "mongodb://localhost:27017"
dbmongo = pymongo.MongoClient(url)

mydb = dbmongo["Kampus"]
dbdosen = mydb["Dosen"]
datadosen = []
for i in dbdosen.find():
    datadosen.append(i)
dbmahasiswa = mydb["Mahasiswa"]
datamahasiswa = []
for j in dbmahasiswa.find():
    datamahasiswa.append(j)

# print(datamahasiswa)
# print(datadosen)

# Membuat DataFrame Dosen dan Mahasiswa
dfDosen = pd.DataFrame(datadosen)
dfD = dfDosen.drop(columns=['_id','status'])
dfMahasiswa = pd.DataFrame(datamahasiswa)
dfM = dfMahasiswa.drop(columns=['_id'])
df1 = pd.DataFrame({'status': ['dosen','dosen','dosen']})
df2 = pd.DataFrame({'status': ['mahasiswa','mahasiswa','mahasiswa']})
print(dfD.join(df1).loc[:,['asal','nama','status','usia']])
print(dfM.join(df2).loc[:,['asal','nama','status','usia']])

# Membuat grafik batang dari DataFrame Dosen dan Mahasiswa
nDosen = dfDosen.iloc[:,4]
uDosen = dfDosen.iloc[:,8]
nMahasiswa = dfMahasiswa.iloc[:,3]
uMahasiswa = dfMahasiswa.iloc[:,6]
nD = []
for k in nDosen:
    nD.append(k)
uD = []
for l in uDosen:
    uD.append(l)
nM = []
for m in nMahasiswa:
    nM.append(m)
uM = []
for n in uMahasiswa:
    uM.append(n)
plt.bar(nD,uD)
plt.bar(nM,uM)
plt.title('Usia Warga Kampus')
plt.legend(['Dosen','Mahasiswa'])
plt.grid(True)
plt.show()