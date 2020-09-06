def CBC_Mode_Encrtyp(algorithm, key, fileName):

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
            tempPlaitBytes_XOR_IV=bytes(a ^ b for a, b in zip(tempPlainBytes, InitialVector))
            block_cyper_result=bytes(algorithm(key, tempPlaitBytes_XOR_IV))
            InitialVector=block_cyper_result
            result+=block_cyper_result
            
    # print("cyper_result : ", result.hex())
    
    with open(fileName+".ucf", 'wb') as fout:
        fout.write(result)

def CBC_Mode_Decrtyp(algorithm, key, fileName):

    result=bytes()

    InitialVector=key[15::-1]

    with open(fileName, 'rb') as fin:
        while True:
            tempCipherBytes=fin.read(16)
            if not tempCipherBytes:
                break
            block_cipher_result=bytes(algorithm(key, tempCipherBytes))
            block_cipher_result_XOR_IV=bytes(a ^ b for a, b in zip(block_cipher_result, InitialVector))
            InitialVector=tempCipherBytes
            result+=block_cipher_result_XOR_IV;
            
    # print("plain_result : ", result.hex())
    
    with open(fileName+".unlock", 'wb') as fout:
        fout.write(result)