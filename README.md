# QR Code Decoder

Цей простий Python-скрипт декодує QR-коди з зображення `.png` за допомогою бібліотеки `pyzbar` та `Pillow`.

## 📷 Приклад використання

Є зображення QR-коду `qr_code.png`, скрипт зчитує його, декодує та виводить вміст у консоль.

## 📁 Структура проєкту

```
qr-code-decoder/
├── main.py              # Основний скрипт для запуску декодування
├── qr_code.png          # Зображення з QR-кодом
├── requirements.txt     # Список залежностей
└── README.md            # Документація проєкту
```

## ▶️ Як запустити

### 1. Клонувати репозиторій

```bash
git clone https://github.com/hanashiko/qr-code-decoder.git
cd qr-code-decoder
```

### 2. Встановити залежності

Рекомендується використати віртуальне середовище:

```bash
python -m venv venv
source venv/bin/activate  # або venv\Scripts\activate на Windows
pip install -r requirements.txt
```

### 3. Запустити скрипт

```bash
python main.py
```

### ✅ Результат

У консоль буде виведений текст, що міститься в QR-коді на зображенні `qr_code.png`.

## 🛠 Залежності

Усі залежності вказані у файлі `requirements.txt`:

```
pyzbar
Pillow
```

## 📌 Примітка

- Зображення QR-коду має бути у форматі `.png`.
- Скрипт обробляє лише **перший** QR-код на зображенні.

## 📄 Ліцензія

Цей проєкт розповсюджується під ліцензією MIT.
