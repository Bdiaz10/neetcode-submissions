class Solution:

    def encode(self, strs: List[str]) -> str:
        return '2318231293123'.join(strs) if len(strs) > 0 else "!!!!"
    def decode(self, s: str) -> List[str]:
        
        return s.split("2318231293123") if s != "!!!!" else []
