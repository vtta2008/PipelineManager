//Maya ASCII 2017ff04 scene
//Name: test 5.ma
//Last modified: Tue, May 16, 2017 10:59:24 AM
//Codeset: 1252
requires maya "2017ff04";
currentUnit -l centimeter -a degree -t film;
fileInfo "application" "maya";
fileInfo "product" "Maya 2017";
fileInfo "version" "2017";
fileInfo "cutIdentifier" "201702071345-1015190";
fileInfo "osv" "Microsoft Windows 7 Enterprise Edition, 64-bit Windows 7 Service Pack 1 (Build 7601)\n";
fileInfo "license" "education";
createNode transform -n "Spike_Cross_Control";
	rename -uid "0C6B1D36-45D5-513A-C57F-CF87D6EEA8F8";
createNode nurbsCurve -n "Spike_Cross_ControlShape" -p "Spike_Cross_Control";
	rename -uid "16F6F788-49E3-FCB6-246D-6698946C2E2E";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 19;
	setAttr ".cc" -type "nurbsCurve" 
		1 39 0 no 3
		40 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36 37 38 39
		40
		0.56982715083383706 4.0911216636629888e-009 -2.1328837350509389e-005
		0.42089523917311311 0.14888739445176391 -1.5755096100633637e-005
		0.27209314192421008 4.0735560498550427e-005 -1.0184545420344193e-005
		0.42093980071123838 -0.14876136179267441 -1.5755096101521815e-005
		0.56982715083383706 4.0911216636629888e-009 -2.1328837350509389e-005
		0.42091194939160675 6.3015495567864122e-005 -0.14884013478191349
		0.27209314192421008 4.0735560498550427e-005 -1.0184545420344193e-005
		0.42092309049279564 6.3017163522971487e-005 0.14880862458971134
		0.56982715083383706 4.0911216636629888e-009 -2.1328837350509389e-005
		0.42089523917311311 0.14888739445176391 -1.5755096100633637e-005
		0.27209314192421008 4.0735560498550427e-005 -1.0184545420344193e-005
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		-0.4209971894939688 -6.3028257021535694e-005 0.14884013797247952
		-0.56982713806255436 -8.5309860045956754e-005 2.1328837348733032e-005
		-0.4210083305952077 -6.3029924976643059e-005 -0.14880862139914619
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		-0.42085456057731463 0.14876116408473417 1.5751905531047328e-005
		-0.56982713806255436 -8.5309860045956754e-005 2.1328837348733032e-005
		-0.42098047927552518 -0.14888740721321847 1.5758286666667232e-005
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		-0.27209312915292649 -0.00012604132942328761 1.0184545417679658e-005
		0 -1.3322676295501878e-015 0
		-1.1141101238898443e-005 -1.6679564396326896e-009 0.27211440318025648
		0.00014271626145045957 0.14882419235483146 0.42093877648166433
		0 -1.3322676295501878e-015 0.56976316255188397
		1.6710218443627411e-005 -0.14882437895619827 0.42093878286606934
		-1.1141101238898443e-005 -1.6679564396326896e-009 0.27211440318025648
		-0.14882987953462568 -2.2281592690021057e-005 0.42094435341416769
		0 -1.3322676295501878e-015 0.56976316255188397
		0.14890412937122033 -6.29878057401001e-005 0.42093320912223664
		-1.1141101238898443e-005 -1.6679564396326896e-009 0.27211440318025648
		-3.1511783191717768e-005 -4.7176880180188618e-009 -0.27211440158374511
		-5.9356788792541693e-005 0.14882437257149927 -0.42093878126979423
		-4.2652884430616211e-005 -6.3856417931162923e-009 -0.56976316095537172
		-1.4801564748090357e-005 -0.14882438367388451 -0.42093878126955797
		-3.1511783191717768e-005 -4.7176880180188618e-009 -0.27211440158374511
		-0.14886139131781739 -2.2286310378039076e-005 -0.42093321072146139
		-4.2652884430616211e-005 -6.3856417931162923e-009 -0.56976316095537172
		0.14887261758802861 -6.299252342767403e-005 -0.42094435501339156
		-3.1511783191717768e-005 -4.7176880180188618e-009 -0.27211440158374511
		;
createNode transform -n "Circle_Arrow_2D";
	rename -uid "C8963872-47C4-C649-D25D-C6878D956527";
createNode nurbsCurve -n "Circle_Arrow_2DShape" -p "Circle_Arrow_2D";
	rename -uid "488A8A4C-4D7A-2911-94EE-19B06219AA9D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 20;
	setAttr ".cc" -type "nurbsCurve" 
		1 41 0 no 3
		42 0 2 4.0871430000000002 6.1743430000000004 8.2614889999999992 10.348646 12.435838
		 14.522990999999999 16.610143000000001 18.697337999999998 20.784490000000002 22.871642000000001
		 24.958836000000002 27.045988999999999 29.133140999999998 31.220334999999999 33.307487999999999
		 35.394638999999998 37.481833999999999 39.568986000000002 41.686399999999999 48.748496000000003
		 55.810591000000002 58.009692000000001 59.575055999999996 61.140450999999999 62.705815999999999
		 64.271180999999999 65.836574999999996 67.401939999999996 68.967304999999996 70.532698999999994
		 72.098063999999994 73.663428999999994 75.228823000000006 76.794188000000005 78.359554000000003
		 79.924946000000006 81.490313999999998 83.055674999999994 84.621072999999996 86.186430999999999
		
		42
		0 0 -2.4000000000000004
		0 0 -3.2000000000000002
		0.82733600000000007 0 -3.0881896000000002
		1.5986624000000003 0 -2.7686900000000003
		2.2627592000000001 0 -2.2627604000000003
		2.7686924000000004 0 -1.5986616
		3.0881860000000003 0 -0.82733640000000008
		3.2000248 0 2.0621280000000001e-007
		3.0881860000000003 0 0.82733600000000007
		2.7686924000000004 0 1.5986624000000003
		2.2627592000000001 0 2.2627592000000001
		1.5986624000000003 0 2.7686924000000004
		0.82733600000000007 0 3.0881860000000003
		0 0 3.2000248
		-0.82733600000000007 0 3.0881860000000003
		-1.5986624000000003 0 2.7686924000000004
		-2.2627592000000001 0 2.2627592000000001
		-2.7686924000000004 0 1.5986624000000003
		-3.0881860000000003 0 0.82733600000000007
		-3.2000248 0 2.0621280000000001e-007
		-4.0469904000000003 0 0
		-2.7836844000000003 0 -2.5266120000000001
		-1.5203784000000002 0 0
		-2.4000184000000004 0 1.5477240000000003e-007
		-2.3161396000000001 0 0.62050240000000001
		-2.0765191999999999 0 1.1989964000000002
		-1.6970696000000001 0 1.6970692000000001
		-1.1989964000000002 0 2.0765191999999999
		-0.62050240000000001 0 2.3161396000000001
		0 0 2.4000184000000004
		0.62050240000000001 0 2.3161396000000001
		1.1989964000000002 0 2.0765191999999999
		1.6970696000000001 0 1.6970692000000001
		2.0765191999999999 0 1.1989964000000002
		2.3161396000000001 0 0.62050240000000001
		2.4000184000000004 0 1.5477240000000003e-007
		2.3161396000000001 0 -0.62050280000000013
		2.0765191999999999 0 -1.198996
		1.6970696000000001 0 -1.6970704000000003
		1.1989964000000002 0 -2.0765176000000003
		0.62050240000000001 0 -2.3161420000000001
		0 0 -2.4000000000000004
		;
createNode transform -n "Male_Symbol";
	rename -uid "B54E55CD-498A-A48C-69CC-84A262C68F61";
createNode nurbsCurve -n "Male_SymbolShape" -p "Male_Symbol";
	rename -uid "7912705A-47B6-4BF2-3A74-8CBE516AAC08";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 9;
	setAttr ".cc" -type "nurbsCurve" 
		1 36 0 no 3
		37 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30 31 32 33 34 35 36
		37
		4.4964032497318838e-016 1.6000000000000012 -2.2557010682735437e-015
		-0.3119235293234579 1.5688757999304204 -2.2506959151650479e-015
		-0.61179992425629959 1.4775355211816883 -2.2360072780566864e-015
		-0.88816423422255186 1.3295695200849658 -2.2122125302821148e-015
		-1.130589804340127 1.1308261083641808 -2.1802521520958941e-015
		-1.3293898447288988 0.88844923528803887 -2.1412749781607401e-015
		-1.4772553023026735 0.61203519477418755 -2.0968242102368441e-015
		-1.5682658227913404 0.31205878131852949 -2.0485843237521635e-015
		-1.5991784838738627 0.00011039946844738636 -1.9984191979138542e-015
		-1.5682630253857908 -0.31183819334539664 -1.9482540381499844e-015
		-1.4772753935903149 -0.61182275836088429 -1.9000128407945046e-015
		-1.3295355374380915 -0.88830478098581056 -1.8555511405133494e-015
		-1.1308474670756683 -1.1307718807569309 -1.8165594570190147e-015
		-0.88839144588362751 -1.3294735186432725 -1.7846057965777277e-015
		-0.61191601590586864 -1.477226285107555 -1.760845339547368e-015
		-0.31194415892591898 -1.5682561640787946 -1.7462066185302709e-015
		2.2815083156046968e-015 -1.5992086836047279 -1.7412290737588495e-015
		0.31194415892592231 -1.5682561640787931 -1.7462066185302711e-015
		0.61191601590587175 -1.4772262851075539 -1.7608453395473682e-015
		0.8883914458836305 -1.3294735186432698 -1.7846057965777281e-015
		1.1308474670756701 -1.1307718807569294 -1.8165594570190151e-015
		1.3295355374380942 -0.88830478098580823 -1.8555511405133494e-015
		1.4772753935903185 -0.61182275836088262 -1.9000128407945046e-015
		1.568263025385791 -0.31183819334539253 -1.9482540381499848e-015
		1.5991784838738625 0.00011039946845280424 -1.998419197913855e-015
		1.5682658227913402 0.3120587813185336 -2.0485843237521639e-015
		1.4772553023026744 0.61203519477419133 -2.0968242102368445e-015
		1.3293898447288983 0.88844923528804043 -2.1412749781607401e-015
		1.1305898043401246 1.1308261083641831 -2.1802521520958948e-015
		0.88816423422255164 1.3295695200849658 -2.2122125302821148e-015
		0.61179992425629914 1.4775355211816885 -2.2360072780566864e-015
		0.31192352932345913 1.5688757999304204 -2.2506959151650479e-015
		4.4964032497318838e-016 1.6000000000000012 -2.2557010682735437e-015
		3.6082248300317588e-016 4.4000000000000004 -2.9753977059954196e-015
		-1.1999999999999997 2.8000000000000003 -2.6201263381153696e-015
		3.6082248300317588e-016 4.4000000000000004 -2.9753977059954196e-015
		1.2000000000000006 2.8000000000000003 -2.6201263381153696e-015
		;
createNode transform -n "Arrow_Curve";
	rename -uid "2A43A01F-4F3A-EE15-92BC-B1960271966A";
createNode nurbsCurve -n "Arrow_CurveShape" -p "Arrow_Curve";
	rename -uid "5BCF9D48-455B-7258-0148-CB9BAE127C73";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 25;
	setAttr ".cc" -type "nurbsCurve" 
		1 7 0 no 3
		8 0 1 2 3 4 5 6 7
		8
		-1 0 0
		-1 0 2
		1 0 2
		1 0 0
		2 0 0
		0 0 -2
		-2 0 0
		-1 0 0
		;
createNode transform -n "Origin_Control";
	rename -uid "5CF72620-4E86-6C2B-AE28-D9A4D1618B4E";
createNode nurbsCurve -n "Origin_ControlShape" -p "Origin_Control";
	rename -uid "6667DF04-4EF3-249B-08C0-7DA6D0695AF2";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 26;
	setAttr ".cc" -type "nurbsCurve" 
		1 62 0 no 3
		63 0 1.411065 6.7736340000000004 12.136203 13.547268000000001 18.909838000000001
		 24.272407000000001 25.683471000000001 31.046040999999999 36.408610000000003 37.819674999999997
		 43.182243999999997 48.544812999999998 49.955877999999998 55.318447999999997 60.681016999999997
		 62.092081999999998 67.454650999999998 95.205282999999994 122.955915 128.31848400000001
		 129.72954899999999 135.092118 140.45468700000001 141.86575199999999 143.27681699999999
		 144.687883 150.05045200000001 160.41302099999999 156.82408599999999 162.186655 167.54922400000001
		 168.96028999999999 174.32285899999999 179.685428 181.09649300000001 186.45906199999999
		 208.56543400000001 214.20969400000001 219.85395500000001 225.49821499999999 231.14247499999999
		 236.78673499999999 242.43099599999999 248.075256 253.719516 275.82588800000002 281.18845700000003
		 282.59952199999998 287.96209099999999 293.32465999999999 294.735726 300.09829500000001
		 305.46086400000002 306.87192900000002 308.28299399999997 309.69405999999998 315.05662899999999
		 320.41919799999999 321.830263 323.24132800000001 328.60389700000002 333.96646600000003
		
		63
		0.1058298 3.3865561500000001 0.18330270000000001
		-0.10582994999999999 3.3865561500000001 0.18330270000000001
		0 4.1625947999999999 0
		0.1058298 3.3865561500000001 0.18330270000000001
		0.21165975000000001 3.3865561500000001 0
		0 4.1625947999999999 0
		0.21165975000000001 3.3865561500000001 0
		0.10582994999999999 3.3865561500000001 -0.18330270000000001
		0 4.1625947999999999 0
		0.10582994999999999 3.3865561500000001 -0.18330270000000001
		-0.1058298 3.3865561500000001 -0.18330284999999999
		0 4.1625947999999999 0
		-0.1058298 3.3865561500000001 -0.18330284999999999
		-0.21165975000000001 3.3865561500000001 -3.3622199999999999e-008
		0 4.1625947999999999 0
		-0.21165975000000001 3.3865561500000001 -3.3622199999999999e-008
		-0.10582994999999999 3.3865561500000001 0.18330270000000001
		0 4.1625947999999999 0
		0 0 0
		0 0 4.1625947999999999
		-0.18330270000000001 0.10582994999999999 3.3865561500000001
		0 0.21165975000000001 3.3865561500000001
		0 0 4.1625947999999999
		0.18330270000000001 0.1058298 3.3865561500000001
		0 0.21165975000000001 3.3865561500000001
		0.18330270000000001 0.1058298 3.3865561500000001
		0.18330270000000001 -0.10582994999999999 3.3865561500000001
		0 0 4.1625947999999999
		0.18330270000000001 -0.10582994999999999 3.3865561500000001
		-3.3622199999999999e-008 -0.21165975000000001 3.3865561500000001
		0 0 4.1625947999999999
		-3.3622199999999999e-008 -0.21165975000000001 3.3865561500000001
		-0.18330284999999999 -0.1058298 3.3865561500000001
		0 0 4.1625947999999999
		-0.18330284999999999 -0.1058298 3.3865561500000001
		-0.18330270000000001 0.10582994999999999 3.3865561500000001
		0 0 4.1625947999999999
		0 0 0.84663900000000003
		0 0.84663900000000003 0.84663900000000003
		0 0.84663900000000003 0
		0.84663900000000003 0.84663900000000003 0
		0.84663900000000003 0 0
		0 0 0
		0 0 0.84663900000000003
		0.84663900000000003 0 0.84663900000000003
		0.84663900000000003 0 0
		4.1625947999999999 0 0
		3.3865561500000001 0.21165975000000001 0
		3.3865561500000001 0.1058298 -0.18330270000000001
		4.1625947999999999 0 0
		3.3865561500000001 0.1058298 -0.18330270000000001
		3.3865561500000001 -0.10582994999999999 -0.18330270000000001
		4.1625947999999999 0 0
		3.3865561500000001 -0.21165975000000001 3.3622199999999999e-008
		3.3865561500000001 -0.10582994999999999 -0.18330270000000001
		3.3865561500000001 -0.21165975000000001 3.3622199999999999e-008
		3.3865561500000001 -0.1058298 0.18330284999999999
		4.1625947999999999 0 0
		3.3865561500000001 -0.1058298 0.18330284999999999
		3.3865561500000001 0.10582994999999999 0.18330270000000001
		3.3865561500000001 0.21165975000000001 0
		4.1625947999999999 0 0
		3.3865561500000001 0.10582994999999999 0.18330270000000001
		;
createNode transform -n "Fish_Nail";
	rename -uid "E7ADEFA2-4AB2-09B7-140B-4CAD7B913C2F";
createNode nurbsCurve -n "Fish_NailShape" -p "Fish_Nail";
	rename -uid "7BABADC5-4F10-EB4F-1E67-F7B57EB8CD77";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 19;
	setAttr ".cc" -type "nurbsCurve" 
		1 30 0 no 3
		31 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27
		 28 29 30
		31
		0 0 0
		6.8580220752251786e-016 5.6000000000000005 0
		0.20683760000000073 5.6279536000000006 0
		0.39966240000000075 5.7078255999999996 0
		0.56568960000000068 5.8343100000000003 0
		0.69217500000000076 6.0003378000000005 0
		0.77204560000000089 6.1931621999999997 0
		0.80000600000000066 6.4000000461260003 0
		0 6.4000000000000004 0
		6.8580220752251786e-016 5.6000000000000005 0
		-0.20683759999999932 5.6279536000000006 0
		-0.39966239999999931 5.7078256000000005 0
		-0.56568959999999924 5.8343100000000003 0
		-0.69217499999999932 6.0003378000000005 0
		-0.77204559999999933 6.1931622000000006 0
		-0.80000599999999933 6.4000000461260003 0
		-0.77204559999999933 6.6068376000000004 0
		-0.69217499999999921 6.7996623999999999 0
		-0.56568959999999913 6.965689600000001 0
		-0.39966239999999914 7.092175000000001 0
		-0.20683759999999915 7.1720456000000006 0
		8.8174643017417381e-016 7.200006000000001 0
		0.20683760000000093 7.1720456000000006 0
		0.39966240000000092 7.092175000000001 0
		0.5656896000000009 6.965689600000001 0
		0.69217500000000098 6.7996623999999999 0
		0.77204560000000089 6.6068376000000004 0
		0.80000600000000066 6.4000000461260003 0
		-0.80000599999999933 6.4000000461260003 0
		0 6.4000000000000004 0
		8.8174643017417381e-016 7.200006000000001 0
		;
createNode transform -n "Nail_Arrow_Up";
	rename -uid "A6E70BC2-42BB-DFA0-36E6-72AE04B0C9B4";
createNode nurbsCurve -n "Nail_Arrow_UpShape" -p "Nail_Arrow_Up";
	rename -uid "6A99F2A5-4EF1-7C70-1469-E0B3B3B52A66";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 7;
	setAttr ".cc" -type "nurbsCurve" 
		1 37 0 no 3
		38 0 9.9992300000000007 13.898834000000001 17.798387999999999 21.697965 25.597534
		 35.596760000000003 45.595986000000003 49.495555000000003 53.395130999999999 57.294685999999999
		 61.194290000000002 71.193520000000007 81.192749000000006 85.092258000000001 88.991923
		 92.891391999999996 96.791135999999995 106.79113599999999 116.79113599999999 120.690881
		 124.59035 128.490015 132.38952399999999 142.38875300000001 162.38875300000001 166.38875300000001
		 175.33302499999999 184.277297 188.277297 192.277297 201.22156899999999 210.165841
		 215.82269500000001 221.47954899999999 227.136403 232.79325800000001 236.79325800000001
		
		38
		7.8826092109875007e-016 5.5999999999999917 5.854783632927615e-017
		1.9998460000000011 5.5999999999999917 -4.4471999999414518e-006
		1.8457720000000009 5.5999999999999917 0.76454620000000018
		1.4141046000000008 5.5999999999999917 1.4141032
		0.76454380000000088 5.5999999999999917 1.8457728
		7.8826092109875007e-016 5.5999999999999917 1.9998452000000002
		7.8826092109875007e-016 5.5999999999999917 5.854783632927615e-017
		7.8826092109875007e-016 5.5999999999999917 1.9998452000000002
		-0.76454379999999933 5.5999999999999917 1.8457728
		-1.414104599999999 5.5999999999999917 1.4141032
		-1.8457719999999991 5.5999999999999917 0.76454620000000018
		-1.9998459999999993 5.5999999999999917 -4.4471999999414518e-006
		7.8826092109875007e-016 5.5999999999999917 5.854783632927615e-017
		-1.9998459999999993 5.5999999999999917 -4.4471999999414518e-006
		-1.8457719999999991 5.5999999999999917 -0.76453559999999987
		-1.414104599999999 5.5999999999999917 -1.4141192
		-0.76454379999999933 5.5999999999999917 -1.8457498000000001
		7.8826092109875007e-016 5.5999999999999917 -2
		7.8826092109875007e-016 5.5999999999999917 5.854783632927615e-017
		7.8826092109875007e-016 5.5999999999999917 -2
		0.76454380000000088 5.5999999999999917 -1.8457498000000001
		1.4141046000000008 5.5999999999999917 -1.4141192
		1.8457720000000009 5.5999999999999917 -0.76453559999999987
		1.9998460000000011 5.5999999999999917 -4.4471999999414518e-006
		7.8826092109875007e-016 5.5999999999999917 5.854783632927615e-017
		2.9840220143980878e-016 1.5999999999999917 5.854783632927615e-017
		2.9840220143980878e-016 1.5999999999999917 0.80000000000000016
		1.0245871357623221e-016 -8.8817841970012523e-015 5.854783632927615e-017
		2.9840220143980878e-016 1.5999999999999917 -0.79999999999999993
		2.9840220143980878e-016 1.5999999999999917 5.854783632927615e-017
		-0.79999999999999971 1.5999999999999917 5.854783632927615e-017
		1.0245871357623221e-016 -8.8817841970012523e-015 5.854783632927615e-017
		0.80000000000000038 1.5999999999999917 5.854783632927615e-017
		2.9840220143980878e-016 1.5999999999999917 0.80000000000000016
		-0.79999999999999971 1.5999999999999917 5.854783632927615e-017
		2.9840220143980878e-016 1.5999999999999917 -0.79999999999999993
		0.80000000000000038 1.5999999999999917 5.854783632927615e-017
		2.9840220143980878e-016 1.5999999999999917 5.854783632927615e-017
		;
createNode transform -n "Two_Way_Arrow";
	rename -uid "190953CE-48CC-A6D7-883D-72891A699A2A";
createNode nurbsCurve -n "Two_Way_ArrowShape" -p "Two_Way_Arrow";
	rename -uid "94CDC36C-4C51-7573-5723-C3B8EF8AB3A0";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 13;
	setAttr ".cc" -type "nurbsCurve" 
		1 23 0 no 3
		24 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23
		24
		-2.187163 -0.5 -0.5
		-2.187163 -0.5 0.5
		-2.187163 0.5 0.5
		-2.187163 0.5 -0.5
		-2.187163 -0.5 -0.5
		-3.812837 0 0
		-2.187163 -0.5 0.5
		-2.187163 0.5 0.5
		-3.812837 0 0
		-2.187163 0.5 -0.5
		-3.812837 0 0
		0 0 0
		3.812837 0 0
		2.187163 0.5 0.5
		2.187163 0.5 -0.5
		3.812837 0 0
		2.187163 0.5 -0.5
		2.187163 -0.5 -0.5
		3.812837 0 0
		2.187163 -0.5 -0.5
		2.187163 -0.5 0.5
		3.812837 0 0
		2.187163 -0.5 0.5
		2.187163 0.5 0.5
		;
createNode transform -n "Bear_Foot_Control";
	rename -uid "81512D92-4781-47FC-BCE1-6E81820A6BAC";
createNode nurbsCurve -n "Bear_Foot_ControlShape" -p "Bear_Foot_Control";
	rename -uid "95858888-4D68-AC27-54B0-749CC8FA88C8";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 12;
	setAttr ".cc" -type "nurbsCurve" 
		2 32 0 no 3
		35 0 0 0.03125 0.0625 0.09375 0.125 0.15625 0.1875 0.21875 0.25 0.28125 0.3125
		 0.34375 0.375 0.40625 0.4375 0.46875 0.5 0.53125 0.5625 0.59375 0.625 0.65625 0.6875
		 0.71875 0.75 0.78125 0.8125 0.84375000000000011 0.875 0.90625 0.9375 0.96875 1 1
		
		34
		1.2760358807837899 -0.97838365661065585 0
		0.90814202020255952 -0.69662064413776004 0
		0.38216986052950103 -0.50348432875199789 -8.4709398363252871e-019
		-0.099495232080049498 -0.41642425866385091 -1.9052679222664819e-018
		-0.8179434195163503 -0.49339324922786321 -1.4830322280713755e-018
		-1.3119400593594779 -0.86109674853764884 6.7274539123863291e-018
		-1.2779459679340806 -1.4713367597030014 -2.8882694283436788e-018
		-0.60334366183634358 -1.7036354285180624 -1.3373038982381737e-017
		-0.011917466409856942 -1.6990757065576552 -5.7173642517224206e-019
		0.5702844021096648 -1.4300397328167522 2.933244909221897e-017
		1.2048356243487746 -1.7235495734005259 7.1167824023927416e-018
		1.1089403113033698 -2.2491812442752837 -1.1097876902128557e-016
		0.38227812453539201 -2.2384939323474802 -1.6423150377622724e-016
		-0.19423914124238653 -2.1661528138748154 -1.92998001638554e-016
		-0.82373418287847866 -2.1942533359210592 -1.8536383724453082e-016
		-1.4353205624286198 -2.3094990856093935 -1.3071211359465302e-016
		-2.1478113629899105 -2.2756563786258233 -1.1845652744173071e-016
		-2.6497715163869153 -1.939371278349626 -1.2258325700549487e-016
		-2.7630913685427787 -1.3032204397322737 -1.868357371089103e-016
		-2.5054176871230989 -0.70619044669475461 -2.5830054477709535e-016
		-2.1032101903288907 -0.24862198960147786 -3.251080455544342e-016
		-1.5843686162324753 0.12719899303009496 -3.8141342345219598e-016
		-1.0029689934902117 0.38248169198978577 -4.2036792860554472e-016
		-0.42131578809042419 0.52595804679784708 -4.4312605036974659e-016
		0.19849613061491012 0.57116823817710305 -4.4842321471339974e-016
		0.81673662601764507 0.44968606313010318 -4.3676569896025518e-016
		1.3858269320371137 0.20758555690405656 -3.9816466614863837e-016
		1.9145110538903138 -0.1296906841666976 -3.3332295691815949e-016
		2.3439396207874093 -0.55888240118746091 -2.7860249287649361e-016
		2.64766910436926 -1.131178705669494 -2.4181129437627538e-016
		2.6176160844681737 -1.7788271973226091 -1.5947174925992623e-016
		2.2478234742110157 -2.1839312462172291 -4.8766755489312473e-017
		1.6342254918008643 -2.2134716564190371 0
		1.3410994874315185 -2.0800197971601282 0
		;
createNode nurbsCurve -n "Bear_Foot_ControlShape1" -p "Bear_Foot_Control";
	rename -uid "B3B86BF6-473B-DF2E-5DDB-BAAE9FEB2576";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 18;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		-1.2696684120546053 2.3094990856093935 7.5738152707983916e-021
		-1.355103987599422 1.9894488744397196 -7.4800598342921068e-017
		-1.578256781857672 1.8628097463805529 -4.0442472509667758e-017
		-1.7368401785606933 1.661118241691208 6.580933343716059e-021
		-1.8050909656161429 1.4137840648821234 4.0457095444940552e-017
		-1.7746054270660094 1.1590279342956187 7.4813622289192876e-017
		-1.6479748196654769 0.93587810351054879 9.7662040528035272e-017
		-1.4462772184349491 0.7772943225276987 1.0579975479070844e-016
		-1.1989456093872457 0.70904614966689339 9.7662040528035161e-017
		-0.94418751275990209 0.73953335867077241 7.4813622289192641e-017
		-0.72104025570078079 0.86616414402366182 4.0457095444940182e-017
		-0.56245595911385748 1.0678653731412511 6.5809333434291729e-021
		-0.49421246543532582 1.3151930552641216 -4.0442472509667844e-017
		-0.52469457450496215 1.5699585932937237 -7.4800598342921155e-017
		-0.65133974361129943 1.7930915032780432 -9.7645531954068031e-017
		-0.85298201522037476 1.9517623463094167 -1.0579975479070844e-016
		-1.1003508700761979 2.0199143218881388 -9.7645531954067994e-017
		-1.2696684120546053 2.3094990856093935 7.5738152707983916e-021
		;
createNode nurbsCurve -n "Bear_Foot_ControlShape2" -p "Bear_Foot_Control";
	rename -uid "4D5FD8ED-4651-DB0A-80FC-5C9D5156A116";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 23;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		1.2696684120546067 2.3094990856093927 4.5247657638222111e-016
		1.3551039875994233 1.9894488744397187 3.6933453777881835e-016
		1.5782567818576738 1.8628097463805529 4.2109245993543549e-016
		1.7368401785606951 1.6611182416912076 4.6773898814187173e-016
		1.8050909656161447 1.4137840648821229 5.0199246649480479e-016
		1.7746054270660108 1.1590279342956182 5.1894934160886466e-016
		1.6479748196654787 0.93587810351054834 5.1563383018721509e-016
		1.4462772184349508 0.77729432252769826 4.9296735819803953e-016
		1.198945609387247 0.70904614966689294 4.5402545768351787e-016
		0.94418751275990298 0.73953335867077197 4.0501310978418361e-016
		0.72104025570078212 0.86616414402366138 3.5325693120973891e-016
		0.56245595911385882 1.0678653731412506 3.0660938053947725e-016
		0.49421246543532715 1.3151930552641211 2.7235780185989287e-016
		0.52469457450496348 1.5699585932937232 2.5539947235000181e-016
		0.65133974361130076 1.7930915032780423 2.5871912578252132e-016
		0.85298201522037609 1.9517623463094158 2.8136784861662301e-016
		1.1003508700761993 2.0199143218881388 3.2032501712400782e-016
		1.2696684120546067 2.3094990856093927 4.5247657638222111e-016
		;
createNode nurbsCurve -n "Bear_Foot_ControlShape3" -p "Bear_Foot_Control";
	rename -uid "F1815970-4493-FBE8-6CB3-EDA1338E205D";
	setAttr -k off ".v";
	setAttr ".ove" yes;
	setAttr ".ovc" 10;
	setAttr ".cc" -type "nurbsCurve" 
		1 17 0 no 3
		18 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17
		18
		3.6946897904112177 0.64218970589797353 4.5246900256695025e-016
		3.6266386065840659 0.31799776951128589 3.6932696396354754e-016
		3.7687187258109178 0.10434412909920532 4.2108488612016468e-016
		3.8193249476843567 -0.14718552537798812 4.6773141432660087e-016
		3.7687223072905844 -0.39872426540960704 5.0198489267953393e-016
		3.6266433687565778 -0.61236796261865112 5.189417677935938e-016
		3.4129986699037471 -0.75444927863914901 5.1562625637194423e-016
		3.1614634005240712 -0.80505309461244723 4.9295978438276867e-016
		2.9099281311443979 -0.75444927863914835 4.5401788386824701e-016
		2.6962834322915685 -0.61236796261864868 4.050055359689128e-016
		2.5542044937575641 -0.39872426540960437 3.532493573944681e-016
		2.5036018533637825 -0.14718552537798768 3.0660180672420644e-016
		2.5542080752372387 0.10434412909920843 2.7235022804462206e-016
		2.6962881944640777 0.317997769511285 2.55391898534731e-016
		2.909938261257893 0.46005741661433097 2.587116019672505e-016
		3.1614634005240738 0.51076389001845435 2.813602748013522e-016
		3.4129885397902733 0.46005741661433097 3.2031744330873701e-016
		3.6946897904112177 0.64218970589797353 4.5246900256695025e-016
		;
select -ne :time1;
	setAttr ".o" 1;
	setAttr ".unw" 1;
select -ne :hardwareRenderingGlobals;
	setAttr ".otfna" -type "stringArray" 22 "NURBS Curves" "NURBS Surfaces" "Polygons" "Subdiv Surface" "Particles" "Particle Instance" "Fluids" "Strokes" "Image Planes" "UI" "Lights" "Cameras" "Locators" "Joints" "IK Handles" "Deformers" "Motion Trails" "Components" "Hair Systems" "Follicles" "Misc. UI" "Ornaments"  ;
	setAttr ".otfva" -type "Int32Array" 22 0 1 1 1 1 1
		 1 1 1 0 0 0 0 0 0 0 0 0
		 0 0 0 0 ;
	setAttr ".fprt" yes;
select -ne :renderPartition;
	setAttr -s 2 ".st";
select -ne :renderGlobalsList1;
select -ne :defaultShaderList1;
	setAttr -s 4 ".s";
select -ne :postProcessList1;
	setAttr -s 2 ".p";
select -ne :defaultRenderingList1;
select -ne :initialShadingGroup;
	setAttr ".ro" yes;
select -ne :initialParticleSE;
	setAttr ".ro" yes;
select -ne :defaultRenderGlobals;
	setAttr ".ren" -type "string" "vray";
select -ne :defaultResolution;
	setAttr ".pa" 1;
select -ne :hardwareRenderGlobals;
	setAttr ".ctrs" 256;
	setAttr ".btrs" 512;
select -ne :ikSystem;
	setAttr -s 4 ".sol";
// End of test 5.ma