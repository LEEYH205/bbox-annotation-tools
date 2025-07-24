# 바운딩 박스 어노테이션 편집 도구

약품 이미지의 바운딩 박스 어노테이션을 편집하고 분석하는 GUI 도구입니다.

## 주요 기능

### 1. 바운딩 박스 편집기 (BBoxEditor)
- COCO 형식의 어노테이션 파일 편집
- 마우스 드래그로 바운딩 박스 그리기
- 기존 어노테이션과 비교 분석
- 약품별 그룹화된 어노테이션 관리

### 2. 약품 코드 뷰어 (DrugCodeViewer)
- 약품 코드별 이미지 및 어노테이션 조회
- 바운딩 박스 오버랩 분석
- 어노테이션 불일치 분석

## 설치 방법

### 1. Git에서 설치
```bash
git clone https://github.com/LEEYH205/bbox-annotation-tools.git
cd drug_obj_detection
pip install -e .
```

### 2. PyPI에서 설치 (배포 후)
```bash
pip install bbox-annotation-tools
```

## 사용 방법

### GUI 도구 실행
```bash
# 바운딩 박스 편집기
bbox-editor

# 약품 코드 뷰어
drug-viewer
```

### Python에서 사용
```python
from bbox_tools import BBoxEditor, DrugCodeViewer
import tkinter as tk

# 바운딩 박스 편집기
root = tk.Tk()
editor = BBoxEditor(root)
root.mainloop()

# 약품 코드 뷰어
root = tk.Tk()
viewer = DrugCodeViewer(root)
root.mainloop()
```

## 프로젝트 구조

```
drug_obj_detection/
├── bbox_tools/
│   ├── __init__.py
│   ├── bbox_gui_editor.py      # 바운딩 박스 편집기
│   ├── drug_code_viewer.py     # 약품 코드 뷰어
│   └── config.py               # 설정 관리
├── setup.py                    # 패키지 설정
├── README.md                   # 프로젝트 설명
├── requirements.txt            # 의존성 목록
├── .gitignore                  # Git 무시 파일
└── LICENSE                     # 라이선스
```

## 의존성

- Python 3.7+
- OpenCV (opencv-python)
- NumPy
- Matplotlib
- Pillow (PIL)
- tkinter (Python 기본 라이브러리)

## 라이선스

MIT License

## 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 연락처

- 이메일: ejrdkachry@gmail.com
- 프로젝트 링크: https://github.com/LEEYH205/bbox-annotation-tools 