"""_summary_

    Returns:
        _type_: _description_

        # Example usage for an image in the 'images' folder:
        image_path = resource_path("images", "image.png")
"""
import os
import sys

def resource_path(relative_path, file_name) -> str:
    """ Get absolute path to resource, works for development and PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(os.path.join(base_path, relative_path), file_name)
