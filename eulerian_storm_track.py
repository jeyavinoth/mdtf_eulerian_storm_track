# Code created by Jeyavinoth Jeyaratnam, to be implemented in MDTF 

# Import standarad Python packages 
import numpy as np 
from netCDF4 import Dataset
import os
import glob

# Import my code from the current folder
import eulerian_storm_track_util as est
import plotter # do not need this, just debugging purpose

# Setting up the necessary variable names
os.environ['v850_file'] = '*.'+os.environ['v850_var']+'.day.nc'

# Model output filename convection
os.environ['MODEL_OUTPUT_DIR'] = os.environ['DATADIR']+'/day'

missing_file = 0
if (len(glob.glob(os.environ['MODEL_OUTPUT_DIR']+'/'+os.environ['v850_file']))==0):
  print('Required V850 file missing!')
  missing_file = 1

if (missing_file == 1):
  print('Eulerian Strom Tracker will NOT be executed!')
else:
  ##########################################################
  # Create the necessary directories
  ##########################################################

  print ('####################### JJJ ##################\n\n')

  if not os.path.exists(os.environ['variab_dir']+'/eulerian_storm_track/'):
    os.makedirs(os.environ['variab_dir']+'/eulerian_storm_track/')
  if not os.path.exists(os.environ['variab_dir']+'/eulerian_storm_track/model'):
    os.makedirs(os.environ['variab_dir']+'/eulerian_storm_track/model')
  if not os.path.exists(os.environ['variab_dir']+'/eulerian_storm_track/model/netCDF'):
    os.makedirs(os.environ['variab_dir']+'/eulerian_storm_track/model/netCDF')
  if not os.path.exists(os.environ['variab_dir']+'/eulerian_storm_track/model/PS'):
    os.makedirs(os.environ['variab_dir']+'/eulerian_storm_track/model/PS')
  if not os.path.exists(os.environ['variab_dir']+'/eulerian_storm_track/obs'):
    os.makedirs(os.environ['variab_dir']+'/eulerian_storm_track/obs')
  if not os.path.exists(os.environ['variab_dir']+'/eulerian_storm_track/obs/netCDF'):
    os.makedirs(os.environ['variab_dir']+'/eulerian_storm_track/obs/netCDF')
  if not os.path.exists(os.environ['variab_dir']+'/eulerian_storm_track/obs/PS'):
    os.makedirs(os.environ['variab_dir']+'/eulerian_storm_track/obs/PS')
  
  ##########################################################
  # Reading in the necessary data 
  ##########################################################

  netcdf_filename = os.environ['MODEL_OUTPUT_DIR']+'/'+os.environ['CASENAME']+'.'+os.environ['v850_var']+'.day.nc'
  if (not os.path.exists(netcdf_filename)):
    print ('Cannot Find File: ', netcdf_filename)

  # reading in the model data
  ncid = Dataset(netcdf_filename, 'r')
  lat = ncid.variables[os.environ['lat_var']][:]
  lat.fill_value = np.nan
  lat = lat.filled()
  lon = ncid.variables[os.environ['lon_var']][:]
  lon.fill_value = np.nan
  lon = lon.filled()
  time = ncid.variables[os.environ['time_var']][:]
  time.fill_value = np.nan
  time = time.filled()
  v850 = ncid.variables[os.environ['v850_var']][:]
  v850.fill_value = np.nan
  v850 = v850.filled()
  ncid.close()

  # creating the lat and lon in grid format
  lonGrid, latGrid = np.meshgrid(lon, lat)

  # getting the daily difference X(t+1) - X(t)
  diff = est.daily_diff(v850)

  # # getting the all year standard deviation average
  # season = 'all'
  # time_ind = est.get_time_ind(int(os.environ['FIRSTYR']), time, season=season)
  # std_dev = est.std_dev(diff, time_ind)
  # out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season)
  # plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  # out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season)
  # plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')

  season = 'djf'
  time_ind = est.get_time_ind(int(os.environ['FIRSTYR']), time, season=season)
  std_dev = est.std_dev(diff, time_ind)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  
  season = 'jja'
  time_ind = est.get_time_ind(int(os.environ['FIRSTYR']), time, season=season)
  std_dev = est.std_dev(diff, time_ind)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  
  season = 'son'
  time_ind = est.get_time_ind(int(os.environ['FIRSTYR']), time, season=season)
  std_dev = est.std_dev(diff, time_ind)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  
  season = 'mam'
  time_ind = est.get_time_ind(int(os.environ['FIRSTYR']), time, season=season)
  std_dev = est.std_dev(diff, time_ind)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season)
  plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,11), extend='max')

  ##########################################################
  # Running the tracker for the different seasons
  ##########################################################

  time_ind = est.get_time_ind
  
  ##########################################################
  # Creating the plots for the different seasons
  ##########################################################
  # Copy template html (and delete old html if necessary)
  if os.path.isfile( os.environ["variab_dir"]+"/eulerian_storm_track/eulerian_storm_track.html" ):
      os.system("rm -f "+os.environ["variab_dir"]+"/eulerian_storm_track/eulerian_storm_track.html")

  os.system("cp "+os.environ["VARCODE"]+"/eulerian_storm_track/eulerian_storm_track.html "+os.environ["variab_dir"]+"/eulerian_storm_track/.")
  os.system("cp "+os.environ["VARCODE"]+"/eulerian_storm_track/MDTF_Documentation_eulerian_storm_track.pdf "+os.environ["variab_dir"]+"/eulerian_storm_track/.")

  # Replace CASENAME so that the figures are correctly linked through the html
  os.system("cp "+os.environ["variab_dir"]+"/eulerian_storm_track/eulerian_storm_track.html "+os.environ["variab_dir"]+"/eulerian_storm_track/tmp.html")
  os.system("cat "+os.environ["variab_dir"]+"/eulerian_storm_track/eulerian_storm_track.html "+"| sed -e s/casename/"+os.environ["CASENAME"]+"/g > "+os.environ["variab_dir"]+"/eulerian_storm_track/tmp.html")
  os.system("cp "+os.environ["variab_dir"]+"/eulerian_storm_track/tmp.html "+os.environ["variab_dir"]+"/eulerian_storm_track/eulerian_storm_track.html")
  os.system("rm -f "+os.environ["variab_dir"]+"/eulerian_storm_track/tmp.html")

  a = os.system("cat "+os.environ["variab_dir"]+"/index.html | grep eulerian_storm_track")
  if a != 0:
     os.system("echo '<H3><font color=navy>Eulerian Strom Track Diagnostics <A HREF=\"eulerian_storm_track/eulerian_storm_track.html\">plots</A></H3>' >> "+os.environ["variab_dir"]+"/index.html")

  # ### Commnet this section out, because I am plotting and saving the figures already in PNG format
  # # Convert PS to png
  # if os.path.exists(os.environ["variab_dir"]+"/eulerian_storm_track/model"):
  #     files = os.listdir(os.environ["variab_dir"]+"/eulerian_storm_track/model/PS")
  #     a = 0
  #     while a < len(files):
  #         file1 = os.environ["variab_dir"]+"/eulerian_storm_track/model/PS/"+files[a]
  #         file2 = os.environ["variab_dir"]+"/eulerian_storm_track/model/"+files[a]
  #         os.system("convert -crop 0x0+5+5 "+file1+" "+file2[:-3]+".png")
  #         a = a+1
  #     if os.environ["CLEAN"] == "1":
  #         os.system("rm -rf "+os.environ["variab_dir"]+"/eulerian_storm_track/model/PS")
  # if os.path.exists(os.environ["variab_dir"]+"/eulerian_storm_track/obs"):
  #     files = os.listdir(os.environ["variab_dir"]+"/eulerian_storm_track/obs/PS")
  #     a = 0
  #     while a < len(files):
  #         file1 = os.environ["variab_dir"]+"/eulerian_storm_track/obs/PS/"+files[a]
  #         file2 = os.environ["variab_dir"]+"/eulerian_storm_track/obs/"+files[a]
  #         cmd = "convert -crop 0x0+5+5 "+file1+" "+file2[:-3]+".png"
  #         print (cmd) 
  #         os.system("convert -crop 0x0+5+5 "+file1+" "+file2[:-3]+".png")
  #         a = a+1
  #     if os.environ["CLEAN"] == "1":
  #         os.system("rm -rf "+os.environ["variab_dir"]+"/eulerian_storm_track/obs/PS")

  # ======================================================================
  # End of HTML sections
  # ======================================================================    

  print("**************************************************")
  print("Eulerian Storm Track Diagnostic Package (eulerian_storm_track.py) Executed!")
  print("**************************************************")



print ('####################### END JJJ ##################\n\n')
