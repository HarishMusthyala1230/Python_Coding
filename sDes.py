" Python program for encryption and decryption using Simplified DES"
# Permutation and Sbox values
P10 = [3,5,2,7,4,10,1,9,8,6]
P8 = [6,3,7,4,8,5,10,9]
IP = [2,6,3,1,4,8,5,7]
EP = [4,1,2,3,2,3,4,1]
S0 = [[1,0,3,2],[3,2,1,0],[0,2,1,3],[3,1,3,2]]
S1 = [[0,1,2,3],[2,0,1,3],[3,0,1,0],[2,1,0,3]]
S_M = [[2,1,0,3],[2,0,1,3],[3,0,1,0],[0,1,2,3]]
P4 = [2,4,3,1]
IP_INV = [4,1,3,5,7,2,8,6]

Plain_Text = []
Key = []
Left = []
Right = []
EP_K1 = []
EP_KEY = []
L_P4 = []
Last = []
# Function for 10 bit permutation(P10)
def permute_10(K):
    P_P10 = []
    for i in P10:  
        P_P10.append(K[i-1])
    return P_P10
# Function for 8 bit permutation(P8)
def permute_8(K):
    P_P8 = []
    for i in P8:  
        P_P8.append(K[i-1])
    return P_P8
# Function for 4 bit permutation(P4)
def permute_4(K):
    P_P4 = []
    for i in P4:  
        P_P4.append(K[i-1])
    return P_P4
#Function for performing swift operation
def leftswift(ls,n):
    temp = []
    Left = []
    Right = []
    Left_temp = []
    Right_temp = []
    length = int(len(ls)/2)
    for i in range(0,length):
        Left.append(ls[i])
    for i in range(length,int(len(ls))):
        Right.append(ls[i])
    Left_temp = Left[n:] + Left[:n]
    Right_temp = Right[n:] + Right[:n]
    temp = Left_temp + Right_temp
    return(temp)
# Functions to split the list into two halfs(left and right)
def left(List):
    L = []
    length = int(len(List)/2)
    for i in range(0,length):
        L.append(List[i])
    return(L)
def right(List):
    R = []
    length = int(len(List)/2)
    for i in range(length,int(len(List))):
        R.append(List[i])
    return(R)
# Function for Initial Permutation(IP)
def initial_permute(K):
    P = []
    for i in IP:  
        P.append(K[i-1])
    return P
# Function for Inverse of Permutation(IP Inverse)
def inverse_permute(K):
    P = []
    for i in IP_INV:  
        P.append(K[i-1])
    return P
# Function for E permutation (EP)
def E_permute(K):
    P = []
    for i in EP:  
        P.append(K[i-1])
    return P
# Function for look up the value in the SBOX
def Lookup_S(R,n,SBOX):
    b1_b4 = [R[0],R[3]]
    b2_b3 = [R[1],R[2]]
    List = []
    row = int("".join(str(x) for x in b1_b4), 2)
    col = int("".join(str(x) for x in b2_b3), 2)
    if n == 0:
        value = S0[row][col]
    else:
        if SBOX == 0:
            value = S1[row][col]
        else:
            value = S_M[row][col]
    List = list(format(value,'02b'))
    return List
# Function for performing swaping
def swap(List):
    temp = []
    length = int(len(List)/2)
    for i in range(length,int(len(List))):
        temp.append(List[i])
    for i in range(0,length):
        temp.append(List[i])
    return temp
# Function for performing complex funtion(with key) after Initial permutation 
def Function(After_IP,KEY,SBOX):
    Left = left(After_IP)
    Right = right(After_IP)
    After_EP = E_permute(Right)
    EP_KEY = []
    for i in range(0,8):
        EP_KEY.append(After_EP[i]^KEY[i])
    R1 = left(EP_KEY)
    R2 = right(EP_KEY)
    R = Lookup_S(R1,0,SBOX)+Lookup_S(R2,1,SBOX)
    for i in range(0,len(R)):
        R[i] = int(R[i])
    After_P4 = permute_4(R)
    After_P4 = list(After_P4)
    L_P4 = []
    for j in range(0,4):
        L_P4.append(Left[j]^After_P4[j])
    round1 = L_P4 + Right
    return round1
# Program starts from here (taking plain text and key as input from user)
Text_input = input("Enter 8 bit Plain Text : ")
Key_input = input("Enter 10 bit Key : ")
#Storing the input in a List
for i in str(Text_input):
	Plain_Text.append(int(i))
for i in str(Key_input):
	Key.append(int(i))
# Asking the user to use Original Sbox or Modified Sbox	
SBOX = int(input('To use original S1 enter 0, enter any other key for modified S1\nYour Input:'))
if SBOX == 0:
    print("Original S1 is selected")
else:
    print("Modified S1 is selected")
# Key Generation
After_P10 = permute_10(Key)
LS1 = leftswift(After_P10,1)
K1 = permute_8(LS1)
LS2 = leftswift(LS1,2)
K2 = permute_8(LS2)
# Encryption
After_IP = initial_permute(Plain_Text) # IP(P)
round1 = Function(After_IP,K1,SBOX) # F(K1)[IP(P)]
round1_after_swap = swap(round1) # SW(FK1(IP(P)))
print("Result after SW operation while encrypting :",round1_after_swap)
Last = Function(round1_after_swap,K2,SBOX) # FK2(SW(FK1(IP(P))))
Cipher_Text = inverse_permute(Last) # Ciphertext = IP-1(FK2(SW(FK1(IP(P)))))
print("Cipher_Text :",Cipher_Text)
# Decryption
After_IP = initial_permute(Cipher_Text) # IP(C)
round1 = Function(After_IP,K2,SBOX) # F(K2)[IP(C)]
round1_after_swap = swap(round1) # SW(FK2(IP(C)))
print("Result after SW operation while decrypting :",round1_after_swap)
Last = Function(round1_after_swap,K1,SBOX) # FK1(SW(FK2(IP(P))))
Plain = inverse_permute(Last) # Plaintext = IP-1(FK1(SW(FK2(IP(P)))))
print("Plain_Text :",Plain)
# Program Ends
