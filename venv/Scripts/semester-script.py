#!C:\Users\Hasnawir\PycharmProjects\MidPBO\venv\Scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'semester==0.1.1','console_scripts','semester'
__requires__ = 'semester==0.1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('semester==0.1.1', 'console_scripts', 'semester')()
    )
