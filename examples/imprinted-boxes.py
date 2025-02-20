"""Making the stellarmesh logo."""

import logging

import build123d as bd
import stellarmesh as sm

logging.getLogger("stellarmesh").setLevel(logging.INFO)

b1 = bd.Box(10, 10, 10)
b2 = b1.moved(bd.Location((0, 10, 0)))
b3 = b1.moved(bd.Location((0, 5, 10)))

cmp_initial = bd.Compound(b1, b2, b3)

solids = list(cmp_initial)
geom = sm.Geometry(solids, material_names=[""] * len(solids))
geom_imprinted = geom.imprint()
