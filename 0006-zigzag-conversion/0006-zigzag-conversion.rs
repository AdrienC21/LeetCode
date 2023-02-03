impl Solution {
    pub fn convert(s: String, num_rows: i32) -> String {
        if (num_rows == 1) {
            return s;
        }
        let nb_letters_zigzag: i32 = (2 * num_rows - 2);
        let len_s: i32 = (s.len() as i32);
        let nb_complete_zigzags: i32 = (len_s / nb_letters_zigzag);
        let mut numCols: i32 = (num_rows - 1) * nb_complete_zigzags;
        if ((len_s % nb_letters_zigzag) > num_rows) {
            numCols += (1 + (len_s % nb_letters_zigzag) - num_rows);  // incomplete last zigzag, add more columns
        }
        else {
            numCols += 1
        }
        let s_vec: Vec<char> = s.chars().collect();
        let mut m: Vec<Vec<char>> = Vec::new();
        for i in 0..num_rows {
            let mut to_add: Vec<char> = Vec::new();
            for j in 0..numCols {
                to_add.push(' ');
            }
            m.push(to_add);
        }
        
        let mut p: usize = 0;  // pointer on the string
        
        // Draw the zigzag
        let mut j: usize;
        for zigzag in 0..nb_complete_zigzags {  // draw the complete zigzag
            j = ((num_rows - 1) * zigzag) as usize;
            for i in 0..num_rows as usize {
                m[i][j] = s_vec[p as usize];
                p += 1;
            }
            for k in 1..(num_rows - 1) as usize {
                m[(num_rows as usize) - 1 - k][j+k] = s_vec[p as usize];
                p += 1;
            }
        }
        
        // Draw the last incomplete zigzag
        if ((len_s % nb_letters_zigzag) > num_rows) {
            j = ((num_rows - 1) * nb_complete_zigzags) as usize;
            for i in 0..num_rows as usize {
                m[i][j] = s_vec[p as usize];
                p += 1;
            }
            let remaining_letters: i32 = len_s - nb_complete_zigzags * nb_letters_zigzag - num_rows;
            for k in 0..remaining_letters as usize {
                m[(num_rows as usize) - 1 -(k+1)][j+k+1] = s_vec[p as usize];
                p += 1;
            }
        }
        else {
            let remaining_letters: i32 = len_s - nb_complete_zigzags * nb_letters_zigzag;
            j = ((num_rows - 1) * nb_complete_zigzags) as usize;
            for i in 0..remaining_letters as usize {
                m[i][j] = s_vec[p as usize];
                p += 1;
            }
        }
            
        // Collect the final word
        let mut final_word: Vec<char> = Vec::new();
        for i in 0..num_rows as usize {
            for j in 0..numCols as usize {
                if (m[i][j] != ' ') {  // it's a letter
                    final_word.push(m[i][j]);
                }
            }
        }
        let res: String = final_word.iter().collect();
        return res;
    }
}