from ctypes import sizeof
import glob
import glob
from typing import List
from tkinter import filedialog
from PIL import Image

def get_images(target_path: str, is_recursive: bool) -> List[str]:
  """特定のディレクトリ以下の画像を取得する

  Args:
      target_path (str): 画像ディレクトリ
      is_recursive (bool): サブディレクトリを含めるか

  Returns:
      List[str]: 画像のパスリスト
  """
  return glob.glob(f"{target_path}/**/*.png", recursive=is_recursive)

def resize_images(images: List[str]):
  """複数の画像を特定の解像度に変更する

  Args:
      images (List[str]): リサイズする画像リスト
  """
  size: int = int(input("解像度を入力してください: "))
  index: int = 0
  for image in images:
    _image: Image = Image.open(image)
    _image = _image.resize((size, size))
    _image.save(image)
    index += 1
    print(f"\r[{index} / {len(images)}]", end="")

if __name__ == "__main__":
  
  target_path: str = ""
  is_recursive: bool = False
  while True:
    target_path = filedialog.askdirectory()
    recursive_command: str = input("サブディレクトリを含めますか（y/n）: ")
    command:str = input(f"画像のリサイズを実行しますか？（y/n） path: {target_path}: ")

    if command == "y":
      if recursive_command == "y":
        is_recursive = True
      break

  resize_images(get_images(target_path, is_recursive))