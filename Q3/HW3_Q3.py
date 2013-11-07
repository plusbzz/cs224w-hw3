


from collections import Counter
from ggplot import *
import math



def plot_word_freq(filename):
    with open (filename, "r") as myfile:
        words=[s.strip() for s in myfile.readlines()]
        counter = Counter(Counter(words).values())
        
    total = float(sum(counter.values()))
    ctr = {k:(v/total) for k,v in counter.items()}    
    x,y = zip(*(ctr.items()))
    loglog(x,y,'k.')
    title("Distribution of word frequencies for " + filename)
    xlabel("Frequency")
    ylabel("Number of words with frequency")
    return x,y



x,y = plot_word_freq("mobydick.txt")



x,y = plot_word_freq("donquijote.txt")



# Q3.ii) Estimating $\alpha$ and $x_{min}$.



def mle_alpha(x,xmin):
    x_filt = filter(lambda i: i >= xmin, x)
    lxmin = log(xmin)
    logsum = sum([log(d)-lxmin for d in x_filt])
    return 1.0+len(x_filt)/logsum



def find_xmin(filename):
    with open (filename, "r") as myfile:
        words=[s.strip() for s in myfile.readlines()]
        freqs = Counter(words).values()
        for xmin in xrange(1,16):
            alpha = mle_alpha(freqs,xmin)
            print "xmin = %d, alpha = %g" % (xmin,alpha)



find_xmin("mobydick.txt")



find_xmin("donquijote.txt")




