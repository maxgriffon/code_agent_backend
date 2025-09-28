from pathlib import Path
import re
from typing import Optional
from constants.constants import ALLOWED_EXTENSIONS


def sanitize_filename(filename: str) -> str:
    """Sanitize filename to prevent path traversal and invalid characters"""
    filename = filename.replace('..', '').replace('/', '_').replace('\\', '_')
    
    filename = re.sub(r'[<>:"|?*]', '_', filename)
    
    filename = filename.strip(' .')
    
    if not filename:
        filename = "untitled"
    
    return filename

def get_file_extension(language: str, filename: Optional[str] = None) -> str:
    """Get appropriate file extension based on language or filename"""
    
    if filename and '.' in filename:
        return Path(filename).suffix
    
    language_lower = language.lower()
    return ALLOWED_EXTENSIONS.get(language_lower, '.txt')