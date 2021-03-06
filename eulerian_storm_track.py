# Code created by Jeyavinoth Jeyaratnam, to be implemented in MDTF 

# Import standarad Python packages 
import numpy as np 
from netCDF4 import Dataset
import os
import glob

# Import my code from the current folder
import eulerian_storm_track_util as est
import plotter # do not need this, just debugging purpose

print("****************************************************************************************")
print("Started Exeuction of Eulerian Storm Track Diagnostic Package (eulerian_storm_track.py)!")
print("****************************************************************************************")

# Setting up the necessary variable names
os.environ['v850_file'] = '*.'+os.environ['v850_var']+'.day.nc'

# Model output filename convection
os.environ['MODEL_OUTPUT_DIR'] = os.environ['DATADIR']+'/day'

missing_file = 0
if (len(glob.glob(os.environ['MODEL_OUTPUT_DIR']+'/'+os.environ['v850_file']))==0):
  print('Required V850 file missing!')
  missing_file = 1

if (missing_file == 1):
  print('MISSING FILES: Eulerian Strom Tracker will NOT be executed!')
else:
  ##########################################################
  # Create the necessary directories
  ##########################################################

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
  
  ##################################################################
  # Reading in the necessary data, and computing the daily eddies
  ##################################################################

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
  eddies = est.transient_eddies(v850)
  
  ##########################################################
  # Creating the plot for the different seasons
  ##########################################################

  # # getting the all year standard deviation average
  # season = 'all'
  # time_ind = est.get_time_ind(int(os.environ['FIRSTYR']), time, season=season)
  # std_dev = est.model_std_dev(diff, time_ind)
  # out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season)
  # plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,6), extend='max')
  # out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season)
  # plotter.plot(lonGrid, latGrid, std_dev, out_file=out_file, levels=np.arange(0,6), extend='max')

  season = 'djf'
  model_std_dev = est.model_std_dev(eddies, int(os.environ['FIRSTYR']), time, season=season)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')
 
  season = 'mam'
  model_std_dev = est.model_std_dev(eddies, int(os.environ['FIRSTYR']), time, season=season)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')
  
  season = 'jja'
  model_std_dev = est.model_std_dev(eddies, int(os.environ['FIRSTYR']), time, season=season)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')
  
  season = 'son'
  model_std_dev = est.model_std_dev(eddies, int(os.environ['FIRSTYR']), time, season=season)
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/PS/%s.%s.ps'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/model/%s.%s.png'%(os.environ['CASENAME'], season.upper())
  plotter.plot(lonGrid, latGrid, model_std_dev, out_file=out_file, title='%s (%s to %s)'%(season.upper(), os.environ['FIRSTYR'], os.environ['LASTYR']), levels=np.arange(0,6), extend='max')


  #### OBS data ###
  obs_data_file = os.environ['VARDATA'] + '/eulerian_storm_track/erai.nc'
  obs_lat, obs_lon, djf, mam, jja, son, obs_start_year, obs_end_year = est.obs_std_dev(obs_data_file)

  obs_max_lim = 6

  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.erai.ps'%(os.environ['CASENAME'], 'DJF')
  plotter.plot(obs_lon, obs_lat, djf, out_file=out_file, title='%s (%d to %d)'%('DJF', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.erai.png'%(os.environ['CASENAME'], 'DJF')
  plotter.plot(obs_lon, obs_lat, djf, out_file=out_file, title='%s (%d to %d)'%('DJF', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.erai.ps'%(os.environ['CASENAME'], 'MAM')
  plotter.plot(obs_lon, obs_lat, mam, out_file=out_file, title='%s (%d to %d)'%('MAM', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.erai.png'%(os.environ['CASENAME'], 'MAM')
  plotter.plot(obs_lon, obs_lat, mam, out_file=out_file, title='%s (%d to %d)'%('MAM', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.erai.ps'%(os.environ['CASENAME'], 'JJA')
  plotter.plot(obs_lon, obs_lat, jja, out_file=out_file, title='%s (%d to %d)'%('JJA', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.erai.png'%(os.environ['CASENAME'], 'JJA')
  plotter.plot(obs_lon, obs_lat, jja, out_file=out_file, title='%s (%d to %d)'%('JJA', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.erai.ps'%(os.environ['CASENAME'], 'SON')
  plotter.plot(obs_lon, obs_lat, son, out_file=out_file, title='%s (%d to %d)'%('SON', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.erai.png'%(os.environ['CASENAME'], 'SON')
  plotter.plot(obs_lon, obs_lat, son, out_file=out_file, title='%s (%d to %d)'%('SON', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
 
  obs_data_file = os.environ['VARDATA'] + '/eulerian_storm_track/era5.nc'
  obs_lat, obs_lon, djf, mam, jja, son, obs_start_year, obs_end_year = est.obs_std_dev(obs_data_file)

  obs_max_lim = 6

  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.era5.ps'%(os.environ['CASENAME'], 'DJF')
  plotter.plot(obs_lon, obs_lat, djf, out_file=out_file, title='%s (%d to %d)'%('DJF', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.era5.png'%(os.environ['CASENAME'], 'DJF')
  plotter.plot(obs_lon, obs_lat, djf, out_file=out_file, title='%s (%d to %d)'%('DJF', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.era5.ps'%(os.environ['CASENAME'], 'MAM')
  plotter.plot(obs_lon, obs_lat, mam, out_file=out_file, title='%s (%d to %d)'%('MAM', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.era5.png'%(os.environ['CASENAME'], 'MAM')
  plotter.plot(obs_lon, obs_lat, mam, out_file=out_file, title='%s (%d to %d)'%('MAM', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.era5.ps'%(os.environ['CASENAME'], 'JJA')
  plotter.plot(obs_lon, obs_lat, jja, out_file=out_file, title='%s (%d to %d)'%('JJA', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.era5.png'%(os.environ['CASENAME'], 'JJA')
  plotter.plot(obs_lon, obs_lat, jja, out_file=out_file, title='%s (%d to %d)'%('JJA', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/PS/%s.%s.era5.ps'%(os.environ['CASENAME'], 'SON')
  plotter.plot(obs_lon, obs_lat, son, out_file=out_file, title='%s (%d to %d)'%('SON', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  out_file = os.environ['variab_dir']+'/eulerian_storm_track/obs/%s.%s.era5.png'%(os.environ['CASENAME'], 'SON')
  plotter.plot(obs_lon, obs_lat, son, out_file=out_file, title='%s (%d to %d)'%('SON', obs_start_year, obs_end_year), levels=np.arange(0,obs_max_lim), extend='max')
  
  ##########################################################
  # Editting HTML Template for the current CASENAME
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

  a = os.system("cat "+os.environ["variab_dir"]+"/index.html | grep eulerian_storm_track > /dev/null")
  if a != 0:
     os.system("echo '<H3><font color=navy>Eulerian Strom Track Diagnostics <A HREF=\"eulerian_storm_track/eulerian_storm_track.html\">plots</A></H3>' >> "+os.environ["variab_dir"]+"/index.html")

  # ======================================================================
  # End of HTML sections
  # ======================================================================    

  print("*****************************************************************************")
  print("Eulerian Storm Track Diagnostic Package (eulerian_storm_track.py) Executed!")
  print("*****************************************************************************")



