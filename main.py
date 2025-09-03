#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
main.py - Landscape PDF Generator
Tạo PDF khổ ngang với 2 ảnh mỗi trang, có đánh số trang và shuffle ngẫu nhiên
"""

import os
import sys
import random
import configparser
import math
from datetime import datetime
from pathlib import Path
from src.converters.image_to_pdf import convert_images_to_pdf
from src.io.file_handler import get_all_image_files, create_output_folder
from src.logging.logger_setup import setup_logger

def load_config():
    """Đọc cấu hình từ file config.ini"""
    config = configparser.ConfigParser()
    config_file = 'config.ini'
    
    if os.path.exists(config_file):
        config.read(config_file, encoding='utf-8')
        print("📝 Đã tải cấu hình từ config.ini")
    else:
        print("⚠️  Không tìm thấy config.ini, sử dụng cấu hình mặc định")
    
    return config

def display_banner():
    """Hiển thị banner chào mừng"""
    print("=" * 60)
    print(" 🖼️  LANDSCAPE PDF GENERATOR")
    print("=" * 60)
    print(" • Khổ giấy ngang (297x210mm)")
    print(" • 2 ảnh mỗi trang")
    print(" • Đánh số trang tự động")
    print(" • Tạo nhiều bản với thứ tự ngẫu nhiên")
    print("=" * 60)

def get_user_input():
    """Lấy thông tin từ người dùng"""
    try:
        copies = input("\nNhập số bản PDF cần tạo (1-20, mặc định 1): ").strip()
        if not copies:
            copies = 1
        else:
            copies = int(copies)
            if copies < 1 or copies > 20:
                print("Số bản phải từ 1-20, sử dụng mặc định: 1")
                copies = 1
        return copies
    except ValueError:
        print("Số không hợp lệ, sử dụng mặc định: 1")
        return 1

def main():
    """Hàm chính"""
    display_banner()
    
    # Đọc cấu hình
    config = load_config()
    
    # Khởi tạo logger
    log_level = config.get('LOGGING', 'log_level', fallback='INFO')
    log_to_file = config.getboolean('LOGGING', 'log_to_file', fallback=True)
    logger = setup_logger("LandscapePDF", log_level, log_to_file)
    
    # Đường dẫn thư mục từ config
    input_folder = config.get('PATHS', 'input_folder', fallback='input')
    output_folder = config.get('PATHS', 'output_folder', fallback='output')
    
    # Chuyển đổi thành đường dẫn tuyệt đối
    input_folder = os.path.join(os.getcwd(), input_folder)
    output_folder = os.path.join(os.getcwd(), output_folder)
    
    # Tạo thư mục nếu chưa tồn tại
    create_output_folder(output_folder)
    
    # Lấy tất cả file ảnh
    image_files = get_all_image_files(input_folder)
    
    if not image_files:
        logger.error("❌ Không tìm thấy file ảnh nào trong thư mục input!")
        print("\n💡 Hướng dẫn:")
        print("1. Tạo thư mục 'input' nếu chưa có")
        print("2. Đặt file ảnh vào thư mục 'input'")
        print("3. Chạy lại chương trình")
        return False
    
    print(f"\n📁 Tìm thấy {len(image_files)} ảnh:")
    for i, (full_path, rel_path) in enumerate(image_files, 1):
        print(f"   {i:2d}. {rel_path}")
    
    # Lấy số bản cần tạo
    num_copies = get_user_input()
    
    # Tính toán số trang (2 ảnh/trang)
    images_per_page = 2
    total_pages = math.ceil(len(image_files) / images_per_page)
    
    print(f"\n📊 Thông tin:")
    print(f"   • {len(image_files)} ảnh → {total_pages} trang")
    print(f"   • {images_per_page} ảnh/trang (khổ ngang)")
    print(f"   • {num_copies} bản PDF")
    
    # Xác nhận
    confirm = input(f"\n❓ Tạo {num_copies} bản PDF? (y/N): ").strip().lower()
    if confirm not in ['y', 'yes']:
        print("❌ Hủy bỏ.")
        return False
    
    # Tạo PDF
    success_count = 0
    print(f"\n🔄 Bắt đầu tạo {num_copies} bản PDF...")
    
    for copy_num in range(1, num_copies + 1):
        print(f"\n📄 Đang tạo bản {copy_num}/{num_copies}...")
        
        # Shuffle ảnh cho mỗi bản (trừ bản đầu)
        if copy_num > 1:
            shuffled_images = image_files.copy()
            random.shuffle(shuffled_images)
        else:
            shuffled_images = image_files
        
        # Tạo tên file output
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        if num_copies == 1:
            output_filename = f"landscape_pdf_{timestamp}.pdf"
        else:
            output_filename = f"landscape_pdf_{timestamp}_copy{copy_num:02d}.pdf"
        
        output_path = os.path.join(output_folder, output_filename)
        
        # Tạo PDF với cấu hình landscape
        success = convert_images_to_pdf(shuffled_images, output_path, logger, config)
        
        if success:
            success_count += 1
            print(f"   ✅ Hoàn thành: {output_filename}")
        else:
            print(f"   ❌ Thất bại: {output_filename}")
    
    # Kết quả
    print(f"\n{'='*50}")
    print(f"🎉 KẾT QUẢ: {success_count}/{num_copies} bản PDF tạo thành công!")
    
    if success_count > 0:
        print(f"📁 Thư mục output: {output_folder}")
        
        # Mở thư mục output
        open_folder = input("\n🗂️  Mở thư mục output? (y/N): ").strip().lower()
        if open_folder in ['y', 'yes']:
            import subprocess
            import platform
            try:
                if platform.system() == "Windows":
                    os.startfile(output_folder)
                elif platform.system() == "Darwin":  # macOS
                    subprocess.run(["open", output_folder])
                else:  # Linux
                    subprocess.run(["xdg-open", output_folder])
            except Exception as e:
                logger.warning(f"Không thể mở thư mục: {e}")
    
    return success_count > 0

if __name__ == "__main__":
    try:
        success = main()
        sys.exit(0 if success else 1)
    except KeyboardInterrupt:
        print("\n\n❌ Đã hủy bởi người dùng.")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Lỗi không mong muốn: {e}")
        sys.exit(1)