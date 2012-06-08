import pygtk
pygtk.require('2.0')
import gtk
 
class FrameExample:
    def __init__(self):
        # create new window
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_title("Frame Example")
 
        # connect "destroy" event to signal handler
        window.connect("destroy", lambda w: gtk.main_quit())
        window.set_size_request(300, 300)
 
        # set border width of window
        window.set_border_width(10)
 
        # create the Frame
        frame = gtk.Frame()
        window.add(frame)
 
        # set the frame's label
        frame.set_label("GTK Frame Widget")
 
        # align the label at the right of the frame
        frame.set_label_align(1.0, 0.0)
 
        # set the style of the frame
        frame.set_shadow_type(gtk.SHADOW_ETCHED_OUT)
        frame.show()
 
        # display the window
        window.show()
 
def main():
    # enter the event loop
    gtk.main()
    return 0
 
if __name__ == "__main__":
    FrameExample()
    main()
