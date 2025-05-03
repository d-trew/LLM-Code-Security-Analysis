def main():
    T = int(input())
    
    for t in range(T):
        A, B = map(float, input().split())
        Ci = list(map(float, input().split()))
        
        # calculate the integral from 0 to X of Di-2 using trapezoidal rule with N+1 points
        def f(x, i):
            return (A + x) ** 2 - (B + Ci[i]) ** 2
        
        def integrand(x, i):
            return f(x, i) * (x**2) / 2
        
        X = abs(B-A)
        total_radiation = sum([integrate.quad(lambda x: integrand(x, i), 0, X)[0] for i in range(len(Ci))])
        
        print("Case #{}: {}".format(t+1, round(total_radiation, 3))
    
if __name__ == "__main__":
    main()