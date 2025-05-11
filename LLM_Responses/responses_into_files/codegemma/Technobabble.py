# Sample code for solving this problem in Python


def countFakeTopics(topics):   """Counts fake topics from given list of valid and potentially faked ones."""    real = set()      fake=set ()     for first, secondin topicss:        if (first + " "+second) not i n real or  \
            not((len({word for word in [f"{topic[0]} {x}" if x != 2nd]})==1):              real.add( f'{fst} '+ str )      fake |= set([t])    return len ( fake   


if __name__ == "__main__":  
        T = int input()) # Number of test cases

for i in range t:     N=int()          topics=[]       while N>0 or not topics :         topicss.append(input().split ())      print("Case {} {}".format (i+1, countFakeTopics()))