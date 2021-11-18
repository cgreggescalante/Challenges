### Prime Generation

Fastest found prime sieve is the package primesieve by GitGub user kimwalisch.
Primes under an integer `n` generated with the statement:
```python
primesieve.primes(n)
```

### Factoring

Current factoring algorithms are found in the file `Factoring.py`.

To generate the unique prime factors of a integer `n`, use the following statement.
```python
Factoring.prime_factors(n)
```

To generate the complete prime factorization use
```python
Factoring.prime_factors(n, True)
```

To generate the divisors of `n`, use
```python
Factoring.divisors(n)
```
or
```python
Factoring.divisors(n, True)
```
to include the divisors `1` and `n`.
