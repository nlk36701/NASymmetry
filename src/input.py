#Settings = dict()
#
#Settings["basis"] = "sto-3g"
#Settings["molecule"] = """
#  0 1
#  O
#  H 1 R
#  H 1 R 2 A
#  R = 1.0
#  A = 104.5
#  symmetry c2v
#"""
#Settings["nalpha"] = 5
#Settings["nbeta"] = 5
#Settings["scf_max_iter"] = 50

Settings = dict()

Settings["basis"] = "sto-3g"
Settings["molecule"] = """
<<<<<<< HEAD
C	0.0000000	1.3916730	0.0000000
C	1.2052240	0.6958360	0.0000000
C	1.2052240	-0.6958360	0.0000000
C	0.0000000	-1.3916730	0.0000000
C	-1.2052240	-0.6958360	0.0000000
C	-1.2052240	0.6958360	0.0000000
H	0.0000000	2.4695880	0.0000000
H	2.1387260	1.2347940	0.0000000
H	2.1387260	-1.2347940	0.0000000
H	0.0000000	-2.4695880	0.0000000
H	-2.1387260	-1.2347940	0.0000000
H	-2.1387260	1.2347940	0.0000000
=======
  0 1
  N     0.0000000       0.0000000       0.1173470  
  H     0.0000000       0.9326490       -0.2738090 
  H     0.8076980       -0.4663250      -0.2738090 
  H     -0.8076980      -0.4663250      -0.2738090 
  symmetry cs
>>>>>>> d3387b1fdcef18e784564922dde188a7f64baadb
"""
Settings["nalpha"] = 5
Settings["nbeta"] = 5
Settings["scf_max_iter"] = 50

