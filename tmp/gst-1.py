import gi

gi.require_version("Gst", "1.0")
gi.require_version("Gtk", "4.0")

from gi.repository import Gst, GObject

filepath = "/videos/video-0.mp4"

Gst.init(None)

main_loop = GObject.MainLoop()
player = Gst.ElementFactory.make("playbin", "player")
# fakesink = Gst.ElementFactory.make("autovideosink", "autovideosink")
# player.set_property("video-sink", fakesink)

player.set_property("uri", "file://" + filepath)
player.set_state(Gst.State.PLAYING)
main_loop.run()




