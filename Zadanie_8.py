import math


attackVector = [0.85, 0.62, 0.55, 0.2]
attackComplexity = [0.77, 0.44]
scope = [1, 0]
userInteraction = [0.85, 0.62]
confidentiality = [0, 0.56, 0.22]
integrity = [0, 0.56, 0.22]
availability = [0, 0.56, 0.22]
privilegesRequired = [0.85, 0.62, 0.27]
privilegesRequiredScopeChanged= [0.85, 0.68, 0.5]


def cal_iss(confidentiality, integrity, availability):
    return 1 - ((1 - confidentiality) * (1 - integrity) * (1 - availability))

def cal_exploitability(attackVector, attackComplexity, privilegesRequired, userInteraction):
    return 8.22 * attackVector * attackComplexity * privilegesRequired * userInteraction

def cal_impact(scope, iss):
    if(scope == 0):
        return 7.52 * (iss - 0.029) - 3.25 * (iss-0.02)**15
    elif(scope == 1):
        return 6.42 * iss

def cal_base(impact, exploitability, scope):
    if(impact <= 0):
        return 0
    elif(scope == 0):
        #ceil
        min_val = min((impact + exploitability), 10)
        return math.ceil(min_val * 10) / 10
    elif(scope == 1):
        min_val = min(1.08 * (impact + exploitability), 10)
        return math.ceil(min_val * 10) / 10

f = open(r"\path\to\file.txt", "w")

for AV in attackVector:
    for AC in attackComplexity:
        for S in scope:
            for UI in userInteraction:
                for C in confidentiality:
                    for I in integrity:
                        for A in availability:
                            if(S == 0):
                                for PR in privilegesRequired:
                                    iss = cal_iss(C, I, A)
                                    exploitability = cal_exploitability(AV, AC, PR, UI)
                                    impact = cal_impact(S, iss)
                                    base = cal_base(impact, exploitability, S)
                                    print(base)
                                    f.write(str(base) + '\n')
                            if(S == 1):
                                for PR in privilegesRequiredScopeChanged:
                                    iss = cal_iss(C, I, A)
                                    exploitability = cal_exploitability(AV, AC, PR, UI)
                                    impact = cal_impact(S, iss)
                                    base = cal_base(impact, exploitability, S)
                                    print(base)
                                    f.write(str(base) + '\n')

f.close()


                        
