class Codec:

    code_hashmap, url_hashmap = defaultdict(), defaultdict()
    chars = string.ascii_letters + string.digits
    
    def getCode(self) -> str:
        code = "".join(random.choice(self.chars) for i in range(6))
        return f"http://tinyurl.com/{code}"
    
    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl in self.url_hashmap:
            return self.url_hashmap[longUrl]
        code = self.getCode()
        while code in self.code_hashmap:
            code = getCode()
        self.code_hashmap[code] = longUrl
        self.url_hashmap[longUrl] = code
        return code

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.code_hashmap[shortUrl]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))