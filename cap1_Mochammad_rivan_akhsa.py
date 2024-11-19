import sys
from tabulate import tabulate
# inventory list of lists
list_item_roti = [
    ['ITM001', 'Donat', 10000, 10],
    ['ITM002', 'Muffin', 15000, 10],
    ['ITM003', 'Brownies', 20000, 10],
    ['ITM004', 'Roti Tawar', 10000, 10],
    ['ITM005', 'Cupcake', 5000, 10]
]
index_item_roti = 6

def tampilkan_tabel_roti(data):
    # tabel header
    headers = ["ID", "Nama Roti", "Harga", "Stok"]
    table = tabulate(data, headers=headers, tablefmt="grid")
    print(table)
#tambah roti
def tambah_roti():
    print("\nOpsi: Tambah Roti")
    print("== Pilih Menu Tambah Roti ==")
    print("1. Tambah Item")
    print("2. Keluar")
    while True:
        opsi_tambah_roti = input("\nPilih Opsi Tambah 1/2: ")
        if opsi_tambah_roti == '1':
            input_roti_baru()
        elif opsi_tambah_roti == '2':
            print("Kembali ke menu utama.")
            menu_utama()  
            break
        else:
            print("Input Tidak Valid. Silakan masukkan 1 atau 2.")

def generate_new_id():
    # Mengambil ID terakhir yang ada dalam list_item_roti
    last_id = list_item_roti[-1][0]  # ID terakhir
    # Mengambil angka terakhir dari ID dan menambahkannya dengan 1
    last_number = int(last_id[3:])  # Ambil angka dari ID, misalnya ITM001 -> 1
    new_number = last_number + 1  # Increment angka terakhir
    new_id = f"ITM{new_number:03d}"  # Format dengan 3 digit (misalnya ITM001, ITM002, dst.)
    return new_id
    
def input_roti_baru():
    while True:
        # Generate ID otomatis
        new_id = generate_new_id()
        print(f"ID Roti Baru yang akan digunakan: {new_id}")

        # Input nama roti
        input_nama_roti = input("Masukkan Nama Roti Baru: ").strip()
        if not input_nama_roti:
            print("Nama roti tidak boleh kosong. Silakan masukkan nama roti.")
        elif not input_nama_roti.isalpha():
            print("Nama roti hanya boleh berisi huruf. Silakan masukkan nama roti yang valid.")
        else:
            while True:
                input_harga_roti = input("Masukkan Harga Roti Baru: ").strip()
                if input_harga_roti.isdigit() and int(input_harga_roti) > 0:
                    input_harga_roti = int(input_harga_roti)
                    tambahkan_stock_roti(new_id, input_nama_roti, input_harga_roti)
                    return  # Selesai, kembali ke menu tambah roti
                else:
                    print("Masukkan nominal harga yang valid!")


def tambahkan_stock_roti(new_id, input_nama_roti, input_harga_roti):
    while True:
        input_stock_roti = input("Masukkan Stock Roti Baru: ").strip() #masukkan  input roti baru
        if input_stock_roti.isdigit():
            input_stock_roti = int(input_stock_roti)
            konfirmasi_hapus = konfirmasi(
                f"Apakah Anda yakin ingin menambahkan item {input_nama_roti} dengan ID {new_id}, harga Rp {input_harga_roti}, dan stok {input_stock_roti}? (y/n): "
            )
            if konfirmasi_hapus == True:
                list_item_roti.append([new_id, input_nama_roti, input_harga_roti, input_stock_roti])  
                print(f"\nItem dengan ID {new_id}, nama {input_nama_roti}, harga {input_harga_roti}, stock {input_stock_roti} berhasil ditambahkan!")
                break
            elif konfirmasi_hapus == False:
                print("\nPenambahan item dibatalkan.")
                break
            else:
                print("Masukkan 'y' untuk ya atau 'n' untuk tidak.")
        else:
            print("Masukkan nominal stock yang valid.")

    # Setelah selesai menambah roti, kembali ke menu tambah roti
    tambah_roti()


# Fungsi untuk menampilkan menu utama
def tampilkan_main_menu():
    global list_item_roti
    while True:
        print("\nOpsi:")
        print("1. Tampilkan Menu Keseluruhan")
        print("2. Tampilkan Menu Berdasarkan ID")
        print("3. Keluar")

        choice = input("Pilih opsi: ")
        if choice == '1':
            menu_keseluruhan()
        elif choice == '2':
            # Tampilkan ID dan Nama Roti
            print("\nMenu Roti Berdasarkan ID:")
            tabel_baru = [[roti[0], roti[1]] for roti in list_item_roti]
            headers = ["ID", "Nama Roti"]
            print(tabulate(tabel_baru, headers=headers, tablefmt="grid"))

            while True:
                input_id = input('Masukkan ID Roti yang ingin dilihat (misal: ITM001): ').strip().upper()

                # Cari dan tampilkan informasi lengkap tentang roti yang dipilih
                found = False
                for roti in list_item_roti:
                    if roti[0] == input_id:
                        print(f'\nDetail Roti:')
                        tabel_baru = [[roti[0], roti[1], roti[2], roti[3]]]
                        headers = ["ID", "Nama Roti", "Harga", "Stok"]
                        print(tabulate(tabel_baru, headers=headers, tablefmt="grid"))
                        found = True
                        break

                if found:
                    break  # Keluar dari loop setelah ID ditemukan dan detail ditampilkan
                else:
                    print(f"ID '{input_id}' tidak ditemukan. Silakan coba lagi.")
        elif choice == '3':
            print("Terima kasih! Keluar dari program.")
            break  # Keluar dari program
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, atau 3.")

# Fungsi untuk menampilkan menu keseluruhan
def menu_keseluruhan():
    tampilkan_tabel_roti(list_item_roti)

    while True:
        print("\nTampilkan Menu Keseluruhan:")
        print("1. Sortir berdasarkan harga termurah")
        print("2. Sortir berdasarkan harga termahal")
        print("3. Sortir berdasarkan stok terendah")
        print("4. Sortir berdasarkan stok tertinggi")
        print("5. Kembali ke menu utama")

        opsi_sortir = input("Pilih opsi (1/2/3/4/5): ")
        if opsi_sortir == '1':
            sorted_menu = bubble_sort(list_item_roti, ascending=True, by_stock=False)
            print("\nMenu Roti (Harga Termurah ke Termahal):")
            print(tabulate(sorted_menu, headers=["ID", "Nama Roti", "Harga", "Stok"], tablefmt="grid"))
            break
        elif opsi_sortir == '2':
            sorted_menu = bubble_sort(list_item_roti, ascending=False, by_stock=False)
            print("\nMenu Roti (Harga Termahal ke Termurah):")
            print(tabulate(sorted_menu, headers=["ID", "Nama Roti", "Harga", "Stok"], tablefmt="grid"))
            break
        elif opsi_sortir == '3':
            sorted_menu = bubble_sort(list_item_roti, ascending=True, by_stock=True)
            print("\nMenu Roti (Stok Terendah ke Tertinggi):")
            print(tabulate(sorted_menu, headers=["ID", "Nama Roti", "Harga", "Stok"], tablefmt="grid"))
            break
        elif opsi_sortir == '4':
            sorted_menu = bubble_sort(list_item_roti, ascending=False, by_stock=True)
            print("\nMenu Roti (Stok Tertinggi ke Terendah):")
            print(tabulate(sorted_menu, headers=["ID", "Nama Roti", "Harga", "Stok"], tablefmt="grid"))
            break
        elif opsi_sortir == '5':
            break  # Kembali ke menu utama
        else:
            print("Pilihan tidak valid. Silakan pilih 1, 2, 3, 4, atau 5.")

# Fungsi Bubble Sort untuk mengurutkan berdasarkan harga atau stok
def bubble_sort(roti_list, ascending=True, by_stock=False):
    n = len(roti_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            # Tentukan indeks yang digunakan untuk sorting: harga (indeks 2) atau stok (indeks 3)
            if by_stock:
                compare_index = 3  # Indeks untuk stok
            else:
                compare_index = 2  # Indeks untuk harga

            # Bandingkan dan tukar berdasarkan arah ascending/descending
            if (ascending and roti_list[j][compare_index] > roti_list[j + 1][compare_index]) or \
               (not ascending and roti_list[j][compare_index] < roti_list[j + 1][compare_index]):
                roti_list[j], roti_list[j + 1] = roti_list[j + 1], roti_list[j]
    return roti_list






def menu_update_roti():
    while True:
        print("\nOpsi 3: Update Roti")
        print(" == Pilih Opsi Update == ")
        print(" 1. Perbaharui Harga ")
        print(" 2. Perbaharui Stock ")
        print(" 3. Keluar")

#input update roti

        input_nomor_roti = input('Pilih Opsi Update 1/2/3: ')
        if input_nomor_roti.isdigit():
            input_nomor_roti = int(input_nomor_roti)  # Mengubah ke indeks list (0-based)
                # Menentukan dan memperbarui harga atau stock
            if input_nomor_roti == 1:
                    update_roti('harga')
            elif input_nomor_roti == 2:
                    update_roti('stock')
            elif input_nomor_roti == 3:
                    menu_utama()
                    break
            else:
                    print('Input tidak Valid')
        else:
            print('Masukkan Index Valid !!')

def update_roti(kolom):
    while True:
        # Menampilkan daftar roti
        print("\nDaftar Menu Roti:")
        tampilkan_tabel_roti (list_item_roti)

        input_id_roti = input('Masukkan ID Roti Yang Mau Diupdate: ').strip().upper()

        # Mencari roti berdasarkan ID
        roti_ditemukan = None
        for roti in list_item_roti:
            if roti[0] == input_id_roti:
                roti_ditemukan = roti
                break  # Keluar dari loop jika ID ditemukan

        if not roti_ditemukan:
            print(f"ID '{input_id_roti}' tidak ditemukan. Silakan coba lagi.\n")
            continue  # Kembali meminta input ID
        else:
            # Proses pembaruan
            while True:
                try:
                    nilai_baru = int(input(f"Masukkan {kolom.capitalize()} Baru untuk {roti_ditemukan[1]}: "))
                    if kolom == 'harga' and nilai_baru <= 0:
                        print("Harga harus lebih besar dari 0.")
                    elif kolom == 'stock' and nilai_baru < 0:
                        print("Stock tidak boleh negatif.")
                    else:
                        if konfirmasi(f"Apakah Anda yakin ingin mengubah {kolom} menjadi {nilai_baru}? (y/n): "):
                            roti_ditemukan[2 if kolom == 'harga' else 3] = nilai_baru
                            print(f"Roti dengan ID {roti_ditemukan[0]}, nama {roti_ditemukan[1]} berhasil diubah {kolom}nya menjadi {nilai_baru}.")
                        else:
                            print(f"Pengubahan {kolom} dibatalkan.")
                        return  # Keluar setelah selesai proses pembaruan
                except:
                    print(f"Masukkan nilai {kolom} yang valid (angka).")




def hapus_roti():
    while True:
        print("\nOpsi: Hapus Roti")
        print("== Pilih Menu Hapus Roti ==")
        print("1. Hapus Item")
        print("2. Keluar")
        
        opsi_hapus_roti = input("Pilih Opsi Hapus (1/2): ")
        if opsi_hapus_roti == '1':
            pilihan_hapus()
        elif opsi_hapus_roti == '2':
            print("Kembali ke menu utama.")
            menu_utama()  # Fungsi untuk kembali ke menu utama (pastikan ini sudah didefinisikan)
            break
        else:
            print("Input tidak valid. Silakan masukkan 1 atau 2.")

def pilihan_hapus():
    print("\nMenu Roti:")
    tampilkan_tabel_roti (list_item_roti)

    while True:
        input_id_roti = input("Masukkan ID Roti yang ingin dihapus: ").strip().upper()

        # Cek apakah ID ditemukan
        roti_ditemukan = None
        for roti in list_item_roti:
            if roti[0] == input_id_roti:
                roti_ditemukan = roti
                break

        if roti_ditemukan:
            print(f"Anda akan menghapus item: {roti_ditemukan[0]} | {roti_ditemukan[1]} | Stok: {roti_ditemukan[3]} | Harga: Rp {roti_ditemukan[2]}")
            
            # Konfirmasi penghapusan
            while True:
                konfirmasi_hapus = konfirmasi("Apakah Anda yakin ingin menghapus item ini? (y/n): ")
                if konfirmasi_hapus == True:
                    list_item_roti.remove(roti_ditemukan)
                    print(f"\nItem {roti_ditemukan[0]} | {roti_ditemukan[1]} | Stok: {roti_ditemukan[3]} | Harga: Rp {roti_ditemukan[2]} berhasil dihapus.")
                    break
                elif konfirmasi_hapus == False:
                    print("\nPenghapusan dibatalkan.")
                    break
                else:
                    print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")
            break
        else:
            print(f"ID '{input_id_roti}' tidak ditemukan. Silakan coba lagi.")




def konfirmasi(text):
    while True:
        konfirmasi_input = input(text).lower().strip()
        if konfirmasi_input == "y":
            return True
        elif konfirmasi_input == "n":
            return False
        else:
            print("Input tidak valid. Masukkan 'y' untuk ya atau 'n' untuk tidak.")



# Menu utama
def menu_utama():
    while True:
        print("\n== Inventory Toko Roti == \n 1. Tambahkan Roti \n 2. Lihat Menu Roti \n 3. Perbaharui Stok/Harga Item \n 4. Hapus Item \n 5. Keluar\n")
        input_opsi = input('Pilih Opsi 1-5: ')
        
        if input_opsi == '1':
            tambah_roti()
        elif input_opsi == '2':
            tampilkan_main_menu()
        elif input_opsi == '3':
            menu_update_roti()
        elif input_opsi == '4':
            hapus_roti()
        elif input_opsi == '5':
            print('Keluar')
            sys.exit()
        else:
            print("Opsi tidak valid, silakan pilih 1-5.")
menu_utama()
