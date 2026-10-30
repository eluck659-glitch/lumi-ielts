# Lumi — Python LIVE app

Bu loyiha Lumi robotining LIVE ovozli suhbat prototipi. Backend Python Flask’da ishlaydi; brauzer mikrofoni va OpenAI Realtime API orqali jonli ovozli suhbat qiladi.

## 1) Kerak bo‘ladigan narsalar
- Python 3.10 yoki yangiroq
- OpenAI API key (Realtime API ishlatish huquqi va billing yoqilgan hisob)
- Chrome yoki Edge
- Mikrofon ruxsati va internet

## 2) Ishga tushirish — Windows
1. ZIP faylni oching (Extract All).
2. Ochilgan `Lumi_Python` papkasiga kiring.
3. Papkaning manzil satriga `cmd` yozib Enter bosing.
4. Quyidagilarni bittadan bajaring:

```bash
python -m venv .venv
.venv\\Scripts\\activate
pip install -r requirements.txt
copy .env.example .env
```

5. `.env` faylini Notepad’da oching va `OPENAI_API_KEY=...` qatoriga o‘z API kalitingizni yozing. Kalitni hech kimga yubormang.
6. Serverni ishga tushiring:

```bash
python app.py
```

7. Brauzerda `http://127.0.0.1:5000` manzilini oching.
8. `Start talking` tugmasini bosing va mikrofon ruxsatini bering.

## 3) Mac / Linux
Virtual muhitni `python3 -m venv .venv` bilan yarating, `source .venv/bin/activate` orqali yoqing. `.env.example` faylidan `.env` nusxa oling, API kalitini kiriting, `pip install -r requirements.txt`, so‘ng `python app.py` bajaring.

## Muhim
- Bu Python backend + HTML/CSS/JavaScript frontend’li web-ilova. Python serverni ishga tushiradi, ovozli interfeys esa brauzerda ko‘rinadi.
- OpenAI API kaliti va API xarajatlari ushbu loyihaga kiritilmagan.
- Asosiy API kaliti serverdagi `.env` faylida qoladi; brauzerga faqat qisqa muddatli sessiya kaliti beriladi.
- Robot og‘iz animatsiyasi soddalashtirilgan; mukammal fonema-lip-sync emas.
- Agar API kaliti bo‘lmasa yoki Realtime API hisobingizda yoqilmagan bo‘lsa, Lumi jonli gaplasha olmaydi.
