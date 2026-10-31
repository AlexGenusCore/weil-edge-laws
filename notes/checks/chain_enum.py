"""Enumerate interior chain points (prime-power shifts from the edges +-L) for X = e^{2L}.
Used in tail_kink_laws_note.md §10.1: is the chain set finite at the proposed test cases X = 4, 5?
Run: python3 chain_enum.py > chain_enum.out"""
import math


def prime_power(n):
    p = next(q for q in range(2, n + 1) if n % q == 0)  # smallest prime factor
    while n % p == 0:
        n //= p
    return n == 1


def chains(X, gens=12):
    L = 0.5 * math.log(X)
    ns = [n for n in range(2, int(X) + 1) if prime_power(n) and math.log(n) < 2 * L - 1e-12]
    pts, front, seen = {}, [L, -L], set()
    for g in range(1, gens + 1):
        new = []
        for x in front:
            for n in ns:
                for e in (1, -1):
                    y = x + e * math.log(n)
                    if -L + 1e-12 < y < L - 1e-12 and round(y, 9) not in seen:
                        seen.add(round(y, 9)); new.append(y); pts[round(y, 9)] = g
        front = new
        if not new:
            break
    return L, ns, sorted(pts.items()), bool(front)


for X in (4, 5, 5.9, 6.5):
    L, ns, p, growing = chains(X)
    print(f"X={X}: L={L:.4f}, shifts n={ns}, points found={len(p)} (max generation {max(g for _, g in p)}),"
          f" {'still growing at generation 12' if growing else 'closed (finite)'}")
    if len(p) <= 30:
        print('   ', ', '.join(f'{a:+.4f}(g{g})' for a, g in p))

assert [n for n in range(2, 17) if prime_power(n)] == [2, 3, 4, 5, 7, 8, 9, 11, 13, 16]
