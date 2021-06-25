# Testing

## Changing number of index vectors

```
number of query vectors: 5
dimensions: 5
k: 4
```

| Number of index vectors | time (s)             |
| ----------------------- | -------------------- |
| 8                       | 0.007208756          |
| 16                      | 0.007772675          |
| 32                      | 0.007572055000000001 |
| 64                      | 0.008286572999999998 |
| 128                     | 0.008692194000000004 |
| 256                     | 0.010583266000000001 |
| 512                     | 0.013455292999999997 |
| 1024                    | 0.018445296000000003 |
| 2048                    | 0.02911971           |
| 4096                    | 0.048315397999999996 |
| 8192                    | 0.088948716          |
| 16384                   | 0.201967038          |
| 32768                   | 0.339961488          |
| 65536                   | 0.676532763          |
| 131072                  | 1.35098415           |
| 26214                   | 2.703998529          |
| 524288                  | 5.425651005          |
| 1048576                 | 10.869279074         |

Runtime scales linearly with the number of index vectors (runtime doubles as
number of index vectors doubles).

## Changing dimensionality

```
number of index vectors: 10
number of query vectors: 5
k: 4
```

| dimensions | time (s)             |
| ---------- | -------------------- |
| 8          | 0.009175359000000004 |
| 16         | 0.008042422999999996 |
| 32         | 0.008170163000000005 |
| 64         | 0.008975898          |
| 128        | 0.009404246000000002 |
| 256        | 0.011919671          |
| 512        | 0.015130013999999997 |
| 1024       | 0.023075648999999997 |
| 2048       | 0.036468890000000004 |
| 4096       | 0.064743222          |
| 8192       | 0.11931943400000002  |
| 16384      | 0.232770841          |
| 32768      | 0.4615918            |
| 65536      | 0.919626181          |
| 131072     | 1.825930206          |
| 26214      | 3.63860836           |
| 524288     | 7.175299816          |
| 1048576    | 14.739313679         |

Runtime scales linearly with dimensionality (runtime doubles as dimensionality
doubles).
