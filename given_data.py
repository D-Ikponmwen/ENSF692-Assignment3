# given_data.py
# ENSF 692 P2024
# School enrollment data provided in single NumPy arrays for each year. There are 20 schools with data for Grade 10, Grade 11, and Grade 12 across ten years.
# The data below can be viewed in the accompanying .csv file. The schools are arranged from smallest school code to largest.

import numpy as np

year_2013 = np.array([591, 572, 558,
472,	346,	0,
45,	    57,	    52,
160,	176,	189,
426,	483,	567,
620,	584,	585,
658,	631,	632,
289,	280,	311,
496,	465,	528,
523,	467,	517,
487,	413,	457,
29,	    29,	    45,
399,	361,	380,
210,	225,	359,
657,	566,	501,
163,	146,	228,
587,	611,	648,
514,	577,	522,
435,	364,	509,
504,	530,	512
])

year_2014 = np.array([
599,	592,	598,
444,	452,	341,
40,	    49,	    55,
151,	137,	173,
430,	404,	572,
662,	611,	602,
618,	639,	605,
323,	370,	395,
422,	437,	524,
522,	549,	529,
537,	502,	416,
36,	    44,	    44,
362,	371,	354,
219,	200,	222,
569,	619,	562,
131,	164,	208,
604,	641,	720,
549,	541,	581,
438,	431,	459,
518,	501,	565
])

year_2015 = np.array([
558,	585,	598,
419,	411,	463,
29, 	36,	    68,
137,	115,	106,
373,	403,	532,
659,	643,	583,
624,	610,	594,
271,	227,	316,
564,	383,	455,
565,	530,	543,
469,	491,	499,
48, 	37, 	43,
361,	337,	373,
215,	209,	212,
578,	489,	590,
116,	126,	201,
726,	626,	651,
515,	523,	529,
461,	406,	494,
552,	495,	515
])

year_2016 = np.array([
625,	555,	600,
345,	396,	436,
16,	    47,	    56,
155,	93,	    137,
431,	384,	567,
440,	514,	659,
682,	571,	630,
183,	210,	230,
197,	237,	459,
581,	583,	546,
460,	438,	499,
41,	    46,	    48,
341,	367,	377,
233,	207,	221,
535,	546,	543,
74,	    95,	    179,
691,	740,	680,
556,	528,	568,
420,	456,	511,
459,	512,	564
])

year_2017 = np.array([
611,	617,	582,
433,	374,	450,
15, 	48,	    58,
115,	123,	106,
395,	378,	531,
408,	388,	529,
798,	665,	636,
355,	368,	491,
215,	193,	330,
607,	557,	555,
491,	439,	423,
45,	    50,	    56,
422,	338,	390,
249,	241,	232,
583,	506,	534,
127,	127,	191,
706,	680,	763,
546,	580,	549,
459,	418,	517,
497,	423,	582
])

year_2018 = np.array([
485,	540,	582,
398,	423,	391,
23,	    25,	    58,
150,	83,	    120,
395,	402,	527,
568,	426,	510,
716,	688,	651,
387,	388,	419,
242,	204,	254,
685,	576,	535,
437,	473,	428,
38,	    45,	    57,
417,	391,	398,
386,	238,	249,
229,	250,	495,
81,	    112,	135,
703,	705,	744,
533,	496,	580,
443,	438,	460,
551,	456,	473
])

year_2019 = np.array([
463,	481,	556,
355,	430,	455,
13,	    23,	    52,
146,	146,	127,
383,	397,	441,
556,	615,	530,
723,	724,	798,
391,	391,	409,
251,	234,	322,
674,	692,	629,
476,	447,	507,
61,	    56,	    69,
458,	434,	424,
391,	381,	254,
241,	245,	299,
102,	77,	    146,
749,	677,	744,
488,	514,	503,
474,	449,	531,
535,	528,	553
])

year_2020 = np.array([
455,	436,	437,
360,	352,	437,
12,	    21,	    34,
137,	143,	142,
378,	361,	438,
565,	555,	629,
690,	727,	734,
543,	401,	459,
290,	234,	315,
491,	662,	680,
420,	465,	434,
34, 	59,	    64,
532,	449,	431,
402,	382,	364,
482,	251,	293,
128,	102,	144,
739,	746,	709,
540,	463,	503,
452,	482,	475,
537,	533,	559
])

year_2021 = np.array([
518,	453,	493,
464,	493,	420,
4,	    7,  	42,
164,	136,	139,
475,	424,	450,
664,	623,	642,
663,	679,	737,
489,	522,	566,
482,	431,	413,
507,	476,	643,
448,	404,	448,
np.nan,	np.nan,	np.nan,
652,	497,	552,
435,	384,	404,
574,	474,	498,
139,	123,	176,
750,	728,	747,
529,	571,	508,
578,	459,	484,
478,	487,	571
])

year_2022 = np.array([
419,	445,	446,
427,	378,	352,
2,	    4,  	38,
170,	148,	127,
424,	365,	424,
583,	602,	601,
706,	728,	714,
558,	522,	437,
372,	289,	318,
514,	510,	491,
413,	463,	405,
np.nan,	np.nan,	np.nan,
488,	520,	458,
375,	403,	391,
465,	486,	290,
109,	127,	166,
815,	748,	742,
565,	521,	435,
605,	589,	477,
496,	507,	527
])
