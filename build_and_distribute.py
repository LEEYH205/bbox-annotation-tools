#!/usr/bin/env python3
"""
패키지 빌드 및 배포 스크립트
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """명령어 실행"""
    print(f"\n🔄 {description}...")
    print(f"실행 명령어: {command}")
    
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} 완료")
        if result.stdout:
            print(f"출력: {result.stdout}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} 실패")
        print(f"오류: {e.stderr}")
        return False

def clean_build():
    """빌드 파일 정리"""
    print("\n🧹 빌드 파일 정리 중...")
    
    dirs_to_clean = ['build', 'dist', '*.egg-info']
    for pattern in dirs_to_clean:
        for path in Path('.').glob(pattern):
            if path.is_dir():
                shutil.rmtree(path)
                print(f"삭제됨: {path}")
            elif path.is_file():
                path.unlink()
                print(f"삭제됨: {path}")

def build_package():
    """패키지 빌드"""
    return run_command("python -m build", "패키지 빌드")

def check_package():
    """패키지 검사"""
    return run_command("twine check dist/*", "패키지 검사")

def upload_to_testpypi():
    """TestPyPI에 업로드"""
    return run_command("twine upload --repository testpypi dist/*", "TestPyPI 업로드")

def upload_to_pypi():
    """PyPI에 업로드"""
    return run_command("twine upload dist/*", "PyPI 업로드")

def main():
    """메인 함수"""
    print("🚀 바운딩 박스 어노테이션 도구 패키지 빌드 및 배포")
    print("=" * 60)
    
    # 1. 빌드 파일 정리
    clean_build()
    
    # 2. 패키지 빌드
    if not build_package():
        print("❌ 빌드 실패로 인해 배포를 중단합니다.")
        sys.exit(1)
    
    # 3. 패키지 검사
    if not check_package():
        print("❌ 패키지 검사 실패로 인해 배포를 중단합니다.")
        sys.exit(1)
    
    # 4. 배포 옵션 선택
    print("\n📦 배포 옵션을 선택하세요:")
    print("1. TestPyPI에 업로드 (테스트용)")
    print("2. PyPI에 업로드 (실제 배포)")
    print("3. 빌드만 완료 (업로드 안함)")
    
    choice = input("\n선택 (1-3): ").strip()
    
    if choice == "1":
        if upload_to_testpypi():
            print("\n🎉 TestPyPI 업로드 완료!")
            print("설치 명령어: pip install --index-url https://test.pypi.org/simple/ bbox-annotation-tools")
        else:
            print("❌ TestPyPI 업로드 실패")
            sys.exit(1)
    
    elif choice == "2":
        print("\n⚠️  실제 PyPI에 업로드합니다. 계속하시겠습니까? (y/N): ", end="")
        confirm = input().strip().lower()
        if confirm == 'y':
            if upload_to_pypi():
                print("\n🎉 PyPI 업로드 완료!")
                print("설치 명령어: pip install bbox-annotation-tools")
            else:
                print("❌ PyPI 업로드 실패")
                sys.exit(1)
        else:
            print("❌ 업로드가 취소되었습니다.")
    
    elif choice == "3":
        print("\n✅ 빌드 완료! dist/ 폴더에 패키지 파일들이 생성되었습니다.")
    
    else:
        print("❌ 잘못된 선택입니다.")
        sys.exit(1)

if __name__ == "__main__":
    main() 