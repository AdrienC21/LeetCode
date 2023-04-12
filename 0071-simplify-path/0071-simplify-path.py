class Solution:
    def simplifyPath(self, path: str) -> str:
        path2 = path[:]
        if path2 != "" and path2[-1] != "/":
            path2 = path2 + "/"
        while "//" in path2:
            path2 = path2.replace("//", "/")
        while "/./" in path2:
            path2 = path2.replace("/./", "/")
        if path2[-1] == "/":
            path2 = path2[:-1]
        path_list = path2.split("/")[1:]
        
        final_path = ""
        list_of_words = []
        path_level = 0  # we start at the root level
        
        for _, w in enumerate(path_list):
            if w == "":
                ()
            elif w != "..":
                final_path = final_path + "/" + w
                list_of_words.append(w)
                path_level += 1
            else:
                if path_level != 0:
                    path_level -= 1
                    final_path = final_path[:-(len(list_of_words.pop(-1))+1)]
        if final_path == "":
            return "/"
        else:
            return final_path
