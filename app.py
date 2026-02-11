from flask import Flask, render_template, request, flash, redirect, url_for

app = Flask(__name__)
app.secret_key = "smkicipasung_keren" # Wajib untuk fitur Flash Message

@app.route('/')
def home():
    daftar_jurusan = [
        {"kode": "TJKT", "nama": "Teknik Jaringan Komputer & Telekomunikasi", "deskripsi": "Fokus pada keahlian jaringan dan cloud.", "ikon": "bi-cpu"},
        {"kode": "TBSM", "nama": "Teknik Bisnis Sepeda Motor", "deskripsi": "Mempelajari mesin otomotif roda dua.", "ikon": "bi-gear-wide"},
        {"kode": "MPLB", "nama": "Manajemen Perkantoran & Layanan Bisnis", "deskripsi": "Administrasi digital dan layanan bisnis.", "ikon": "bi-briefcase"}
    ]
    return render_template('index.html', jurusan=daftar_jurusan)

# Bagian ini yang memperbaiki error 404 di screenshot Anda
@app.route('/daftar', methods=['POST'])
def daftar():
    nama = request.form.get('nama')
    if nama:
        flash(f"Terima kasih {nama}! Data pendaftaran Anda telah berhasil terkirim.", "success")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)