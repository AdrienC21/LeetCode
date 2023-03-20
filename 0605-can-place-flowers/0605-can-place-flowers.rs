impl Solution {
    pub fn can_place_flowers(flowerbed: Vec<i32>, n: i32) -> bool {
        let mut nb_to_place: i32 = n;
        let flowers: i32 = flowerbed.len() as i32;
        if (flowers == 1) {
            if ((nb_to_place == 0) || ((nb_to_place == 1) && (flowerbed[0] == 0))) {
                return true;
            }
            return false;
        }
        let mut f_bed: Vec<i32> = Vec::from(flowerbed);  // mutable version
        for i in 0..flowers as usize {
            if (nb_to_place < 1) {
                break;
            }
            if (f_bed[i] == 0) {
                if (i == 0) {
                    if (f_bed[1] == 0) {
                        f_bed[i] = 1;
                        nb_to_place -= 1;
                        if (nb_to_place < 1) {
                            break
                        }
                    }
                }
                else if (i == ((flowers as usize) - 1)) {
                    if (f_bed[(flowers as usize)-2] == 0) {
                        f_bed[i] = 1;
                        nb_to_place -= 1;
                        if (nb_to_place < 1) {
                            break
                        }
                    }
                }
                else if ((f_bed[i-1] == 0) && (f_bed[i+1] == 0)) {
                    f_bed[i] = 1;
                    nb_to_place -= 1;
                    if (nb_to_place < 1) {
                        break
                    }
                }
            }
        }
        return (nb_to_place < 1);
    }
}
