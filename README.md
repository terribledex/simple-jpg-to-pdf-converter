# Быстрый конвертор JPG → PDF

Простая утилита для конвертации JPG изображений в единый PDF файл.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

### Базовое использование
```bash
python jpg_to_pdf.py image1.jpg image2.jpg image3.jpg
```
Создаст файл `output.pdf` с указанными изображениями.

### С указанием имени выходного файла
```bash
python jpg_to_pdf.py image1.jpg image2.jpg -o my_document.pdf
```

### Конвертация всех JPG в папке
```bash
python jpg_to_pdf.py *.jpg -o album.pdf
```

## Особенности

- ✅ Поддерживает файлы .jpg и .jpeg
- ✅ Автоматически конвертирует в RGB формат
- ✅ Показывает прогресс загрузки
- ✅ Обрабатывает ошибки
- ✅ Простой интерфейс командной строки

## Требования

- Python 3.6+
- Pillow (PIL)