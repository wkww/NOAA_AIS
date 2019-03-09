import os
from pandas import Series
import netCDF4 
import csv


#navigating to folder location. You may have to change this.
base_dir = os.path.abspath(os.path.dirname( __file__ ))

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

        # Ice data
        # If you print the variable ice, you'll find: 
        #   int16 ice(time, zlev, lat, lon)
        #   ...
        #   current shape = (1, 1, 720, 1440)
        # Thus, we insert time[0], zlev[0], lat[i] and lon[j] into our csv with the corresponding labels
        with open('ice_data.csv', mode='w') as ice_file:
            ice_writer = csv.writer(ice_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            ice_writer.writerow(['time', 'zlev', 'lat', 'lon', 'ice'])

            for i in range(0,720):
                print("row " , i+1, " of 720")
                for j in range(0,1440):
                    # print(time_var[0] , '\t', zlev[0], '\t', lat[600], '\t', lon[i],'\t', ice[0,0,600,i] )
                    ice_writer.writerow([time_var[0], zlev[0], lat[i], lon[j], ice[0,0,i,j]])
            ice_writer.close()

        # SST data
        # Same format as above
        with open('sst_data.csv', mode='w') as sst_file:
            sst_writer = csv.writer(sst_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            sst_writer.writerow(['time', 'zlev', 'lat', 'lon', 'sst'])

            for i in range(0,720):
                print("row " , i+1, " of 720")
                for j in range(0,1440):
                    sst_writer.writerow([time_var[0], zlev[0], lat[i], lon[j], sst[0,0,i,j]])
            sst_writer.close()

        # anom data
        # Same format as above
        with open('anom_data.csv', mode='w') as anom_file:
            anom_writer = csv.writer(anom_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            anom_writer.writerow(['time', 'zlev', 'lat', 'lon', 'anom'])

            for i in range(0,720):
                print("row " , i+1, " of 720")
                for j in range(0,1440):
                    anom_writer.writerow([time_var[0], zlev[0], lat[i], lon[j], anom[0,0,i,j]])
            anom_writer.close()

        # err data
        # Same format as above
        with open('err_data.csv', mode='w') as err_file:
            err_writer = csv.writer(err_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            err_writer.writerow(['time', 'zlev', 'lat', 'lon', 'err'])

            for i in range(0,720):
                print("row " , i+1, " of 720")
                for j in range(0,1440):
                    err_writer.writerow([time_var[0], zlev[0], lat[i], lon[j], err[0,0,i,j]])
            err_writer.close()

dataset.close()
        
