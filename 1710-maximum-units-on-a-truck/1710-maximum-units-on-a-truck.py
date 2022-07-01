class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        boxTypes.sort(key=lambda x: x[1], reverse=True)
        box_used = 0
        units = 0
        for nb_box, unit_per_box in boxTypes:
            if box_used + nb_box >= truckSize:
                units += (truckSize - box_used) * unit_per_box
                break
            units += nb_box * unit_per_box
            box_used += nb_box
        return units
