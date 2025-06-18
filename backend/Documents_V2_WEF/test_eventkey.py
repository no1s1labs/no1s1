import codecs


from hexbytes import HexBytes
value = 0x587caa6b8d039f1032481d8bb82740a116fa1453d5a86924e29784b96be848f0


#decoded_str=value.decode("utf-8")
decoded_str=codecs.decode(value, 'UTF-8')
print(decoded_str)
#print(int(decoded_str).decode("utf-8"))




#Jens1
#[AttributeDict({'args': AttributeDict({'qrCode': b'9\xe3/\x02t\x9f5<\x07\xa0\x8c\xc7\x1c\x02\xc9n\x9c0+\x1a\x8a{\x93h\xa4P\xbfF[\\@\xa1'}), 'event': 'newQRcode', 'logIndex': 193, 'transactionIndex': 83, 'transactionHash': HexBytes('0x96613329dccb311b461680901ea0e328a2aa1bdb01538566e5687ce4eb665a76'), 'address': '0x8e5d2494FFd23FB458dA4EA9b8AD9508955C1697', 'blockHash': HexBytes('0xd2e8c6fed5dd6e492755758d31d0c70959c3dc48dfbe73819d33ffbc87785a30'), 'blockNumber': 9451724})]
#AttributeDict({'qrCode': b'9\xe3/\x02t\x9f5<\x07\xa0\x8c\xc7\x1c\x02\xc9n\x9c0+\x1a\x8a{\x93h\xa4P\xbfF[\\@\xa1'})


#Jens
#[AttributeDict({'args': AttributeDict({'qrCode': b'\xe3\x87~I\xb5F=\x91\x04\x91/S\xf5\x95Q\xb7\xd5}g\xea\xd3&\xfd\xca\xd9z<\n\x8b\xf8\xeb\x86'}), 'event': 'newQRcode', 'logIndex': 88, 'transactionIndex': 63, 'transactionHash': HexBytes('0x62a47421d1d4a1e92aa19b3e0ae96514f24b51e57d956206ba7775cc304bc38c'), 'address': '0x8e5d2494FFd23FB458dA4EA9b8AD9508955C1697', 'blockHash': HexBytes('0xb93befec394ab24a12aaea8f0bb9cbc6471c285794706eb5e9bb2d0ea72ef423'), 'blockNumber': 9451529})]
#AttributeDict({'qrCode': b'\xe3\x87~I\xb5F=\x91\x04\x91/S\xf5\x95Q\xb7\xd5}g\xea\xd3&\xfd\xca\xd9z<\n\x8b\xf8\xeb\x86'})

