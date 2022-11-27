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
    # fh.setLevel(logging.WARN)
    # sh.setLevel(logging.ERROR)
    logger.info('starting TEST_axob_bat')
    data_source = "H:/AXOB_data_newP/20220616/sbe_20220616_all.log"
    all_inc=[200045, 200512, 200992, 200530, 200706, 200521, 200541, 200054, 200020, 200505, 200553, 200613, 201872, 200011, 200726, 611, 200771, 200488, 300023, 200761, 301051, 2147, 2618, 200869, 971, 200012, 300492, 673, 300312, 802, 2535, 2668, 300356, 2219, 2200, 2927, 300923, 806, 301045, 2021, 2931, 300325, 300178, 300064, 2656, 2005, 300795, 2321, 300038, 300367, 301043, 638, 972, 2464, 301023, 300798, 300897, 2972, 300069, 2187, 2188, 3004, 300905, 300635, 809, 2995, 300392, 300269, 301042, 300530, 3013, 300909, 300989, 301008, 526, 301037, 2072, 2501, 2857, 2358, 3036, 301196, 2592, 2356, 7, 301024, 301061, 300844, 300965, 300736, 300907, 300952, 410, 586, 300434, 2058, 301053, 3018, 300557, 300201, 301062, 300977, 300959, 301075, 1270, 2816, 2956, 300938, 301076, 300876, 2586, 300906, 300837, 2933, 300461, 2599, 2875, 300899, 300948, 300583, 2427, 2632, 300980, 2514, 3020, 300910, 300717, 300594, 300126, 2846, 23, 300756, 300417, 300103, 301066, 300903, 300779, 301031, 300889, 2199, 300814, 2896, 2870, 301108, 300849, 2981, 300518, 300886, 2980, 300669, 2973, 300689, 889, 2289, 2102, 300997, 301178, 301122, 2394, 300514, 2388, 2930, 300611, 301100, 300396, 300901, 2022, 3025, 300892, 2295, 301167, 2868, 300986, 301002, 2880, 2963, 2090, 2953, 300442, 2755, 2319, 300822, 300928, 1210, 300713, 300695, 2327, 1202, 300882, 301032, 2968, 2890, 301129, 301199, 301068, 2864, 300853, 2749, 301106, 3028, 300522, 2911, 300336, 2899, 2856, 300964, 2802, 301148, 2862, 301013, 301063, 300935, 300495, 301040, 2830, 300469, 300112, 301188, 300335, 300840, 300797, 301288, 300265, 300154, 300816, 300512, 300255, 2983, 300845, 300823, 301005, 300857, 300774, 3005, 1266, 668, 301117, 3031, 2928, 663, 300489, 301003, 300908, 2640, 2076, 2631, 301017, 2884, 300950, 300824, 300536, 300660, 301047, 2159, 2949, 300993, 2753, 2813, 1267, 300968, 300301, 525, 2451, 301130, 300946, 2951, 301011, 300673, 300626, 952, 300670, 2901, 300690, 3017, 301181, 300273, 300210, 300493, 2395, 300554, 2403, 2467, 2347, 2381, 2768, 301087, 2029, 300462, 300749, 301052, 300939, 300915, 300400, 2847, 300176, 2227, 301159, 300875, 300513, 301213, 300870, 301012, 2177, 2767, 2853, 300277, 301190, 300942, 2921, 1208, 301009, 300701, 300859, 1216, 2134, 544, 300150, 2575, 300187, 300555, 2193, 2715, 2829, 300447, 300042, 301050, 2287, 2290, 995, 2479, 301046, 300864, 300622, 2691, 300486, 2542, 301131, 300388, 300739, 300440, 300407, 300683, 301041, 300854, 2644, 2694, 300470, 2940, 531, 2845, 300667, 2262, 2898, 301119, 2362, 2835, 301123, 300620, 300359, 301029, 2527, 300731, 839, 301057, 300577, 300913, 300981, 2595, 2751, 2296, 3000, 300898, 2225, 300758, 300430, 2231, 300791, 300521, 609, 300881, 2849, 300632, 301193, 300941, 2858, 2173, 301025, 301166, 565, 2820, 301185, 301027, 2992, 301007, 3043, 3011, 300381, 300807, 301126, 300932, 300341, 2808, 300230, 70, 697, 301102, 301257, 301268, 300006, 300211, 300867, 300262, 300828, 300675, 2913, 300096, 300044, 2014, 300545, 2848, 300684, 2609, 300195, 300076, 300140, 300953, 300152, 300833, 300525, 300508, 300318, 1205, 300424, 2959, 573, 300634, 300768, 48, 2038, 2117, 300406, 300423, 1228, 2903, 300973, 2796, 2150, 2095, 301163, 300259, 3038, 301088, 300032, 300631, 61, 856, 300107, 300276, 908, 955, 1696, 300349, 301183, 2859, 300066, 2741, 2860, 300567, 300645, 2490, 2950, 300591, 2228, 300705, 300609, 560, 56, 2678, 301001, 300548, 300425, 1215, 300664, 300368, 55, 2003, 300345, 300086, 2833, 300120, 679, 2982, 301226, 301168, 300097, 300607, 300547, 301150, 1308, 2877, 300863, 300566, 2406, 2189, 300893, 300270, 2553, 2055, 300218, 2137, 2935, 300621, 1296, 300992, 1219, 2420, 2785, 300143, 682, 2515, 300596, 2937, 300550, 301118, 300762, 301018, 3010, 300929, 300871, 2910, 300221, 300137, 300996, 300078, 300982, 2957, 300925, 300441, 501, 300313, 2929, 28, 301097, 2961, 300709, 2523, 300196, 300573, 2615, 300245, 300610, 300659, 300519, 300020, 301198, 300657, 300987, 2254, 2724, 3042, 301069, 655, 2626, 2247, 300449, 300011, 2148, 300719, 3002, 2712, 548, 300933, 592, 300055, 2946, 300093, 300119, 2198, 300467, 631, 300516, 701, 300902, 2873, 301217, 2103, 300589, 2828, 409, 2651, 300922, 300327, 300226, 2667, 2863, 2947, 520, 300162, 2084, 608, 2303, 300640, 300138, 301206, 2391, 903, 2614, 300266, 301191, 300510, 2039, 96, 300538, 301137, 2275, 300153, 300742, 920, 2421, 300040, 2788, 300681, 2398, 300114, 30, 2566, 2616, 8, 2541, 2683, 300578, 561, 300776, 300071, 89, 2522, 766, 3019, 300394, 2345, 755, 300571, 300504, 301133, 300825, 300022, 403, 300706, 757, 2696, 300213, 300025, 2831, 300497, 2169, 300331, 300110, 300344, 300835, 300173, 300369, 698, 300175, 2357, 300785, 300455, 300696, 2133, 301092, 300682, 737, 300593, 962, 300572, 2727, 2818, 2401, 300945, 300404, 300855, 2320, 300943, 300678, 300856, 2730, 2383, 300275, 300940, 790, 300191, 2622, 2309, 300300, 301160, 2918, 581, 2495, 300384, 1289, 2153, 300279, 2437, 300520, 300796, 2762, 300145, 678, 300214, 2033, 2397, 2454, 68, 301263, 300722, 300444, 710, 300725, 564, 300278, 2758, 300726, 620, 300091, 2645, 300560, 300439, 1319, 421, 300917, 6, 2737, 811, 2649, 300624, 919, 300751, 917, 2925, 2031, 301038, 300067, 300575, 3021, 300310, 925, 2161, 2288, 2906, 300832, 300692, 300228, 536, 300232, 2792, 300570, 514, 558, 978, 2917, 2908, 1234, 605, 2213, 300220, 300036, 2423, 300841, 413, 2675, 2111, 2149, 823, 300842, 2922, 2314, 2285, 2915, 300105, 301177, 980, 2469, 2154, 639, 2815, 300511, 2435, 300168, 612, 300896, 2158, 2272, 300285, 2676, 40, 300048, 2503, 2416, 2106, 300074, 300793, 300305, 2837, 300602, 2999, 2046, 2498, 300579, 300766, 300291, 300653, 2850, 300203, 300098, 300198, 2685, 2196, 300322, 301125, 2233, 2725, 2546, 2412, 300113, 650, 300770, 2361, 967, 927, 2752, 911, 300024, 300460, 300357, 2248, 301039, 798, 300603, 2043, 2902, 2172, 2232, 300587, 996, 2135, 300435, 300647, 300452, 2017, 426, 300809, 2984, 2461, 2165, 576, 300558, 300165, 300546, 300415, 300082, 2627, 300306, 2297, 836, 2126, 2302, 300046, 300451, 301207, 2646, 2167, 300490, 652, 300352, 401, 2852, 301187, 2344, 2920, 597, 969, 2608, 751, 300671, 2958, 2141, 300650, 2082, 417, 2226, 2643, 2378, 300132, 2317, 300487, 2081, 300792, 2440, 2283, 2116, 2540, 300775, 2642, 976, 50, 2723, 2746, 2278, 300021, 2419, 420, 300169, 300528, 539, 2365, 301078, 2119, 300131, 990, 300324, 301111, 11, 672, 503, 36, 553, 300054, 2370, 49, 2048, 31, 2483, 570, 882, 300234, 300323, 2203, 300355, 2665, 300209, 717, 2023, 300761, 2452, 2484, 2301, 2840, 300083, 2004, 2786, 300443, 300499, 300569, 913, 300049, 300263, 510, 720, 19, 2745, 65, 2705, 2936, 2246, 2277, 2810, 300332, 2655, 2063, 2765, 300483, 2075, 2747, 2941, 2932, 300353, 300879, 997, 2693, 2217, 2533, 300699, 2630, 300039, 2276, 300238, 735, 300687, 818, 2438, 953, 2042, 300151, 2803, 300229, 34, 300160, 300250, 2821, 301089, 300636, 2766, 2279, 29, 899, 300204, 300043, 999, 2791, 300184, 596, 300613, 2139, 958, 300328, 2138, 727, 2434, 2372, 598, 2065, 300472, 2662, 300760, 546, 300532, 2339, 2330, 2721, 2897, 39, 1313, 2263, 300655, 300239, 46, 423, 300748, 877, 513, 2252, 2584, 2410, 2905, 2068, 300366, 300598, 686, 861, 931, 716, 2580, 2270, 300001, 300253, 300738, 2659, 78, 300007, 537, 300311, 300085, 300600, 1318, 2223, 657, 667, 838, 2078, 2806, 584, 2682, 2110, 300251, 300471, 758, 2739, 2756, 883, 2805, 793, 2389, 1212, 617, 2085, 988, 300401, 66, 2053, 2010, 300688, 2266, 767, 300212, 2431, 2414, 300072, 2409, 300031, 2041, 300630, 966, 2221, 300351, 2261, 2049, 300712, 2354, 300003, 2759, 2091, 2703, 2530, 2702, 488, 300316, 795, 2386, 505, 2057, 2030, 935, 2701, 300661, 300219, 761, 559, 2943, 2728, 2064, 300249, 300413, 898, 300454, 300142, 2192, 2549, 599, 300677, 731, 2156, 2179, 2561, 300179, 2625, 2080, 680, 2380, 2100, 2926, 828, 300144, 2568, 300224, 300013, 910, 300236, 2002, 729, 2455, 2708, 959, 425, 2216, 2292, 300724, 2235, 2601, 300079, 300136, 300919, 2256, 887, 2079, 300094, 829, 300373, 810, 2750, 2422, 2635, 2673, 300075, 2500, 3032, 300185, 671, 300612, 2938, 893, 543, 300409, 799, 300398, 998, 733, 922, 300101, 863, 300568, 300437, 572, 300708, 1896, 2324, 2180, 2284, 2390, 300772, 2222, 300458, 2517, 2236, 554, 408, 568, 709, 2590, 300296, 707, 629, 547, 2478, 2436, 1979, 768, 301298, 2585, 963, 300261, 563, 300393, 300534, 875, 300015, 2506, 830, 815, 2424, 825, 778, 728, 2353, 300073, 300217, 2132, 2371, 2239, 2895, 736, 2507, 2839, 2182, 2125, 800, 2291, 2443, 498, 2648, 25, 300122, 2807, 661, 400, 2539, 300088, 2074, 3022, 712, 2062, 2271, 2197, 937, 932, 2061, 300337, 750, 2537, 2202, 722, 2657, 155, 2194, 2268, 3816, 2545, 301, 300498, 63, 2505, 300595, 2407, 300390, 2531, 300803, 630, 2218, 300459, 12, 552, 2385, 2497, 2797, 300118, 2183, 876, 151, 2475, 703, 2027, 2610, 2607, 2384, 2555, 2241, 2415, 300026, 300750, 2124, 651, 2176, 762, 2639, 2349, 2466, 2060, 776, 100, 792, 625]

    try:
        behave.TEST_mu_bat(data_source, all_inc, batch_nb=16, bgn_batch=0, SecurityIDSource=SecurityIDSource_SZSE, instrument_type=INSTRUMENT_TYPE.STOCK, logPack=logPack) #
    except Exception as e:
        logger.error(f'{traceback.format_exc()}')
