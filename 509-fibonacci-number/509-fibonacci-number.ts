function fib(n: number): number {
    const phi = (1 + Math.sqrt(5)) / 2;
    const res = Math.round(Math.pow(phi, n) / Math.sqrt(5));
    return Math.floor(res);
};