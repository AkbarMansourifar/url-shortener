# URL Shortener

یک سرویس ساده ساخته‌شده با Django و Django REST Framework برای ساخت لینک‌های کوتاه با لاگین و پیگیری هوشمند بازدیدها.

---

## 🚀 امکانات اصلی

- ثبت‌نام و لاگین کاربر با JWT 
- کاربران احراز هویت‌شده می‌توانند:
  - لینک بلند را کوتاه کنند
  - وضعیت لینک (فعال یا غیرفعال) را مدیریت کنند
  - گزارش بازدید شامل زمان، IP، مرورگر و نوع دستگاه (موبایل/دسکتاپ) را مشاهده کنند
- پنل مدیریت (admin panel) برای مدیریت کاربران و لینک‌ها 

---

##  تکنولوژی‌های استفاده‌شده

- Python3
- Django 
- Django REST Framework 
- djangorestframework-simplejwt 
- SQLite به‌صورت پیش‌فرض (قابل تغییر به PostgreSQL یا MySQL)

---

##  راه‌اندازی پروژه (Local Development)

```bash
git clone https://github.com/AkbarMansourifar/url-shortener.git
cd url-shortener
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser  # برای ساخت ادمین
python manage.py runserver
```

---

##  احراز هویت و API

برای دریافت توکن وارد شوید:

```
POST /api/token/
```

درخواست:
```json
{
  "username": "your_username",
  "password": "your_password"
}
```

پاسخ:
```json
{
  "access": "<access_token>",
  "refresh": "<refresh_token>"
}
```

در درخواست‌های بعدی هِدر `Authorization` را اضافه کنید:

```
Authorization: Bearer <access_token>
```

---

##  API Endpoints

| متد   | مسیر              | توضیحات                            |
|--------|-------------------|------------------------------------|
| POST   | `/api/register/`  | ثبت‌نام کاربر جدید                |
| POST   | `/api/token/`     | دریافت توکن JWT                    |
| POST   | `/api/shorten/`   | ایجاد کوتاه‌کننده لینک (نیاز به token) |
| GET    | `/api/urls/`      | مشاهده لینک‌های ساخته‌شده توسط کاربر |

---

##  ساختار پروژه

```
core/
├── models.py         # مدل‌های URL و Visit
├── serializers.py    # Serializerهای ثبت‌نام و URL
├── views/            # ویوهای مربوط به API
└── urls.py           # مسیرهای URL routing
```

---

##  نکات مهم

- توکن JWT طول عمر دارد و بعد یک روز منقضی می‌شود (قابل تنظیم در `settings.py`)
- برای تولید `short_url` تصادفی، از `random.choices(...)` استفاده شده
- اطلاعات بازدیدکننده در هر بازدید ذخیره می‌شود (تابع `Visit` در مدل‌ها)

---



##  License & Author

This project is open-source under the MIT License. 
تهیه‌شده توسط **Akbar Mansourifar** 
[GitHub Profile](https://github.com/AkbarMansourifar)
