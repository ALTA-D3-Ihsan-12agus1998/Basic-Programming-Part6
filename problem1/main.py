def compare(a, b) :
    pattern = ""
    for i in range(len(a)) :
        for j in range(i + 1, len(a) + 1) :
            if a[i:j] in b and len(a[i:j]) > len(pattern) :
                pattern = a[i:j]
    
    return pattern

if __name__ == '__main__':
    print(compare("AKA", "AKASHI"))  # AKA
    print(compare("KANGOORO", "KANG"))  # KANG
    print(compare("KI", "KIJANG"))  # KI
    print(compare("KUPU-KUPU", "KUPU"))  # KUPU
    print(compare("ILALANG", "ILA"))  # ILA
