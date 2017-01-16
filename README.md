# Analysis of clouds over Ross Sea and the Ross Ice Shelf

## Requirements

- Python 2.7
- Spark >= 2.0.1
- numpy
- matplotlib
- pytz
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

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, ${regime^^}, 2006-2011, 2B-GEOPROF-LIDAR)" -o "out/cloud_top_hist_rs_$regime.pdf" -r "$regime" out/ross_sea.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, ${regime^^}, 2006-2011, 2B-GEOPROF-LIDAR)" -o "out/cloud_top_hist_ris_$regime.pdf" -r "$regime" out/ross_ice_shelf.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, ${regime^^}, 2006-2011, 2B-CLDCLASS-LIDAR)" -o "out/cloud_top_hist_rs_${regime}_cldclass.pdf" -r "$regime" out/ross_sea_cldclass.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, ${regime^^}, 2006-2011, 2B-CLDCLASS-LIDAR)" -o "out/cloud_top_hist_ris_${regime}_cldclass.pdf" -r "$regime" out/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

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

    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar out/ross_sea_cldclass.h5 -o out/cloud_incidence_rs_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar out/ross_ice_shelf_cldclass.h5 -o out/cloud_incidence_ris_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" out/ross_sea_cldclass.h5 -o "out/cloud_incidence_rs_${regime}_cldclass.h5" 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" out/ross_ice_shelf_cldclass.h5 -o "out/cloud_incidence_ris_${regime}_cldclass.h5" 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" out/ross_sea_cldclass.h5 -o "out/cloud_incidence_rs_${season}_cldclass.h5" 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" out/ross_ice_shelf_cldclass.h5 -o "out/cloud_incidence_ris_${season}_cldclass.h5" 2>/dev/null
    done

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

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_rs_${regime}_cldclass.png out/cloud_incidence_rs_cldclass.h5
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_ris_${regime}_cldclass.png out/cloud_incidence_ris_${regime}_cldclass.h5
    done


### plot_cloud_incidence_by_type.py

Plot cloud incidence by type histogram.

Example:

    python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_rs_cldclass.png out/cloud_incidence_rs_cldclass.h5
    python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_ris_cldclass.png out/cloud_incidence_ris_cldclass.h5

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_rs_${regime}_cldclass.png out/cloud_incidence_rs_${regime}_cldclass.h5
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_ris_${regime}_cldclass.png out/cloud_incidence_ris_${regime}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_rs_${season}_cldclass.png out/cloud_incidence_rs_${season}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_type_ris_${season}_cldclass.png out/cloud_incidence_ris_${season}_cldclass.h5
    done

### plot_cloud_incidence_by_phase.py

Plot cloud incidence by phase histogram.

Example:

    python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_phase_rs_cldclass.png out/cloud_incidence_rs_cldclass.h5
    python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_phase_ris_cldclass.png out/cloud_incidence_ris_cldclass.h5

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_phase_rs_${regime}_cldclass.png out/cloud_incidence_rs_${regime}_cldclass.h5
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_phase_ris_${regime}_cldclass.png out/cloud_incidence_ris_${regime}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_phase_rs_${season}_cldclass.png out/cloud_incidence_rs_${season}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o out/cloud_incidence_by_phase_ris_${season}_cldclass.png out/cloud_incidence_ris_${season}_cldclass.h5
    done

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

### plot_regimes.py

Plot regimes distribution by month.

Example:

    python scripts/plot_regimes.py -t 'Regimes distribution by month (2007-2010)' -o out/regimes.pdf

### plot_cloud_incidence_summary_by_phase.py

Plot cloud incidence summary by phase.

Example:

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o out/cloud_incidence_summary_by_phase_rs_seasons.png out/cloud_incidence_rs_djf_cldclass.h5 out/cloud_incidence_rs_mam_cldclass.h5 out/cloud_incidence_rs_jja_cldclass.h5 out/cloud_incidence_rs_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o out/cloud_incidence_summary_by_phase_ris_seasons.png out/cloud_incidence_ris_djf_cldclass.h5 out/cloud_incidence_ris_mam_cldclass.h5 out/cloud_incidence_ris_jja_cldclass.h5 out/cloud_incidence_ris_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o out/cloud_incidence_summary_by_phase_rs_regimes.png out/cloud_incidence_rs_wnc_cldclass.h5 out/cloud_incidence_rs_snc_cldclass.h5 out/cloud_incidence_rs_ras_cldclass.h5 out/cloud_incidence_rs_wsc_cldclass.h5 out/cloud_incidence_rs_ws_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o out/cloud_incidence_summary_by_phase_ris_regimes.png out/cloud_incidence_ris_wnc_cldclass.h5 out/cloud_incidence_ris_snc_cldclass.h5 out/cloud_incidence_ris_ras_cldclass.h5 out/cloud_incidence_ris_wsc_cldclass.h5 out/cloud_incidence_ris_ws_cldclass.h5

### plot_cloud_incidence_summary_by_type.py

Plot cloud incidence summary by type.

Example:

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o out/cloud_incidence_summary_by_type_rs_seasons.png out/cloud_incidence_rs_djf_cldclass.h5 out/cloud_incidence_rs_mam_cldclass.h5 out/cloud_incidence_rs_jja_cldclass.h5 out/cloud_incidence_rs_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o out/cloud_incidence_summary_by_type_ris_seasons.png out/cloud_incidence_ris_djf_cldclass.h5 out/cloud_incidence_ris_mam_cldclass.h5 out/cloud_incidence_ris_jja_cldclass.h5 out/cloud_incidence_ris_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o out/cloud_incidence_summary_by_type_rs_regimes.png out/cloud_incidence_rs_wnc_cldclass.h5 out/cloud_incidence_rs_snc_cldclass.h5 out/cloud_incidence_rs_ras_cldclass.h5 out/cloud_incidence_rs_wsc_cldclass.h5 out/cloud_incidence_rs_ws_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o out/cloud_incidence_summary_by_type_ris_regimes.png out/cloud_incidence_ris_wnc_cldclass.h5 out/cloud_incidence_ris_snc_cldclass.h5 out/cloud_incidence_ris_ras_cldclass.h5 out/cloud_incidence_ris_wsc_cldclass.h5 out/cloud_incidence_ris_ws_cldclass.h5

## plot_cloud_incidence_information_gain.py

Plot cloud incidence information gain.

Example:

    python scripts/plot_cloud_incidence_information_gain.py -x phase -o out/cloud_incidence_information_gain_rs_phase.png -c data/classes_rs.json
    python scripts/plot_cloud_incidence_information_gain.py -x type -o out/cloud_incidence_information_gain_rs_type.png -c data/classes_rs.json

    python scripts/plot_cloud_incidence_information_gain.py -x phase -o out/cloud_incidence_information_gain_ris_phase.png -c data/classes_ris.json
    python scripts/plot_cloud_incidence_information_gain.py -x type -o out/cloud_incidence_information_gain_ris_type.png -c data/classes_ris.json


## Coggins clusters

- `wnc`: weak northern cyclonic (WNC)
- `snc`: strong northern cyclonic (SNC)
- `ras`: Ross Ice Shelf air stream (RAS)
- `wsc`: weak southern cyclonic (WSC)
- `ws`: katabatic and weak synoptic (WS)
