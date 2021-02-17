import time 
# Function for finding P and Q
def PandQ(n):
    data = []
    for i in range(2, n):
        if n % i == 0:
            data.append(i)
    return data
# Function for finding Phi(N)
def PhiN(p,q):
    return (p-1)*(q-1)
# Function for calculating d
def Calculate_d(Phi_N,e):
    for i in range(Phi_N):
        if (e*i)%Phi_N == 1:
            d = i
            break;
    return d
# Taking the values of e,n,c input from the user
e = int(input("Enter the value of e: "))
N = int(input("Enter the value of N: "))
C = int(input("Enter the value of C: "))
print("************************* Attack 1 *************************")
attack1_start_time = time.process_time() # Start time for attack 1
PQ = PandQ(N) # Finding P and Q from N
print("The values of P & Q: ",PQ)
Phi_N = PhiN(PQ[0],PQ[1]) # Calculating Phi(N) from P and Q
d = Calculate_d(Phi_N,e) # Calculating d
print("The value of 'd': ",d)
m = 1
for i in range(1,d+1): # Modular expression calculation
    m = (C*m)%N
print("Plain_Text(M): ",m)
attack1_time = time.process_time() - attack1_start_time # End time for attack 1
print("Time taken for Attack_1: %10s seconds"%(attack1_time))
print("************************* Attack 2 *************************")
attack2_start_time = time.process_time() # Start time for attack 2
c = 1
for m in range(1,N+1): # possible values of M till the value matches
    c = 1
    for i in range(1,e+1): # Modular expression calculation
        c = (m * c)%N
    if c == C:
        print("Plain_Text(M): ",m)
        break
attack2_time = time.process_time() - attack2_start_time # End time for attack 2
print("Time taken for Attack_2: %10s seconds"%(attack2_time))
