#!/usr/bin/env python3
"""
Cybersecurity Environment Verification Script
Validates that all required security libraries are properly installed
"""

import sys
import importlib.util

def verify_library(library_name, display_name=None):
    """Verify that a library can be imported successfully"""
    if display_name is None:
        display_name = library_name
    
    try:
        __import__(library_name)
        print(f'✅ {display_name} - Ready for deployment')
        return True
    except ImportError as e:
        print(f'❌ {display_name} - Installation issue: {e}')
        return False

def main():
    """Main verification routine"""
    print('=== Cybersecurity Arsenal Verification ===')
    print(f'Python Version: {sys.version}')
    print(f'Python Executable: {sys.executable}')
    print(f'Virtual Environment: {sys.prefix}')
    print('=' * 50)
    
    # Core libraries for cybersecurity work
    libraries = [
        ('scapy', 'Scapy (Network Analysis)'),
        ('requests', 'Requests (HTTP Library)'),
        ('cryptography', 'Cryptography (Security Primitives)'),
        ('paramiko', 'Paramiko (SSH Client)'),
        ('bs4', 'BeautifulSoup (HTML Parsing)'),
        ('pandas', 'Pandas (Data Analysis)'),
        ('nmap', 'Python-Nmap (Network Discovery)'),
        ('netaddr', 'NetAddr (Network Address Manipulation)'),
        ('Crypto', 'PyCryptodome (Cryptographic Algorithms)'),
        ('psutil', 'PSUtil (System Monitoring)'),
        ('selenium', 'Selenium (Web Automation)'),
        ('numpy', 'NumPy (Numerical Computing)'),
        ('matplotlib', 'Matplotlib (Visualization)'),
        ('hashlib', 'Hashlib (Built-in Hashing)'),  # Built-in library
    ]
    
    successful = 0
    total = len(libraries)
    
    for lib_name, display_name in libraries:
        if verify_library(lib_name, display_name):
            successful += 1
    
    print('=' * 50)
    print(f'Verification Complete: {successful}/{total} libraries ready')
    
    if successful == total:
        print('🎉 Your cybersecurity arsenal is fully operational!')
        print('Ready for professional security development work.')
    else:
        print('⚠️  Some libraries require attention before proceeding.')
    
    return successful == total

if __name__ == '__main__':
    main()
