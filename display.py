import numpy as np
from matplotlib import pyplot as plt
import io

def plot():
    CHC1= [0,0,1,2,1,3,-1,2,1,2,3]
    TRC1 = [1,1,0,3,1,2,0,-2,-2,-2,-3]
    x = [6,7,8,9,10,11,12,13,14,15,16]

    fig, ax = plt.subplots()

    y1 = [x for x in CHC1]
    y2 = [p for p in TRC1]


    # turn off the right spine/ticks
    ax.spines['right'].set_color('none')
    ax.yaxis.tick_left()

    # set the y-spine
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_position('zero')

    #plot the chart

    ax.plot(x,y1, label = 'CHC1')
    ax.plot(x,y2,label = 'TRC1' )
    #show all values on x-axis
    plt.xticks(x)

    plt.rcParams["figure.figsize"] = [12,9]
    ax.legend('trc1')

    plt.title("Delta")
    ax.legend()

   # plt.show()

    # here is the trick save your figure into a bytes object and you can afterwards expose it via flas
    bytes_image = io.BytesIO()
    plt.savefig(bytes_image, format='png')
    bytes_image.seek(0)
    return bytes_image
