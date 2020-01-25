import ffmpeg # type: ignore
from typing import List, Optional, Union
from abc import ABC, abstractmethod

class Stream(ABC):
  @abstractmethod
  def to_stream(self, start_timestamp: float, end_timestamp: float):
    raise NotImplementedError

class Fullscreen(Stream):
  def __init__(self, filename: str):
    self.filename = filename

  def to_stream(self, start_timestamp: float, end_timestamp: float):
    dur = end_timestamp - start_timestamp
    stream = ffmpeg.input(self.filename, ss=start_timestamp, t=dur)
    return stream

class Overlay(Stream):
  def __init__(self, main_filename: str, inside_filename: str, crop_x: int, crop_y: int, crop_width: int, opacity: float = 1):
    self.main_filename = main_filename
    self.inside_filename = inside_filename
    self.crop_x = crop_x
    self.crop_y = crop_y
    self.crop_width = crop_width
    self.opacity = opacity

  def to_stream(self, start_timestamp: float, end_timestamp: float):
    dur = end_timestamp - start_timestamp
    main = ffmpeg.input(self.main_filename, ss=start_timestamp, t=dur)
    inside = ffmpeg.input(self.inside_filename, ss=start_timestamp, t=dur)
    crop_height = self.crop_width * 9 // 16
    crop = inside.crop(x=self.crop_x, y=self.crop_y, width=self.crop_width, height=crop_height)

    overlay_w = 480
    overlay_h = overlay_w * 9 // 16
    scaled = crop.filter('scale', overlay_w, -1)
    if self.opacity == 1:
      translucent = scaled
    else:
      translucent = scaled.filter('format', 'rgba').filter('colorchannelmixer', aa=self.opacity)
    overlay_margin = 25
    overlay_x = 1920 - overlay_margin - overlay_w
    overlay_y = (1080 - overlay_h) // 2
    overlay = ffmpeg.overlay(main, translucent, x=overlay_x, y=overlay_y)
    return overlay

class Clip:
  def __init__(self, stream: Stream, end: Union[float, str], start: Optional[Union[float, str]] = None):
    self.stream = stream
    self.start: Optional[float] = hms(start) if start is not None and isinstance(start, str) else start
    self.end = hms(end) if isinstance(end, str) else end

class Multitrack:
  def __init__(self, clips: List[Clip], audio_filename: str, audio_volume: Union[float, str], audio_offset: float):
    # You can figure out audio_offset by using VLC's Track Synchronization
    # tool. The sign should match, so you can copy the exactly value from the
    # "Audio track synchronization" in VLC.
    if not clips:
      raise ValueError('no clips')
    if clips[0].start is None:
      raise ValueError('first clip has no start')
    for clip in clips[1:]:
      if clip.start is not None:
        raise ValueError('intermediate clip has explicit start specified; gaps are not supported')
    self.clips = clips
    self.audio_filename = audio_filename
    self.audio_volume = audio_volume
    self.audio_offset = audio_offset

  def streams(self):
    start = self.clips[0].start
    assert start is not None
    current_time = start
    streams = []
    for clip in self.clips:
      end = clip.end
      streams.append(clip.stream.to_stream(current_time, end))
      current_time = end
    video = ffmpeg.concat(*streams)
    audio_duration = current_time - start
    audio_stream = ffmpeg.input(self.audio_filename, ss=start + self.audio_offset, t=audio_duration)
    audio = audio_stream.audio.filter('volume', self.audio_volume)
    return video, audio

  def to_stream(self):
    video, audio = self.streams()
    return ffmpeg.concat(video, audio, a=1, v=1)

  def render(self, output_filename: str) -> None:
    ffmpeg.output(self.to_stream(), output_filename).run()

class Playlist:
  def __init__(self, playlists: List[Multitrack]):
    self.playlists = playlists

  def to_stream(self):
    streams = [p.streams() for p in self.playlists]
    flattened = [s for i in streams for s in i]
    return ffmpeg.concat(*flattened, a=1, v=1)

  def render(self, output_filename: str) -> None:
    ffmpeg.output(self.to_stream(), output_filename).run()

def hms(timestamp: str) -> float:
  parts = timestamp.split(':')
  assert 1 <= len(parts) <= 3
  s = float(parts[-1])
  m = float(parts[-2]) if len(parts) >= 2 else 0
  h = float(parts[-3]) if len(parts) >= 3 else 0
  return 60*60*h + 60*m + s
