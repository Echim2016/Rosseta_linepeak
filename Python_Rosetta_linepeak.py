import numpy as np
import matplotlib.pyplot as plt

File=open("2015133_2015137_H216O.dat","r")

data=File.readlines()

fre=[]
vel=[]
bri=[]
dis=[]
PLone_abs=[]
PLone_emi=[]
PLvel=[]

fromindex=[38]
toindex=[313]
disindex=[14]
plt.figure(figsize=(16,9))
plt.title(r"$ H_2O\ Spectra $")
plt.xlabel(r"$ Sky\ Frequency\ (MHz) $")
plt.ylabel(r"$ Brightness\ Temperature\ (K) $")

"""
plt.title(r"$ H_2O\ Spectra $")
plt.xlabel(r"$ Distance  $")
plt.ylabel(r"$ Average\ Brightness\ Temperature\ (K) $")
"""

for i in range(0,41):
    fromindex.append(fromindex[i]+313)
    toindex.append(toindex[i]+313)
    disindex.append(disindex[i]+313)


#---Baseline---
PLvel[:]=[]
k=0
for i in range(0,1):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))

    markerline, stemlines, baseline = plt.stem(fre,bri,"-.")

plt.setp(markerline, "markerfacecolor", "b")
plt.setp(baseline,"color","r","linewidth",2)
#plt.savefig("BL_abs.png")
#plt.savefig("BL_emi.png")
plt.show()
    
    
    
"""
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLone_emi.append(max(bri))
        abri=np.array(bri)
        g=abri.tolist().index(max(bri))
        PLvel.append(float(vel[g]))
    
    else:
        PLone_abs.append(min(bri))
        abri=np.array(bri)
        g=abri.tolist().index(min(bri))
        PLvel.append(float(vel[g]))
"""
#plt.plot(dis,PLone_abs,label="Group of one")
#plt.plot(dis,PLvel,label="Group of one")
#plt.savefig("PL1_abs.png")
#plt.show()











"""

#---One---
PLvel[:]=[]
for i in range(0,20):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLone_emi.append(max(bri))
        abri=np.array(bri)
        g=abri.tolist().index(max(bri))
        PLvel.append(float(vel[g]))

    else:
        PLone_abs.append(min(bri))
        abri=np.array(bri)
        g=abri.tolist().index(min(bri))
        PLvel.append(float(vel[g]))

plt.plot(dis,PLone_abs,label="Group of one")
#plt.plot(dis,PLvel,label="Group of one")
#plt.savefig("PL1_abs.png")
plt.show()
"""


"""
#---Three---
PLvel[:]=[]
PLthree_abs,PLthree_absbri=[],[]
PLthree_emi,PLthree_emibri=[],[]
PLvel[:]=[]

dis[:]=[]
for i in range(0,20):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLthree_emi[:]=[]
        for k in range(0,91):
            PLthree_emi.append(float((bri[3*k]+bri[3*k+1]+bri[3*k+2])/3))
        PLthree_emi.append(float((bri[273]+bri[274])/2))
        PLthree_emibri.append(float(max(PLthree_emi)))
        abri=np.array(bri)
        g=abri.tolist().index(max(bri))
        PLvel.append(float(vel[g]))
    else:
        PLthree_abs[:]=[]
        for k in range(0,91):
            PLthree_abs.append(float((bri[3*k]+bri[3*k+1]+bri[3*k+2])/3))
        PLthree_abs.append(float((bri[273]+bri[274])/2))
        PLthree_absbri.append(float(min(PLthree_abs)))
        abri=np.array(bri)
        g=abri.tolist().index(min(bri))
        PLvel.append(float(vel[g]))

plt.plot(dis,PLthree_absbri,label="Group of three")
#plt.plot(dis,PLvel,label="Group of three")
#plt.savefig("PL3_abs.png")
plt.show()
"""

"""

#---Five---

PLfive_abs,PLfive_absbri=[],[]
PLfive_emi,PLfive_emibri=[],[]

dis[:]=[]
for i in range(0,20):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLfive_emi[:]=[]
        for k in range(0,55):
            PLfive_emi.append(float((bri[5*k]+bri[5*k+1]+bri[5*k+2]+bri[5*k+3]+bri[5*k+4])/5))
        PLfive_emibri.append(float(max(PLfive_emi)))
    else:
        PLfive_abs[:]=[]
        for k in range(0,55):
            PLfive_abs.append(float((bri[5*k]+bri[5*k+1]+bri[5*k+2]+bri[5*k+3]+bri[5*k+4])/5))
        PLfive_absbri.append(float(min(PLfive_abs)))


plt.plot(dis,PLfive_absbri,label="Group of five")
#plt.savefig("PL5_abs.png")
#plt.show()



#---Eight---

PLeight_abs,PLeight_absbri=[],[]
PLeight_emi,PLeight_emibri=[],[]

dis[:]=[]
for i in range(0,20):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))

    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLeight_emi[:]=[]
        for k in range(0,34):
            PLeight_emi.append(float((bri[8*k]+bri[8*k+1]+bri[8*k+2]+bri[8*k+3]+bri[8*k+4]+bri[8*k+5]+bri[8*k+6]+bri[8*k+7])/8))
        PLeight_emi.append(float((bri[272]+bri[273]+bri[274])/3))
        PLeight_emibri.append(float(max(PLeight_emi)))
    else:
        PLeight_abs[:]=[]
        for k in range(0,34):
            PLeight_abs.append(float((bri[8*k]+bri[8*k+1]+bri[8*k+2]+bri[8*k+3]+bri[8*k+4]+bri[8*k+5]+bri[8*k+6]+bri[8*k+7])/8))
        PLeight_abs.append(float((bri[272]+bri[273]+bri[274])/3))
        PLeight_absbri.append(float(min(PLeight_abs)))

plt.plot(dis,PLeight_absbri,label="Group of eight")
#plt.savefig("PL8_abs.png")
#plt.legend(loc=3)
#plt.savefig("PL1358_abs.png")
#plt.show()
"""

"""
#---3points---
PLvel[:]=[]
PLone_abs[:]=[]
PLone_emi[:]=[]
dis[:]=[]
for i in range(0,20):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))

    if np.average(bri[0:100])<np.average(bri[100:275]):
        tempbri=bri
        maxlist=[]
        for i in range(3):
            max1=max(tempbri)
            maxlist.append(max1)
            tempbri.remove(max1)

        PLone_emi.append(np.average(maxlist))
        abri=np.array(bri)
        g=abri.tolist().index(max(bri))
        PLvel.append(float(vel[g]))

    else:
        tempbri=bri
        minlist=[]
        for i in range(3):
            min1=min(tempbri)
            minlist.append(min1)
            tempbri.remove(min1)

        PLone_abs.append(np.average(minlist))
        abri=np.array(bri)
        g=abri.tolist().index(min(bri))
        PLvel.append(float(vel[g]))

plt.plot(dis,PLone_abs,"k",lw=2,label="3-points")
#plt.plot(dis,PLvel,label="3-points")
#plt.savefig("PL1_3points_abs.png")
plt.show()
"""

"""

#---5points---


PLone_abs[:]=[]
PLone_emi[:]=[]
dis[:]=[]
for i in range(0,20):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        tempbri=bri
        maxlist=[]
        for i in range(5):
            max1=max(tempbri)
            maxlist.append(max1)
            tempbri.remove(max1)
        
        PLone_emi.append(np.average(maxlist))

    else:
        tempbri=bri
        minlist=[]
        for i in range(5):
            min1=min(tempbri)
            minlist.append(min1)
            tempbri.remove(min1)

        PLone_abs.append(np.average(minlist))

plt.plot(dis,PLone_abs,"y",lw=2,label="5-points")
#plt.savefig("PL1_5points_abs.png")
#plt.legend(loc=3)
#plt.savefig("PLall_abs.png")
plt.show()

"""



"""

#emi---One---
for i in range(21,41):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLone_emi.append(max(bri))
    else:
        PLone_abs.append(min(bri))


plt.plot(dis,PLone_emi,label="Group of one")
#plt.savefig("PL1_emi.png")
#plt.show()



#---Three---

PLthree_abs,PLthree_absbri=[],[]
PLthree_emi,PLthree_emibri=[],[]
    
dis[:]=[]
for i in range(21,41):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLthree_emi[:]=[]
        for k in range(0,91):
            PLthree_emi.append(float((bri[3*k]+bri[3*k+1]+bri[3*k+2])/3))
        PLthree_emi.append(float((bri[273]+bri[274])/2))
        PLthree_emibri.append(float(max(PLthree_emi)))
    else:
        PLthree_abs[:]=[]
        for k in range(0,91):
            PLthree_abs.append(float((bri[3*k]+bri[3*k+1]+bri[3*k+2])/3))
        PLthree_abs.append(float((bri[273]+bri[274])/2))
        PLthree_absbri.append(float(min(PLthree_abs)))
    
plt.plot(dis,PLthree_emibri,label="Group of three")
#plt.savefig("PL3_emi.png")
#plt.show()




#---Five---
    
PLfive_abs,PLfive_absbri=[],[]
PLfive_emi,PLfive_emibri=[],[]
    
dis[:]=[]
for i in range(21,41):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLfive_emi[:]=[]
        for k in range(0,55):
            PLfive_emi.append(float((bri[5*k]+bri[5*k+1]+bri[5*k+2]+bri[5*k+3]+bri[5*k+4])/5))
        PLfive_emibri.append(float(max(PLfive_emi)))
    else:
        PLfive_abs[:]=[]
        for k in range(0,55):
            PLfive_abs.append(float((bri[5*k]+bri[5*k+1]+bri[5*k+2]+bri[5*k+3]+bri[5*k+4])/5))
        PLfive_absbri.append(float(min(PLfive_abs)))

plt.plot(dis,PLfive_emibri,label="Group of five")
#plt.savefig("PL5_emi.png")
#plt.show()



#---Eight---
    
PLeight_abs,PLeight_absbri=[],[]
PLeight_emi,PLeight_emibri=[],[]
    
dis[:]=[]
for i in range(21,41):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        PLeight_emi[:]=[]
        for k in range(0,34):
            PLeight_emi.append(float((bri[8*k]+bri[8*k+1]+bri[8*k+2]+bri[8*k+3]+bri[8*k+4]+bri[8*k+5]+bri[8*k+6]+bri[8*k+7])/8))
        PLeight_emi.append(float((bri[272]+bri[273]+bri[274])/3))
        PLeight_emibri.append(float(max(PLeight_emi)))
    else:
        PLeight_abs[:]=[]
        for k in range(0,34):
            PLeight_abs.append(float((bri[8*k]+bri[8*k+1]+bri[8*k+2]+bri[8*k+3]+bri[8*k+4]+bri[8*k+5]+bri[8*k+6]+bri[8*k+7])/8))
        PLeight_abs.append(float((bri[272]+bri[273]+bri[274])/3))
        PLeight_absbri.append(float(min(PLeight_abs)))

plt.plot(dis,PLeight_emibri,label="Group of eight")
#plt.savefig("PL8_emi.png")
#plt.legend(loc=1)
#plt.savefig("PL1358_emi.png")
#plt.show()


#---3points---
    
PLone_abs[:]=[]
PLone_emi[:]=[]
dis[:]=[]
for i in range(21,41):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))
    
    if np.average(bri[0:100])<np.average(bri[100:275]):
        tempbri=bri
        maxlist=[]
        for i in range(3):
            max1=max(tempbri)
            maxlist.append(max1)
            tempbri.remove(max1)
    
        PLone_emi.append(np.average(maxlist))
    
    else:
        tempbri=bri
        minlist=[]
        for i in range(3):
            min1=min(tempbri)
            minlist.append(min1)
            tempbri.remove(min1)
    
        PLone_abs.append(np.average(minlist))
    
    
plt.plot(dis,PLone_emi,lw=2,label="3-points")
#plt.savefig("PL1_3points_emi.png")
#plt.show()


#---5points---

PLone_abs[:]=[]
PLone_emi[:]=[]
dis[:]=[]
for i in range(21,41):
    fre[:]=[]
    vel[:]=[]
    bri[:]=[]
    dis.append(float(data[disindex[i]].split("=")[1]))
    for j in range(fromindex[i],toindex[i]):
        fre.append(float((data[j].split()[0])))
        vel.append(float((data[j].split()[1])))
        bri.append(float((data[j].split()[2])))

    if np.average(bri[0:100])<np.average(bri[100:275]):
        tempbri=bri
        maxlist=[]
        for i in range(5):
            max1=max(tempbri)
            maxlist.append(max1)
            tempbri.remove(max1)
        
        PLone_emi.append(np.average(maxlist))

    else:
        tempbri=bri
        minlist=[]
        for i in range(5):
            min1=min(tempbri)
            minlist.append(min1)
            tempbri.remove(min1)

        PLone_abs.append(np.average(minlist))


plt.plot(dis,PLone_emi,lw=2,label="5-points")
#plt.savefig("PL1_5points_emi.png")
#plt.legend(loc=1)
#plt.savefig("PLall_emi.png")
#plt.show()

"""