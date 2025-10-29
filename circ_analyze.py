import pickle
import matplotlib.pyplot as plt
import numpy as np
# load result file
fname = './TMP/mydata_144_12_p_0.001_cycles_12'
with open(fname, 'rb') as fp:
	mydata = pickle.load(fp)

# print result
print(np.array(mydata['HdecX']).shape)
print(np.array(mydata['HdecZ']).shape)

print(np.array(mydata["probX"]))
print(np.array(mydata["probZ"]))

plt.figure()
plt.plot(np.arange(len(mydata["probX"])), np.array(mydata["probX"]))
plt.xlabel('Index')
plt.ylabel('probX value')
plt.title('probX values by index')
plt.show()

plt.figure()
plt.plot(np.arange(len(mydata["probZ"])), np.array(mydata["probZ"]))
plt.xlabel('Index')
plt.ylabel('probZ value')
plt.title('probZ values by index')
plt.show()

# plt.hist(np.array(mydata["probX"]).transpose()s, bins=100)
# # plt.xlim(0, 0.01)
# plt.show()
# plt.hist(np.array(mydata["probZ"]).transpose(), bins=100)
# # plt.xlim(0, 0.01)
# plt.show()

print(np.max(np.array(mydata["probX"])))
print(np.max(np.array(mydata["probZ"])))