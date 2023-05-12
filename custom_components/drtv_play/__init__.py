import logging
import homeassistant.helpers.config_validation as cv
import voluptuous as vol
from .video_url_fetch.tvapi import Api
from .validation import category_names

DOMAIN = "drtv_play"

DEPENDENCIES = ['media_player']

CONF_ENTITY_ID = 'entity_id'
CONF_PROGRAM_NAME = 'program_name'
CONF_CHANNEL = 'channel'
CONF_SUBTITLES = 'subtitles'

SERVICE_PLAY_LATEST = 'play_latest'
SERVICE_PLAY_LATEST_SCHEMA = vol.Schema({
    CONF_ENTITY_ID: cv.entity_ids,
    CONF_PROGRAM_NAME: str
})

SERVICE_PLAY_CHANNEL = 'play_channel'
SERVICE_PLAY_CHANNEL_SCHEMA = vol.Schema({
    CONF_ENTITY_ID: cv.entity_ids,
    CONF_CHANNEL: str,
    CONF_SUBTITLES: bool,
})

_LOGGER = logging.getLogger(__name__)



async def async_setup(hass, config):

    async def play_latest(service):
        """Play the latest svt play video from a specified program"""

        entity_id = service.data.get(CONF_ENTITY_ID)
        program_name = service.data.get(CONF_PROGRAM_NAME)

        def fetch_video_url():
            api = Api()
            item = api.get_latest(program_name)
            url = ''
            if item:
                url = api.get_stream(item['id'])['url']
            return url, item
        url, item = await hass.async_add_executor_job(fetch_video_url)
        if url:
            await hass.services.async_call('media_player', 'play_media', {
                'entity_id': entity_id,
                'media_content_id': url,
                'media_content_type': 'video',
                'extra': {
                    'title': item['title'],
                    'thumb': item['images']['tile'],
                }
            })
    hass.services.async_register(
        DOMAIN, SERVICE_PLAY_LATEST, play_latest, SERVICE_PLAY_LATEST_SCHEMA
    )

    async def play_channel(service):
        """Play the specified channel"""

        entity_id = service.data.get(CONF_ENTITY_ID)
        channel = service.data.get(CONF_CHANNEL)
        subtitles = service.data.get(CONF_SUBTITLES)

        def fetch_video_url():
            api = Api()
            channels = api.getLiveTV()
            
            url = 'hest'
            for item in channels:
                if item['title'].lower() == channel.lower():
                    url = api.get_channel_url(item, with_subtitles=subtitles)
            return url
        video_url = await hass.async_add_executor_job(fetch_video_url)

        await hass.services.async_call('media_player', 'play_media', {
            'entity_id': entity_id,
            'media_content_id': video_url,
            'media_content_type': 'video'
        })
    hass.services.async_register(
        DOMAIN, SERVICE_PLAY_CHANNEL, play_channel, SERVICE_PLAY_CHANNEL_SCHEMA
    )

    return True
