import ffmpeg # type: ignore
from typing import List, Optional
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
  def __init__(self, main_filename: str, inside_filename: str, crop_x: int, crop_y: int, crop_width: int):
    self.main_filename = main_filename
    self.inside_filename = inside_filename
    self.crop_x = crop_x
    self.crop_y = crop_y
    self.crop_width = crop_width

  def to_stream(self, start_timestamp: float, end_timestamp: float):
    dur = end_timestamp - start_timestamp
    main = ffmpeg.input(self.main_filename, ss=start_timestamp, t=dur)
    inside = ffmpeg.input(self.inside_filename, ss=start_timestamp, t=dur)
    crop_height = self.crop_width * 9 // 16
    crop = inside.crop(x=self.crop_x, y=self.crop_y, width=self.crop_width, height=crop_height)

    overlay_w = 480
    overlay_h = overlay_w * 9 // 16
    scaled = crop.filter('scale', overlay_w, -1)
    translucent = scaled.filter('format', 'rgba').filter('colorchannelmixer', aa=0.3)
    overlay_margin = 25
    overlay_x = 1920 - overlay_margin - overlay_w
    overlay_y = 1080 - overlay_margin - overlay_h
    overlay = ffmpeg.overlay(main, translucent, x=overlay_x, y=overlay_y)
    return overlay

class Clip:
  def __init__(self, stream: Stream, end: float, start: Optional[float] = None):
    self.stream = stream
    self.start = start
    self.end = end

class Playlist:
  def __init__(self, clips: List[Clip], audio_filename: str, audio_offset: float):
    if not clips:
      raise ValueError('no clips')
    if clips[0].start is None:
      raise ValueError('first clip has no start')
    for clip in clips[1:]:
      if clip.start is not None:
        raise ValueError('intermediate clip has explicit start specified; gaps are not supported')
    self.clips = clips
    self.audio_filename = audio_filename
    self.audio_offset = audio_offset

  def render(self, output_filename: str):
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
    audio = ffmpeg.input(self.audio_filename, ss=start + self.audio_offset, t=audio_duration)
    combined = ffmpeg.concat(video, audio.audio, a=1, v=1)
    out = ffmpeg.output(combined, output_filename).run()
