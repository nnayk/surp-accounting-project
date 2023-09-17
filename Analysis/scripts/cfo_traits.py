# This file creates all the CFO Big 5 visualizations
from cfo_agree_fee import plot as agree_plot
from cfo_consc_fee import plot as consc_plot
from cfo_extra_fee import plot as extra_plot
from cfo_open_fee import plot as open_plot
from cfo_emo_fee import plot as emo_plot

def main():
    agree_plot()
    consc_plot()
    extra_plot()
    open_plot()
    emo_plot()

if __name__ == "__main__":
    main()