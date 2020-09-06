from pylib.block_agorithm import aria
from pylib.cipher_mode import cbc_mode
from pylib.cipher_mode import cfb_mode
import jpype
import argparse
import sys
import hashlib

parser = argparse.ArgumentParser(description='''범용 파일 암호화 프로그램입니다. 해당 프로글매 사용시 민감한 정보가 노출되거나 유실되더라도 제작자는 책임지지 않습니다!''')
parser.add_argument('--EncDec', required=True, help='select Encrypt or Decrypt')
parser.add_argument('--source', help='source file path.')
parser.add_argument('--key', help='Encrypt Key')
#parser.add_argument('--algorithm', help='Block Encrypt algorithm')
parser.add_argument('--mode', help='Encrypt Mode. ex) CBC, CFB')
parser.add_argument('--remote', help='server address with gourpid ex) https://domain.com/[gourpid]'+\
                                '이 옵션을 입력하면 source와 key 옵션은 무시됨.')

args = parser.parse_args()

Encrypt_Mod=None
Encrypt_algorithm=aria.runAriaEncrypt
Decrypt_algorithm=aria.runAriaDecrypt

if args.remote:
    pass
elif args.key and args.source and args.mode:
    if args.EncDec == "Encrypt" and args.mode == "CBC":
        Encrypt_Mod = cbc_mode.CBC_Mode_Encrtyp
    elif args.EncDec == "Decrypt" and args.mode == "CBC":
        Encrypt_Mod = cbc_mode.CBC_Mode_Decrtyp
    elif args.EncDec == "Encrypt" and args.mode == "CFB":
        Encrypt_Mod = cfb_mode.CFB_Mode_Encrtyp
    elif args.EncDec == "Decrypt" and args.mode == "CFB":
        Encrypt_Mod = cfb_mode.CFB_Mode_Decrtyp
    else:
        parser.print_help()
        sys.exit()
else :
    parser.print_help()
    sys.exit()

def main():    

    jpype.startJVM(jpype.getDefaultJVMPath())

    Encrypt_Mod(\
        Encrypt_algorithm if args.EncDec == "Encrypt" else Decrypt_algorithm if args.mode == "CBC" else Encrypt_algorithm , \
        hashlib.sha256(args.key.encode()).digest(),\
        args.source \
    )
    
    # cfb_mode.CFB_Mode_Encrtyp( \
    #     aria.runAriaEncrypt \
    #     , bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff \
    #         , 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]\
    #     ) \
    #     #, "concept_drawing.png" \
    #     , "test.txt" \
    # )
    # 
    # cfb_mode.CFB_Mode_Decrtyp( \
    #     aria.runAriaEncrypt \
    #     , bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff \
    #         , 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]\
    #     ) \
    #     # , "concept_drawing.png.ucf" \
    #     , "test.txt.ucf" \
    # )

    # cbc_mode.CBC_Mode_Encrtyp( \
    #     aria.runAriaEncrypt \
    #     , bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff \
    #         , 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]\
    #     ) \
    #     #, "concept_drawing.png" \
    #     , "test.txt" \
    # )
    
    # cbc_mode.CBC_Mode_Decrtyp( \
    #     aria.runAriaDecrypt \
    #     , bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff \
    #         , 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #         , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]\
    #     ) \
    #     # , "concept_drawing.png.ucf" \
    #     , "test.txt.ucf" \
    # )

    # cyperResult=aria.runAriaEncrypt( \
    #     bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #            , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff \
    #            , 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #            , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]\
    #     ), \
    #     bytes([0x11, 0x11, 0x11, 0x11, 0xaa, 0xaa, 0xaa, 0xaa\
    #            , 0x11, 0x11, 0x11, 0x11, 0xbb, 0xbb, 0xbb, 0xbb])
    # )
    # print("cyper   : ", bytes(cyperResult).hex())
    # 
    # decyperResult=aria.runAriaDecrypt( \
    #     bytes([0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #            , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff \
    #            , 0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77 \
    #            , 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]\
    #     ), \
    #     bytes(cyperResult))
    # print("decyper : "+bytes(decyperResult).hex())

    #result = jpype.JClass('kr.re.nsri.aria.ARIA').runTest(bytes([207, 208]))
    #print(bytes(result))
    
    jpype.shutdownJVM()


main()