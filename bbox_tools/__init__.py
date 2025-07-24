"""
바운딩 박스 어노테이션 편집 및 분석 도구

이 패키지는 COCO 형식의 어노테이션 파일을 편집하고 분석하는 도구들을 제공합니다.
"""

__version__ = "1.0.0"
__author__ = "LEEYH205"
__email__ = "ejrdkachry@gmail.com"

from .bbox_gui_editor import BBoxEditor
from .drug_code_viewer import DrugCodeViewer

__all__ = [
    "BBoxEditor",
    "DrugCodeViewer",
] 