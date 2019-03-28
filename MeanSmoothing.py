import numpy as np

def meanSmooth(time, nparray, nsmooth):#get odd (eg. 3, 5 smoothing factor)
    out = []
    n = int((nsmooth + 1)/ 2)
    t = []
    for i, val in enumerate(nparray):
      if i > 0 and i < len(nparray) - 2:
        mean = 0
        for k in range(-n + 1, n): #in 3 smooting goes from -1 to 1
            ind = i + k
            mean += nparray[ind]
        mean /= nsmooth
        out.append(mean)
        t.append(time[i])
    return np.array(t), np.array(out)

def meanSmthIt(time, nparray, nsmooth, iterations):
    smtht = time
    smth = nparray
    for i in range(0, iterations):
        smtht, smth = meanSmooth(smtht, smth, nsmooth)
    return smtht, smth