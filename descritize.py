class discretize:
    def __init__(self, x):
        x['L'] = x['L'].apply(self.calc_L)
        x['R'] = x['R'].apply(self.calc_R)
        x['A_M'] = x['A_M'].apply(self.calc_A_M)

    def calc_L(self, value) -> int:
        if 0 < value and value < 1:
            return 0
        else : 
            return 1

    def calc_R(self, value) -> int:
        if 0 < value and value < 1:
            return 0
        else : 
            return 1
        pass

    def calc_A_M(self, value) -> int:
        pass
