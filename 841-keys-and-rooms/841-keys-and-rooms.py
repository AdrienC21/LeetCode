class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        seen = set()
        
        def visit(room: int) -> None:
            nonlocal seen, rooms
            if room not in seen:
                seen.add(room)
                for r in rooms[room]:
                    visit(r)
        
        visit(0)
        return (len(seen) == n)
