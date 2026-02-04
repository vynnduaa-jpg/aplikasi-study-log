"""Simple Study Log App

Fitur:
- tambah_catatan(): minta input mapel, topik, durasi (menit) -> simpan ke list `catatan`
- lihat_catatan(): tampilkan semua catatan dengan rapi
- total_waktu(): hitung total durasi dari semua catatan
- filter_per_mapel(): fitur pengembangan (Filter per mapel)

Struktur data untuk pemula: list of dicts
Contoh catatan: {'mapel': 'Matematika', 'topik': 'Integral', 'durasi': 60}
"""

from typing import List, Dict

Catatan = Dict[str, object]


# Helper: warna ANSI sederhana
ANSI = {
    'reset': '\u001b[0m',
    'red': '\u001b[31m',
    'green': '\u001b[32m',
    'yellow': '\u001b[33m',
    'blue': '\u001b[34m',
    'magenta': '\u001b[35m',
    'cyan': '\u001b[36m',
    'bright': '\u001b[1m',
    'dim': '\u001b[2m',
}


def color(text: str, name: str) -> str:
    code = ANSI.get(name, '')
    return f"{code}{text}{ANSI['reset']}" if code else text


# Mapel ke emoji (contoh sederhana)
MAPEL_EMOJI = {
    'matematika': '➗',
    'bahasa indonesia': '📚',
    'bahasa inggris': '🗣️',
    'ipa': '🔬',
    'ips': '🌍',
    'pemrograman': '💻',
    'fisika': '⚛️',
    'kimia': '⚗️',
    'biologi': '🧬',
}


def emoji_for_mapel(mapel: str) -> str:
    return MAPEL_EMOJI.get(mapel.lower(), '📝')


def tambah_catatan(catatan: List[Catatan]) -> None:
    """Minta input mapel, topik, dan durasi lalu simpan ke list.

    Validasi: durasi harus bilangan bulat positif.
    """
    mapel = input("Masukkan mapel: ").strip()
    topik = input("Masukkan topik: ").strip()

    while True:
        durasi_input = input("Masukkan durasi belajar (menit): ").strip()
        try:
            durasi = int(durasi_input)
            if durasi <= 0:
                print("Durasi harus lebih dari 0. Coba lagi.")
                continue
            break
        except ValueError:
            print("Masukkan angka bulat untuk durasi (misal: 45). Coba lagi.")

    catatan.append({
        'mapel': mapel,
        'topik': topik,
        'durasi': durasi,
    })
    print(color("Catatan berhasil ditambahkan. ✅", 'green'))


def lihat_catatan(catatan: List[Catatan]) -> None:
    """Tampilkan semua catatan belajar dalam bentuk tabel berwarna dengan emoji.

    Jika tidak ada data, tampilkan pesan yang sesuai.
    """
    if not catatan:
        print(color("Belum ada catatan belajar. Buat catatan baru dulu ya! 📝", 'yellow'))
        return

    # Lebar kolom
    w_no = 4
    w_mapel = 20
    w_topik = 34
    w_dur = 8

    # Header
    header = (
        f"+{'-' * w_no}+{'-' * w_mapel}+{'-' * w_topik}+{'-' * w_dur}+"
    )
    title = (
        f"| {'No'.ljust(w_no - 1)}| {color('Mapel 📚'.ljust(w_mapel - 1), 'bright')}| {color('Topik 🧾'.ljust(w_topik - 1), 'bright')}| {color('Durasi ⏱️'.rjust(w_dur - 1), 'bright')}|"
    )

    print('\n' + color('Daftar Catatan Belajar:', 'magenta'))
    print(header)
    print(title)
    print(header)

    # Rows dengan warna bergantian
    for i, c in enumerate(catatan, start=1):
        emoji = emoji_for_mapel(c['mapel'])
        mapel_display = f"{emoji} {c['mapel']}"
        mapel_display = mapel_display[:w_mapel-1].ljust(w_mapel - 1)
        topik_display = c['topik'][:w_topik-1].ljust(w_topik - 1)
        dur_display = f"{c['durasi']} menit".rjust(w_dur - 1)

        # Pilih warna baris: ganjil = cyan, genap = dim
        warna = 'cyan' if i % 2 == 1 else 'dim'
        row = (
            f"| {str(i).ljust(w_no - 1)}| {mapel_display}| {topik_display}| {dur_display}|"
        )
        print(color(row, warna))

    print(header)
    total = total_waktu(catatan)
    print(color(f"Total catatan: {len(catatan)}   |   Total durasi: {total} menit", 'green'))
    print()


def total_waktu(catatan: List[Catatan]) -> int:
    """Hitung total durasi belajar dari semua catatan (dalam menit)."""
    return sum(c['durasi'] for c in catatan)


# Fitur pengembangan: Filter per mapel
def filter_per_mapel(catatan: List[Catatan]) -> None:
    """Tampilkan semua catatan untuk mapel tertentu (tidak sensitif huruf besar/kecil)."""
    if not catatan:
        print("Belum ada catatan untuk difilter. Tambahkan catatan dulu.")
        return

    pilihan = input("Masukkan nama mapel yang ingin difilter: ").strip()
    if not pilihan:
        print("Nama mapel kosong. Batal.")
        return

    hasil = [c for c in catatan if c['mapel'].lower() == pilihan.lower()]
    if not hasil:
        print(f"Tidak ditemukan catatan untuk mapel '{pilihan}'.")
        return

    print(f"\nCatatan untuk mapel: {pilihan}")
    print("{:<4} {:<30} {:>8}".format("No.", "Topik", "Durasi"))
    print("-" * 55)
    for i, c in enumerate(hasil, start=1):
        print("{:<4} {:<30} {:>6} menit".format(i, c['topik'], c['durasi']))
    print("-" * 55)
    print(f"Total: {len(hasil)} catatan, total durasi: {sum(c['durasi'] for c in hasil)} menit\n")


# Tampilkan menu dalam bentuk tabel berwarna
def print_menu() -> None:
    items = [
        ('1', 'Tambah catatan', '📝'),
        ('2', 'Lihat semua catatan', '📋'),
        ('3', 'Filter per mapel', '🔎'),
        ('4', 'Total waktu belajar', '⏱️'),
        ('5', 'Keluar', '🚪'),
    ]
    w_no = 4
    w_text = 40
    header = f"+{'-' * w_no}+{'-' * w_text}+"

    print('\n' + color('=== Study Log App ===', 'bright'))
    print(header)
    for num, text, emj in items:
        txt = f"{emj} {text}"
        print(f"| {num.ljust(w_no-1)}| {color(txt.ljust(w_text-1), 'blue')}|")
    print(header)


def main() -> None:
    catatan: List[Catatan] = []  # Penyimpanan sementara di memori

    while True:
        print_menu()
        pilih = input("Pilih menu (1-5): ").strip()

        if pilih == '1':
            tambah_catatan(catatan)
        elif pilih == '2':
            lihat_catatan(catatan)
        elif pilih == '3':
            filter_per_mapel(catatan)
        elif pilih == '4':
            total = total_waktu(catatan)
            print(f"Total durasi belajar: {total} menit")
        elif pilih == '5':
            print("Sampai jumpa! 👋")
            break
        else:
            print("Pilihan tidak valid. Masukkan angka antara 1 sampai 5.")


if __name__ == '__main__':
    main()
