class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded_string=''
        for i in strs:
            encoded_string=encoded_string + '-+-' + i
        # encoded_string=encoded_string.strip(' ')
        return encoded_string

    def decode(self, s: str) -> List[str]:
        
        decode_string=s.split('-+-')

        return decode_string[1:]
 
