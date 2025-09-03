# 🖼️ Image to PDF Landscape Converter

Công cụ chuyển đổi ảnh thành PDF với **bố cục khổ ngang (Landscape)**, hỗ trợ **2 ảnh trên mỗi trang**, căn chỉnh thông minh và dễ dàng cấu hình thông qua file `config.ini`.

## ✨ Tính năng

### 🔥 Tính năng chính
- ✅ **Chuyển đổi hàng loạt**: Quét toàn bộ ảnh trong thư mục `input` và các thư mục con
- 🖼️ **2 ảnh trên mỗi trang**: Bố cục tối ưu cho A4 ngang, ảnh trái + ảnh phải
- 🎯 **Căn lề tùy chỉnh (cm)**: Được định nghĩa trong file `config.ini`
- 📱 **Tự động xoay ảnh**: Dựa theo thông tin EXIF orientation
- ✂️ **Crop và resize thông minh**: Giữ tỉ lệ, tránh méo ảnh
- 🕒 **Tự động đặt tên**: File PDF được đặt tên theo ngày giờ (`landscape_pdf_YYYYMMDD_HHMMSS.pdf`)

### 🛠️ Tính năng nâng cao
- 📊 **Thông tin chi tiết**: Hiển thị số trang khi tạo PDF
- 🔢 **Đánh số trang tự động**: Chỉ hiển thị “Trang X”, không có ngày giờ, không có “/ tổng số”
- 🗂️ **Quản lý thư mục**: Tự động tạo `output/` và `logs/` nếu chưa có
- 📝 **Logging**: Ghi log chi tiết ra console và file
- 🔍 **Kiểm tra file**: Chỉ xử lý ảnh hợp lệ (PNG, JPG, JPEG, GIF, BMP, WEBP, TIFF, TIF)
- 🧹 **Dọn dẹp**: Tự động xóa file tạm sau khi xử lý

## 📁 Cấu trúc thư mục

```
imagetopdf_ngang/
├── 📄 README.md              # Hướng dẫn sử dụng
├── 📄 requirements.txt       # Danh sách thư viện cần thiết
├── 📄 main.py                # File chính để chạy
├── 📄 config.ini             # File cấu hình (cm)
├── 📄 .gitignore             # Cấu hình Git ignore
├── 📂 input/                 # Thư mục chứa ảnh đầu vào
│   ├── 🖼️ image1.jpg
│   ├── 🖼️ image2.png
│   └── 📂 subfolder/
│       └── 🖼️ image3.gif
├── 📂 output/                # Thư mục chứa PDF kết quả
└── 📂 logs/                  # Thư mục chứa log files
```

## 🚀 Cài đặt và sử dụng

### 1️⃣ Cài đặt các thư viện cần thiết
```bash
pip install -r requirements.txt
```

### 2️⃣ Chuẩn bị ảnh
- Đặt ảnh cần chuyển đổi vào thư mục `input/`
- Có thể sắp xếp vào thư mục con → chương trình sẽ tự động tìm tất cả ảnh

### 3️⃣ Cấu hình (tùy chọn)
Chỉnh file `config.ini` để thay đổi:
- Kích thước trang (`page_width`, `page_height`) – đơn vị cm
- Căn lề (`margin_left`, `margin_right`, `margin_top`, `margin_bottom`)
- Khoảng cách giữa 2 ảnh (`image_spacing`)
- Cài đặt số trang (bật/tắt, màu chữ, kích thước font)

### 4️⃣ Chạy chương trình
```bash
python main.py
```

### 5️⃣ Làm theo hướng dẫn
- Chương trình sẽ hiển thị danh sách ảnh tìm thấy trong `input/`
- Bạn xác nhận số bản PDF cần tạo
- File PDF sẽ được lưu trong thư mục `output/`

## 📋 Ví dụ sử dụng

### Ví dụ 1: Ảnh trong thư mục chính
```
input/
├── photo1.jpg
├── photo2.png
└── document.pdf  # Bị bỏ qua (không phải ảnh)
```

### Ví dụ 2: Ảnh trong thư mục con
```
input/
├── vacation/
│   ├── pic1.jpg
│   └── pic2.png
└── work/
    ├── slide1.jpg
    └── slide2.jpg
```

➡️ Kết quả: tất cả ảnh sẽ được gộp vào PDF khổ ngang, 2 ảnh trên mỗi trang.

## 🛠️ Yêu cầu hệ thống
- Python 3.9+
- Các thư viện trong `requirements.txt`

## 📌 Ghi chú
- Đơn vị trong `config.ini` mặc định là **cm**
- Chương trình hỗ trợ tối ưu cho khổ A4 ngang (29.7 x 21 cm)
- Có thể chỉnh lại để phù hợp với các khổ giấy khác

---
