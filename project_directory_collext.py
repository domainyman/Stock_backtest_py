import os
import ast
import glob
from pytube import YouTube

# class collect_py_file:
#     def collect_py_files(directory):
#         py_files = []
#         for root, dirs, files in os.walk(directory):
#             for file in files:
#                 if file.endswith('.py'):
#                     file_path = os.path.join(root, file)
#                     py_files.append(file_path)
#         return py_files

#     # 指定项目目录
#     project_directory = 'D:\\Python\\Stock_py'

#     # 收集项目中的 .py 文件路径
#     py_files = collect_py_files(project_directory)

#     # 打印收集到的 .py 文件路径
#     for file in py_files:
#         print(file)


# class det_import:

#     @staticmethod
#     def extract_imports(file_path):
#         with open(file_path, "r", encoding="utf-8", errors="replace") as file:
#             tree = ast.parse(file.read())

#         imports = []
#         for node in ast.walk(tree):
#             if isinstance(node, ast.Import):
#                 for alias in node.names:
#                     imports.append(alias.name)
#             elif isinstance(node, ast.ImportFrom):
#                 if node.module is not None:
#                     for alias in node.names:
#                         imports.append(node.module + '.' + alias.name)
#                 else:
#                     for alias in node.names:
#                         imports.append(alias.name)

#         return imports

# # 指定要檢查的專案目錄路徑
# project_directory = "D:\\Python\\Stock_py"

# # 指定要排除的目錄路徑
# exclude_directories = [
#     "D:\\Python\\Stock_py\\env"
# ]
# import_lists = []
# # 獲取專案目錄中的所有 Python 檔案路徑
# python_files = glob.glob(project_directory + "/**/*.py", recursive=True)

# # 提取並列印每個檔案中的 import 語句
# for file_path in python_files:
#     if any(exclude_dir in file_path for exclude_dir in exclude_directories):
#         continue

#     import_list = det_import.extract_imports(file_path)
#     print("File:", file_path)
#     print("Imports:", import_list)
#     import_lists.append(import_list)
#     print()


# modified_list = list(set(item for sublist in import_lists for item in sublist if sublist))
# print(modified_list)
# if __name__ == "__main__":
#     det_import()

class youtube_download:
# Provide the YouTube video URL
    def url(self):
        return ["https://youtu.be/jM1lmadm9_Y?si=8o0IUegyWW-jaDrx",
                "https://youtu.be/ow6joumT6T4?si=0SOuZFHbFW_HpHNj",
                ]



    # Create a YouTube object
for item in youtube_download().url():
    yt = YouTube(item)

# Get the highest resolution video stream
    stream = yt.streams.get_highest_resolution()

# Download the video
    stream.download()

print("Video downloaded successfully!")


if __name__ == "__main__":
    youtube_download()