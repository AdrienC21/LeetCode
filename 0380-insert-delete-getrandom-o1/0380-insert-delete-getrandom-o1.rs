use rand::Rng;
use std::collections::HashSet;

struct RandomizedSet {
    elements: Vec<i32>,
    set: HashSet<i32>,
    len: i32,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl RandomizedSet {

    fn new() -> Self {
        let mut elements: Vec<i32> = Vec::new();
        let mut set: HashSet<i32> = HashSet::new();
        let mut len: i32 = 0;
        let mut rs = RandomizedSet {
            elements: elements,
            set: set,
            len: len,
        };
        return rs;
    }
    
    fn insert(&mut self, val: i32) -> bool {
        if (self.set.contains(&val)) {
            return false;
        }
        self.set.insert(val);
        self.elements.push(val);
        self.len += 1;
        return true;
    }
    
    fn remove(&mut self, val: i32) -> bool {
        if (!self.set.contains(&val)) {
            return false;
        }
        self.set.remove(&val);
        self.elements.retain(|&x| x != val);
        self.len -= 1;
        return true;
    }
    
    fn get_random(&mut self) -> i32 {
        let mut rng = rand::thread_rng();
        let j: i32 = rng.gen_range(0, self.len);
        return self.elements[j as usize];
    }
}

/**
 * Your RandomizedSet object will be instantiated and called as such:
 * let obj = RandomizedSet::new();
 * let ret_1: bool = obj.insert(val);
 * let ret_2: bool = obj.remove(val);
 * let ret_3: i32 = obj.get_random();
 */
