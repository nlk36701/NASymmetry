import numpy as np
from san_diego.symtext.symtext import CharTable
from pgs.Cn import *
from pgs.Cnh import *
from pgs.Cnv import *
from pgs.Dn import *
from pgs.Dnh import *
from pgs.Dnd import *
from pgs.Sn import *
from san_diego.symtext.main import pg_to_symels, pg_to_chartab, symtext_from_file, cn_class_map, generate_symel_to_class_map

pgs = [
    "C2","C3","C4","C5","C6",
    "C2h","C3h","C4h","C5h","C6h",
    "C2v","C3v","C4v","C5v","C6v",
    "S4","S6","S8","S10",
    "D2","D3","D4","D5","D6",
    "D2d","D3d","D4d","D5d","D6d",
    "D2h","D3h","D4h","D5h","D6h"]

def test_Symel():
    for pg in pgs:
        symels_a = pg_to_symels(pg)
        symels_b = eval(pg+"s")
        beans = True
        a_len = len(symels_a)
        b_len = len(symels_b)
        if a_len != b_len:
            beans = False
        for i in range(a_len):
            if symels_a[i] == symels_b[i]:
                continue
            else:
                print(f"{pg} Symels {symels_a[i]} and {symels_b[i]} do not match!")
                print("Calculated:")
                print(symels_a)
                print("Ref:")
                print(symels_b)
                beans = False
        assert beans

def test_CharTable():
    for pg in pgs:
        ctab_a = pg_to_chartab(pg)
        ctab_b = CharTable(pg,np.array(eval(pg+"irr")),np.array(eval(pg+"cn")),None,eval(pg+"ct"),None)
        beans = ctab_a == ctab_b
        if not beans:
            print("Oh shit! The trout population!")
            print(ctab_a)
            print("Ref.")
            print(ctab_b)
            tab_chk = ctab_a.characters == ctab_b.characters
            irr_chk = ctab_a.irreps == ctab_b.irreps
            name_chk = ctab_a.classes == ctab_b.classes
            print(f"Table Check: {tab_chk.all()}")
            print(f"Irrep. Check: {irr_chk.all()}")
            print(f"Name Check: {name_chk.all()}")
            if not tab_chk.all():
                print(tab_chk)
                print(ctab_a.characters-ctab_b.characters)
            elif not name_chk.all():
                print(name_chk)
        assert beans

def test_symtext():
    #for i in range(2,7):
    #    pg = f"D{i}h"
    #    beans = generate_symel_to_class_map(pg_to_symels(pg),pg_to_chartab(pg))
    #    print(f"pg: {pg}, {beans}")
    print(symtext_from_file("test/sxyz/D6h.xyz")[1])