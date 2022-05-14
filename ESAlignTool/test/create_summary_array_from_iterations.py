#!/usr/bin/env python

myfile = "inputMatrixElements_cfi.py"
detector_labels = ["ESmR", "ESmF", "ESpF", "ESpR"]
spatial_variables = ["dAlpha", "dBeta", "dGamma", "dX", "dY", "dZ"]

def init():
    d = {}
    for l in detector_labels:
        d[l] = {}
        for v in spatial_variables:
            d[l][v] = 0.
    return d

def print_result(d):
    print "\n------------------------------\n"
    for l in detector_labels:
        for v in spatial_variables:
            keyword = l + v
            print "%s: %.4f" % (keyword, d[l][v])
    print "\n------------------------------\n"

def load():
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

    print_result(dict_data)

map_cpp_array = {
    "dAlpha" : "double Ar_Alpha[]",
    "dBeta"  : "double Ar_Beta[]",
    "dGamma" : "double Ar_Gamma[]",
    "dX"     : "double Ar_X[]",
    "dY"     : "double Ar_Y[]",
    "dZ"     : "double Ar_Z[]",
}

def report():
    global dict_data

    for v in spatial_variables:
        counter, summary = 0, ""
        for l in detector_labels:
            counter += 2
            summary += "%.4f, " % dict_data[l][v]
            summary += "%.4f"   % dict_data[l][v]
            if counter < 8: summary += ", "

        print "%s = {%s};" % (map_cpp_array[v], summary)

    print "\n------------------------------\n"

#==================================================

if __name__ == "__main__":
    dict_data = init()
    load()
    report()

## double Ar_X[] = { ES- rear, ES- rear, ES- front, ES- front, ES+ front, ES+ front, ES+ rear, ES+ rear}
#double Ar_Alpha[] = {0.0014, 0.0014, 0.0014, 0.0014, -0.0013, -0.0013, -0.0017, -0.0017};
#double Ar_Beta[] = {0.0005, 0.0005, 0.0008, 0.0008, 0.0001, 0.0001, 0.0004, 0.0004};
#double Ar_Gamma[] = {0.0000, 0.0000, 0.0006, 0.0006, 0.0008, 0.0008, 0.0006, 0.0006};
#double Ar_X[] = {-0.303, -0.303, -0.284, -0.284, 0.324, 0.324, 0.357, 0.357};
#double Ar_Y[] = {-0.462, -0.462, -0.477, -0.477, -0.932, -0.932, -0.905, -0.905};
#double Ar_Z[] = {-0.616, -0.616, -0.443, -0.443,  0.321,  0.321,  0.464, 0.464};
