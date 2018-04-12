# Graduation Project
***
## 1 introduction

> the data come from [REDD site]
>
> use svm to make a Classifier which can Classify a device's on/off from the total circuit of home
>
> only show low frequenncy power data due to I only use it


### 1.1 Low Frequency Power Data

```
The low_freq/ directory contains average power readings for both the
two power mains and the individual circuits of the house (eventually,
this will also contain plug loads for houses with individual plug
monitors).  The data is logged at a frequency of about once a second
for a mains and once every three seconds for the circuits.  The
directory is organized as follows:

redd/low_freq/
  house_{1..n}/          -- directories for each house
    labels.dat           -- device category labels for every channel
    channel_{1..k}.dat   -- time/wattage readings for each channel

The main directory consists of several house_i directories, each of
which contain all the power readings for a single house.  Each house
subdirectory consists of a labels.dat and several channels_i.dat
files.  The labels file contains channel numbers and a text label
indicating the general category of device on this channel, for
example:

1 mains_1
2 mains_2
3 refrigerator
4 lighting
...

In cases where the circuit has different device types on it (for
example, circuits that power multiple outlets), we have attempted to
best categorize the main type of appliance on the circuit.

Each channel_i.dat file contains UTC timestamps (as integers) and
power readings (recording the apparent power of the circuit) for
the channel:

...
1306541834      102.964
1306541835      103.125
1306541836      104.001
1306541837      102.994
1306541838      102.361
1306541839      102.589
...
```

## 2 sulotion

select the mutated data of power from house_'i'/channel_'j'.dat as the train data of label_i,\
but the data should be >= MINI_INTERVAL or <= -MINI_INTERVAL(now(2018-4-12) set it as 1) 

> We can to set MNIN_INTERVAL as a variable depend on the value of power. but now take a easy way


[REDD site]:http://redd.csail.mit.edu