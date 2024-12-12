import pandas as pd
import os
import requests

class ExamFileDownloader:
    def __init__(self, csv_file, download_folder='downloaded_files'):
        """
        初始化下載器，設定 CSV 檔案路徑及下載資料夾。
        :param csv_file: str, CSV 檔案的路徑
        :param download_folder: str, 儲存下載檔案的資料夾
        """
        self.csv_file = csv_file
        self.download_folder = download_folder
        self.file_mapping = {}
        os.makedirs(self.download_folder, exist_ok=True)

    def download_files(self):
        """
        讀取 CSV 檔案並下載檔案。
        """
        # 讀取CSV檔案
        df = pd.read_csv(self.csv_file)

        for index, row in df.iterrows():
            file_url_1 = row['File_1']
            file_url_2 = row['File_2']

            # 為檔案生成新名稱
            new_name_1 = f"file_{index + 1}_1.pdf"
            new_name_2 = f"file_{index + 1}_2.pdf"

            # 嘗試下載 File_1
            if pd.notna(file_url_1) and file_url_1 != '0':
                self._download_file(file_url_1, new_name_1)

            # 嘗試下載 File_2
            if pd.notna(file_url_2) and file_url_2 != '0':
                self._download_file(file_url_2, new_name_2)

    def _download_file(self, url, new_name):
        """
        下載檔案並重新命名。
        :param url: str, 檔案的原始 URL
        :param new_name: str, 檔案的新名稱
        """
        try:
            response = requests.get(url)
            response.raise_for_status()  # 確保下載成功
            file_path = os.path.join(self.download_folder, new_name)
            with open(file_path, 'wb') as file:
                file.write(response.content)
            self.file_mapping[url] = new_name
        except Exception as e:
            print(f"Failed to download {url}: {e}")

    def save_mapping(self, mapping_file='file_mapping.csv'):
        """
        將檔案對應關係儲存到 CSV 檔案。
        :param mapping_file: str, 對應關係檔案的儲存名稱
        """
        mapping_df = pd.DataFrame(list(self.file_mapping.items()), columns=['Original_URL', 'Renamed_File'])
        mapping_df.to_csv(mapping_file, index=False)
        print(f"檔案對應關係已儲存到 {mapping_file}")

# 使用方式範例
# # 初始化下載器
# downloader = ExamFileDownloader('exam_data.csv')
# # 執行下載
# downloader.download_files()
# # 儲存對應關係
# downloader.save_mapping()
