import UOVision_to_ASCII as UA

# work around python version incompatibilities regarding 'reload'...
try:
    _=reload # Python 2
except NameError:
    try:
        from importlib import reload # Python 3 >=3.4
    except ImportError:
        from imp import reload # Python 3 <3.4
reload(UA)


def test_word_decode():
    assert tuple(UA.decode_word(0xab,0xcd)) == (0x25, 0x43)    

def test_convert_decode():
    assert UA.convert(bytearray((0xab,0xcd,0x01,0x23))) == bytearray((0x25,0x43,0xcf,0xed))
        
def test_convert_encode():
    assert UA.convert(bytearray((0x25,0x43,0xcf,0xed)),decode=False) == bytearray((0xab,0xcd,0x01,0x23))
    assert UA.convert(bytearray((0xab,0xcd,0x01,0x23)),decode=False) == bytearray((0x43,0x25,0xed,0xcf))
    

if __name__=='__main__':
    print('Recommended to run tests with: python -m pytest')
    # run test functions anyway    
    for name in dir():
        if name.startswith('test_'):
            print(name+'()')
            eval(name+'()')
