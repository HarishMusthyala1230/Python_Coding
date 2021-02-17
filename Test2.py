
''' Program 1 : Read text file contents and encrypt the contents to a new file '''


#Initialising codes using a dictionary
codes = {'A':'!','B':'@','C':'#','D':'$','E':'%','F':'^','G':'&','H':'*','I':'(','J':')','K':'`','L':'_','M':'+','N':'=','O':'{','P':'}','Q':'|','R':'[','S':']','T':':','U':';','V':'"',
         'W':'~','X':'?','Y':'/','Z':'<',
         'a':'s','b':'t','c':'u','d':'v','e':'w','f':'x','g':'y','h':'z','i':'>','j':'a','k':'b','l':'c','m':'d','n':'e','o':'f','p':'g','q':'h','r':'i','s':'j','t':'k','u':'l','v':'m',
         'w':'o','x':'p','y':'q','z':'r'}

#Opening a file "text.txt" in reading format
file = open('text.txt','r')
#Loading the contents
load = file.read()
#Closing the file after reading its content
file.close()
#Creating another file in writing mode to save the encryoted data
encrypt_file = open('encrypted_text.txt','w')

# Reading each character and converting to respective codes which are initialised and then writing it to new file "encrypted_text.txt"
for char in load:
    if char in codes:
        encrypt_file.write(codes[char])
    else:
        encrypt_file.write(char)
#Closing the new file after encrypted data is written
encrypt_file.close()


'''Program 2 : To opens the encrypted file and display'''
#Initialising decrypt codes using a dictionary
decrypt_codes = {'!':'A','@':'B','#':'C','$':'D','%':'E','^':'F','&':'G','*':'H','(':'I',')':'J','`':'K','_':'L','+':'M','=':'N','{':'O','}':'P','|':'Q','[':'R',']':'S',':':'T',';':'U','"':'V',
         '~':'W','?':'X','/':'Y','<':'Z',
         's':'a','t':'b','u':'c','v':'d','w':'e','x':'f','y':'g','z':'h','>':'i','a':'j','b':'k','c':'l','d':'m','e':'n','f':'o','g':'p','h':'q','i':'r','j':'s','k':'t','l':'u','m':'v',
         'o':'w','p':'x','q':'y','r':'z',}
#Opening encrypted file "encrypted_text.txt" in reading format
en_file = open('encrypted_text.txt','r')
#Loading the contents
en_load = en_file.read()
#Closing the file after reading its content
en_file.close()
#Creating another file in writing mode to save the decrypted data
decrypt_file = open('decrypted_text.txt','w')


#Reading each character and decrypting codes and then writing it to new file "deencrypted_text.txt"
for char in en_load:
    if char in decrypt_codes:
        decrypt_file.write(decrypt_codes[char])
    else:
        decrypt_file.write(char)
#Closing the new file after encrypted data is written
decrypt_file.close()

#Printing the decrypted file
d = open('decrypted_text.txt','r')
read_decrypt = d.read()
d.close()
print(read_decrypt)













