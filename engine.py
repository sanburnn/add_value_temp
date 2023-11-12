import pandas as pd

# Membaca file Excel
file_path = '/Users/dimas/Downloads/test.xls'  # Ganti dengan path file Excel yang sesuai
df = pd.read_excel(file_path)

# Menambahkan nilai 0.5 ke semua nilai di kolom "Temp.(°C)"
df['Temp.(°C)'] = df['Temp.(°C)'] + 0.5

# Menyimpan perubahan kembali ke file Excel
df.to_excel(file_path, index=False)

print("Nilai 0.5 telah ditambahkan ke semua nilai di kolom 'Temp.(°C)'.")
