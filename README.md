# NOAA_AIS
##### Basic Python 3 toolkit for working with NOAA AIS, ICOADS, OISST and NETCDF4 Data in general. Since we have entered an era where the federal budget means that this data may go offline for extended periods, bulk download scripts have been included. 
#### Download Scripts
Since this is an I/O Bound activity, we can make use of  multi threading to speed up the process. Pool size is set at 4 but can be increased to whatever you like. 
ais.py, icoads.py and oisst.py use HTML parsing to return a series of links. Adjust parameters in the files to choose what range of files you would like to download. 
Run download_{type}.py to begin downloading the files. 
#### AIS Filter 
Simple script to filter AIS Data. Adjust accordingly to filter by column name and value such as Vessel Name, Vessel Type, etc. 
#### NETCDF4 Translator
Script to convert NETCDF4 to CSV which may be neccesary if want to utilize legacy database injection scripts.
#### Visualization
Uses Jupyter Notebooks and Plotly to visualize Some of the NOAA data. The example notebook visualizes sea surface temperatures (SST) 
