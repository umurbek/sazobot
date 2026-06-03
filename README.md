<h1 align="center">🎵 SazoBot — YouTube Music Downloader</h1>

<p align="center">
  <img src="https://img.shields.io/badge/version-1.0.0-blue.svg?style=for-the-badge" alt="Version">
  <img src="https://img.shields.io/badge/Aiogram-3.x-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white" alt="Aiogram">
  <img src="https://img.shields.io/badge/status-active-brightgreen.svg?style=for-the-badge" alt="Status">
</p>

<p align="center">
  <a href="#english">English</a> •
  <a href="#русский">Русский</a> •
  <a href="#o'zbekcha">O'zbekcha</a>
</p>

---

<a id="english"></a>
## 🌐 English Version

### 📖 About the Project
**SazoBot** is a high-performance Telegram bot built with **Aiogram 3** for searching and downloading music directly from YouTube. It offers seamless user experience with fast downloads (M4A) and high-quality audio extraction (MP3), backed by an intelligent job queue system.

### 🚀 Key Features
- **🔍 Fast YouTube Search:** Instant search results utilizing a caching mechanism.
- **⚡ M4A & 🎧 MP3 Modes:** Option to download lightning-fast M4A or high-quality MP3 files.
- **🧵 Download Job Queue:** Asynchronous processing (1 user = 1 active job) to prevent blocking.
- **⏱ Performance Logging:** Precise execution time tracking (in milliseconds).
- **🧹 Auto Cleanup:** Cron-like background tasks to delete temporary media files.
- **📄 Pagination & Controls:** Smooth navigation through search results using inline buttons.

### 🛠️ Tech Stack
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Telegram](https://img.shields.io/badge/Aiogram_3-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white) ![YouTube](https://img.shields.io/badge/yt--dlp-%23FF0000.svg?style=for-the-badge&logo=YouTube&logoColor=white) ![Asyncio](https://img.shields.io/badge/asyncio-black?style=for-the-badge)

---

<a id="русский"></a>
## 🇷🇺 Русская Версия

### 📖 О проекте
**SazoBot** — это высокопроизводительный Telegram-бот на базе **Aiogram 3** для поиска и скачивания музыки с YouTube. Бот обеспечивает быструю загрузку (M4A) и качественную конвертацию (MP3), используя асинхронную очередь задач.

### 🚀 Основные возможности
- **🔍 Быстрый поиск:** Мгновенные результаты поиска на YouTube с кэшированием.
- **⚡ Форматы M4A и MP3:** Выбор между быстрой загрузкой M4A или качественным MP3.
- **🧵 Очередь скачиваний:** Асинхронная обработка (1 пользователь = 1 задача).
- **⏱ Логирование производительности:** Точный контроль времени выполнения (в мс).
- **🧹 Автоочистка:** Фоновые задачи для удаления временных файлов.
- **📄 Пагинация:** Удобная навигация по результатам через inline-кнопки.

---

<a id="o'zbekcha"></a>
## 🇺🇿 O'zbekcha Versiyasi

### 📖 Loyiha haqida
**SazoBot** — bu **Aiogram 3** yordamida yaratilgan, YouTube'dan musiqalarni qidirish va yuklab olish imkonini beruvchi yuqori tezlikdagi Telegram bot. Tizim asinxron navbat (queue) asosida ishlaydi, bu esa foydalanuvchilarga M4A va MP3 formatlarida musiqalarni qotishlarsiz yuklab olish imkonini beradi.

### 🚀 Asosiy Imkoniyatlar
- **🔍 Tezkor qidiruv:** Kesh (cache) orqali YouTube'dan ma'lumotlarni tezkor izlash.
- **⚡ M4A & 🎧 MP3 rejimi:** Yuqori tezlikdagi M4A yoki sifatli MP3 formatni tanlash.
- **🧵 Yuklab olish navbati:** Bot qotib qolmasligi uchun asinxron navbat tizimi (1 foydalanuvchi = 1 jarayon).
- **⏱ Performansni loglash:** Har bir jarayonning ishlash vaqtini millisekundlarda o'lchash.
- **🧹 Avto-tozalash:** Vaqtinchalik fayllarni fonda avtomatik o'chirib borish.
- **📄 Paginatsiya:** Inline tugmalar yordamida qidiruv natijalari bo'ylab qulay harakatlanish.

---

## 🧱 Project Structure / Loyiha Strukturasi

```text
sazobot/
├── bot.py                # Main bot entry point
├── config.py             # Environment variables and configuration
├── handlers/             # Telegram message and callback handlers
│   ├── search.py         # YouTube search handlers
│   └── download.py       # Download and queue management
├── keyboards/            # Inline pagination and reply keyboards
├── services/             # Core logic (yt-dlp integration, caching)
├── utils/                # Helpers, loggers, and auto-cleanup tasks
├── .env.example          # Example environment variables
└── requirements.txt      # Python dependencies.
