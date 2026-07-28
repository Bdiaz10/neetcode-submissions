class Solution:

    def encode(self, strs: List[str]) -> str:
        return '4619'.join(strs) if len(strs) > 0 else "!!!!"
    def decode(self, s: str) -> List[str]:
        
        return s.split("4619") if s != "!!!!" else []
