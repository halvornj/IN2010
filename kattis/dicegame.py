gunnar = list(map(int, input().strip().split()))
emma = list(map(int, input().strip().split()))

gscore = ((gunnar[0]+gunnar[1])/2)+((gunnar[2]+gunnar[3])/2)
escore = ((emma[0]+emma[1])/2) + ((emma[2]+emma[3])/2)

if gscore > escore: print("Gunnar")
elif escore > gscore:print("Emma")
else:print("Tie")