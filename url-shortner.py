import bitly_api

BITLY_GENERIC_ACCESS_TOKEN ="dfeb0739f7c506dced3a4dc35baf94f446e82d6a"
bitly = bitly_api.Connection(access_token = BITLY_GENERIC_ACCESS_TOKEN)
full_link = input()
short_url = bitly.shorten(full_link) 
print("Short URL = %s" % short_url['url'])