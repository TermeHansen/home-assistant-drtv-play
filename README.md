# Home Assistant DRTV Play

Play DRTV videos and channels via Home Assistant

## Available actions

### Play Latest
Play the latest video or clip from a specific program. There exists two options to exclude or include videos matching specific categories.
```yaml
- service: drtv_play.play_latest
  entity_id: media_player.living_room_tv
  data:
    program_name: gurli
    subtitles: false # Optional, default is false
```

### Play Channel
Play one of the svt channels.
```yaml
- service: drtv_play.play_channel
  entity_id: media_player.living_room_tv
  data:
    channel: dr2 # Available channels: dr1, dr2, drtv, drtv ekstra, dr ramasjang
```

## Installation

### Add the code

Copy the `custom_components/drtv_play` folder in this repository to `<home assistant config>/custom_components/drtv_play`

Or:

Add the repository as a custom repository in HACS

### Active the service

Add:
```yaml
drtv_play:
```
to your configuration.yaml file and restart Home Assistant.

### Use in automations

And then add the automation you want:
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
