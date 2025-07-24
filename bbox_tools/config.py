"""
설정 관리 모듈
"""

import os
import json
from pathlib import Path
from typing import Optional, Dict, Any

class Config:
    """설정 관리 클래스"""
    
    def __init__(self, config_file: Optional[str] = None):
        self.config_file = config_file or os.path.expanduser("~/.bbox_tools_config.json")
        self.config = self.load_config()
    
    def load_config(self) -> Dict[str, Any]:
        """설정 파일 로드"""
        if os.path.exists(self.config_file):
            try:
                with open(self.config_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except Exception as e:
                print(f"설정 파일 로드 오류: {e}")
                return self.get_default_config()
        else:
            return self.get_default_config()
    
    def save_config(self):
        """설정 파일 저장"""
        try:
            os.makedirs(os.path.dirname(self.config_file), exist_ok=True)
            with open(self.config_file, 'w', encoding='utf-8') as f:
                json.dump(self.config, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"설정 파일 저장 오류: {e}")
    
    def get_default_config(self) -> Dict[str, Any]:
        """기본 설정 반환"""
        return {
            "annotations_path": "",
            "images_path": "",
            "last_used_folder": "",
            "last_used_drug_code": "",
            "window_geometry": "1800x1100",
            "show_existing_annotations": True,
            "scale_factor": 1.0,
            "bbox_color": "red",
            "existing_bbox_color": "blue",
            "temp_bbox_color": "blue",
            "font_family": "Arial",
            "font_size": 12,
        }
    
    def get(self, key: str, default: Any = None) -> Any:
        """설정 값 가져오기"""
        return self.config.get(key, default)
    
    def set(self, key: str, value: Any):
        """설정 값 설정"""
        self.config[key] = value
        self.save_config()
    
    def validate_paths(self) -> Dict[str, bool]:
        """경로 유효성 검사"""
        results = {}
        
        # 어노테이션 경로 검사
        annotations_path = self.get("annotations_path", "")
        results["annotations_path"] = os.path.exists(annotations_path) if annotations_path else False
        
        # 이미지 경로 검사
        images_path = self.get("images_path", "")
        results["images_path"] = os.path.exists(images_path) if images_path else False
        
        return results
    
    def prompt_for_paths(self) -> bool:
        """사용자로부터 경로 입력받기"""
        print("=== 경로 설정 ===")
        
        # 어노테이션 경로 입력
        current_annotations = self.get("annotations_path", "")
        if current_annotations:
            print(f"현재 어노테이션 경로: {current_annotations}")
        
        annotations_path = input("어노테이션 폴더 경로를 입력하세요 (Enter로 현재 경로 유지): ").strip()
        if not annotations_path:
            annotations_path = current_annotations
        
        if annotations_path and not os.path.exists(annotations_path):
            print(f"⚠️  경고: 경로가 존재하지 않습니다: {annotations_path}")
            if input("계속 진행하시겠습니까? (y/n): ").lower() != 'y':
                return False
        
        # 이미지 경로 입력
        current_images = self.get("images_path", "")
        if current_images:
            print(f"현재 이미지 경로: {current_images}")
        
        images_path = input("이미지 폴더 경로를 입력하세요 (Enter로 현재 경로 유지): ").strip()
        if not images_path:
            images_path = current_images
        
        if images_path and not os.path.exists(images_path):
            print(f"⚠️  경고: 경로가 존재하지 않습니다: {images_path}")
            if input("계속 진행하시겠습니까? (y/n): ").lower() != 'y':
                return False
        
        # 설정 저장
        self.set("annotations_path", annotations_path)
        self.set("images_path", images_path)
        
        print("✅ 경로 설정이 완료되었습니다.")
        return True

# 전역 설정 인스턴스
config = Config() 