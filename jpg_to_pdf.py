#!/usr/bin/env python3
"""
Быстрый конвертор JPG изображений в единый PDF файл
Использование: python jpg_to_pdf.py image1.jpg image2.jpg ... -o output.pdf
"""

import argparse
import sys
from pathlib import Path
from PIL import Image


def convert_jpg_to_pdf(image_paths, output_path):
    """Конвертирует список JPG изображений в единый PDF файл"""
    if not image_paths:
        print("Ошибка: не указаны файлы изображений")
        return False
    
    images = []
    
    try:
        # Загружаем все изображения
        for img_path in image_paths:
            path = Path(img_path)
            if not path.exists():
                print(f"Ошибка: файл {img_path} не найден")
                return False
            
            if not path.suffix.lower() in ['.jpg', '.jpeg']:
                print(f"Предупреждение: {img_path} не является JPG файлом, пропускаем")
                continue
            
            img = Image.open(path)
            # Конвертируем в RGB если необходимо
            if img.mode != 'RGB':
                img = img.convert('RGB')
            images.append(img)
            print(f"Загружено: {img_path}")
        
        if not images:
            print("Ошибка: не найдено подходящих изображений")
            return False
        
        # Сохраняем в PDF
        output_path = Path(output_path)
        images[0].save(
            output_path,
            format='PDF',
            save_all=True,
            append_images=images[1:] if len(images) > 1 else []
        )
        
        print(f"PDF файл создан: {output_path}")
        print(f"Страниц в PDF: {len(images)}")
        return True
        
    except Exception as e:
        print(f"Ошибка при конвертации: {e}")
        return False


def main():
    parser = argparse.ArgumentParser(
        description="Конвертор JPG изображений в единый PDF файл",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Примеры использования:
  python jpg_to_pdf.py image1.jpg image2.jpg -o document.pdf
  python jpg_to_pdf.py *.jpg -o album.pdf
  python jpg_to_pdf.py photo1.jpg photo2.jpg photo3.jpg
        """
    )
    
    parser.add_argument(
        'images',
        nargs='+',
        help='JPG файлы для конвертации'
    )
    
    parser.add_argument(
        '-o', '--output',
        default='output.pdf',
        help='Имя выходного PDF файла (по умолчанию: output.pdf)'
    )
    
    args = parser.parse_args()
    
    print("Начинаем конвертацию")
    success = convert_jpg_to_pdf(args.images, args.output)
    
    if success:
        print("Конвертация завершена успешно!")
        sys.exit(0)
    else:
        print("Конвертация завершилась с ошибкой")
        sys.exit(1)


if __name__ == "__main__":
    main()