from .Utils import HexToDGB
from .lib import Hexlify, MnemonicToBytes, DecToBytes


def Address_From_PrivateKey(privatekey: str) -> str: return HexToDGB(privatekey)


def Address_From_Bytes(byte: bytes) -> str: return Address_From_PrivateKey(Hexlify(byte))


def Address_From_Mnemonic(mnemonics: str) -> str: return Address_From_Bytes(MnemonicToBytes(mnemonics))


def Address_From_Dec(dec: int) -> str: return Address_From_Bytes(DecToBytes(dec))