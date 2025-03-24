# Import module yang diperlukan
import csv
import os

# Menentukan lokasi file CSV
namafile = r'C:\Users\LENOVO\OneDrive\Desktop\py\data karyawan.csv'

# Fungsi untuk membuat file CSV jika belum ada
def init_csv():
    if not os.path.exists(namafile):
        with open(namafile, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['ID', 'Nama', 'Jabatan', 'Gaji'])

# Fungsi untuk menambahkan karyawan
def tambah_karyawan(id, nama, jabatan, gaji):
    with open(namafile, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([id, nama, jabatan, gaji])
    print('Berhasil menambahkan data karyawan baru')

# Fungsi untuk menghapus data karyawan
def hapus_karyawan(id):
    rows = []
    found = False
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        # Mengumpulkan semua baris dan memeriksa ID dengan memperhatikan spasi dan tipe data
        for row in reader:
            # Membandingkan dengan memastikan tidak ada spasi ekstra dan ID adalah string
            if row[0].strip() == id.strip():
                found = True
            else:
                rows.append(row)

    if found:
        with open(namafile, mode='w', newline='') as file:
            writer = csv.writer(file)
            # Menulis kembali semua baris kecuali yang dihapus
            writer.writerows(rows)
        print(f'Data Karyawan dengan ID {id} berhasil dihapus')
    else:
        print(f'Data Karyawan dengan ID {id} tidak ditemukan')

# Fungsi untuk mengubah data karyawan
def update_karyawan(id, nama=None, jabatan=None, gaji=None):
    rows = []
    updated = False
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        rows = list(reader)

    with open(namafile, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(rows[0])
        for row in rows[1:]:
            if row[0] == id:
                if nama:
                    row[1] = nama
                if jabatan:
                    row[2] = jabatan
                if gaji:
                    row[3] = gaji
                updated = True
            writer.writerow(row)

    if updated:
        print(f'Data Karyawan dengan ID {id} berhasil diperbarui')
    else:
        print(f'Data karyawan dengan ID {id} tidak dapat diperbarui')

# Fungsi untuk menampilkan semua karyawan
def tampilkan_karyawan():
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')

# Fungsi untuk menampilkan karyawan berdasarkan ID
def tampilkan_karyawan_berdasarkan_id(id):
    found = False
    with open(namafile, mode='r', newline='') as file:
        reader = csv.reader(file)
        for row in reader:
            if row[0] == id:
                found = True
                print(f'ID: {row[0]}, Nama: {row[1]}, Jabatan: {row[2]}, Gaji: {row[3]}')
                break
    if not found:
        print(f'Tidak dapat menemukan karyawan dengan ID {id}')

# Membuat menu
def menu():
    while True:
        print('\n Pilihan:')
        print('1. Menambahkan Karyawan')
        print('2. Menghapus Karyawan')
        print('3. Update Karyawan')
        print('4. Tampilkan Karyawan')
        print('5. Tampilkan Karyawan berdasarkan ID')
        print('6. Keluar')

        inputUser = input('Masukkan angka yang ingin anda lakukan (1-6): ')

        if inputUser == '1':
            id = input('Masukkan ID: ')
            nama = input('Masukkan Nama Karyawan: ')
            jabatan = input('Masukkan Jabatan: ')
            gaji = input('Masukkan Gaji: ')
            tambah_karyawan(id, nama, jabatan, gaji)
        elif inputUser == '2':
            id = input('Masukkan ID karyawan yang ingin dihapus: ')
            hapus_karyawan(id)
        elif inputUser == '3':
            id = input('Masukkan ID karyawan yang akan diperbarui: ')
            nama = input('Masukkan nama baru (kosongkan jika tidak diubah): ')
            jabatan = input('Masukkan Jabatan Baru (kosongkan jika tidak di ubah): ')
            gaji = input('Masukkan Gaji baru (kosongkan jika tidak di ubah): ')
            update_karyawan(id, nama if nama else None, jabatan if jabatan else None, gaji if gaji else None)
        elif inputUser == '4':
            tampilkan_karyawan()
        elif inputUser == '5':
            id = input('Masukkan ID karyawan yang ingin anda cari: ')
            tampilkan_karyawan_berdasarkan_id(id)
        elif inputUser == '6':
            print('Keluar dari program')
            break
        else:
            print('Silahkan masukkan angka dari 1-6')

if __name__ == '__main__':
    init_csv()
    menu()