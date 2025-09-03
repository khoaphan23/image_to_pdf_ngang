import os
from typing import List, Tuple

def get_all_image_files(folder_path: str) -> List[Tuple[str, str]]:
    """
    Lấy tất cả file ảnh từ thư mục và các thư mục con
    
    Args:
        folder_path: Đường dẫn thư mục gốc
    
    Returns:
        List of tuples: (full_path, relative_path)
    """
    if not os.path.exists(folder_path):
        print(f"⚠️  Thư mục '{folder_path}' không tồn tại!")
        return []
    
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff', '.tif'}
    image_files = []
    
    # Duyệt qua tất cả file và thư mục con
    for root, dirs, files in os.walk(folder_path):
        # Sắp xếp thư mục và file để đảm bảo thứ tự nhất quán
        dirs.sort()
        files.sort()
        
        for file in files:
            file_ext = os.path.splitext(file)[1].lower()
            if file_ext in image_extensions:
                full_path = os.path.join(root, file)
                # Tạo đường dẫn tương đối từ thư mục gốc
                relative_path = os.path.relpath(full_path, folder_path)
                image_files.append((full_path, relative_path))
    
    return image_files

def get_image_files_from_folder(folder_path: str) -> List[str]:
    """
    Lấy danh sách file ảnh từ một thư mục cụ thể (không bao gồm thư mục con)
    
    Args:
        folder_path: Đường dẫn thư mục
    
    Returns:
        List of filenames
    """
    if not os.path.exists(folder_path):
        return []
    
    image_extensions = {'.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp', '.tiff', '.tif'}
    return [f for f in os.listdir(folder_path) 
            if os.path.splitext(f)[1].lower() in image_extensions]

def sort_files_naturally(files: List[str]) -> List[str]:
    """
    Sắp xếp file theo thứ tự tự nhiên (1, 2, 10 thay vì 1, 10, 2)
    """
    import re
    
    def natural_key(text):
        return [int(c) if c.isdigit() else c.lower() for c in re.split(r'(\d+)', text)]
    
    return sorted(files, key=natural_key)

def create_output_folder(output_path: str) -> bool:
    """
    Tạo thư mục output nếu chưa tồn tại
    
    Args:
        output_path: Đường dẫn thư mục output
    
    Returns:
        bool: True nếu thành công hoặc đã tồn tại
    """
    try:
        if not os.path.exists(output_path):
            os.makedirs(output_path)
            print(f"📁 Đã tạo thư mục output: {output_path}")
        return True
    except Exception as e:
        print(f"❌ Không thể tạo thư mục output: {e}")
        return False

def get_file_info(file_path: str) -> dict:
    """
    Lấy thông tin chi tiết của file
    
    Args:
        file_path: Đường dẫn file
    
    Returns:
        dict: Thông tin file
    """
    if not os.path.exists(file_path):
        return {}
    
    stat = os.stat(file_path)
    return {
        'name': os.path.basename(file_path),
        'size': stat.st_size,
        'size_mb': round(stat.st_size / (1024 * 1024), 2),
        'modified': stat.st_mtime,
        'extension': os.path.splitext(file_path)[1].lower()
    }

def validate_image_file(file_path: str) -> Tuple[bool, str]:
    """
    Kiểm tra tính hợp lệ của file ảnh
    
    Args:
        file_path: Đường dẫn file
    
    Returns:
        Tuple[bool, str]: (is_valid, error_message)
    """
    try:
        if not os.path.exists(file_path):
            return False, "File không tồn tại"
        
        if os.path.getsize(file_path) == 0:
            return False, "File rỗng"
        
        # Thử mở file bằng PIL
        from PIL import Image
        with Image.open(file_path) as img:
            img.verify()  # Kiểm tra tính toàn vẹn
        
        return True, ""
        
    except Exception as e:
        return False, f"File không hợp lệ: {str(e)}"

def clean_temp_files(directory: str = ".") -> int:
    """
    Xóa các file tạm thời
    
    Args:
        directory: Thư mục cần dọn dẹp
    
    Returns:
        int: Số file đã xóa
    """
    temp_patterns = ['temp_landscape_*.jpg', 'temp_image_*.jpg', '*.tmp', '*~']
    deleted_count = 0
    
    try:
        for pattern in temp_patterns:
            import glob
            for file_path in glob.glob(os.path.join(directory, pattern)):
                try:
                    os.remove(file_path)
                    deleted_count += 1
                except:
                    pass
    except:
        pass
    
    return deleted_count