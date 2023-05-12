# BioPhonia x 24h de l'innovation

## Get Started

### In Audacity
- Launch ``Pipeline.aup3`` file on Audacity
- Go to ``Edit > Preferences > Modules`` and set **mod-script-pipe** to *enabled*

### Input files
- Both files must have the same sample rate and be in ``.wav`` format and be placed in ``/input_files``
- Name your recorded audio from your omnidirectionnel microphone: ``omni.wav``
- Name your recorded audio from your unidirectionnal microphone: ``mono.wav`` <br>
(There already have some recorded test samples to try in ``/input_files``)

### In your Python IDE
- Minimum version required: ``Python 3``
- Install required python package:
``` python
pip install win32file
```
- Run ``audacity_script.py`` <br>
You can now listen to the treated audio file in ``/output_file/treated_audio.wav`` and quit Audacity