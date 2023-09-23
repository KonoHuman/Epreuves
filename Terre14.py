def verifier_suite_croissante():
    for i in range(1, len(suite)):
        if suite[i] < suite[i-1]:
            return False
    return True if suite[i] > suite[i-1] else False


        
suite = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(verifier_suite_croissante())
