# -*- coding: utf-8 -*-

import traceback
import logging
import datetime
from time import localtime
import os
import behave.test.test_axob as behave
from tool.axsbe_base import INSTRUMENT_TYPE, SecurityIDSource_SZSE

if __name__== '__main__':
    myname = os.path.split(__file__)[1][:-3]
    mytime = str(datetime.datetime(*localtime()[:6])).replace(':',"").replace('-',"").replace(" ","_")

    logger = logging.getLogger('main')
    logger.setLevel(logging.DEBUG)

    fh = logging.FileHandler(f'log/{myname}_{mytime}.log')
    # fh = logging.FileHandler(f'log/{myname}.log', mode='w')
    fh.setLevel(logging.DEBUG)

    sh = logging.StreamHandler()
    sh.setLevel(logging.WARNING)

    formatter_ts = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    formatter_nts = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
    fh.setFormatter(formatter_nts)
    sh.setFormatter(formatter_ts)

    logger.addHandler(fh)
    logger.addHandler(sh)
    logPack = logger.debug, logger.info, logger.warn, logger.error

    ###测试20220617所有有委托的只股票，全天
    fh.setLevel(logging.WARN)
    sh.setLevel(logging.ERROR)
    logger.info('starting TEST_axob_bat')
    data_source = "H:/AXOB_data_newP/20220620/sbe_20220620_all.log"
    all_inc=[200054, 200045, 200512, 200613, 200037, 200553, 200030, 200011, 300795, 200055, 200029, 200505, 200058, 2569, 300354, 200541, 200726, 300286, 200570, 300029, 300789, 200429, 300668, 695, 502, 2942, 586, 300475, 300870, 300103, 2872, 2917, 300953, 300530, 752, 300442, 200869, 300203, 300837, 300935, 300886, 301075, 200596, 300389, 2319, 300906, 2740, 3033, 300417, 300536, 301031, 300416, 300920, 2336, 2858, 200017, 200152, 200488, 2289, 2830, 300606, 23, 2919, 2991, 4, 300089, 809, 300960, 300858, 2209, 301041, 300405, 301037, 2700, 300756, 2058, 2021, 2870, 20, 300964, 300434, 300446, 300893, 301052, 300371, 301097, 300698, 300718, 300686, 300876, 2656, 300566, 300928, 300864, 300822, 300833, 300489, 1209, 300948, 2188, 300462, 301045, 301023, 300614, 301030, 2577, 301011, 2849, 2282, 300790, 3028, 300937, 2069, 2977, 300277, 300522, 300709, 300814, 300958, 300400, 300281, 2963, 3000, 301080, 300330, 300840, 300625, 606, 2159, 410, 300991, 300341, 3036, 301043, 2333, 2826, 300125, 300681, 300949, 300174, 3023, 300779, 300752, 906, 2907, 2295, 2553, 300683, 301029, 300321, 300720, 301059, 2855, 2592, 2880, 2729, 300955, 300550, 300938, 2632, 803, 2293, 3025, 300126, 300491, 2748, 300097, 300356, 2827, 611, 301021, 2264, 3003, 409, 300936, 300947, 301122, 300965, 32, 2875, 300596, 300820, 2147, 2832, 2831, 301085, 300861, 300856, 300788, 300802, 300609, 2575, 200012, 300753, 300538, 300736, 300154, 300786, 300862, 300399, 2859, 300715, 2634, 300407, 300064, 301213, 2842, 300056, 300791, 301026, 300696, 300150, 2953, 300808, 3002, 2250, 2337, 300486, 300542, 301179, 3017, 2845, 300394, 300501, 2735, 301005, 605, 300670, 300899, 300455, 301235, 300121, 2395, 759, 679, 2186, 300819, 300210, 1215, 300908, 2777, 300662, 300984, 2290, 576, 301119, 300963, 3005, 2338, 300823, 2790, 301035, 300615, 300616, 300853, 2749, 2841, 301082, 301032, 2231, 300818, 300982, 820, 300939, 300985, 300921, 668, 300989, 301135, 2763, 300995, 669, 2535, 300881, 2362, 2637, 2976, 300838, 720, 2998, 626, 2719, 2724, 301178, 300577, 3015, 300344, 301004, 2313, 300187, 300907, 301279, 300004, 300470, 2755, 2016, 2678, 2633, 300877, 801, 593, 300555, 300218, 2609, 300430, 2846, 2595, 300703, 300931, 300334, 2527, 300509, 300591, 2099, 300813, 2698, 2090, 300847, 2817, 300381, 300440, 300226, 300927, 300730, 300141, 2559, 300608, 300968, 2792, 300975, 300781, 301077, 48, 2616, 2911, 300030, 300196, 300176, 2984, 300761, 301051, 2694, 300480, 300220, 2287, 2238, 2381, 301015, 2654, 2318, 300805, 2962, 2040, 2462, 300291, 300913, 300325, 300548, 2869, 659, 2935, 301022, 300640, 301118, 300868, 301130, 2901, 300206, 301218, 301169, 755, 300562, 300322, 2992, 300441, 300575, 300543, 300996, 2868, 300898, 300161, 300134, 300957, 2989, 300885, 2089, 300559, 300449, 301100, 688, 2671, 300092, 300719, 300162, 697, 300290, 2882, 300796, 301229, 300137, 935, 2322, 2398, 2679, 561, 301061, 300466, 2785, 850, 30, 300771, 300589, 300520, 2055, 2820, 300411, 2566, 300644, 2574, 2095, 301025, 300587, 300902, 2088, 2908, 301111, 2379, 300387, 2900, 931, 300932, 1289, 300388, 2993, 2180, 2990, 2387, 2672, 411, 2148, 919, 2866, 300747, 300054, 2484, 300096, 2544, 2833, 301055, 976, 300135, 301079, 300648, 300859, 300107, 1205, 300285, 300854, 300572, 300402, 300962, 2214, 300585, 300195, 300597, 300227, 403, 2084, 1207, 300903, 300675, 2779, 2184, 301007, 2757, 300866, 301148, 2583, 300988, 2627, 300368, 300691, 1201, 300627, 300809, 300630, 2573, 300262, 881, 301036, 2793, 2324, 300579, 2225, 300242, 429, 301167, 300567, 301040, 3012, 300519, 2813, 609, 2369, 301196, 2320, 300766, 2795, 766, 300289, 200625, 2025, 300674, 300998, 915, 2775, 300560, 1216, 300739, 300830, 300641, 2173, 300943, 2105, 2521, 2346, 300890, 300895, 300055, 300863, 2006, 300245, 2690, 2528, 2296, 2905, 2515, 300231, 2920, 300183, 300436, 300732, 300516, 2368, 300302, 2955, 300214, 301185, 301190, 708, 300236, 510, 300074, 300235, 2925, 892, 301133, 2557, 300712, 300479, 300843, 300190, 2358, 430, 2347, 300221, 300867, 301288, 2865, 2316, 2361, 300725, 300412, 300140, 300119, 301069, 2688, 300726, 301126, 922, 885, 301168, 2420, 300351, 541, 300042, 300951, 300571, 2906, 300005, 300252, 300888, 300318, 2227, 300167, 2474, 300072, 153, 2593, 300335, 300783, 300403, 300201, 300452, 300700, 300336, 68, 159, 300464, 150, 635, 2815, 300992, 300256, 985, 301038, 2164, 2190, 2683, 2490, 300755, 300273, 811, 1296, 2982, 300860, 869, 301237, 300367, 301078, 300651, 58, 902, 2017, 2378, 2597, 35, 300487, 301110, 2329, 2046, 300310, 300404, 2751, 301191, 2879, 2428, 300460, 300193, 300576, 300967, 300439, 2111, 300510, 2279, 608, 300941, 300420, 300511, 2149, 603, 300619, 300638, 1308, 2928, 2762, 300283, 300891, 2918, 300561, 300048, 300483, 407, 2300, 301071, 2416, 300219, 28, 301107, 2626, 300006, 2523, 2605, 14, 2028, 301160, 2782, 2586, 917, 300080, 2772, 2392, 300494, 2103, 2087, 300969, 300981, 2969, 2286, 300332, 300350, 2664, 2727, 911, 2020, 962, 300584, 300110, 2206, 300558, 301259, 555, 300323, 300034, 2063, 2441, 300690, 55, 300551, 692, 2705, 300438, 889, 600, 1234, 301183, 1317, 2417, 798, 973, 2780, 2403, 2332, 300485, 301137, 300100, 417, 300278, 2873, 300248, 300581, 300127, 300329, 2897, 2676, 2375, 2215, 300018, 300086, 300340, 777, 300299, 29, 802, 2560, 300879, 2885, 300128, 525, 2840, 2686, 300769, 2649, 533, 300304, 300664, 300132, 300774, 88, 300194, 2067, 2022, 2651, 300053, 300222, 707, 300484, 300366, 301200, 300692, 2043, 2851, 2580, 300046, 300598, 300467, 2608, 2445, 301092, 2488, 300541, 301060, 300919, 2650, 503, 900, 300178, 300044, 2533, 6, 2746, 2471, 300191, 2791, 300143, 2216, 300012, 2085, 300842, 2968, 59, 300264, 300994, 300451, 301211, 2642, 419, 301163, 819, 905, 300533, 2452, 300294, 2996, 978, 967, 2167, 2483, 2281, 2581, 300671, 2348, 300102, 751, 2693, 2136, 300244, 952, 300212, 2045, 2563, 948, 908, 301236, 2543, 300331, 851, 2137, 300131, 2226, 2837, 2038, 2662, 56, 791, 596, 2549, 523, 685, 2039, 300751, 2175, 300180, 2243, 300145, 589, 300379, 826, 928, 2681, 2803, 301136, 300139, 300228, 2189, 301088, 300238, 2177, 530, 2334, 2572, 300111, 2201, 300172, 2562, 2311, 2697, 2174, 717, 300036, 300197, 2733, 3037, 301125, 2516, 796, 2606, 300582, 2867, 721, 300497, 300503, 2959, 2988, 2267, 416, 2701, 2753, 813, 300306, 301216, 300363, 300534, 2822, 65, 300741, 2434, 300408, 2677, 300532, 2628, 2054, 2948, 738, 2486, 2015, 988, 301116, 300894, 888, 2154, 560, 99, 612, 936, 300603, 918, 2725, 877, 3009, 401, 2141, 619, 300831, 657, 300529, 2285, 2922, 2053, 2130, 2059, 886, 2047, 300386, 300233, 300827, 300428, 2640, 2413, 2350, 893, 732, 300471, 2299, 726, 2341, 50, 2507, 2051, 949, 2571, 2584, 300945, 2564, 300297, 2064, 300081, 301198, 655, 300271, 2353, 300782, 545, 2745, 2354, 2283, 300199, 300708, 2066, 581, 2530, 727, 969, 90, 2166, 2370, 300085, 2646, 2548, 300047, 2447, 300079, 901, 861, 300360, 2325, 793, 2805, 2081, 2314, 300463, 2513, 2297, 2076, 2493, 300173, 2931, 301181, 300093, 2702, 300148, 2278, 2958, 1203, 2588, 300613, 2194, 3039, 2941, 21, 423, 839, 2187, 2458, 923, 951, 639, 301089, 2611, 2721, 2682, 2233, 927, 2596, 300021, 300253, 300803, 300505, 2425, 301217, 300002, 2389, 2807, 2926, 300676, 300223, 2342, 300083, 2598, 408, 2009, 514, 300061, 2932, 2465, 300039, 402, 300748, 300793, 300284, 2579, 2036, 883, 2235, 2463, 592, 2335, 2113, 301187, 2512, 2510, 2309, 786, 300017, 2284, 300773, 300413, 2181, 300303, 2550, 2139, 2140, 300346, 2145, 636, 8, 300263, 563, 3040, 300458, 2041, 2390, 60, 300347, 300040, 2540, 300065, 300502, 735, 2590, 3006, 300568, 623, 2192, 975, 301215, 300075, 300507, 2582, 2481, 300217, 2739, 2222, 300033, 2384, 2328, 300287, 2108, 862, 926, 2601, 39, 2110, 681, 2589, 2307, 2242, 300727, 2252, 2258, 2673, 300315, 2429, 2443, 2599, 2824, 301286, 2892, 2456, 2078, 300009, 2648, 650, 2304, 2945, 2717, 300373, 963, 2249, 300144, 300115, 300763, 970, 505, 413, 2736, 300693, 2001, 729, 300546, 930, 2277, 3032, 300376, 301155, 629, 2263, 1208, 2291, 46, 2636, 2539, 2128, 1979, 833, 716, 2269, 2665, 683, 3022, 66, 599, 300037, 2091, 300007, 300224, 2821, 2431, 2371, 667, 2600, 300164, 2057, 2255, 2864, 519, 2426, 2657, 300003, 2002, 830, 2457, 2380, 526, 301, 400, 2613, 736, 300182, 2074, 1896, 2478, 2142, 960, 938, 2131, 2424, 722, 300595, 767, 157, 2104, 2270, 69, 300261, 2400, 2195, 965, 300026, 300058, 155, 2236, 2030, 300393, 831, 2132, 713, 1212, 2617, 2273, 2256, 2797, 709, 300459, 2349, 422, 2639, 2183, 2971, 876, 2230, 301156, 2101, 151, 300343, 2080, 2121, 2050, 37, 166, 987, 933, 2271, 2129, 671, 2204, 860, 807, 909, 661, 982, 800, 300731, 2480, 2241, 2326, 627, 753, 630, 564, 628, 2407, 2475, 2467, 2388, 2125, 300750, 2126, 2621, 723, 300337, 2536, 300094, 70, 2497, 570, 3816, 2610, 2432, 2460, 300052, 2439, 595, 2155, 2, 100, 762, 2487, 17, 2466, 1, 2506, 2454, 2703, 2909, 651, 301238, 2094, 821, 300059, 1270, 2630, 25, 957]

    try:
        behave.TEST_mu_bat(data_source, all_inc, batch_nb=16, bgn_batch=0, SecurityIDSource=SecurityIDSource_SZSE, instrument_type=INSTRUMENT_TYPE.STOCK, logPack=logPack) #
    except Exception as e:
        logger.error(f'{traceback.format_exc()}')
