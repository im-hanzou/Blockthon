# Bytes (seed) To WIF

### Generated Bytes and Convert To WIF

Generated and Convert Bytes To WIF `Compressed`:
```python
from Blockthon.Wallet import getBytes, Bytes_To_Wif
# generated random bytes without repeat
bytes_str = getBytes()
# Convert Bytes To WIF Compress:
WifCompress = Bytes_To_Wif(bytes_str, compressed=True)
```

Generated and Convert Bytes To WIF `UnCompressed`:
```python
from Blockthon.Wallet import getBytes, Bytes_To_Wif
# generated random bytes without repeat
bytes_str = getBytes()
# Convert Bytes To WIF Compress:
WifCompress = Bytes_To_Wif(bytes_str, compressed=False)
```