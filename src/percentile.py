def percentile(student, roster):
    r = sorted(roster)
    i = r.index(student)
    t = len(r)
    return i / t * 100
