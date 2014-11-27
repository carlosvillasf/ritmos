# -*- coding: utf-8 -*-
"""
Created on Thu Nov 20 13:08:40 2014

@author: eduardo
"""
import h5py
import numpy as np
import matplotlib.pyplot as plt
import csv
import matplotlib,os
matplotlib.rcParams['backend'] = "Qt4Agg"


class ecg:
    def __init__(self):
        ecg.fdb = ""       
    def creategroup(self,FILE,GROUP):
        print(GROUP)           
        with h5py.File(FILE, 'r+') as f:
            print(f.require_group(GROUP))
            #grp = f.create_group(GROUP)
        # Re-open the group, obtaining a new handle.
        #grp = f[GROUP]        
            
    def readdata(self,dfile,group):
        f = h5py.File(dfile,"r")
        dat = f['/'+group]
        for item in dat.attrs.keys():
            print(item + ":", dat.attrs[item])
        
    def savedata(self,dfile,group,record,data):
        # Open an existing file using defaut properties.
        file = h5py.File(dfile,'r+')
        # Open "group" dataset.
        dataset = file['/'+group]
        for name in record.keys():
            print(name),record[name]
            dataset.attrs.create(name,record[name],(len(record[name]),),'f')
        for i in range(len(data[0])):
            print(data[0][i],data[1][i])
            dataset.attrs.create(data[0][i],data[1][i])
        # Create string attribute.        
#        attr_string = "Meter per second"        
#        dataset.attrs["Units"] = attr_string
#        # Create integer array attribute.
#        attr_data = np.zeros((2))
#        attr_data[0] = 100
#        attr_data[1] = 200
        #dataset.attrs.create("Speed", attr_data, (2,), h5py.h5t.STD_I32BE)        
        #dataset.attrs.create(,record[1][0] ,(2,), h5py.h5t.STD_I32BE)
        file.close()

    def readecg(self,fecg):
#        sdata = []        
        with open(fecg, 'rb') as data_file:#,newline='\n'
            data_reader = csv.reader(data_file)            
            for j, row in enumerate(data_reader):
                if j == 0:
                    names = [name.strip('\'') for name in row]
#                    sdata.append(names)
                    data = {str(name): list() for name in names}
#                    print(names)                    
                elif j > 1:
                    for k in range(len(row)):                                              
                        data[names[k]].append(float(row[k]))
#                    sdata.append(data) 
                    if(j>7):
                        #print(data[names[0]])
                        return data
        time = np.asarray(data[names[0]])
        return sdata

    def getregis(self,rdir):
        for filename in os.listdir(rdir):
            #print(filename)
            data = [[],[]]
            if(os.path.isfile(rdir+"/"+filename)):                 
                reg = filename.split("_") 
                print(reg)
                print(len(reg),reg[0],reg[2],reg[3],reg[4].replace(".csv",""))
                dat= self.readecg(rdir+"/"+filename)
                reg[0] = reg[0].replace("re","")
                data[0].append('sex')
                data[1].append(reg[2])
                data[0].append('age')
                data[1].append(str(reg[3]))                
                data[0].append("type")
                data[1].append(reg[4].replace(".csv",""))
                ec.creategroup("dset.h5",reg[1])                              
                ec.creategroup("dset.h5",str(reg[1]+'/'+reg[0]))
                self.savedata("dset.h5",str(reg[1]+'/'+reg[0]),dat,data)
                                                            

if __name__=="__main__":
    ec = ecg()
    file = h5py.File('dset.h5','w')
    #dat = ec.readecg("data.csv")
    ecg.fdb = "dset.h5"
    #ec.creategroup("dset.h5","ot")
    #ec.savedata("dset.h5","ot",dat)
    #ec.readdata(ecg.fdb,"Healthy-control/s0291lre")
    ec.getregis("cvs")