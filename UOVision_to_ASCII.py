"""
Drag and drop UOVision binary file to convert to ASCII
or drag and drop ASCII file to convert to UOVision binary.
Files with names ending on ".txt" are treated as ASCII files.
Tested on PROFILE.BIN of UM785, UM595, UM565, and UM562,
and LogFile.DAT of UM785.

Author: Christian Petrich
Date: 11 Nov 2016
License: MIT
"""

def decode_word(byte1, byte2):
    """Bit-rotate 0xAB 0xCD into 0xDA 0xBC and bit-invert result"""
    word = (byte1 * 0x100 + byte2) ^ 0xffff
    rotated = word // 0x10 + (word % 0x10) * 0x1000
    return rotated // 0x100, rotated % 0x100

def convert(input_data, decode=True):
    """Decode UOVision data stream to ASCII
(Encode ASCII to UOVision data with decode=False)"""
    output_data = bytearray([])
    for char1, char2 in zip(input_data[::2], input_data[1::2]):
        value1, value2 = decode_word(char1, char2)
        out = (value1,value2) if decode else (value2,value1)
        output_data.append(out[0])
        output_data.append(out[1])
    return output_data


if __name__=='__main__':
    import sys

    # default used for testing:
    fn_in, decode = 'PROFILE.BIN', True

    if len(sys.argv)==2:
        # drag-and-drop file to convert
        fn_in = sys.argv[1]    
        decode = not fn_in.lower().endswith('.txt')

    fn_out = fn_in+('.txt' if decode else '.bin')

    # Use bytearray so this runs on both Python 2 and 3.
    print('%scoding %s' % ('De' if decode else 'En', fn_in))
    open(fn_out,'wb').write(convert(bytearray(open(fn_in,'rb').read()), decode))
