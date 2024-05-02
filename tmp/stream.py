# Building gstreamer for python
# sudo apt-get install gobject-introspection libgirepository1.0-dev python3-gi python3-dev
# pip install PyGobject
from threading import Thread
from time import sleep
import redis
import gi
gi.require_version("Gst", "1.0")
gi.require_version("GstBase", "1.0")

from gi.repository import Gst, GLib

redis_con = redis.Redis(host='localhost', port=6380, decode_responses=True)

def start_streaming():
    Gst.init(None)

    main_loop = GLib.MainLoop()
    main_loop_thread = Thread(target=main_loop.run)
    main_loop_thread.start()

    pipeline = Gst.parse_launch("videotestsrc ! decodebin ! videoconvert ! autovideosink")
    pipeline.set_state(Gst.State.PLAYING)
# player = Gst.ElementFactory.make("playbin", "player")
# fakesink = Gst.ElementFactory.make("fakesink", "fakesink")
# player.set_property("video-sink", fakesink)


    try:
        while True:
            sleep(0.1)
    except KeyboardInterrupt:
        pass


    pipeline.set_state(Gst.State.NULL)
    main_loop.quit()
    main_loop_thread.join()


def check_redis():
    pass


if __name__ == "__main__":
    # start_streaming()
    pass


