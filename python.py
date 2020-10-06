def find_fib_n(n): # 0,1,1,2,...
    if n == 0:
        return([0, 1])
    s = find_fib_n(n >> 1)  # find_fib_n(n//2)
    ans = [s[0]*(2*s[1]-s[0]), s[1]**2+s[0]**2]
    if n & 1:  # if n%2==1
        return([ans[1], ans[0]+ans[1]])
    return ans


if __name__ == '__main__':
    s = find_fib_n(100000)
    # s[0] = fib(100000) , s[1]=fib(100001)
    print(s[0])

// c++ implemenation


pair<ll, ll> fib (int n) {
    if (n == 0)
        return {0, 1};

    auto p = fib(n >> 1);
    ll c = p.first * (2 * p.second - p.first);
    ll d = p.first * p.first + p.second * p.second;
    if (n & 1)
        return {d, c + d};
    else
        return {c, d};
}
