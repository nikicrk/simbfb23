import marshal,zlib,base64
exec(marshal.loads(zlib.decompress(base64.b64decode("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"))))