from argparse import ArgumentParser
from matplotlib import pyplot as plt
from greengraph import Greengraph
from map import Map

def process():

    parser = ArgumentParser(description = "Create a graph showing number of green pixels between two locations on a satellite image")
    
    parser.add_argument('--origin', help="origin" , default = 'London')
    parser.add_argument('--dest', help = "destination", default = 'Oxford')
    parser.add_argument('--nsteps', help = 'number of points inbetween, default 10', type=int, default = 10 )
    parser.add_argument('--output', help = 'Output file name', default = False)
    arguments= parser.parse_args()
    
    plt.close()
    figure = plt.figure()
    figure_axes = figure.add_subplot(1,1,1)
    figure_axes.plot(Greengraph(arguments.origin ,arguments.dest).green_between(arguments.nsteps))
    if arguments.output:
        figure.savefig(arguments.output)

    plt.show()
    
if __name__ == "__main__":
    process()    