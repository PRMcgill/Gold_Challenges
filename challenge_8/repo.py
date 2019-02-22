import infractions
base_points = 100
infractions_list = []
class Calc_Points:

    def add_infractions(self,speeding,swerve,rolling,tail_gating):
        ai = infractions.Infractions(speeding,swerve,rolling,tail_gating)
        infractions_list.append(ai)

    def speeding(self, speeding):
        speed_points = 0
        for s in infractions_list: 
            speed_points +=  int(s.speeding)
        return speed_points
    
    def swerving(self, swerve):
        swerve_points = 0
        for sp in infractions_list:
            swerve_points += 1.25 * int(sp.swerve)
        return swerve_points

    def rolling_stop(self, rolling):
        rolling_points = 0
        for rp in infractions_list:
            rolling_points += 1.5 * int(rp.rolling)
        return rolling_points

    def tail_gate(self,tail_gating):
        tg_points = 0
        for tg in infractions_list:
            tg_points += 1.65 * int(tg.tail_gating)
        return tg_points

    def total_points(self,base_points, swerve_points, rolling_points, speed_points, tg_points):
        total_points = base_points + swerve_points + rolling_points + speed_points + tg_points
        return total_points

    