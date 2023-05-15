# BioPhonia - 24h de l'Innovation

Solution to remove human noise in natural sound recordings with two microphones (omnidirectionnel to capture nature and unidirectionnel to capture human noises) using scripting module of Audacity in Python. This solution could be embedded in recording devices as the Audacity's noise reduction algorithm is open source. <br>
*:exclamation: This solution was found, made and tested in 24h. It only is a proof of concept* <br>

## Get Started

### In Audacity
- Launch ``Pipeline.aup3`` file on Audacity
- Go to ``Edit > Preferences > Modules`` and set **mod-script-pipe** to *enabled*

### Input files
- Both files must have the same sample rate, be in ``.wav`` format and be placed in ``/input_files``
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
You can now listen the treated audio file in ``/output_file/treated_audio.wav`` and quit Audacity

> :warning: The Noise Reduction feature cannot take parameters in the script (see [here](https://manual.audacityteam.org/man/scripting_reference.html) in line *NoiseReduction*), so it can only apply the last configuration used on **your** computer. To get our results, the first time you try, you must go to ``Effect > Noise Removal and Repair > Noise Reduction`` and set ``Noise reduction (dB)`` at ``30``.