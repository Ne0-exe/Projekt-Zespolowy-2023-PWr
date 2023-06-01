def f(Impact):
    if Impact == 0:
        return 0
    else:
        return 1.176
    
def baseScore(AV, AC, Au, C, I, A):


    Exploitability = 20 * AC * Au * AV

    Impact = 10.41 * (1 - (1 - C) * (1 - I) * (1 - A))

    BaseScore = (.6*Impact +.4*Exploitability-1.5)*f(Impact)

    return round(BaseScore,1)


AccessVector = [0.395, 0.646, 1]
AccessComplexity = [0.35, 0.61, 0.71]
Authentication = [0.704, 0.56, 0.45]
ConfImpact = [0, 0.275, 0.660]
IntegImpact = [0, 0.275, 0.660]
AvailImpact = [0, 0.275, 0.660]

for AV in AccessVector:
    for AC in AccessComplexity:
        for Au in Authentication:
            for C in ConfImpact:
                for I in IntegImpact:
                    for A in AvailImpact:
                        print(abs(baseScore(AV, AC, Au, C, I, A)))