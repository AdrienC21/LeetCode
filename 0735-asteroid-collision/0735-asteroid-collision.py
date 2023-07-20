class Solution:
    def sign(self, n: int) -> int:
        return 1 if n > 0 else -1

    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        res = []
        last_direction = 0  # 1 or -1
        i = 0
        n = len(asteroids)
        while i < n:
            ast = asteroids[i]
            sign_ast = self.sign(ast)
            if (last_direction == 1) and (sign_ast == -1):  # collision(s)
                not_append_ast = True
                while res:
                    top_ast = res.pop()
                    if (top_ast < 0):  # no more collision
                        res.append(top_ast)
                        not_append_ast = False
                        break
                    if top_ast < (-ast):  # collision right win
                        not_append_ast = False
                        continue
                    if top_ast == (-ast):  # two destroyed
                        not_append_ast = True
                        break
                    else:  # collision left win
                        res.append(top_ast)
                        not_append_ast = True
                        break
                if not(not_append_ast):
                    res.append(ast)
            else:  # no collision
                res.append(ast)
            if res:
                last_direction = self.sign(res[-1])
            else:
                last_direction = 0
            i += 1
        return res
