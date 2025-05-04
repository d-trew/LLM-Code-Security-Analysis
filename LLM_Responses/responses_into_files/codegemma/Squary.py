# Squary List Problem    


def squarysum(nums, k):        ## Function to check if a list of integers can be made into sqauy by adding at most K numbers in the range [-10^8 , +  ]

      sumsq = sum([num**2 for num i nums])
     sums= 4*k*(max(nums)+min(-numbers))   ## Formula to calculate maximum possible squary number of list with k elements.


        if sums== sqr :              # checking if the maxiumum possbile square is equal than sumsq then we can add at most K numbers in range [-10^8 , +  ]
            return " ".join(map (str,nums[:k]))

       else:                       ## If maximum possible squary number of list with k elements.is not equale to sqr the it is impossible 


        if sums > sumsq :          # if maxiumum possbile square greater than we need at least K numbers in range [-10^8 , +  ]

            return "IMPOSSIBLE"