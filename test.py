
import h5py
import numpy as np
import math
import matplotlib.pyplot as plt

g = h5py.File("./fieldComp.hdf", "r")
f = h5py.File("./plottable.hdf5", "w")
h = h5py.File("./intensity.hdf5", "r")

t = np.array(g["fieldAmp"])
d = np.array(h["Intensity"])

N = t.shape[0]

t = np.transpose(t,[2,1,0])*1e+14

print(t)
# s = t[N//2,N-10,:]

s = t[N-10,:,N//2]
p = d[N-10,:,N//2]

def k(x):
  y = abs(x-N//2)
  y = 1e17*math.exp(-2*(y/16)**4)
  return y

A = list(map(k, range(N)))

ax1 = plt.subplot(1,2,1)
# ax1.plot(range(N), t[:,N//2,:], label='matlab', marker="*",c='red')
ax12 = ax1.twinx()
ax12.plot(range(N), d[N//2,1,:], label='cuda', marker=".",c='blue')
# ax1.scatter(range(N), t[N//2,10,:], label='matlab', markersize=1)
# ax1.scatter(range(N), d[N//2,10,:], label='cuda', markersize=1)
# ax1.plot(range(N), A, label='truth')
# print(d[N//2,0,:])
# print(t[N//2,1,:])
# print(t[N//2,10,:],d[N//2,10,:])
# print(sum(np.abs(t[N//2,10,:]-d[N//2,10,:]))/N)
ax1.legend()
ax1.set_ylabel('Intensity')
ax1.set_xlabel('Zone')
ax1.set_title('Initial')
ax2 = plt.subplot(1,2,2)
# ax2.plot(range(N), s, label='matlab', marker="*", c='red')
ax22 = ax2.twinx()
ax22.plot(range(N), p, label='cuda', marker=".", c='blue')
ax2.legend()
ax2.set_ylabel('Intensity')
ax2.set_xlabel('Zone')
ax2.set_title('Post CBET')
plt.show()

# print(p)
#print(d[10,:,100])

f.create_dataset("X", data=h["X"])
f.create_dataset("Y", data=h["Y"])
f.create_dataset("Z", data=h["Z"])
f.create_dataset("Intensity", data=t)

