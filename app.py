from flask import Flask, render_template, request
import pandas as pd
import os

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nama = request.form['nama']
        skor = request.form['skor']

        # Data baru yang dimasukkan user
        data_baru = pd.DataFrame([[nama, int(skor)]], columns=['Nama', 'Skor'])

        # Cek apakah file sudah ada
        if os.path.exists('data_peserta.csv'):
            data_lama = pd.read_csv('data_peserta.csv')
            data = pd.concat([data_lama, data_baru], ignore_index=True)
        else:
            data = data_baru

        # Simpan kembali ke file
        data.to_csv('data_peserta.csv', index=False)

        return "Data berhasil disimpan ke CSV!"

    return render_template('form.html')

if __name__ == '__main__':
    app.run(debug=True)