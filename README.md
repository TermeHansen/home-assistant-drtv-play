# Home Assistant DRTV Play

Play DRTV videos and channels via Home Assistant

## Available actions

### Play Latest
Play the latest video or clip from a specific program. You can search by entering a string (eg. "gurli"), or by writing the path (eg. /alene-i-vildmarken) or id (integer, eg. 69758) from the url. 
```yaml
- service: drtv_play.play_latest
  entity_id: media_player.living_room_tv
  data:
    program_name: gurli
```

### Play Channel
Play one of the DRTV channels. Available channels are DR 1, DR 2, DRTV, DRTV Ekstra and DR Ramasjang.
```yaml
- service: drtv_play.play_channel
  entity_id: media_player.living_room_tv
  data:
    channel: dr2 # Available channels: dr1, dr2, drtv, drtv ekstra, dr ramasjang
    subtitles: false # Optional, default is false
```

## Installation

There are two options for installing the add-on:

1. If you have [HACS](https://hacs.xyz/) installed, you can add this repository as a custom repository and download the add-on, or
2. Copy the `custom_components/drtv_play` folder in this repository to `<home assistant config>/custom_components/drtv_play`

Afterwards, you should **add the following** line to your `configuration.yaml` file:
```yaml
drtv_play:
```
...and **restart Home Assistant**.

### Use in automations

Use in automations as follows:
```yaml
automation:
- alias:
  trigger:
  # Some trigger
  action:
  - service: drtv_play.play_channel
    entity_id: media_player.living_room_tv
    data:
      channel: dr2
```

## Get the `program_name` field

1. Search and click on the program you want at [dr.dk/tv](https://www.dr.dk/tv)
2. You can provide the program name, or program identifier from the url.

## Inspiration

This add-on draws heavily on the [plugin.video.drnu for XBMC/Kodi](https://github.com/TermeHansen/plugin.video.drnu) as well as the [home-assistant-svt-play addon](https://github.com/lindell/home-assistant-svt-play).
