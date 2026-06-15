"""
Setup Verification Script for E-Commerce Conversion Prediction
Checks if all dependencies and data files are properly set up
"""

import sys
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is 3.9 or higher"""
    version = sys.version_info
    print(f"✓ Python version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or (version.major == 3 and version.minor < 9):
        print("  ⚠ Warning: Python 3.9+ recommended")
        return False
    return True

def check_dependencies():
    """Check if all required packages are installed"""
    packages = [
        'numpy',
        'pandas',
        'sklearn',
        'xgboost',
        'lightgbm',
        'matplotlib',
        'seaborn',
        'jupyter'
    ]
    
    missing = []
    versions = {}
    
    for package in packages:
        try:
            if package == 'sklearn':
                module = __import__('sklearn')
            else:
                module = __import__(package)
            
            version = getattr(module, '__version__', 'unknown')
            versions[package] = version
            print(f"✓ {package:15} {version}")
        except ImportError:
            print(f"✗ {package:15} NOT INSTALLED")
            missing.append(package)
    
    if missing:
        print(f"\n⚠ Missing packages: {', '.join(missing)}")
        print("  Install with: pip install -r requirements.txt")
        return False
    
    return True

def check_project_structure():
    """Check if project directories exist"""
    directories = ['src', 'data', 'notebooks', 'outputs']
    
    all_exist = True
    for directory in directories:
        if os.path.exists(directory):
            print(f"✓ Directory: {directory}/")
        else:
            print(f"✗ Directory: {directory}/ NOT FOUND")
            all_exist = False
    
    return all_exist

def check_source_files():
    """Check if source code files exist"""
    files = [
        'src/__init__.py',
        'src/feature_engineering.py',
        'src/preprocessing.py',
        'src/model.py',
        'src/utils.py',
        'train.py'
    ]
    
    all_exist = True
    for file in files:
        if os.path.exists(file):
            print(f"✓ File: {file}")
        else:
            print(f"✗ File: {file} NOT FOUND")
            all_exist = False
    
    return all_exist

def check_data_files():
    """Check if data files are present"""
    data_dir = Path('data')
    required_files = ['train.csv', 'public_test.csv', 'private_test.csv']
    
    all_exist = True
    for file in required_files:
        file_path = data_dir / file
        if file_path.exists():
            size = file_path.stat().st_size / 1024  # KB
            print(f"✓ Data file: {file} ({size:.1f} KB)")
        else:
            print(f"✗ Data file: {file} NOT FOUND")
            all_exist = False
    
    if not all_exist:
        print("\n  ⚠ Download data files from the hackathon portal")
        print("     Place them in the data/ directory")
    
    return all_exist

def check_notebook():
    """Check if notebook exists"""
    notebook_path = Path('notebooks/notebook.ipynb')
    
    if notebook_path.exists():
        size = notebook_path.stat().st_size / 1024  # KB
        print(f"✓ Notebook: notebook.ipynb ({size:.1f} KB)")
        return True
    else:
        print("✗ Notebook: notebook.ipynb NOT FOUND")
        return False

def main():
    """Run all setup checks"""
    print("="*70)
    print("E-COMMERCE CONVERSION PREDICTION - SETUP VERIFICATION")
    print("="*70)
    
    print("\n[1] Python Version")
    print("-" * 70)
    python_ok = check_python_version()
    
    print("\n[2] Dependencies")
    print("-" * 70)
    deps_ok = check_dependencies()
    
    print("\n[3] Project Structure")
    print("-" * 70)
    structure_ok = check_project_structure()
    
    print("\n[4] Source Files")
    print("-" * 70)
    source_ok = check_source_files()
    
    print("\n[5] Data Files")
    print("-" * 70)
    data_ok = check_data_files()
    
    print("\n[6] Notebook")
    print("-" * 70)
    notebook_ok = check_notebook()
    
    # Summary
    print("\n" + "="*70)
    print("SUMMARY")
    print("="*70)
    
    checks = [
        ("Python Version", python_ok),
        ("Dependencies", deps_ok),
        ("Project Structure", structure_ok),
        ("Source Files", source_ok),
        ("Data Files", data_ok),
        ("Notebook", notebook_ok)
    ]
    
    for check_name, passed in checks:
        status = "✓ PASS" if passed else "✗ FAIL"
        print(f"{check_name:20} {status}")
    
    all_passed = all(passed for _, passed in checks)
    
    print("\n" + "="*70)
    if all_passed:
        print("✓ ALL CHECKS PASSED! You're ready to go!")
        print("\nNext steps:")
        print("  1. Run: python train.py")
        print("  2. Or open: jupyter notebook notebooks/notebook.ipynb")
    else:
        print("⚠ SOME CHECKS FAILED")
        print("\nPlease fix the issues above before proceeding.")
        print("See INSTALLATION.md for detailed setup instructions.")
    print("="*70)

if __name__ == "__main__":
    main()
