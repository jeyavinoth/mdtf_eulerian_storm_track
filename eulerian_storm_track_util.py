#!/usr/bin/env python

############# EULERIAN STROM TRACKER ############
###### Created by: Jeyavinoth Jeyaratnam     ####
###### Created Date: 03/29/2019              ####
###### Last Modified: 05/02/2019             ####
#################################################

# Importing standard libraries
import numpy as np 
import datetime as dt

def daily_diff(daily_data):
  '''
  Data has to be provided as daily_data
  it will compute the difference between the current day and the previous day
  i.e. X(t+1) - X(t), nans for the last index 
  '''
  # pad the right of the array with nan values along the first dimension
  # then extract the values from the 2nd column (index = 1) to the end
  # this will give us a shifted array of daily data, i.e. X(t+1)
  daily_data_shift = np.pad(daily_data, ((0,1), (0,0), (0,0)), mode='constant', constant_values=np.nan)[1:, :, :]

  return daily_data_shift - daily_data # X(t+1) - X(t), with nan values for the last time dimension


def std_dev(data, time_ind):
  '''
  Given data input in the format (time, lat, lon)
  we will calculate the std_dev for the given time_ind, the time_ind has to be a logical array of the size of the time dimension 
  '''
  out_std_dev = np.empty((data.shape[1], data.shape[2]))*np.nan

  # check if any value is true for the selected time, if so then return nan values, else compute standard deviation 
  if np.all(np.invert(time_ind)):
    print ('No time index selected!')
    return (out_std_dev)
  else:
    # print(time_ind.shape,data.shape)
    out_std_dev = np.nanstd(data[time_ind, :, :], axis=0)
    return out_std_dev

def get_time_ind(start_year, time, season='djf'):
  ''' Get the time index for the given season '''

  # convert time as numpy array
  time = np.asarray(time)

  # getting the datetime values for the time index
  dates_month=[]
  dates_year=[]
  for i_time in time: 
    temp_time = dt.datetime(start_year, 1, 1) + dt.timedelta(days=np.float(i_time)-1)
    dates_month.append(temp_time.month)
    dates_year.append(temp_time.year)

  uni_year = sorted(set(dates_year))
  dates_month = np.asarray(dates_month)
  dates_year = np.asarray(dates_year)

  # getting the time index
  if (season == ''):
    raise Exception('Set which season you want to extract!')
  elif (season == 'djf'):
    time_ind = (dates_month == 12) | (dates_month == 1) | (dates_month == 2)
  elif (season == 'mam'):
    time_ind = (dates_month == 3) | (dates_month == 4) | (dates_month == 5)
  elif (season == 'jja'):
    time_ind = (dates_month == 6) | (dates_month == 7) | (dates_month == 8)
  elif (season == 'son'):
    time_ind = (dates_month == 9) | (dates_month == 10) | (dates_month == 11)
  elif (season == 'all'):
    time_ind = (np.ones(time.shape) == 1)

  return time_ind

