import os
import sys
import struct

from matplotlib import pyplot as plt
from codecs import decode

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from vcd_parser.vcd_parser import VcdParser

class VcdPlotter():
    def __init__(self,vcd_file:str):
        self.__vcd_parser = VcdParser()
        self.__signal_store = self.__vcd_parser.parse(vcd_file)
         
    def show(self,signals_list:[str], start_time:int, stop_time:int, base:str):
        self.plot(signals_list, start_time, stop_time, base)
        plt.show()
    
    def counter(self, value, size_x, j, data):
        count = 0
        for k in data[j:]:
            if value == k:
                count += 1
            else:
                return count
            if count > size_x-j:
                return count
        return count
            
    def plot(self,signals_list:[str], start_time:int, stop_time:int, base:str):
        data = {}
        for s in signals_list:
            id = self.__signal_store.name_id_map[s]
            raw = self.__signal_store.signals[id].get_values(self.__signal_store.get_max_time_stamp())
            data[s] = self.convert(base,raw[start_time:stop_time],self.__signal_store.signals[id].width)
        data["Time (%s)"%(self.__signal_store.get_unit())] = []
        size_y = len(data)
        size_x = stop_time - start_time + 1
        plt.figure(figsize=(size_x,size_y))
        plt.axis([0,size_x,0,size_y])
        i = size_y-1
        for key in data:
            start_vert = i/size_y 
            end_vert   = start_vert + 0.5/size_y
            for j in range(len(data[key])):
                if j >= size_x: # up to size_x
                    break
                value = data[key][j]
                value_before = data[key][j-1] if j > 0 else value
                start_hor = j/size_x
                end_hor   = start_hor + 1/size_x
                if value[2:] == '0':
                    if j == 0:
                        plt.text(j+0.08, i+0.1, value[2:], fontsize=14)
                    if value != value_before:
                        if 'x' in value_before:
                            plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='r')
                        elif 'z' in value_before:
                            plt.axvline(x=j, ymin=start_vert, ymax=start_vert+0.25/size_y, color='g')
                        else:
                            plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='g')
                        plt.text(j+0.08, i+0.1, value[2:], fontsize=14)
                    plt.axhline(y=i, xmin=start_hor, xmax=end_hor, color='g') 
                elif value[2:] == '1':
                    if j == 0 or value != value_before:
                        if j > 0 and 'x' in value_before:
                            plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='r')
                        elif j > 0 and 'z' in value_before:
                            plt.axvline(x=j, ymin=start_vert+0.25/size_y, ymax=end_vert, color='g')
                        else:
                            plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='g')
                        plt.text(j+0.08, i+0.1, value[2:], fontsize=14)
                    plt.axhline(y=i+0.5, xmin=start_hor, xmax=end_hor, color='g')
                elif 'z' in value:
                    if j > 0 and value != value_before:
                        if 'x' in value_before: 
                            plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='r')
                        elif value_before[2:] == '1':
                            plt.axvline(x=j, ymin=start_vert+0.25/size_y, ymax=end_vert, color='g')
                        elif value_before[2:] == '0':
                            plt.axvline(x=j, ymin=start_vert, ymax=start_vert+0.25/size_y, color='g')
                        else:
                            plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='g')
                    plt.axhline(y=i+0.25, xmin=start_hor, xmax=end_hor, color='y')
                elif 'x' in value:
                    if j == 0 or value != value_before:
                        plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='r')
                        count = self.counter(value, size_x, j, data[key])
                        if len(value) > count * 7:
                            plt.text(j+0.08, i+0.1, value[:count*7-3] + "...", fontsize=14, color='r')
                        else:
                            plt.text(j+0.08, i+0.1, value, fontsize=14, color='r')
                    plt.axhline(y=i, xmin=start_hor, xmax=end_hor, color='r')
                    plt.axhline(y=i+0.5, xmin=start_hor, xmax=end_hor, color='r')
                else:
                    if j == 0 or value != value_before:  
                        plt.axvline(x=j, ymin=start_vert, ymax=end_vert, color='g')
                        count = self.counter(value, size_x, j, data[key])
                        if len(value) > count * 7:
                            plt.text(j+0.08, i+0.1, value[:count*7-3] + "...", fontsize=14)
                        else:
                            plt.text(j+0.08, i+0.1, value, fontsize=14)
                    plt.axhline(y=i, xmin=start_hor, xmax=end_hor, color='g')
                    plt.axhline(y=i+0.5, xmin=start_hor, xmax=end_hor, color='g')
            i -= 1

        xticks = range(0,size_x)
        labelsx = range(start_time, stop_time+1)
        yticks = [i+0.25 for i in range(size_y-1, 0, -1)] + [0]
        labelsy = list(data.keys())

        plt.yticks(yticks, labelsy)
        plt.xticks(xticks, labelsx)
        plt.grid(linestyle='--',axis='x')
        
    
    def convert(self, base:str, data:[str], data_width:int):
        for i in range(len(data)):
            if base == 'dec':
                if data[i] != 'x' and data[i] != 'z':
                    data[i] = 'd\'' + str(int(data[i],2))
                else:
                    data[i] = 'd\''+ data[i]
            elif base == 'bin':
                if data[i] == 'x' or data[i] == 'z':
                    data[i] = 'b\''+(data[i] * data_width)
                else:
                    data[i] = 'b\''+format(int(data[i], 2), '0%db' % data_width)
            elif base == 'hex':
                if data[i] == 'x' or data[i] == 'z':
                    data[i] = 'h\''+(data[i] * data_width)
                else:
                    data[i] = 'h\''+format(int(data[i], 2), '0%dx' % data_width)
            elif base == 'dec2':
                if data[i] != 'x' and data[i] != 'z':
                    data[i] = format(int(data[i], 2), '0%db' % data_width)
                    if len(data[i]) > 1:
                        if(data[i][0] == '1'):
                            data[i] = "".join(['1' if d == '0' else '0' for d in data[i]])
                            data[i] = 'd\'-' + str(int(data[i],2)+1)
                        else:
                            data[i] = 'd\'' + str(int(data[i],2))
                    else:
                        data[i] = 'd\'' + str(int(data[i],2))
                else:
                    data[i] = 'd\''+ data[i]
                    
        return data
                
    def print_signals(self):
        for s in self.__signal_store.signals:
            print(self.__signal_store.signals[s])
    
    def save_figure(self,filename:str, signals_list:[str], start_time:int, stop_time:int, base:str):
        self.plot(signals_list, start_time, stop_time, base)
        plt.savefig(filename)
