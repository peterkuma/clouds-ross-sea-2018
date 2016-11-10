# Analysis of clouds over the Ross Sea and Ross Ice Shelf

## Requirements

- Python 2.7
- Spark >= 2.0.1
- dpath
- ccplot (the `ccplot.hdfeos` module)

## Data

- CloudSat 2B-GEOPROF-LIDAR P2_R04 products

## Spark scripts

Use `spark-submit scripts/<script>.py --help` for more information.

### ross_area_files.py

Output a list of CloudSat HDF-EOS2 files containing data over the
Ross Sea/Ross Ice Shelf area.

Example:

	spark-submit scripts/ross_area_files.py '/data/datasets/cloudsat/2b-geoprof-lidar/**/*.zip' 2>/dev/null > out/ross_area_files

### extract_area.py

Extract profile columns from CloudSat HDF-EOS2 files in a given area.

Example:

	spark-submit scripts/extract_area.py -o out/ross_sea.h5 -a ross_sea -f out/ross_area_files 2>/dev/null
	spark-submit scripts/extract_area.py -o out/ross_ice_shelf.h5 -a ross_ice_shelf -f out/ross_area_files 2>/dev/null

### cloud_top_hist.py

Produce a histogram of the topmost cloud top height.

Example:

	spark-submit scripts/cloud_top_hist.py -o out/cloud_top_hist_rs.pdf out/ross_sea.h5 2>/dev/null
	spark-submit scripts/cloud_top_hist.py -o out/cloud_top_hist_ris.pdf out/ross_ice_shelf.h5 2>/dev/null
	spark-submit scripts/cloud_top_hist.py -i 1 -o out/cloud_top_hist_rs_cpr.pdf out/ross_sea.h5 2>/dev/null
	spark-submit scripts/cloud_top_hist.py -i 2 -o out/cloud_top_hist_rs_caliop.pdf out/ross_sea.h5 2>/dev/null
	spark-submit scripts/cloud_top_hist.py -i 1 -o out/cloud_top_hist_ris_cpr.pdf out/ross_ice_shelf.h5 2>/dev/null
	spark-submit scripts/cloud_top_hist.py -i 2 -o out/cloud_top_hist_ris_caliop.pdf out/ross_ice_shelf.h5 2>/dev/null

### profile_sample.py

Plot a profile sample.

Example:

	spark-submit scripts/profile_sample.py -o out/profile_sample_rs.pdf out/ross_sea.h5 2>/dev/null
	spark-submit scripts/profile_sample.py -o out/profile_sample_ris.pdf out/ross_ice_shelf.h5 2>/dev/null

### cloud_top_base_scatter.py

Plot cloud top/cloud base scatter plot from a sample of data.

Example:

	spark-submit scripts/cloud_top_base_scatter.py -o out/cloud_top_base_scatter_rs.png out/ross_sea.h5 2>/dev/null
	spark-submit scripts/cloud_top_base_scatter.py -o out/cloud_top_base_scatter_ris.png out/ross_ice_shelf.h5 2>/dev/null
