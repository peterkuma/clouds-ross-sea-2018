# Analysis of clouds over Ross Sea and the Ross Ice Shelf

## Requirements

- Python 2.7
- Spark >= 2.0.1
- numpy
- matplotlib
- h5py
- dpath
- ccplot (the `ccplot.hdfeos` module)

## Data

- CloudSat 2B-GEOPROF-LIDAR P2_R04 products (2006-2011)
- CloudSat 2B-CLDCLASS-LIDAR P_R04 products (2007-2010)

## Contents

- `doc` - Documents
- `lib` - Python libraries
- `out` - Output files
- `scripts` - Spark and plotting python scripts

## Spark scripts

Use `spark-submit scripts/<script>.py --help` for more information about how
to submit the scripts.

### ross_area_files.py

Output a list of CloudSat HDF-EOS2 files containing data over the
Ross Sea/Ross Ice Shelf area.

Example:

    spark-submit scripts/ross_area_files.py '/data/datasets/cloudsat/2b-geoprof-lidar/*/*/*.zip' 2>/dev/null > out/ross_area_files
    spark-submit scripts/ross_area_files.py '/data/datasets/cloudsat/2b-cldclass-lidar.p_r04/*/*/*.zip' 2>/dev/null > out/ross_area_cldclass_files

### extract_area.py

Extract profile columns from CloudSat HDF-EOS2 files in a given area.

Example:

    spark-submit scripts/extract_area.py -o out/ross_sea.h5 -a ross_sea -f out/ross_area_files 2>/dev/null
    spark-submit scripts/extract_area.py -o out/ross_ice_shelf.h5 -a ross_ice_shelf -f out/ross_area_files 2>/dev/null

    spark-submit scripts/extract_area.py -o out/ross_sea_cldclass.h5 -p 2b-cldclass-lidar -a ross_sea -f out/ross_area_cldclass_files 2>/dev/null
    spark-submit scripts/extract_area.py -o out/ross_ice_shelf_cldclass.h5 -p 2b-cldclass-lidar -a ross_ice_shelf -f out/ross_area_cldclass_files 2>/dev/null

### cloud_top_hist.py

Produce a histogram of the topmost cloud top height.

Example:

    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR)" -o out/cloud_top_hist_rs.pdf out/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR)" -o out/cloud_top_hist_ris.pdf out/ross_ice_shelf.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, CPR)" -i 1 -o out/cloud_top_hist_rs_cpr.pdf out/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, CALIOP)" -i 2 -o out/cloud_top_hist_rs_caliop.pdf out/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, CPR)" -i 1 -o out/cloud_top_hist_ris_cpr.pdf out/ross_ice_shelf.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, CALIOP)" -i 2 -o out/cloud_top_hist_ris_caliop.pdf out/ross_ice_shelf.h5 2>/dev/null

    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_top_hist_rs_cldclass.pdf out/ross_sea_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_top_hist_ris_cldclass.pdf out/ross_ice_shelf_cldclass.h5 2>/dev/null

### profile_sample.py

Plot a profile sample.

Example:

    spark-submit scripts/profile_sample.py -o out/profile_sample_rs.pdf out/ross_sea.h5 2>/dev/null
    spark-submit scripts/profile_sample.py -o out/profile_sample_ris.pdf out/ross_ice_shelf.h5 2>/dev/null

### cloud_top_base_scatter.py

Plot cloud top/cloud base scatter plot from a sample of data.

Example:

    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Sea, 2B-GEOPROF-LIDAR)' -o out/cloud_top_base_scatter_rs.png out/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Ice Shelf, 2B-GEOPROF-LIDAR)' -o out/cloud_top_base_scatter_ris.png out/ross_ice_shelf.h5 2>/dev/null

    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Sea, 2B-CLDCLASS-LIDAR)' -o out/cloud_top_base_scatter_rs_cldclass.png out/ross_sea_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Ice Shelf, 2B-CLDCLASS-LIDAR)' -o out/cloud_top_base_scatter_ris_cldclass.png out/ross_ice_shelf_cldclass.h5 2>/dev/null

### cloud_incidence.py

Produce cloud incidence histogram.

Example:

    spark-submit scripts/cloud_incidence.py out/ross_sea.h5 -o out/cloud_incidence_rs.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 0 out/ross_sea.h5 -o out/cloud_incidence_rs_night.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 1 out/ross_sea.h5 -o out/cloud_incidence_rs_day.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py out/ross_ice_shelf.h5 -o out/cloud_incidence_ris.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 0 out/ross_ice_shelf.h5 -o out/cloud_incidence_ris_night.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 1 out/ross_ice_shelf.h5 -o out/cloud_incidence_ris_day.h5 2>/dev/null

    spark-submit scripts/cloud_incidence.py out/ross_sea_cldclass.h5 -o out/cloud_incidence_rs_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py out/ross_ice_shelf_cldclass.h5 -o out/cloud_incidence_ris_cldclass.h5 2>/dev/null

### plot_cloud_incidence.py

Plot cloud incidence histogram.

Example:

    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR)" -o out/cloud_incidence_rs.png out/cloud_incidence_rs.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, night)" -o out/cloud_incidence_rs_night.png out/cloud_incidence_rs_night.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, day)" -o out/cloud_incidence_rs_day.png out/cloud_incidence_rs_day.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR)" -o out/cloud_incidence_ris.png out/cloud_incidence_ris.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, night)" -o out/cloud_incidence_ris_night.png out/cloud_incidence_ris_night.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, day)" -o out/cloud_incidence_ris_day.png out/cloud_incidence_ris_day.h5

    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_rs_cldclass.png out/cloud_incidence_rs_cldclass.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_ris_cldclass.png out/cloud_incidence_ris_cldclass.h5

### plot_cloud_incidence_by_type.py

Plot cloud incidence by type histogram.

Example:

    python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_rs_cldclass.pdf out/cloud_incidence_rs_cldclass.h5
    python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_ris_cldclass.pdf out/cloud_incidence_ris_cldclass.h5

### cloud_incidence_map_8000_8300

Calculate cloud incidence map for two heights (8000 m and 8300 m).

    Example:

        spark-submit scripts/cloud_incidence_map_8000_8300.py -o out/cloud_incidence_map_8000_8300.h5 '/data/datasets/cloudsat/2b-geoprof-lidar/*/*/*.zip' 2>/dev/null

### plot_correction_factor.py

Plot a map of cloud incidence correction factor (cloud incidence at 8000 m over cloud incidence at
8300 m).

Example:

    python scripts/plot_correction_factor.py out/cloud_incidence_map_8000_8300.h5 -t 'Cloud incidence correction factor 8000 m vs. 8300 m' -o out/correction_factor.pdf

    python scripts/plot_correction_factor.py out/cloud_incidence_map_8000_8300_djf.h5 -t 'Cloud incidence correction factor 8000 m vs. 8300 m (DJF)' -o out/correction_factor_djf.pdf

    python scripts/plot_correction_factor.py out/cloud_incidence_map_8000_8300_jja.h5 -t 'Cloud incidence correction factor 8000 m vs. 8300 m (JJA)' -o out/correction_factor_jja.pdf
