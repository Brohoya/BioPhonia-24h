import errno
import os
import sys
import win32file

if sys.platform == 'win32':
    print("pipe-test.py, running on windows")
    TONAME = '\\\\.\\pipe\\ToSrvPipe'
    FROMNAME = '\\\\.\\pipe\\FromSrvPipe'
    EOL = '\r\n\0'
else:
    print("pipe-test.py, running on linux or mac")
    TONAME = '/tmp/audacity_script_pipe.to.' + str(os.getuid())
    FROMNAME = '/tmp/audacity_script_pipe.from.' + str(os.getuid())
    EOL = '\n'

print("Write to  \"" + TONAME +"\"")
if not os.path.exists(TONAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("Read from \"" + FROMNAME +"\"")
if not os.path.exists(FROMNAME):
    print(" ..does not exist.  Ensure Audacity is running with mod-script-pipe.")
    sys.exit()

print("-- Both pipes exist.  Good.")

TOFILE = win32file.CreateFile(
    TONAME,
    win32file.GENERIC_WRITE,
    0,
    None,
    win32file.OPEN_EXISTING,
    0,
    None
)
print("-- File to write to has been opened")

FROMFILE = win32file.CreateFile(
    FROMNAME,
    win32file.GENERIC_READ,
    0,
    None,
    win32file.OPEN_EXISTING,
    0,
    None
)
print("-- File to read from has now been opened too\r\n")


def send_command(command):
    """Send a single command."""
    print("Send: >>> \n"+command)
    win32file.WriteFile(TOFILE, (command + EOL).encode())

def get_response():
    """Return the command response."""
    result = ''
    while True:
        hr, data = win32file.ReadFile(FROMFILE, 4096)
        result += data.decode()
        if '\n' in result:  # end of message
            break
    return result

def do_command(command):
    """Send one command, and return the response."""
    send_command(command)
    response = get_response()
    print("Rcvd: <<< \n" + response)
    return response

def make_sure_dir_exists(directory, is_file_path=False):
    """
    Forces creating directory if such does not exist.

    :param directory: path to directory that we wish to exist
    :type directory: basestring
    """
    if is_file_path:
        directory = os.path.dirname(directory)
    try:
        os.makedirs(directory)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise

def select_omni_track():
    do_command("Select: Track=1")

def select_mono_track():
    do_command("Select: Track=0")

def remove_track_selection():
    do_command("SelectNone:")

def remove_track(track_number):
    do_command("RemoveTracks: Track={}".format(track_number))

def import_wav(input_path):
    do_command("Select: Track=0")
    do_command("Import2: Filename={}".format(input_path))

def export_wave(output_path):
    export_command = "Export2: Filename={}".format(output_path)
    do_command(export_command)

def mute_mono_track():
    remove_track_selection()
    select_mono_track()
    do_command("MuteTracks:")

def apply_noise_pattern_reduction():
    do_command('NoiseReduction:')

if __name__ == '__main__':
    dir_path = os.path.dirname(os.path.realpath(__file__))
    raw_files_folder = os.path.join(dir_path, "input_files")
    output_folder = os.path.join(dir_path, "output_file")

    omni_track = os.path.join(raw_files_folder, "omni.wav")
    mono_track = os.path.join(raw_files_folder, "mono.wav")

    make_sure_dir_exists(mono_track, is_file_path=True)
    make_sure_dir_exists(omni_track, is_file_path=True)
    print("Files exist")

    import_wav(mono_track)
    print("Monodirectional track imported")

    apply_noise_pattern_reduction()
    remove_track(0)
    print("Noise reduction profile set")

    import_wav(omni_track)
    print("Omnidirectional track imported")

    apply_noise_pattern_reduction()
    print("Noise reduction profile applied")

    export_wave(os.path.join(output_folder, "treated_audio.wav"))
    print("Treated audio exported")
    remove_track(0)
    print("File tracks removed")