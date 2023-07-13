from itertools import groupby


def nonoverlapping(hits):
    """Returns a list of non-overlapping hits."""
    nonover = list(hits)
    overst = False
    for i in range(1, len(hits)):
        (p, c) = hits[i - 1], hits[i]
        # Check whether hits overlap.
        if c[2] <= p[3]:
            if not overst:
                nonover.remove(p)
            nonover.remove(c)
            overst = True
        else:
            overst = False
    return nonover


fh = open('file.txt')
oh = open('results.txt', 'w')
fh.next()  # Ignore header line in BLAST output.

# Loop over BLAST hits (grp) for each query (qid).
for qid, grp in groupby(fh, lambda l: l.split()[0]):
    hits = []
    # I need to convert start and end positions
    # from strings into integers.
    for line in grp:
        hsp = line.split()
        hsp[2], hsp[3] = int(hsp[2]), int(hsp[3])
        hits.append(hsp)
    # Sort hits by start position.
    hits.sort(key=lambda x: x[2])
    for hit in nonoverlapping(hits):
        oh.write('\t'.join([str(f) for f in hit]) + '\n')
