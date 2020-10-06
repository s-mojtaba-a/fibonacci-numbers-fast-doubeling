We have two formulas : 

	fib(2n) = fib(n)(2fib(n+1)-fib(n))
	fib(2n+1) = fib(n+1)^2 + fib(n)^2

if we want to calculate fib(n), first we have to calculate fib(n//2) and fib(n//2+1).
Recursivly, we have to calculate some other fibonacci terms.
So we can implement this by a recursive function.
The function calculates fib(n) and returns (fib(n),fib(n+1)).

