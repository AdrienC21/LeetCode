struct StockSpanner {
    spans: Vec<i32>,
    prices: Vec<i32>,
}


/** 
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl StockSpanner {

    fn new() -> Self {
        let mut obj = StockSpanner {
            spans: Vec::new(),
            prices: Vec::new(),
        };
        return obj;
    }
    
    fn next(&mut self, price: i32) -> i32 {
        if (self.prices.len() == 0) {  // span 1
            self.prices.push(price);
            self.spans.push(1);
            return 1;
        }
        if (price < *self.prices.last().unwrap_or(&0)) {  // span 1
            self.spans.push(1);
            self.prices.push(price);
            return 1;
        }
        let mut span: i32 = 1;
        let mut i: i32 = (self.prices.len() as i32) - 1;
        while (i >= 0) {
            if (self.prices[i as usize] <= price) {
                span += self.spans[i as usize];
                i = (self.prices.len() as i32) - span;
            }
            else {
                break;
            }
        }

        self.spans.push(span);
        self.prices.push(price);
        return span;
    }
}

/**
 * Your StockSpanner object will be instantiated and called as such:
 * let obj = StockSpanner::new();
 * let ret_1: i32 = obj.next(price);
 */