# -*- coding: utf-8 -*-
"""altyazi.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1Ve02abKKshhfimBWNwOXLKBe7g9NtlCv
"""

!pip install git+https://github.com/openai/whisper.git
 !sudo apt update && sudo apt install ffmpeg

!whisper "muzik.mp3" --model medium
