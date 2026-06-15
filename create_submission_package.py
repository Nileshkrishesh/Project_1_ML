"""
Automated Submission Package Creator
Creates the ZIP file required for hackathon submission
"""

import os
import zipfile
import shutil
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if required file exists"""
    if os.path.exists(filepath):
        size = os.path.getsize(filepath) / 1024  # KB
        print(f"✓ Found {description}: {filepath} ({size:.1f} KB)")
        return True
    else:
        print(f"✗ Missing {description}: {filepath}")
        return False

def create_report_pdf_instructions():
    """Provide instructions for creating report.pdf"""
    print("\n" + "="*70)
    print("REPORT.PDF CREATION")
    print("="*70)
    print("\nYou need to convert report.md to report.pdf")
    print("\nOption 1: Using Pandoc (if installed)")
    print("  pandoc report.md -o report.pdf")
    print("\nOption 2: Using VS Code")
    print("  1. Install 'Markdown PDF' extension")
    print("  2. Open report.md")
    print("  3. Right-click > 'Markdown PDF: Export (pdf)'")
    print("\nOption 3: Online Converters")
    print("  - https://www.markdowntopdf.com/")
    print("  - https://cloudconvert.com/md-to-pdf")
    print("  - https://dillinger.io/ (export as PDF)")
    print("\nOption 4: Copy to Google Docs/Word and export as PDF")
    print("\nAfter creating report.pdf, run this script again.")
    print("="*70)

def create_submission_zip():
    """Create submission ZIP file with notebook and report"""
    print("="*70)
    print("SUBMISSION PACKAGE CREATOR")
    print("Summer Analytics 2026 - Week 2 Hackathon")
    print("="*70)
    
    # Define file paths
    notebook_path = Path("notebooks/notebook.ipynb")
    report_pdf_path = Path("report.pdf")
    submission_csv_path = Path("outputs/submission.csv")
    output_zip_path = Path("submission.zip")
    
    # Check if files exist
    print("\n[1] Checking required files...")
    print("-" * 70)
    
    notebook_exists = check_file_exists(notebook_path, "Notebook")
    report_exists = check_file_exists(report_pdf_path, "Report PDF")
    csv_exists = check_file_exists(submission_csv_path, "Submission CSV")
    
    # Handle missing report.pdf
    if not report_exists:
        create_report_pdf_instructions()
        return False
    
    if not notebook_exists:
        print("\n✗ ERROR: notebook.ipynb not found!")
        print("  Expected location: notebooks/notebook.ipynb")
        return False
    
    if not csv_exists:
        print("\n⚠ WARNING: submission.csv not found!")
        print("  Run 'python train.py' first to generate predictions")
        print("  This file needs to be uploaded separately to the portal")
    
    # Create ZIP file
    print("\n[2] Creating submission ZIP file...")
    print("-" * 70)
    
    try:
        with zipfile.ZipFile(output_zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            # Add notebook
            print(f"Adding: {notebook_path}")
            zipf.write(notebook_path, arcname="notebook.ipynb")
            
            # Add report
            print(f"Adding: {report_pdf_path}")
            zipf.write(report_pdf_path, arcname="report.pdf")
        
        # Verify ZIP contents
        print("\n[3] Verifying ZIP contents...")
        print("-" * 70)
        
        with zipfile.ZipFile(output_zip_path, 'r') as zipf:
            files = zipf.namelist()
            print(f"ZIP contains {len(files)} files:")
            for file in files:
                info = zipf.getinfo(file)
                print(f"  ✓ {file} ({info.file_size / 1024:.1f} KB)")
        
        zip_size = os.path.getsize(output_zip_path) / (1024 * 1024)  # MB
        
        print("\n" + "="*70)
        print("✓ SUCCESS! Submission package created")
        print("="*70)
        print(f"\nZIP file: {output_zip_path}")
        print(f"Size: {zip_size:.2f} MB")
        print("\nContents:")
        print("  1. notebook.ipynb - Reproducible solution notebook")
        print("  2. report.pdf - One-page methodology summary")
        
        if csv_exists:
            print(f"\n📄 Also ready: {submission_csv_path}")
            print("   Upload this separately to the submission portal")
        
        print("\n" + "="*70)
        print("SUBMISSION CHECKLIST")
        print("="*70)
        print("Upload to: https://www.hackerearth.com/challenges/")
        print("          competitive/summer-analytics-2026/")
        print("\n1. Upload submission.csv (predictions)")
        print("   ✓ File: outputs/submission.csv")
        print(f"   {'✓' if csv_exists else '✗'} Status: {'Ready' if csv_exists else 'NOT FOUND - Run train.py'}")
        print("\n2. Upload submission.zip (code + report)")
        print(f"   ✓ File: {output_zip_path}")
        print("   ✓ Status: Ready")
        print("\n" + "="*70)
        
        return True
        
    except Exception as e:
        print(f"\n✗ ERROR creating ZIP file: {e}")
        return False

def verify_submission_csv():
    """Verify submission CSV format"""
    import pandas as pd
    
    csv_path = Path("outputs/submission.csv")
    
    if not csv_path.exists():
        print("\n⚠ WARNING: submission.csv not found")
        print("Run 'python train.py' to generate predictions")
        return False
    
    print("\n[4] Verifying submission.csv format...")
    print("-" * 70)
    
    try:
        df = pd.read_csv(csv_path)
        
        # Check columns
        expected_cols = ['User_ID', 'Converted']
        if list(df.columns) != expected_cols:
            print(f"✗ Column error. Expected {expected_cols}, got {list(df.columns)}")
            return False
        print(f"✓ Columns: {list(df.columns)}")
        
        # Check shape
        print(f"✓ Shape: {df.shape[0]} rows, {df.shape[1]} columns")
        
        # Check for missing values
        missing = df.isnull().sum().sum()
        if missing > 0:
            print(f"✗ Contains {missing} missing values")
            return False
        print("✓ No missing values")
        
        # Check Converted values
        unique_vals = df['Converted'].unique()
        if not set(unique_vals).issubset({0, 1}):
            print(f"✗ Converted should only contain 0 and 1, found: {unique_vals}")
            return False
        print("✓ Converted contains only 0 and 1")
        
        # Check for duplicates
        duplicates = df['User_ID'].duplicated().sum()
        if duplicates > 0:
            print(f"✗ Contains {duplicates} duplicate User_IDs")
            return False
        print("✓ No duplicate User_IDs")
        
        # Display distribution
        print(f"\nPrediction distribution:")
        print(df['Converted'].value_counts().to_string())
        
        print("\n✓ submission.csv format is valid!")
        return True
        
    except Exception as e:
        print(f"✗ Error reading CSV: {e}")
        return False

def main():
    """Main function"""
    
    # Change to project directory
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    
    # Verify submission CSV if it exists
    verify_submission_csv()
    
    # Create submission ZIP
    success = create_submission_zip()
    
    if success:
        print("\n🎉 All done! Your submission package is ready!")
        print("\nNext steps:")
        print("1. Go to the hackathon submission portal")
        print("2. Upload 'outputs/submission.csv' (predictions)")
        print("3. Upload 'submission.zip' (notebook + report)")
        print("\nGood luck! 🚀")
    else:
        print("\n⚠ Please fix the issues above and try again.")

if __name__ == "__main__":
    main()
