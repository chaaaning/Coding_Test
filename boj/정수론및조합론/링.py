import sys
import math

input = sys.stdin.readline

n = int(input().rstrip())
rings = list(map(int, input().split()))
main_ring = rings.pop(0)
result_list = []

for ring in rings:
    gcd_val = math.gcd(main_ring, ring)
    result_list.append(f"{main_ring//gcd_val}/{ring//gcd_val}")

for result in result_list:
    print(result)