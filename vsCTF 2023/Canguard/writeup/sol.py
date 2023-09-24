#run in the same directory as the log files
import os
import sys
import struct

KEYMASK = [
    0xB1, 0x54, 0x45, 0x57, 0xA7, 0xC4, 0x64, 0x2E, 0x98, 0xD8, 0xB1, 0x1A, 
    0x0B, 0xAA, 0xD8, 0x8E, 0x7F, 0x1E, 0x5B, 0x8D, 0x08, 0x67, 0x96, 0xCB, 
    0xAA, 0x11, 0x50, 0x84, 0x17, 0x46, 0xA3, 0x30
]
LOG_EXTENSION = '.log'
FLAG_START = 'vsctf'
FLAG_END = '}'

def rc4(data, key):
    S = [i for i in range(256)]
    j = 0
    out = []
    
    for i in range(256):
        j = (j + S[i] + key[i % len(key)]) % 256
        S[i], S[j] = S[j], S[i]
    
    i = j = 0
    for char in data:
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        out.append(char ^ S[(S[i] + S[j]) % 256])
    
    return bytearray(out)

def decrypt_file(filename):
    with open(filename, 'rb') as f:
        DATA = f.read()

    DATA = DATA[4:]
    REAL_KEY = [DATA[i] ^ KEYMASK[i] for i in range(32)]
    DATA = DATA[32:]

    decrypted_blocks = []

    while DATA:
        BLOCK_LEN = struct.unpack('<L', DATA[:4])[0]
        DATA = DATA[4:]
        decrypted_blocks.append(rc4(DATA[:BLOCK_LEN], REAL_KEY).decode('utf-16'))
        DATA = DATA[BLOCK_LEN:]

    return ''.join(decrypted_blocks)

def main():
    for file in os.listdir('.'):
        if file.endswith(LOG_EXTENSION):
            try:
                decrypted_content = decrypt_file(file)
                
                if FLAG_START in decrypted_content:
                    flag_position = decrypted_content.index(FLAG_START)
                    flag_end_position = decrypted_content.index(FLAG_END, flag_position) + 1
                    print(f'Flag found in {file}: {decrypted_content[flag_position:flag_end_position]}')
                    sys.exit(0)
            except Exception as e:
                print(f'Error processing {file}: {e}')

if __name__ == '__main__':
    main()
#vsctf{0h_w0W!_v4Ngu4rd_l0Gs_d3CrYpt3D_sHh!!_d0Nt_T3Ll_3vErd0X_>:(}