#!/usr/bin/env python3
"""
ARES-NET Setup and Installation Script
"""

import os
import sys
import subprocess
from pathlib import Path

def create_project_structure():
    """Create the project directory structure"""
    directories = [
        'data',
        'logs', 
        'docs',
        'tests'
    ]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
    
    print("✅ Project structure created")

def install_dependencies():
    """Install all required dependencies"""
    print("📦 Installing dependencies...")
    
    subprocess.check_call([
        sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
    ])
    
    print("✅ Dependencies installed")

def setup_database():
    """Initialize the database"""
    print("🗄️ Setting up database...")
    
    try:
        from ares_net_core import AresNetworkDatabase
        db = AresNetworkDatabase()
        print("✅ Database initialized")
    except Exception as e:
        print(f"❌ Database setup failed: {e}")

def main():
    """Main setup function"""
    print("🚀 ARES-NET Setup")
    print("=" * 50)
    
    create_project_structure()
    install_dependencies()
    setup_database()
    
    print("\n🎉 ARES-NET setup completed successfully!")
    print("To start the application, run: python main.py")

if __name__ == "__main__":
    main()
