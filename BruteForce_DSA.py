" Python program for performing bruteforce attack on DSA"

# Function for calculating inverse
def inverse(a,q):
    for i in range(1,q):
        if ((a*i)%q) == 1:
            inv = i
    return inv

# Inputing global public values (p,q,g)
p = int(input("Enter the value of p: "))
q = int(input("Enter the value of q: "))
g = int(input("Enter the value of g: "))
r = int(input("Enter the value of r: "))
s = int(input("Enter the value of s: "))
H_M = int(input("Enter the value of H(M): "))

# For finding secret key number(k)
for i in range(1,q):
    if r == (pow(g,i)%p)%q:
          k = i
print("Secret key(k): ",k)

# For finding private key(x)
for n in range(1,q):
    if s == (inverse(k,q)*(H_M+(n*r)))%q:
          x = n
print("private Key(x): ",x)






























