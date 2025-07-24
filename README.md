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

### Quick Start

After installation, you can run the GUI tools directly from the command line:

```bash
# Bounding Box Editor
bbox-editor

# Drug Code Viewer
drug-viewer
```

### Detailed Usage Guide

#### 1. Bounding Box Editor (bbox-editor)

The Bounding Box Editor is designed for editing COCO format annotation files with an intuitive GUI interface.

**Key Features:**
- **Folder Selection**: Choose annotation folders organized by drug categories
- **Drug Code Selection**: Select specific drug codes (K-XXXX format)
- **Annotation List**: Browse through all annotations for the selected drug
- **Interactive Drawing**: Click and drag to create or modify bounding boxes
- **Coordinate Input**: Manually input precise coordinates (X, Y, Width, Height)
- **Reference Display**: Show existing annotations from other drugs in the same folder
- **Save & Navigation**: Save changes and navigate between annotations

**Workflow:**
1. Launch the editor: `bbox-editor`
2. Select annotation folder from the dropdown
3. Choose drug code (e.g., K-1234)
4. Browse annotation list and select an image
5. Edit bounding box by:
   - Dragging on the image to create new boxes
   - Using coordinate input fields for precise adjustments
   - Clicking "Apply Coordinates" to update
6. Save changes with "Save" button
7. Navigate between annotations with "Next"/"Previous" buttons

**Keyboard Shortcuts:**
- `Ctrl+S`: Save current annotation
- `Ctrl+N`: Next annotation
- `Ctrl+P`: Previous annotation
- `Ctrl+Z`: Restore original bounding box

#### 2. Drug Code Viewer (drug-viewer)

The Drug Code Viewer provides a comprehensive view of all annotations organized by drug codes.

**Key Features:**
- **Drug Code Overview**: See all available drug codes and their annotation counts
- **Image Gallery**: Browse all images for a selected drug code
- **Bounding Box Visualization**: Display bounding boxes on images
- **Overlap Analysis**: Identify overlapping bounding boxes
- **Annotation Statistics**: View annotation metadata and statistics
- **Export Capabilities**: Export analysis results

**Workflow:**
1. Launch the viewer: `drug-viewer`
2. Select a drug code from the list
3. Browse through images for that drug code
4. Analyze bounding box positions and overlaps
5. View annotation metadata and statistics
6. Export results if needed

### Advanced Usage

#### Using in Python Scripts

You can also use the tools programmatically in your Python scripts:

```python
from bbox_tools import BBoxEditor, DrugCodeViewer
import tkinter as tk

# Create and run Bounding Box Editor
def run_bbox_editor():
    root = tk.Tk()
    editor = BBoxEditor(root)
    root.mainloop()

# Create and run Drug Code Viewer
def run_drug_viewer():
    root = tk.Tk()
    viewer = DrugCodeViewer(root)
    root.mainloop()

# Run the tools
if __name__ == "__main__":
    run_bbox_editor()  # or run_drug_viewer()
```

#### Configuration

The tools automatically save your preferences:
- Last used folder and drug code
- Window geometry and settings
- Display preferences

Configuration is stored in `~/.bbox_tools_config.json`

#### Data Format

**Supported Annotation Format:**
- COCO JSON format
- Single annotation per file
- Bounding box coordinates: [x, y, width, height]

**Expected Directory Structure:**
```
annotations/
├── folder1_json/
│   ├── K-1234/
│   │   ├── annotation1.json
│   │   └── annotation2.json
│   └── K-5678/
│       ├── annotation3.json
│       └── annotation4.json
└── folder2_json/
    └── K-9999/
        └── annotation5.json
```

**Image Requirements:**
- Supported formats: JPG, PNG, BMP, TIFF
- Images should be in a separate directory
- Image filenames must match those referenced in annotation files

### Troubleshooting

**Common Issues:**

1. **"Path not found" error:**
   - Ensure annotation and image paths are correctly set
   - Check file permissions

2. **Images not loading:**
   - Verify image files exist in the specified directory
   - Check image format compatibility

3. **Annotations not saving:**
   - Ensure write permissions for annotation files
   - Check JSON file format validity

4. **GUI not responding:**
   - Close and restart the application
   - Check system resources

**Getting Help:**
- Check the console output for error messages
- Verify your data format matches the expected structure
- Ensure all dependencies are properly installed

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