import os
from datetime import datetime
import git

def create_txt_folders_and_push(dates):
    current_directory = os.getcwd()

    for date in dates:
        # Tarih formatını ayarla ve klasör adını oluştur
        formatted_date = date.strftime("%Y-%m-%d")
        folder_name = formatted_date
        folder_path = os.path.join(current_directory, folder_name)

        # Gerçek tarih ile istenen tarih arasındaki farkı kontrol et
        today = datetime.now().date()
        if today == date.date():
            # Klasörü oluştur
            os.makedirs(folder_path)
            print(f"{folder_name} klasörü oluşturuldu.")

            # GitHub'a pushla
            push_to_github(folder_name)
        else:
            print(f"{folder_name} klasörü oluşturulmadı.")

def push_to_github(folder_name):
    try:
        # Git deposunu aç
        repo = git.Repo(os.getcwd())

        # Değişiklikleri etkinleştir
        repo.index.add(folder_name)

        # Commit yap
        repo.index.commit(f"{folder_name} klasörü oluşturuldu.")

        # Değişiklikleri GitHub'a it
        origin = repo.remote(name="origin")
        origin.push()
        print(f"{folder_name} klasörü GitHub'a başarıyla pushlandı.")
    except Exception as e:
        print(f"Hata oluştu: {e}")

if __name__ == "__main__":
    # Oluşturmak istediğiniz tarihleri belirleyin
    dates = [
        datetime(2024, 12, 28),
        datetime(2024, 12, 30),
        datetime(2024, 12, 31),
        datetime(2025, 1, 27),
        datetime(2025, 1, 8),
        datetime(2025, 1, 9),
        datetime(2025, 1, 10),
        datetime(2025, 1, 11),
        datetime(2025, 4, 12),
        datetime(2025, 4, 19),
        datetime(2025, 4, 22),
        datetime(2025, 4, 23),
        datetime(2025, 4, 24),
        datetime(2025, 4, 25),
        datetime(2025, 4, 26)
    ]

    # Klasörleri oluştur ve GitHub'a pushla
    create_txt_folders_and_push(dates)
