import pandas as pd

# Data nama dan skor
data = {
    'Nama': ['Nahda', 'Sam', 'Dina',],
    'Skor': [92, 88, 85]
}

# Bikin tabel dan simpan
df = pd.DataFrame(data)
df.to_csv('data_peserta.csv', index=False)

print("CSV udah jadi!")