import pytest
import tvapi

tvapi.EXPIRE_HOURS = -1
tvapi.CLEAUP_EVERY = 1e6
api = tvapi.Api()

liveurls = '''
https://drlive01hls.akamaized.net/hls/live/2014185/drlive01/master.m3u8
https://drlive02hls.akamaized.net/hls/live/2014187/drlive02/master.m3u8
https://drevent01hls.akamaized.net/hls/live/2014198/drevent01/master.m3u8
https://drevent02hls.akamaized.net/hls/live/2028694/drevent02/master.m3u8
https://drlive03hls.akamaized.net/hls/live/2014190/drlive03/master.m3u8
'''
def test_live():
    def geturl(channel):
        channels = api.getLiveTV()
        url = ''
        for item in channels:
            if item['title'].lower() == channel.lower():
                url = api.get_channel_url(item)
        return url
    for i, channel in enumerate(['dr1', 'dr2', 'DRTV', 'DRTV Ekstra', 'DR Ramasjang']):
        assert liveurls.splitlines()[i+1] == geturl(channel)

tests = [
['gurli', 'Gurli Gris: Sejlturen hjem', 'https://drod20d.akamaized.net/dk/encrypted/none/5d/644368e4ab5a621810963c5d/00852108640/stream_fmp4/master_manifest.m3u8'] ,
['tv-avisen', 'TV AVISEN: Er det slut med Erdogan?', 'https://drod23c.akamaized.net/all/clear/none/aa/64611705181329129c686daa/00122320330/stream_fmp4/master_manifest.m3u8'] ,
['debatten', 'Debatten: Sundhedstyranni?', 'https://drod24m.akamaized.net/all/clear/none/c5/645d471e55dfad36f4adcec5/00212350150/stream_fmp4/master_manifest.m3u8'] ,
['bonderøven', 'Frank & Kastaniegaarden: Pigsten og Påskelam', 'https://drod20s.akamaized.net/all/clear/none/e4/645226713bcfa2034caf35e4/00952330050/stream_fmp4/master_manifest.m3u8'] ,
['knight and day', 'Knight and Day', 'https://drod24k.akamaized.net/dk/clear/none/1f/645b84c055dfad36f4adce1f/00021133910/stream_fmp4/master_manifest.m3u8'] ,
['/serie/alene-i-vildmarken_69758', 'Alene i vildmarken: Hvem vinder i vildmarken?', 'https://drod23h.akamaized.net/all/clear/none/54/64522917a92c5d28106f8454/00922303360/stream_fmp4/master_manifest.m3u8'] ,
['69758', 'Alene i vildmarken: Hvem vinder i vildmarken?', 'https://drod23h.akamaized.net/all/clear/none/54/64522917a92c5d28106f8454/00922303360/stream_fmp4/master_manifest.m3u8'] ,
]
def test():
    for label, title, turl in tests + [
        ]:
        item = api.get_latest(label)
        url = api.get_stream(item['id'])['url']
        if (item['title'] != title) or (url != turl):
            print([label, item['title'], url], ',')
#    print(item)
test()

test_live()
# print()

# path = '/episode/frank-and-kastaniegaarden_113317'
# data['path'] = path
# card = api.get_programcard(path, data=data)
# import json
# with open('debug.json', 'w') as fh: json.dump(card, fh, indent=2)

# season = 0
# for item in card['item']['season']['show']['seasons']['items']:
#     if item['seasonNumber'] > season:
#         print(item['seasonNumber'], item['path'])
#         season = item['seasonNumber']
#         path = item['path']
# if season > 0:
#     card = api.get_programcard(path)
#     if card['item']['type'] == 'season':
#         # find latest
#         for item in card['item']['episodes']['items'][:3]:
#             print(item['episodeNumber'])
#         item = card['item']['episodes']['items'][0]
