"""
Landscape PDF Generator Package
Tạo PDF khổ ngang với 2 ảnh mỗi trang và xáo trộn thứ tự
"""

__version__ = "1.0.0"
__author__ = "Landscape PDF Generator"
__description__ = "Tạo PDF khổ ngang với layout 2 ảnh/trang và shuffle ngẫu nhiên"

# Import các module chính
from src.converters.image_to_pdf import convert_images_to_pdf
from src.io.file_handler import get_all_image_files, create_output_folder
from src.logging.logger_setup import setup_logger

__all__ = [
    'convert_images_to_pdf',
    'get_all_image_files', 
    'create_output_folder',
    'setup_logger'
]