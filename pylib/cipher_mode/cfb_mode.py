def CFB_Mode_Encrtyp(algorithm, key, fileName):

    result=bytes()
    
    InitialVector=key[15::-1]
    
    with open(fileName, 'rb') as fin:
        while True:
            tempPlainBytes=fin.read(16)
            if not tempPlainBytes:
                break
            if len(tempPlainBytes)<16:
                for i in range(0, 16-len(tempPlainBytes)):
                    tempPlainBytes+=bytes(1)
            IV_cyper_result=bytes(algorithm(key, InitialVector))
            tempPlaitBytes_XOR_IV_cyper_result=bytes(a ^ b for a, b in zip(tempPlainBytes, IV_cyper_result))
            InitialVector=tempPlaitBytes_XOR_IV_cyper_result
            result+=tempPlaitBytes_XOR_IV_cyper_result
            
    # print("cyper_result : ", result.hex())
    
    with open(fileName+".ucf", 'wb') as fout:
        fout.write(result)

def CFB_Mode_Decrtyp(algorithm, key, fileName):

    result=bytes()

    InitialVector=key[15::-1]

    with open(fileName, 'rb') as fin:
        while True:
            tempCipherBytes=fin.read(16)
            if not tempCipherBytes:
                break
            IV_cipher_result=bytes(algorithm(key, InitialVector))
            tempCipherBytes_XOR_IV_cipher_result=bytes(a ^ b for a, b in zip(tempCipherBytes, IV_cipher_result))
            InitialVector=tempCipherBytes
            result+=tempCipherBytes_XOR_IV_cipher_result;
            
    # print("plain_result : ", result.hex())
    
    with open(fileName+".unlock", 'wb') as fout:
        fout.write(result)