## Export matplotlib cmaps to ncview format

`ncview_cmap.py` takes the name of a matplotlib colormap as input and writes an ncview formated
colormap to standard out.  Save to a file named `something.ncmap`.  Ncview looks for these colormap
files in `/usr/share/ncview`, a directory in the `$NCVIEWBASE` environment variable, your home
directory, or the current directory where ncview is run from.

You can also optionally add light and dark bands to the colormap using the `-b` flag.

Should run in python 2 or 3.  Several generated colormaps are in the cmap directory.

### Usage

```bash
python ./ncview_cmap.py viridis > viridis.ncmap
python ./ncview_cmap.py -b viridis > viridis_bands.ncmap
```
