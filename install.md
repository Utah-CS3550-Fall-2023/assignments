Installing all of the Software
==============================

Installing Python
-----------------

Find or install Python 3. Ideally you would have version 3.10 or 3.11,
but in principle versions as old as 3.8 might work. CADE machines have
Python 3.10 installed. Python comes preinstalled with recent version
of macOS, but it may be out of date. Python is available for all
platforms from [python.org]. Check your Python version with:

    python3 --version

If this command fails, or prints a version older than 3.8, you need to
go to [python.org] and install Python. (You can also install Python
through VS Code, Homebrew, your system package manager, or any other
source, as long as it is recent enough.)

Make sure that you have database support:

    python3 -c "import sqlite3"

If this command succeeds with no output, that means everything is
good. This should be the case for most Python installations, since the
`sqlite3` module ships with Python by default. If it produces what
looks like an error, seek help from the instructors.

Installing Django
-----------------

Install Django by running:

    python3 -m pip install django

Check your Django version by running:

    python3 -m django --version
    
Make sure the version starts with 4.2.
