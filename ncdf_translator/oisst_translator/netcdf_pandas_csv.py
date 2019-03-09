import os
import numpy as np
import netCDF4 
import csv
import pandas as pd


#navigating to folder location. You may have to change this.
base_dir = os.path.abspath(os.path.dirname( '//your oisst ncdf file here//'))

for file in os.listdir(base_dir):
    if file.endswith(".nc"):
        dataset = netCDF4.Dataset(base_dir+"/"+file)
        
        lat = dataset.variables['lat'][:]
        lon = dataset.variables['lon'][:]
        time_var = dataset.variables['time']
        zlev = dataset.variables['zlev']
        sst = dataset.variables['sst']
        anom  = dataset.variables['anom']
        err = dataset.variables['err']
        ice = dataset.variables['ice']

        df_lat = pd.DataFrame(data=lat[:])
        df_lat = pd.DataFrame(np.repeat(df_lat.values,1440,axis=0), columns={'lat'})   
        df_lon= pd.DataFrame(data=lon[:])
        df_lon = pd.DataFrame(np.repeat(df_lon.values,720,axis=0), columns={'lon'})
        df_time = pd.DataFrame(np.repeat([time_var[0]],1036800, axis=0), columns={'time'})
        df_zlev = pd.DataFrame(np.repeat([zlev[0]],1036800, axis=0), columns={'zlev'})
        base_df = pd.concat([df_time, df_zlev, df_lat, df_lon], axis=1)
        
        
        # Ice data
        # If you print the variable ice, you'll find: 
        #   int16 ice(time, zlev, lat, lon)
        #   ...
        #   current shape = (1, 1, 720, 1440)
        # base_df is of size 1036800 x 4 so we just have to append the ice values, preserving the order of the values
        raw_icedata = ice[0,0,:,:]
        df_ice = pd.DataFrame(data=np.ndarray.flatten(raw_icedata), columns={'ice'})
        df_ice = pd.concat([base_df, df_ice],axis=1)     
        
        
        # SST data
        # Same principle as Ice data
        raw_sstdata = sst[0,0,:,:]
        df_sst = pd.DataFrame(data=np.ndarray.flatten(raw_sstdata), columns={'sst'})
        df_sst = pd.concat([base_df, df_sst],axis=1)   
        
        # ANOM data
        # Same principle as Ice data
        raw_anomdata = anom[0,0,:,:]
        df_anom = pd.DataFrame(data=np.ndarray.flatten(raw_anomdata), columns={'anom'})
        df_anom = pd.concat([base_df, df_anom],axis=1)   
        
        # ERR data
        # Same principle as Ice data
        raw_errdata = err[0,0,:,:]
        df_err = pd.DataFrame(data=np.ndarray.flatten(raw_errdata), columns={'err'})
        df_err = pd.concat([base_df, df_err],axis=1)   


dataset.close()
        

df_ice.to_csv('ice_data.csv', line_terminator='\n', index=False, header=True)
df_err.to_csv('err_data.csv', line_terminator='\n', index=False, header=True)
df_sst.to_csv('sst_data.csv', line_terminator='\n', index=False, header=True)
df_anom.to_csv('anom_data.csv', line_terminator='\n', index=False, header=True)