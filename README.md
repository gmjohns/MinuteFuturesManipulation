# MinuteFuturesManipulation
## About 
This is a repository for scripts dealing with manuipulating minute based futures data for various entities. These scripts are used in combination with a raw data set aquired from kibot.com. This data set is not freely distributed, however some sample data is provided for testing of certain scripts. In general, this repository is intended for personal use only. Therefore, generallity and ease of use is not a major concern of this repository.

## Files
### compress.py:
It takes a raw dataset in the form `[date,time,open,close,high,low,volume]` 
and outputs a new csv file in the form `[date,time,vwa]` where '_vwa_' is '_volume weighted average_'.

### combine_data.py
It takes in multiple datasets and combines them with a common pandas DateTime object. Missing vallues are dealt with by using the most recent value of that particular entity.
