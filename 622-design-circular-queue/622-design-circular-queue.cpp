class MyCircularQueue {
public:
    int front = 0;
    int rear = 0;
    int len;
    vector<int> queue;
    MyCircularQueue(int k) {
        for (int i=0; i<k; i++) {
            queue.push_back(-1);
        }
        this->len = k;
    }
    
    bool enQueue(int value) {
        if (this->isFull()) {
            return false;
        }
        if (!(this->queue[this->rear] == -1)) {
            this->rear = (this->rear + this->len - 1) % this->len;
        }
        this->queue[this->rear] = value;
        return true;
    }
    
    bool deQueue() {
        if (this->isEmpty()) {
            return false;
        }
        this->queue[this->front] = -1;
        if (this->front != this->rear) {
            this->front = (this->front + this->len - 1) % this->len;
        }
        return true;
    }
    
    int Front() {
        if (!(this->queue[this->front] == -1)) {
            return this->queue[this->front];
        }
        return -1;
    }
    
    int Rear() {
        if (!(this->queue[this->rear] == -1)) {
            return this->queue[this->rear];
        }
        return -1;
    }
    
    bool isEmpty() {
        return ((this->front == this->rear) & (this->queue[this->front] == -1));
    }
    
    bool isFull() {
        return (((this->front == (this->len - 1)) & (this->rear == 0)) || (this->front == (this->rear - 1))) & !(this->queue[this->front] == -1) & !(this->queue[this->rear] == -1);
    }
};

/**
 * Your MyCircularQueue object will be instantiated and called as such:
 * MyCircularQueue* obj = new MyCircularQueue(k);
 * bool param_1 = obj->enQueue(value);
 * bool param_2 = obj->deQueue();
 * int param_3 = obj->Front();
 * int param_4 = obj->Rear();
 * bool param_5 = obj->isEmpty();
 * bool param_6 = obj->isFull();
 */