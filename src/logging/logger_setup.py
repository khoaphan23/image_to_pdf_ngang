import logging
import os
from datetime import datetime

def setup_logger(name: str, level: str = "INFO", log_to_file: bool = True) -> logging.Logger:
    """
    Thiết lập logger với cấu hình nâng cao
    
    Args:
        name: Tên logger
        level: Mức độ log (DEBUG, INFO, WARNING, ERROR)
        log_to_file: Có ghi log vào file không
    
    Returns:
        logging.Logger: Logger object
    """
    logger = logging.getLogger(name)
    
    # Tránh tạo handler trùng lặp
    if logger.handlers:
        return logger
    
    # Thiết lập level
    numeric_level = getattr(logging, level.upper(), logging.INFO)
    logger.setLevel(numeric_level)
    
    # Formatter cho log
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Console handler (luôn có)
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)
    console_handler.setLevel(numeric_level)
    logger.addHandler(console_handler)
    
    # File handler (nếu được yêu cầu)
    if log_to_file:
        try:
            # Tạo thư mục logs nếu chưa có
            log_dir = "logs"
            if not os.path.exists(log_dir):
                os.makedirs(log_dir)
            
            # Tên file log theo ngày
            log_filename = f"{name}_{datetime.now().strftime('%Y%m%d')}.log"
            log_filepath = os.path.join(log_dir, log_filename)
            
            # File handler
            file_handler = logging.FileHandler(log_filepath, encoding='utf-8')
            file_handler.setFormatter(formatter)
            file_handler.setLevel(numeric_level)
            logger.addHandler(file_handler)
            
        except Exception as e:
            logger.warning(f"Không thể tạo log file: {e}")
    
    return logger

def create_progress_logger(name: str) -> logging.Logger:
    """
    Tạo logger đặc biệt cho việc hiển thị tiến trình
    """
    logger = logging.getLogger(f"{name}_progress")
    
    if logger.handlers:
        return logger
    
    logger.setLevel(logging.INFO)
    
    # Custom formatter cho progress
    class ProgressFormatter(logging.Formatter):
        def format(self, record):
            if record.levelname == 'INFO':
                return f"⏳ {record.getMessage()}"