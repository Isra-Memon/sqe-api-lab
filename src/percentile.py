def percentile(student, roster):
    r = sorted(roster)
    i = r.index(student)
    t = len(r)
    return i / (t - 1) * 100 if t > 1 else 100.0
