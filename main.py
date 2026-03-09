#!/usr/bin/env python3
"""
ARES-NET Main Application Runner
Autonomous Reliability & Erasure-coding Network Simulator
"""

import sys
import os
import subprocess
import logging
from pathlib import Path

def setup_logging():
    """Setup logging for the application"""
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler('ares_net.log'),
            logging.StreamHandler()
        ]
    )

def check_dependencies():
    """Check if all required dependencies are installed"""
    required_packages = [
        'streamlit',
        'plotly', 
        'pandas',
        'numpy',
        'reedsolo'
    ]
    
    missing_packages = []
    
    for package in required_packages:
        try:
            __import__(package)
        except ImportError:
            missing_packages.append(package)
    
    if missing_packages:
        print(f"Missing required packages: {missing_packages}")
        print("Installing missing packages...")
        
        for package in missing_packages:
            subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        
        print("All packages installed successfully!")

def main():
    """Main application entry point"""
    print("🚀 Starting ARES-NET System...")
    print("Autonomous Reliability & Erasure-coding Network Simulator")
    print("-" * 60)
    
    # Setup
    setup_logging()
    check_dependencies()
    
    # Start Streamlit application
    try:
        print("Launching ARES-NET Web Interface...")
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", "frontend.py",
            "--server.address", "localhost",
            "--server.port", "8501",
            "--server.headless", "false"
        ])
    except KeyboardInterrupt:
        print("\n🛑 ARES-NET System shutdown requested")
    except Exception as e:
        print(f"❌ Error starting ARES-NET: {e}")
        return 1
    
    return 0

if __name__ == "__main__":
    sys.exit(main())
