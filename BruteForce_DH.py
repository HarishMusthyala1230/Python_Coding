
" Python program for performing brute force attack on Diffie-Hellman"

# Inputing public known values
q = int(input("Enter the value of q: "))
a = int(input("Enter the value of a: "))
Y_A = int(input("Enter the value of Y_A: "))
Y_B= int(input("Enter the value of Y_B: "))

# For calculating private key of A
for X in range(1,q):
    if pow(a,X)%q == Y_A:
        private_key = X
X_A = private_key
print("X_A: ",X_A)

# For calculating private key of B
for X in range(1,q):
    if pow(a,X)%q == Y_B:
        private_key = X
X_B = private_key
print("X_B: ",X_B)

# For calculating session Key
K_AB = pow(Y_B,X_A)%q
print("Shared session Key (K_AB): ",K_AB)

" Program Ends "
