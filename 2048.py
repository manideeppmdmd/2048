import random
arr =[[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
#arr1 =[[0,1,2,3],[0,1,2,3],[0,1,2,3],[0,1,2,3]]
list=[0,1,2,3]
arr[random.choice(list)][random.choice(list)]=2

def usermove(arr,move):
    if move=="u":
        i=0
        for j in range(0,4):
            if arr[i][j]!=0 or arr[i+1][j]!=0 or arr[i+2][j]!=0 or arr[i+3][j]!=0:
                if arr[i][j]==0:
                    while arr[i][j]==0:
                        arr[i][j]=arr[i+1][j]
                        arr[i+1][j]=arr[i+2][j]
                        arr[i+2][j]=arr[i+3][j]
                        arr[i+3][j]=0
                if arr[i+1][j]==0 and (arr[i+2][j]!=0 or arr[i+3][j!=0]):
                    while arr[i+1][j]==0:
                        arr[i+1][j]=arr[i+2][j]
                        arr[i+2][j]=arr[i+3][j]
                        arr[i+3][j]=0
                if arr[i+2][j]==0 and arr[i+3][j]!=0:
                    while arr[i+2][j]:
                        arr[i+2][j]=arr[i+3][j]
                        arr[i+3][j]=0 

        i=0
        for j in range(0,4):
            if arr[i][j]==arr[i+1][j]:
                arr[i][j]=arr[i][j]+arr[i+1][j]
                arr[i+1][j]=arr[i+2][j]
                arr[i+2][j]=arr[i+3][j]
                arr[i+3][j]=0
            if arr[i+1][j]==arr[i+2][j]:
                arr[i+1][j]=arr[i+1][j]+arr[i+2][j]
                arr[i+2][j]=arr[i+3][j]
                arr[i+3][j]=0
            if arr[i+2][j]==arr[i+3][j]:
                arr[i+2][j]=arr[i+2][j]+arr[i+3][j]
                arr[i+3][j]=0
       

    elif move=="d":
        i=0
        for j in range(0,4):
            if arr[i][j]!=0 or arr[i+1][j]!=0 or arr[i+2][j]!=0 or arr[i+3][j]!=0:
                if arr[i+3][j]==0:
                    while arr[i+3][j]==0:
                        arr[i+3][j]=arr[i+2][j]
                        arr[i+2][j]=arr[i+1][j]
                        arr[i+1][j]=arr[i][j]
                        arr[i][j]=0       
                if arr[i+2][j]==0 and (arr[i+1][j]!=0 or arr[i][j]!=0):
                    while arr[i+2][j]==0:
                        arr[i+2][j]=arr[i+1][j]
                        arr[i+1][j]=arr[i][j]
                        arr[i][j]=0  
                if arr[i+1][j]==0 and arr[i][j]!=0:
                    while arr[i+1][j]==0:
                        arr[i+1][j]=arr[i][j]
                        arr[i][j]=0  
                       
        i=0
        for j in range(0,4):
            if arr[i+3][j]==arr[i+2][j]:
                arr[i+3][j]=arr[i+3][j]+arr[i+2][j]
                arr[i+2][j]=arr[i+1][j]
                arr[i+1][j]=arr[i][j]
                arr[i][j]=0
            if arr[i+2][j]==arr[i+1][j]:
                arr[i+2][j]=arr[i+2][j]+arr[i+1][j]
                arr[i+1][j]=arr[i][j]
                arr[i][j]=0
            if arr[i+1][j]==arr[i][j]:
                arr[i+1][j]=arr[i+1][j]+arr[i][j]
                arr[i][j]=0
    

    elif move=="l":
        j=0
        for i in range(0,4):
            if arr[i][j]!=0 or arr[i][j+1]!=0 or arr[i][j+2]!=0 or arr[i][j+3]!=0:
                if arr[i][j]==0:
                    while arr[i][j]==0:
                        arr[i][j]=arr[i][j+1]
                        arr[i][j+1]=arr[i][j+2]
                        arr[i][j+2]=arr[i][j+3]
                        arr[i][j+3]=0       
                if arr[i][j+1]==0 and (arr[i][j+2]!=0 or arr[i][j+3]!=0):
                    while arr[i][j+1]==0:
                        arr[i][j+1]=arr[i][j+2]
                        arr[i][j+2]=arr[i][j+3]
                        arr[i][j+3]=0 
                if arr[i][j+2]==0 and arr[i][j+3]!=0:
                    while arr[i][j+2]==0:
                       arr[i][j+2]=arr[i][j+3]
                       arr[i][j+3]=0 

        j=0
        for i in range(0,4):
            if arr[i][j]==arr[i][j+1]:
                arr[i][j]=arr[i][j]+arr[i][j+1]
                arr[i][j+1]=arr[i][j+2]
                arr[i][j+2]=arr[i][j+3]
                arr[i][j+3]=0
            if arr[i][j+1]==arr[i][j+2]:
                arr[i][j+1]=arr[i][j+1]+arr[i][j+2]
                arr[i][j+2]=arr[i][j+3]
                arr[i][j+3]=0
            if arr[i][j+2]==arr[i][j+3]:
                arr[i][j+2]= arr[i][j+2]+arr[i][j+3]
                arr[i][j+3]=0

    elif move=="r":
        j=0
        for i in range(0,4):
            if arr[i][j]!=0 or arr[i][j+1]!=0 or arr[i][j+2]!=0 or arr[i][j+3]!=0:
                if arr[i][j+3]==0:
                    while arr[i][j+3]==0:
                        arr[i][j+3]=arr[i][j+2]
                        arr[i][j+2]=arr[i][j+1]
                        arr[i][j+1]=arr[i][j]
                        arr[i][j]=0       
                if arr[i][j+2]==0 and (arr[i][j+1]!=0 or arr[i][j]!=0):
                    while arr[i][j+2]==0:
                        arr[i][j+2]=arr[i][j+1]
                        arr[i][j+1]=arr[i][j]
                        arr[i][j]=0  
                if arr[i][j+1]==0 and arr[i][j]!=0:
                    while arr[i][j+1]==0:
                        arr[i][j+1]=arr[i][j]
                        arr[i][j]=0

        j=0
        for i in range(0,4):
            if arr[i][j+3]==arr[i][j+2]:
                arr[i][j+3]=arr[i][j+3]+arr[i][j+2]
                arr[i][j+2]=arr[i][j+1]
                arr[i][j+1]=arr[i][j]
                arr[i][j]=0
            if arr[i][j+2]==arr[i][j+1]:
                arr[i][j+2]=arr[i][j+2]+arr[i][j+1]
                arr[i][j+1]=arr[i][j]
                arr[i][j]=0
            if arr[i][j+1]==arr[i][j]:
                arr[i][j+1]= arr[i][j+1]+arr[i][j]
                arr[i][j]=0

while True:
    print(arr[0][0],"\t",arr[0][1],"\t",arr[0][2],"\t",arr[0][3],"\t")
    print(arr[1][0],"\t",arr[1][1],"\t",arr[1][2],"\t",arr[1][3],"\t")
    print(arr[2][0],"\t",arr[2][1],"\t",arr[2][2],"\t",arr[2][3],"\t") 
    print(arr[3][0],"\t",arr[3][1],"\t",arr[3][2],"\t",arr[3][3],"\t")
    move= input("enter your move:")
    print(arr[1][3])
    usermove(arr,move)
    listfori=[]
    listforj=[]
    count = 0
    for i in range(0,4):
        for j in range(0,4):
            arr[i][j]=8
    for i in range(0,4):
        for j in range(0,4):
            if arr[i][j]==0:
                count+=1
                listfori.append(i)
                listforj.append(j)
    if count > 0:
        if count >1:
            randomindex= listfori.index(random.choice(listfori))
            arr[listfori[randomindex]][listforj[randomindex]]=2
        else:
            arr[listfori[0]][listforj[0]]=2
    else:
        break
print("Game Over")
   






                                




