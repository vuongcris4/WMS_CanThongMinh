


**Hệ thống cân thông minh sử dụng trong quản lý kho** cho doanh nghiệp sản xuất, hỗ trợ nhập – xuất – tồn vật tư nhỏ dựa trên khối lượng, mã QR, và bảng quy đổi đơn vị.
## 🔧 Tính năng nổi bật

- Nhận dạng vật tư bằng mã QR (ESP32-CAM).
- Tự động quy đổi khối lượng sang số lượng theo định mức.
- Cập nhật tồn kho khi nhấn nút Nhập/Xuất.
- Quản lý danh sách vật tư, đơn vị, định mức và lịch sử giao dịch.
- Giao diện web hiện đại, responsive (Django + HTMX + DaisyUI).

[//]: # (## 📁 Video demo)



---
## 🚀 Cài đặt & chạy dự án

### 1. Clone project

```bash
git clone git@github.com:vuongcris4/WMS_CanThongMinh.git
cd can_thong_minh
````

### 2. Tạo và kích hoạt môi trường ảo

```bash
python -m venv venv
source venv/bin/activate      # (Linux/macOS)
venv\Scripts\activate         # (Windows)
```

### 3. Cài thư viện phụ thuộc

```bash
pip install -r requirements.txt
```

### 4. Chạy server

```bash
python manage.py runserver
```

Sau đó truy cập:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/) để sử dụng hệ thống.

## 🖼 Giao diện demo

> 📌 Sau khi up hình ảnh vào thư mục `demo_images/`, bạn có thể thay đường dẫn tương ứng:

### 🌐 Trang quản lý nguyên vật liệu

![Quản lý nguyên vật liệu](demo_images/material_list.png)

### 🌐 Thêm đơn vị, thêm nguyên vật liệu

![Thêm thông tin](demo_images/don_vi_nvl.png)


### 🔁 Quy đổi đơn vị tính cho vật tư

![Quy đổi đơn vị](demo_images/unit_conversion.png)

### 📥 Giao diện nhập - xuất - tồn kho

![Nhập kho](demo_images/nhap_xuat_ton.png)

### 📊 Tìm kiếm lịch sử nhập – xuất

![Lịch sử nhập xuất](demo_images/history_table.png)


### ⚙️ Ảnh phần cứng ESP32 + STM32 + LCD

![Phần cứng hệ thống](demo_images/hardware.jpeg)

---



## 📬 Liên hệ

📧 Email: [tranduyvuong100@gmail.com](mailto:tranduyvuong100@gmail.com)
