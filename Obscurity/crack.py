def encrypt(text, key):                                                                                          
   keylen = len(key)                                                                                            
   keyPos = 0                                                                                                    
   encrypted = ""                                                                                                
   for x in text:                                                                                                
       keyChr = key[keyPos]                                                                                      
       newChr = ord(x)                                                                                          
       newChr = chr((newChr + ord(keyChr)) % 255)                                                                
       encrypted += newChr                                                                                      
       keyPos += 1                                                                                              
       keyPos = keyPos % keylen                                                                                  
   return encrypted                                                                                              
                                                                                                                 
def decrypt(text, key):                                                                                          
   keylen = len(key)                                                                                            
   keyPos = 0                                                                                                    
   decrypted = ""                                                                                                
   for x in text:                                                                                                
       keyChr = key[keyPos]                                                                                      
       newChr = ord(x)                                                                                          
       newChr = chr((newChr - ord(keyChr)) % 255)                                                                
       decrypted += newChr                                                                                      
       keyPos += 1                                                                                              
       keyPos = keyPos % keylen                                                                                  
   return decrypted

i = 'Encrypting this file with your key should result in out.txt, make sure your key is correct!'
e = 'ÑÈÌÉàÙÁÑé¯·¿k'
k = 'alexandrov'
o = '¦ÚÈêÚÞØÛÝÝ×ÐÊßÞÊÚÉæßÝËÚÛÚêÙÉëéÑÒÝÍÐêÆáÙÞãÒÑÐáÙ¦ÕæØãÊÎÍßÚêÆÝáäèÎÍÚÎëÑÓäáÛÌ×v'
print('encrypt:', o)
ans = decrypt(e, k)
print('key', ans)
