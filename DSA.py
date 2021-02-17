
" Python program for DSA algorithm "
# Inputing the required values
p = int(input("Enter the large prime value - p: "))
q = int(input("Enter the prime factor value - q: "))
h = int(input("Enter the value - h: "))
x = int(input("Enter the private key value - x: "))
k = int(input("Enter the secret number value - k: "))
H_M1 = int(input("Enter the real hash value of Message- H(M1): "))

# Function for calculating inverse
def inverse(a,q):
    for i in range(1,q):
        if ((a*i)%q) == 1:
            inv = i
    return inv
x = int((p-1)/q)
g = (pow(h,x))%p
y = pow(g,x)%p # public key calculation
print("g = ",g,"\ny = ",y)
# Function for signature verification
def verify(v,r):
    if v == r:
        print("Signature is verified")
    else:
        print("Signature is not verified")
# Signature pair computation
r = (pow(g,k)%p)%q
s = (inverse(k,q)*(H_M1+(x*r)))%q
print("Signature Pair (r,s): (%s,%s)" %(r,s))
print("verifying the signature for H(M1)")
# verifying signature for H(M1)
w = inverse(s,q)%q
u_1 = (H_M1*w)%q
u_2 = (r*w)%q
v = ((pow(g,u_1)*pow(y,u_2))%p)%q
print("w = ",w,"\nu_1 = ",u_1,"\nu_2 = ",u_2,"\nv = ",v)
verify(v,r) # calling function for verifying signature
print("verifying the signature for H(M2)")
H_M2 = int(input("Enter the fake hash value of Message - H(M2): "))
# verifying signature for H(M2)
w = inverse(s,q)%q
u_1 = (H_M2*w)%q
u_2 = (r*w)%q
v = ((pow(g,u_1)*pow(y,u_2))%p)%q
print("w = ",w,"\nu_1 = ",u_1,"\nu_2 = ",u_2,"\nv = ",v)
verify(v,r) # calling function for verifying signature
# Program Ends

