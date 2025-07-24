"""
패키지 임포트 테스트
"""

import unittest

class TestImports(unittest.TestCase):
    """임포트 테스트 클래스"""
    
    def test_bbox_tools_import(self):
        """bbox_tools 패키지 임포트 테스트"""
        try:
            import bbox_tools
            self.assertTrue(True, "bbox_tools 패키지 임포트 성공")
        except ImportError as e:
            self.fail(f"bbox_tools 패키지 임포트 실패: {e}")
    
    def test_classes_import(self):
        """주요 클래스들 임포트 테스트"""
        try:
            from bbox_tools import BBoxEditor, DrugCodeViewer
            self.assertTrue(True, "주요 클래스들 임포트 성공")
        except ImportError as e:
            self.fail(f"주요 클래스들 임포트 실패: {e}")
    
    def test_config_import(self):
        """설정 모듈 임포트 테스트"""
        try:
            from bbox_tools import config
            self.assertTrue(True, "config 모듈 임포트 성공")
        except ImportError as e:
            self.fail(f"config 모듈 임포트 실패: {e}")
    
    def test_package_version(self):
        """패키지 버전 테스트"""
        try:
            import bbox_tools
            self.assertIsNotNone(bbox_tools.__version__, "버전 정보가 있어야 함")
        except AttributeError:
            self.fail("버전 정보가 없음")

if __name__ == '__main__':
    unittest.main() 