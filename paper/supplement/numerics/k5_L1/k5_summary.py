"""Apply the registered kink criteria (kink_summary.py, unchanged) to the K5 rerun files.
Usage: python k5_summary.py 'TITLE=GLOB' ['TITLE=GLOB' ...]   (run from the folder that holds out/)"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import kink_summary as KS

KS.GROUPS = [tuple(a.split('=', 1)) for a in sys.argv[1:]]
KS.main()
