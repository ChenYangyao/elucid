import os, elucid

def test_env():
    print('Python PATH:', os.environ['PYTHONPATH'])    
    
def test_version():
    print(elucid.version)