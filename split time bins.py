import os
import sys
import csv
import time
from sys import argv
from operator import itemgetter
from math import radians,cos,sin,asin,sqrt

def haversine(lon1,lat1,lon2,lat2):
    #calculate the great circle distance between two points on the earth
    lon1,lat1,lon2,lat2 = map(radians, [lon1,lat1,lon2,lat2])

    #haversine
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    R = 6371000
    return c * R
    
def comparetime(time1,time2):#calculation time span
        h = int(time2[-8:-6]) - int(time1[-8:-6])
        m = int(time2[-5:-3]) - int(time1[-5:-3])
        s = int(time2[-2:]) - int(time1[-2:])

        return h * 3600 + m * 60 + s 
def midstoptime(time1,time2):#calculation time point
        h = int(time2[-8:-6]) + int(time1[-8:-6])
        m = int(time2[-5:-3]) + int(time1[-5:-3])
        s = int(time2[-2:]) + int(time1[-2:])

        return (h * 3600 + m * 60 + s)/2 

output_file = ''
path = 'C:\Python27\hgl\rawstoppoints'
filelist = os.listdir(path)
all_file = []
count = 0
for file_name in filelist:
    full_file_name = os.path.join(path,file_name)
    try:
        source = open(full_file_name, 'r')
    except:
        e = sys.exc_info()[0]
        sys.exit("Error - Could not open input file %r: %s" % (full_file_name, e))
    reader = csv.reader(source)
    for row in reader:
        count+=1
        if int(row[7]) < 60:
            print("skip")
            continue
        if comparetime('2014-12-01 00:20:00',row[5])<0 and comparetime('2014-12-01 00:00:00',row[6])>0:
            group = '0000_0020'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 00:40:00',row[5])<0 and comparetime('2014-12-01 00:20:00',row[6])>0:
            group = '0020_0040'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 01:00:00',row[5])<0 and comparetime('2014-12-01 00:40:00',row[6])>0:
            group = '0040_0100'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 01:20:00',row[5])<0 and comparetime('2014-12-01 01:00:00',row[6])>0:
            group = '0100_0120'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 01:40:00',row[5])<0 and comparetime('2014-12-01 01:20:00',row[6])>0:
            group = '0120_0140'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 02:00:00',row[5])<0 and comparetime('2014-12-01 01:40:00',row[6])>0:
            group = '0140_0200'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 02:20:00',row[5])<0 and comparetime('2014-12-01 02:00:00',row[6])>0:
            group = '0200_0220'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 02:40:00',row[5])<0 and comparetime('2014-12-01 02:20:00',row[6])>0:
            group = '0220_0240'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 03:00:00',row[5])<0 and comparetime('2014-12-01 02:40:00',row[6])>0:
            group = '0240_0300'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 03:20:00',row[5])<0 and comparetime('2014-12-01 03:00:00',row[6])>0:
            group = '0300_0320'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 03:40:00',row[5])<0 and comparetime('2014-12-01 03:20:00',row[6])>0:
            group = '0320_0340'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 04:00:00',row[5])<0 and comparetime('2014-12-01 03:40:00',row[6])>0:
            group = '0340_0400'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 04:20:00',row[5])<0 and comparetime('2014-12-01 04:00:00',row[6])>0:
            group = '0400_0420'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 04:40:00',row[5])<0 and comparetime('2014-12-01 04:20:00',row[6])>0:
            group = '0420_0440'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 05:00:00',row[5])<0 and comparetime('2014-12-01 04:40:00',row[6])>0:
            group = '0440_0500'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 05:20:00',row[5])<0 and comparetime('2014-12-01 05:00:00',row[6])>0:
            group = '0500_0520'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 05:40:00',row[5])<0 and comparetime('2014-12-01 05:20:00',row[6])>0:
            group = '0520_0540'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 06:00:00',row[5])<0 and comparetime('2014-12-01 05:40:00',row[6])>0:
            group = '0540_0600'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 06:20:00',row[5])<0 and comparetime('2014-12-01 06:00:00',row[6])>0:
            group = '0600_0620'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 06:40:00',row[5])<0 and comparetime('2014-12-01 06:20:00',row[6])>0:
            group = '0620_0640'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 07:00:00',row[5])<0 and comparetime('2014-12-01 06:40:00',row[6])>0:
            group = '0640_0700'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 07:20:00',row[5])<0 and comparetime('2014-12-01 07:00:00',row[6])>0:
            group = '0700_0720'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 07:40:00',row[5])<0 and comparetime('2014-12-01 07:20:00',row[6])>0:
            group = '0720_0740'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 08:00:00',row[5])<0 and comparetime('2014-12-01 07:40:00',row[6])>0:
            group = '0740_0800'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 08:20:00',row[5])<0 and comparetime('2014-12-01 08:00:00',row[6])>0:
            group = '0800_0820'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 08:40:00',row[5])<0 and comparetime('2014-12-01 08:20:00',row[6])>0:
            group = '0820_0840'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 09:00:00',row[5])<0 and comparetime('2014-12-01 08:40:00',row[6])>0:
            group = '0840_0900'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 09:20:00',row[5])<0 and comparetime('2014-12-01 09:00:00',row[6])>0:
            group = '0900_0920'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 09:40:00',row[5])<0 and comparetime('2014-12-01 09:20:00',row[6])>0:
            group = '0920_0940'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 10:00:00',row[5])<0 and comparetime('2014-12-01 09:40:00',row[6])>0:
            group = '0940_1000'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 10:20:00',row[5])<0 and comparetime('2014-12-01 10:00:00',row[6])>0:
            group = '1000_1020'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 10:40:00',row[5])<0 and comparetime('2014-12-01 10:20:00',row[6])>0:
            group = '1020_1040'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 11:00:00',row[5])<0 and comparetime('2014-12-01 10:40:00',row[6])>0:
            group = '1040_1100'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 11:20:00',row[5])<0 and comparetime('2014-12-01 11:00:00',row[6])>0:
            group = '1100_1120'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 11:40:00',row[5])<0 and comparetime('2014-12-01 11:20:00',row[6])>0:
            group = '1120_1140'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 12:00:00',row[5])<0 and comparetime('2014-12-01 11:40:00',row[6])>0:
            group = '1140_1200'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 12:20:00',row[5])<0 and comparetime('2014-12-01 12:00:00',row[6])>0:
            group = '1200_1220'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 12:40:00',row[5])<0 and comparetime('2014-12-01 12:20:00',row[6])>0:
            group = '1220_1240'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 13:00:00',row[5])<0 and comparetime('2014-12-01 12:40:00',row[6])>0:
            group = '1240_1300'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 13:20:00',row[5])<0 and comparetime('2014-12-01 13:00:00',row[6])>0:
            group = '1300_1320'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 13:40:00',row[5])<0 and comparetime('2014-12-01 13:20:00',row[6])>0:
            group = '1320_1340'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 14:00:00',row[5])<0 and comparetime('2014-12-01 13:40:00',row[6])>0:
            group = '1340_1400'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 14:20:00',row[5])<0 and comparetime('2014-12-01 14:00:00',row[6])>0:
            group = '1400_1420'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 14:40:00',row[5])<0 and comparetime('2014-12-01 14:20:00',row[6])>0:
            group = '1420_1440'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 15:00:00',row[5])<0 and comparetime('2014-12-01 14:40:00',row[6])>0:
            group = '1440_1500'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 15:20:00',row[5])<0 and comparetime('2014-12-01 15:00:00',row[6])>0:
            group = '1500_1520'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 15:40:00',row[5])<0 and comparetime('2014-12-01 15:20:00',row[6])>0:
            group = '1520_1540'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 16:00:00',row[5])<0 and comparetime('2014-12-01 15:40:00',row[6])>0:
            group = '1540_1600'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 16:20:00',row[5])<0 and comparetime('2014-12-01 16:00:00',row[6])>0:
            group = '1600_1620'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 16:40:00',row[5])<0 and comparetime('2014-12-01 16:20:00',row[6])>0:
            group = '1620_1640'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 17:00:00',row[5])<0 and comparetime('2014-12-01 16:40:00',row[6])>0:
            group = '1640_1700'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 17:20:00',row[5])<0 and comparetime('2014-12-01 17:00:00',row[6])>0:
            group = '1700_1720'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 17:40:00',row[5])<0 and comparetime('2014-12-01 17:20:00',row[6])>0:
            group = '1720_1740'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 18:00:00',row[5])<0 and comparetime('2014-12-01 17:40:00',row[6])>0:
            group = '1740_1800'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 18:20:00',row[5])<0 and comparetime('2014-12-01 18:00:00',row[6])>0:
            group = '1800_1820'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 18:40:00',row[5])<0 and comparetime('2014-12-01 18:20:00',row[6])>0:
            group = '1820_1840'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 19:00:00',row[5])<0 and comparetime('2014-12-01 18:40:00',row[6])>0:
            group = '1840_1900'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 19:20:00',row[5])<0 and comparetime('2014-12-01 19:00:00',row[6])>0:
            group = '1900_1920'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 19:40:00',row[5])<0 and comparetime('2014-12-01 19:20:00',row[6])>0:
            group = '1920_1940'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 20:00:00',row[5])<0 and comparetime('2014-12-01 19:40:00',row[6])>0:
            group = '1940_2000'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 20:20:00',row[5])<0 and comparetime('2014-12-01 20:00:00',row[6])>0:
            group = '2000_2020'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 20:40:00',row[5])<0 and comparetime('2014-12-01 20:20:00',row[6])>0:
            group = '2020_2040'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 21:00:00',row[5])<0 and comparetime('2014-12-01 20:40:00',row[6])>0:
            group = '2040_2100'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 21:20:00',row[5])<0 and comparetime('2014-12-01 21:00:00',row[6])>0:
            group = '2100_2120'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 21:40:00',row[5])<0 and comparetime('2014-12-01 21:20:00',row[6])>0:
            group = '2120_2140'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 22:00:00',row[5])<0 and comparetime('2014-12-01 21:40:00',row[6])>0:
            group = '2140_2200'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 22:20:00',row[5])<0 and comparetime('2014-12-01 22:00:00',row[6])>0:
            group = '2200_2220'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 22:40:00',row[5])<0 and comparetime('2014-12-01 22:20:00',row[6])>0:
            group = '2220_2240'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 23:00:00',row[5])<0 and comparetime('2014-12-01 22:40:00',row[6])>0:
            group = '2240_2300'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 23:20:00',row[5])<0 and comparetime('2014-12-01 23:00:00',row[6])>0:
            group = '2300_2320'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        if comparetime('2014-12-01 23:40:00',row[5])<0 and comparetime('2014-12-01 23:20:00',row[6])>0:
            group = '2320_2340'
            output_file = './stoppoints/tripstoppoint0_600_' + row[5][0:11] + str(group) + '.csv'
            target = open(output_file, 'a')
            writer = csv.writer(target,lineterminator='\n')  
            writer.writerow(row)
            target.closed
        print (full_file_name + ' ' + str(count) + 'line' +' is done.')

    source.closed 
        
print()