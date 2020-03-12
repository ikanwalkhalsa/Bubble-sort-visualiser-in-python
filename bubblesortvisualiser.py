'''Below is the Src of Second Video 
on my youtube Channel JUGAD PY 
Here i tried to build a basic bubble sort visualisation 
just under 3 Minutes'''

import os

#Function to Animate each Swap
def visualise(arr):
    os.system('cls')    #clears the screen so that output remains in single line
    print("Sorting......",arr)
    #adjust this range to coustomize the speed
    for _ in range(14300000):
        pass

'''Now we will create a basic bubble sort algo
with visualising at starting and after each swap done'''
def sortVisual(arr):
    #firt we will visualise the given array
    visualise(arr)
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                #here it visualises each swap
                visualise(arr)

#creating a dummy array to test the function
demoarr=[9,8,7,6,5,4,3,2,1]
sortVisual(demoarr)