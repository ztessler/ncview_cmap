from __future__ import print_function
import sys
import argparse
import colorsys
import numpy as np
import matplotlib.cm as cm

parser = argparse.ArgumentParser(description='Export matplotlib cmap in ncview format.')
parser.add_argument('cmap', help='matplotlib colormap name')
parser.add_argument('-b', '--bands', action='store_true', help='Add light and dark banding to cmap')
args = parser.parse_args()

try:
    cmap = getattr(cm, args.cmap)
except AttributeError:
    print('matplotlib colormap \'{}\' not found'.format(args.cmap))
    sys.exit(1)

nbands = 10
bandwidth = 5 # odd

xs = np.linspace(0, 1, 256)
if args.bands:
    bandi = np.round(np.linspace(0, 255, nbands+2))[1:-1].astype(np.int)
    offsets = list(range(-(bandwidth//2),(bandwidth//2)+1))
    halfband = np.linspace(.10, .30, bandwidth//2)
    mixing = np.r_[halfband, .60, halfband[::-1]]
    whites = np.zeros_like(xs)
    blacks = np.zeros_like(xs)
    for off, mix in zip(offsets, mixing):
        whites[bandi[::2] + off] = mix
        blacks[bandi[1::2] + off] = mix

for i, n in enumerate(xs):
    rgb = np.array(cmap(n)[:3])
    if args.bands:
        hls = colorsys.rgb_to_hls(*rgb)
        rgb = np.array(colorsys.hls_to_rgb(
            hls[0],
            (hls[1] + 1*whites[i] + 0*blacks[i])/(1 + whites[i] + blacks[i]),
            hls[2]))
    print('{} {} {}'.format(*map(int, rgb*255)))

sys.exit(0)
