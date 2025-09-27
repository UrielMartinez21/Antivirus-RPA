# ESET NOD32 License Automation Tool

RPA (Robotic Process Automation) tool for automatically changing licenses in ESET NOD32. This project uses PyAutoGUI to automate the graphical interface and process multiple licenses from a CSV file.

## 📋 Description

This tool automates the ESET NOD32 license changing process, allowing sequential processing of multiple licenses without manual intervention. The system automatically detects activation errors and continues with the next available license.

## 🚀 Features

- ✅ Complete automation of the license changing process
- ✅ Multiple license processing from CSV file
- ✅ Automatic activation error detection
- ✅ Robust exception handling
- ✅ Simple command-line interface

## 📁 Project Structure

```
antivirus/
├── main.py                 # Main execution file
├── requirements.txt        # Project dependencies
├── packages/
│   ├── functions.py        # Main automation functions
│   └── pahts.py           # Project paths and constants
├── licenses/
│   └── main.csv           # License database
└── images/                # Images for visual recognition
    ├── section.png
    ├── change_subs.png
    ├── change_license.png
    ├── enter_license.png
    ├── continue_process.png
    ├── activation_error.png
    └── button_to_back.png
```

## 🛠️ Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/UrielMartinez21/Antivirus-RPA.git
   cd antivirus
   ```

2. **Create a virtual environment:**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment:**
   ```bash
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

4. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📦 Dependencies

- **PyAutoGUI**: GUI automation
- **pandas**: CSV data handling
- **opencv-python**: Image processing
- **pillow**: Image manipulation
- **numpy**: Numerical operations

## 🚀 Usage

1. **Make sure ESET NOD32 is closed**
2. **Run the main script:**
   ```bash
   python main.py
   ```

3. **The program will automatically:**
   - Open ESET NOD32
   - Navigate to the license section
   - Process each license from the CSV file
   - Handle activation errors automatically

## ⚙️ Main Functions

### `open_eset_nod32(path)`
Opens the ESET NOD32 application from the specified path.

### `get_licenses(path)`
Reads licenses from the CSV file and returns them as a list.

### `get_location(image_path, confidence)`
Locates elements on screen using image recognition.

### `click_at_location(location, time_to_sleep)`
Clicks at a specific location and waits for the specified time.

## ⚠️ Important Considerations

- **Screen resolution**: Images must match your resolution
- **Display settings**: Keep the same configuration during execution
- **Permissions**: Run as administrator if necessary
- **Antivirus**: Some antivirus software may block automation