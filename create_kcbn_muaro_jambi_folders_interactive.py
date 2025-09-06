import os

def get_root_directory():
    while True:
        root_dir = input("Masukkan lokasi root folder untuk KCBN Muaro Jambi (misal D:\\KCBN_Muaro_Jambi): ").strip()
        if root_dir:
            return root_dir
        else:
            print("Lokasi tidak boleh kosong. Silakan coba lagi.")

candis = [
    "Candi_Kedaton",
    "Candi_Gumpung",
    "Candi_Tinggi",
    "Candi_Kembar_Batu",
    "Candi_Gedong_I",
    "Candi_Gedong_II",
    "Candi_Astano",
    "Candi_Koto_Mahligai"
]

folders = {
    "Deskripsi_Situs": ["Sejarah.pdf", "Arsitektur.pdf", "Nilai_Kultural.pdf", "Status_Hukum.pdf", "Pendaftaran_UNESCO.pdf"],
    "Peta_Dan_Lokasi": ["Peta_Geografis.pdf", "Peta_Situs.pdf", "Peta_Zonasi.pdf", "GIS_Data/shapefile", "GIS_Data/geodatabase"],
    "Struktur_Bangunan_Dan_Candi": candis,
    "Situs_Ritual": ["Punden", "Petirtaan", "Tempat_Persembahan"],
    "Artefak_Dan_Koleksi": ["Patung", "Prasasti", "Peralatan", "Koleksi_Lainnya"],
    "Sastra_Lisan_Dan_Tradisi": ["Cerita_Rakyat.pdf", "Lagu_Tradisional.pdf", "Upacara_Adat.pdf", "Rekaman_Audio"],
    "Permukiman_Kuno": ["Desa_Muara_Jambi", "Desa_Lainnya"],
    "Sistem_Perairan": ["Kanal", "Kolam", "Danau"],
    "Keanekaragaman_Hayati": ["Flora", "Fauna", "Ekosistem"],
    "Pendidikan_Dan_Penelitian": ["Program_Pendidikan.pdf", "Hasil_Penelitian.pdf", "Kolaborasi_Institusi.pdf", "Dataset/LiDAR", "Dataset/Drone", "Dataset/Survey_Lapangan"],
    "Revitalisasi_Dan_Pemeliharaan": ["Rencana_Pemugaran.pdf", "Anggaran.pdf", "Laporan_Progres.pdf", "Kontrak_Dan_Perizinan.pdf"],
    "Dokumentasi": ["Foto", "Video", "Audio"],
    "Komunikasi_Dan_Publikasi": ["Siaran_Pers.pdf", "Artikel_Media.pdf", "Materi_Promosi.pdf", "Website_SosialMedia"]
}

def create_folder_structure(base_path, folder_dict):
    for folder, subitems in folder_dict.items():
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)  # buat folder utama
        for item in subitems:
            # pastikan path item bertingkat juga dibuat
            item_path = os.path.join(folder_path, item)
            if folder == "Struktur_Bangunan_Dan_Candi":
                candi_subfolders = ["Deskripsi.pdf", "Foto", "Rencana_Pemugaran.pdf", "3D_Model"]
                for sub in candi_subfolders:
                    os.makedirs(os.path.join(item_path, sub), exist_ok=True)
            elif folder in ["Situs_Ritual", "Artefak_Dan_Koleksi", "Sistem_Perairan", "Keanekaragaman_Hayati", "Permukiman_Kuno", "Dokumentasi", "Komunikasi_Dan_Publikasi"]:
                os.makedirs(item_path, exist_ok=True)
            elif "/" in item or "\\" in item:
                # jika ada folder bertingkat di string (misal "GIS_Data/shapefile"), buat seluruh jalur
                os.makedirs(item_path, exist_ok=True)
            else:
                # buat file kosong placeholder
                with open(item_path, 'a', encoding='utf-8') as f:
                    f.write("")

if __name__ == "__main__":
    root_dir = get_root_directory()
    create_folder_structure(root_dir, folders)
    print(f"Struktur folder KCBN Muaro Jambi berhasil dibuat di: {root_dir}")
