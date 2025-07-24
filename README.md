# Bounding Box Annotation Editing Tools

A GUI tool for editing and analyzing bounding box annotations of drug images.

## Main Features

### 1. Bounding Box Editor (BBoxEditor)
- Edit COCO format annotation files
- Draw bounding boxes with mouse drag
- Compare and analyze existing annotations
- Manage annotations grouped by drug codes

### 2. Drug Code Viewer (DrugCodeViewer)
- View images and annotations by drug codes
- Analyze bounding box overlaps
- Analyze annotation mismatches

## Installation

### 1. Install from Git
```bash
git clone https://github.com/LEEYH205/bbox-annotation-tools.git
cd drug_obj_detection
pip install -e .
```

### 2. Install from PyPI (after release)
```bash
pip install bbox-annotation-tools
```

## Usage

### Run GUI Tools
```bash
# Bounding Box Editor
bbox-editor

# Drug Code Viewer
drug-viewer
```

### Use in Python
```python
from bbox_tools import BBoxEditor, DrugCodeViewer
import tkinter as tk

# Bounding Box Editor
root = tk.Tk()
editor = BBoxEditor(root)
root.mainloop()

# Drug Code Viewer
root = tk.Tk()
viewer = DrugCodeViewer(root)
root.mainloop()
```

## Project Structure

```
drug_obj_detection/
├── bbox_tools/                    # Main package
│   ├── __init__.py               # Package initialization
│   ├── bbox_gui_editor.py        # Bounding box editor
│   ├── drug_code_viewer.py       # Drug code viewer
│   └── config.py                 # Configuration management
├── tests/                        # Test files
│   ├── __init__.py
│   └── test_imports.py
├── .github/workflows/            # GitHub Actions
│   └── build-and-test.yml
├── setup.py                      # Package configuration
├── pyproject.toml                # Modern package configuration
├── requirements.txt              # Dependencies
├── README.md                     # Project description
├── LICENSE                       # MIT License
├── .gitignore                    # Git ignore file
├── MANIFEST.in                   # Package include file
├── build_and_distribute.py       # Distribution script
```

## Dependencies

- Python 3.7+
- OpenCV (opencv-python)
- NumPy
- Matplotlib
- Pillow (PIL)
- tkinter (Python built-in library)

## License

MIT License

## Contributing

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Contact

- Email: ejrdkachry@gmail.com
- Project Link: https://github.com/LEEYH205/bbox-annotation-tools 