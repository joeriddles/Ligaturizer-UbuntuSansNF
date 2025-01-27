#!/usr/bin/env python
#
# Rebuild script for ligaturized fonts.
# Uses ligaturize.py to do the heavy lifting; this file basically just contains
# the mapping from input font paths to output fonts.

#### User configurable settings ####

# For the prefixed_fonts below, what word do we stick in front of the font name?
LIGATURIZED_FONT_NAME_PREFIX = "Liga"

# Should we copy some individual punctuations characters like &, ~, and <>,
# as well as ligatures? The full list is in ligatures.py.
# You can also override this (and OUTPUT_DIR) automatically by passing
# --copy-character-glyphs on the command line.
COPY_CHARACTER_GLYPHS = False

# If copying individual characters, how different in width (relative to the font
# we're ligaturizing) should they be before we attempt to width-correct them?
# The default (0.1) means to width-correct if they're +/- 10%. Values >1.0
# effectively disable this feature.
SCALE_CHARACTER_GLYPHS_THRESHOLD = 0.1

# Where to put the generated fonts.
OUTPUT_DIR = 'fonts/output/'

#### Fonts that should be prefixed with "Liga" when ligaturized. ####
# Don't put fonts licensed under UFL here, and don't put fonts licensed under
# SIL OFL here either unless they haven't specified a Reserved Font Name.

prefixed_fonts = [
  # UBUNTU FONT LICENCE
  'fonts/UbuntuSansMonoNerdFont/*.ttf'
]

#### No user serviceable parts below this line. ####

import sys
from glob import glob

from ligaturize import ligaturize_font

if '--copy-character-glyphs' in sys.argv:
  COPY_CHARACTER_GLYPHS=True
  OUTPUT_DIR='fonts/output-with-characters'


for pattern in prefixed_fonts:
  files = glob(pattern)
  if not files:
    print("Error: pattern '%s' didn't match any files." % pattern)
    sys.exit(1)
  for input_file in files:
    ligaturize_font(
      input_file, ligature_font_file=None, output_dir=OUTPUT_DIR,
      prefix=LIGATURIZED_FONT_NAME_PREFIX, output_name=None,
      copy_character_glyphs=COPY_CHARACTER_GLYPHS,
      scale_character_glyphs_threshold=SCALE_CHARACTER_GLYPHS_THRESHOLD)
