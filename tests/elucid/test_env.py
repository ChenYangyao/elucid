import os, elucid

def test_env():
    print('Python PATH:', os.environ.get('PYTHONPATH', None))    
    
def test_version():
    print(elucid.version)