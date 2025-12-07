"""
https://leetcode.com/problems/encode-and-decode-tinyurl/
535. Encode and Decode TinyURL
Note: This is a companion problem to the System Design problem: Design TinyURL.
TinyURL is a URL shortening service where you enter a URL such as https://leetcode.com/problems/design-tinyurl and it returns a short URL such as http://tinyurl.com/4e9iAk. Design a class to encode a URL and decode a tiny URL.
There is no restriction on how your encode/decode algorithm should work. You just need to ensure that a URL can be encoded to a tiny URL and the tiny URL can be decoded to the original URL.
Implement the Solution class:
Solution() Initializes the object of the system.
String encode(String longUrl) Returns a tiny URL for the given longUrl.
String decode(String shortUrl) Returns the original long URL for the given shortUrl. It is guaranteed that the given shortUrl was encoded by the same object.
Example 1:
Input: url = "https://leetcode.com/problems/design-tinyurl"
Output: "https://leetcode.com/problems/design-tinyurl"
Explanation:
Solution obj = new Solution();
string tiny = obj.encode(url); // returns the encoded tiny url.
string ans = obj.decode(tiny); // returns the original url after decoding it.
Constraints:
1 <= url.length <= 104
url is guranteed to be a valid URL.
"""
# Time - O(1)
# Space - O(1)

class Codec:

    def __init__(self) -> None:
        self.encode_map = {}
        self.decode_map = {}
        self.base = "http://tinyurl.com/"    

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.encode_map:
            short_url = self.base + str(len(self.encode_map) + 1)
            self.encode_map[longUrl] = short_url
            self.decode_map[short_url] = longUrl
        return self.encode_map[longUrl]

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        return self.decode_map[shortUrl]

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))

url = "https://leetcode.com/problems/design-tinyurl"
obj = Codec()
tiny = obj.encode(url)
print(tiny)
ans = obj.decode(tiny)
print(ans)
