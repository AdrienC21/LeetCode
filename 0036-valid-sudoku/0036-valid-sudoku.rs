use std::collections::HashSet;

impl Solution {
    pub fn is_valid_sudoku(board: Vec<Vec<char>>) -> bool {
        return (Solution::rowsValid(&board) & Solution::colsValid(&board) & Solution::blocksValid(&board));
    }
    pub fn rowsValid(board: &Vec<Vec<char>>) -> bool {
        for li in board {
            let mut s: HashSet<char> = HashSet::new();
            for v in &(*li) {
                if (*v != '.') {
                    if (s.contains(v)) {
                        return false;
                    }
                    else {
                        s.insert(*v);
                    }
                }
            }
        }
        return true;
    }
    pub fn colsValid(board: &Vec<Vec<char>>) -> bool {
        let mut v: char;
        for j in 0..9 {
            let mut s: HashSet<char> = HashSet::new();
            for i in 0..9 {
                v = board[i as usize][j as usize];
                if (v != '.') {
                    if (s.contains(&v)) {
                        return false;
                    }
                    else {
                        s.insert(v);
                    }
                }
            }
        }
        return true;
    }
    pub fn blocksValid(board: &Vec<Vec<char>>) -> bool {
        let mut i: i32;
        let mut j: i32;
        let mut v: char;
        for q in 0..9 {
            i = q / 3;
            j = q % 3;
            let mut s: HashSet<char> = HashSet::new();
            for k in 0..3 {
                for l in 0..3 {
                    v = board[(3*i+k) as usize][(3*j+l) as usize];
                    if (v != '.') {
                        if (s.contains(&v)) {
                            return false;
                        }
                        else {
                            s.insert(v);
                        }
                    }
                }
            }
        }
        return true;
    }
}