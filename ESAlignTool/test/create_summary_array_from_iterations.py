#!/usr/bin/env python

txtfile = "output_20220609/AlignmentFile_iter11.txt"
myfile = "inputMatrixElements_cfi.py"
detector_labels = ["ESmR", "ESmF", "ESpF", "ESpR"]
spatial_variables = ["dAlpha", "dBeta", "dGamma", "dX", "dY", "dZ"]

map_detector = {"-R":"ESmR", "-F":"ESmF", "+F":"ESpF", "+R":"ESpR"}

cms_init = {
    "ESmR" : { "dX": 0., "dY": 0., "dZ": -308.306, "dAlpha": 0., "dBeta": 0., "dGamma": 0., },
    "ESmF" : { "dX": 0., "dY": 0., "dZ": -303.846, "dAlpha": 0., "dBeta": 0., "dGamma": 0., },
    "ESpF" : { "dX": 0., "dY": 0., "dZ":  303.846, "dAlpha": 0., "dBeta": 0., "dGamma": 0., },
    "ESpR" : { "dX": 0., "dY": 0., "dZ":  308.306, "dAlpha": 0., "dBeta": 0., "dGamma": 0., },
}

#Aligned, P-dP
result_manual = {
    "ESmR" : { "dX": 0.00744316, "dY": -0.584197, "dZ": -308.899, "dAlpha": 0.00183372  , "dBeta": 0.00127591 , "dGamma": -0.000342555 },
    "ESmF" : { "dX": -0.0970111, "dY": -0.517947, "dZ": -304.364, "dAlpha": 0.0024619   , "dBeta": 0.00136538 , "dGamma": 0.000296892 } ,
    "ESpF" : { "dX": 0.30871   , "dY": -0.884685, "dZ": 304.146 , "dAlpha": -0.000306388, "dBeta": 0.000279071, "dGamma": 0.00137031 }  ,
    "ESpR" : { "dX": 0.235793  , "dY": -0.861538, "dZ": 308.782 , "dAlpha": -0.0025668  , "dBeta": 0.000428364, "dGamma": 0.00130676 }  ,
}

def init(): #{{{
    d = {}
    for l in detector_labels:
        d[l] = {}
        for v in spatial_variables:
            d[l][v] = 0.
    return d
#}}}
def print_content(d): #{{{
    print "\n------------------------------\n"
    for l in detector_labels:
        for v in spatial_variables:
            keyword = l + v
            print "%s: %.4f" % (keyword, d[l][v])
    print "\n------------------------------\n"
#}}}
def load_from_inputMatrix(): #{{{
    global dict_data, list_keywords

    fin = open(myfile, 'r')
    #--------------------------------------------------
    for line in fin.readlines():
        if '#' in line or not '.Iter' in line: continue

        # method 2
        key = line.split('_')[1].split()[0]
        value = float( line.strip().split('(')[1].split(')')[0] )
        l = key[:4]
        v = key[4:]
        dict_data[l][v] += value

        if key=='ESmRdAlpha': print "%s %.5f" % (key, value)

        continue

        # method 1
        found = False
        for l in detector_labels:
            print ">>> first layer", l
            for v in spatial_variables:
                print ">>> 2nd layer", v
                keyword = l + v
                if keyword in line:
                    found = True
                    value = float( line.strip().split('(')[1].split(')')[0] )
                    dict_data[l][v] += value

                    if keyword=='ESpFdX': print "%s %.4f" % (keyword, value)

                    if found: break
            if found: break
    #--------------------------------------------------
    fin.close()

    print_content(dict_data)
#}}}

def load():
    result = init()
    start, counter = False, 0

    fin = open(txtfile, 'r')
    for line in fin.readlines():
        if 'Aligned, P-dP' in line: start = True
        if start and counter<9:
            info = line.strip()
            print info

            #-F X: -0.0970111, Y: -0.517947, Z: -304.364
            #-R X: 0.00744316, Y: -0.584197, Z: -308.899
            #+F X: 0.30871, Y: -0.884685, Z: 304.146
            #+R X: 0.235793, Y: -0.861538, Z: 308.782
            #-F Alpha: 0.0024619, Beta: 0.00136538, Gamma: 0.000296892
            #-R Alpha: 0.00183372, Beta: 0.00127591, Gamma: -0.000342555
            #+F Alpha: -0.000306388, Beta: 0.000279071, Gamma: 0.00137031
            #+R Alpha: -0.0025668, Beta: 0.000428364, Gamma: 0.00130676

            if counter > 0:
                det = map_detector[ info.split()[0] ]
                var1 = info[3:].split(", ")[0]
                var2 = info[3:].split(", ")[1]
                var3 = info[3:].split(", ")[2]
                key1, value1 = 'd'+var1.split(": ")[0], var1.split(": ")[1]
                key2, value2 = 'd'+var2.split(": ")[0], var2.split(": ")[1]
                key3, value3 = 'd'+var3.split(": ")[0], var3.split(": ")[1]

                result[det][key1] = value1
                result[det][key2] = value2
                result[det][key3] = value3

            counter += 1

        elif counter==9: break

    fin.close()
    return result

def diff(): #{{{
    global dict_data, result
    for l in detector_labels:
        for v in spatial_variables:
            if v == "dZ":
                difference = float(result[l][v]) - cms_init[l][v]
                dict_data[l][v] = "%.3f" % difference
            else:
                dict_data[l][v] = result[l][v]
#}}}
map_cpp_array = { #{{{
    "dAlpha" : "double Ar_Alpha[]",
    "dBeta"  : "double Ar_Beta[]",
    "dGamma" : "double Ar_Gamma[]",
    "dX"     : "double Ar_X[]",
    "dY"     : "double Ar_Y[]",
    "dZ"     : "double Ar_Z[]",
}
#}}}
def report(dict_data): #{{{
    print "\n------------------------------\n"

    for v in spatial_variables:
        counter, summary = 0, ""
        for l in detector_labels:
            counter += 2
            summary += "%s, " % dict_data[l][v]
            summary += "%s"   % dict_data[l][v]
            if counter < 8: summary += ", "

        print "%s = {%s};" % (map_cpp_array[v], summary)

    print "\n------------------------------\n"
#}}}

#==================================================


if __name__ == "__main__":
    dict_data = init()
    result = load()

    #print_content(cms_init)
    #print_content(result)

    diff()
    report(dict_data)

## double Ar_X[] = { ES- rear, ES- rear, ES- front, ES- front, ES+ front, ES+ front, ES+ rear, ES+ rear}
#double Ar_Alpha[] = {0.0014, 0.0014, 0.0014, 0.0014, -0.0013, -0.0013, -0.0017, -0.0017};
#double Ar_Beta[] = {0.0005, 0.0005, 0.0008, 0.0008, 0.0001, 0.0001, 0.0004, 0.0004};
#double Ar_Gamma[] = {0.0000, 0.0000, 0.0006, 0.0006, 0.0008, 0.0008, 0.0006, 0.0006};
#double Ar_X[] = {-0.303, -0.303, -0.284, -0.284, 0.324, 0.324, 0.357, 0.357};
#double Ar_Y[] = {-0.462, -0.462, -0.477, -0.477, -0.932, -0.932, -0.905, -0.905};
#double Ar_Z[] = {-0.616, -0.616, -0.443, -0.443,  0.321,  0.321,  0.464, 0.464};
