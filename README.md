# FuturesWithFeatureTools

## Purpose
The purpose of this project is to take end of minute prices on various futures entities and engineer a new dataset. 
This new dataset will be volume based, so that data points will be seperated based on relative trading volume rather than time.

## Files
### compress.py:
This is the main script. It takes a raw dataset in the form `[date,time,open,close,high,low,volume]` 
and outputs a new csv file in the form `[date,time,vwa]` where '_vwa_' is '_volume weighted average_'.
