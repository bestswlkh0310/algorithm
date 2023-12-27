# 10000f + 1000o + 100r + 10t + y
# 200t + 20e + 2n
# 10000s + 1000i + 100x + 10t + y

for f in range(1, 10):
    for t in range(1, 10):
        if t in [f]: continue
        for s in range(1, 10):
            if s in [t, f]: continue
            for o in range(10):
                if o in [t, f, s]: continue
                for r in range(10):
                    if r in [f, t, s, o]: continue
                    for y in range(10):
                        if y in [f, t, s, o, r]: continue
                        for i in range(10):
                            if i in [f, t, s, o, r, y]: continue
                            for x in range(10):
                                if x in [f, t, s, o, r, y, i]: continue
                                for e in range(10):
                                    if e in [f, t, s, o, r, y, i, x]: continue
                                    for n in range(10):
                                        if n in [f, t, s, o, r, y, i, x, e]: continue
                                        if 10000 * f + 1000 * o + 100 * r + 10 * t + y + 200 * t + 20 * e + 2 * n == 10000 * s + 1000 * i + 100 * x + 10 * t + y:
                                            print(f"{f}{o}{r}{t}{y}+{t}{e}{n}+{t}{e}{n}={s}{i}{x}{t}{y}")