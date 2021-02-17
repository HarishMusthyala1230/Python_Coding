
''' Program for attempting an attack on Hill Cipher '''
# Convering the input(plaintext and ciphertext) into capital letters
Plain_Text = input("Plain_Text: ")
Cipher_Text = input("Cipher_Text: ")
Plain_Text = list(Plain_Text.upper())
Cipher_Text = list(Cipher_Text.upper())
print("Plain_Text: ",Plain_Text,"\nCipher_Text: ",Cipher_Text)
P_T = []
C_T = []
# defining Converting aplhabetical numbers
char = ['A','B','C','D','E','F','G','H','I','J','K','L','M',
        'N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
def Number(Text): # Function for getting alphabetical number
    temp = []
    for i in Text:
        temp.append(int((char.index(i))))
    return temp
def Matrix(Text): # Function for converting list into matrix
    matrix = []
    for i in range(0,2):
        temp = []
        temp.append(Text[i])
        temp.append(Text[i+2])
        matrix.append(temp)
    return matrix
def Matrix_Inv(m,x): # Function for finding det inverse * matrix
    return [[(x*m[1][1])%26, (-1*x*m[0][1])%26],
                [(-1*x*m[1][0])%26, (x*m[0][0])%26]]
def Multi(a,b): # Function for multiplication of matrices
    return [[((a[0][0]*b[0][0])+(a[0][1]*b[1][0]))%26, ((a[0][0]*b[0][1])+(a[0][1]*b[1][1]))%26],
                [((a[1][0]*b[0][0])+(a[1][1]*b[1][0]))%26, ((a[1][0]*b[0][1])+(a[1][1]*b[1][1]))%26]]
P_T = Number(Plain_Text) # converting to alphabetical number 
C_T = Number(Cipher_Text) # converting to alphabetical number 
P = Matrix(P_T) # converting to matrix 
C = Matrix(C_T) # converting to matrix 
print("P: ",P_T,"\nC: ",C_T,"\nP_Matrix: ",P,"\nC_Matrix: ",C)
det_P = (P[0][0]*P[1][1])-(P[0][1]*P[1][0])%26 # Finding determinant of matrix
# For inverse of determinant
for i in range(det_P):
    if (i*det_P)%26 == 1:
        det_P_Inv = i
        break;
P_I = Matrix_Inv(P,det_P_Inv) # For det inverse * matrix
Key = Multi(C,P_I) # Calculating Key
print("KEY: ",Key)
''' Program ends '''
