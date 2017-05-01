# Code and data for the paper "An analysis of the cloud environment over the Ross Sea and Ross Ice Shelf using CloudSat/CALIPSO satellites: The importance of Synoptic Forcing"

Ben Jolly <<jollyb@landcareresearch.co.nz>>¹,
Peter Kuma <<peter.kuma@pg.canterbury.ac.nz>>²,
Adrian McDonald <<adrian.mcdonald@canterbury.ac.nz>>²,
Simon Parsons <<simon.parsons@canterbury.ac.nz>>²

¹Landcare Research, Lincoln, New Zealand, ²University of Canterbury, Christchurch, New Zealand

This repository contains scientific datasets and scripts for processing CloudSat
datasets and producing results presented in the paper
*An analysis of the cloud environment over the Ross Sea and Ross Ice Shelf
using CloudSat/CALIPSO satellites: The importance of Synoptic Forcing*.

## Setup

It is recommended that the scripts are run on Linux or another unix-like
operating system. Most scripts are written in the Python programming language.
Some of the scripts need to be run on the [Spark](https://spark.apache.org/)
cluster computing platform.
Note that Spark does not require cluster deployment, it works equally well
when run locally on a single machine with 4 GB RAM or more.

For running on Windows we recommended the
[Anaconda Python distribution](https://www.continuum.io/downloads),
although we haven't attempted to run the code on this platform, and Linux
is strongly preferrable.

The following programs need to be installed:

- [Spark](https://spark.apache.org/) >= 2.0.1
- Python 2.7
- GNU Make

On most Linux distributions Python and GNU Make can be found in the package
manager, while Spark is available as a
[binary package on their website](https://spark.apache.org/downloads.html).

Python libraries:

- numpy == 1.11.2
- matplotlib == 1.5.3
- pytz == 2016.7
- h5py == 2.2.1
- dpath == 1.4.0
- ccplot == 1.5.2

To install the libraries with the python package manager (PIP) in a Python
virtual environment (virtualenv):

    virtualenv env
    . env/bin/activate
    pip install -r requirements.txt

### Optional

The following software is needed only for generating the map in Figure 1
(script `map.R`):

- [R](https://www.r-project.org/)
- R packages:
    - raster
    - sp
    - rgdal
    - rgeos
    - maptools
    - geosphere
    - RColorBrewer
    - graticule

The following software is needed for conversion between graphical formats
(PDF to PNG):

- ImageMagick

## Source Datasets

In order to run the scripts the following products should be available
on your file system:

- [CloudSat 2B-CLDCLASS-LIDAR P_R04 products (2007-2010)](http://www.cloudsat.cira.colostate.edu/data-products/level-2b/2b-cldclass-lidar?term=26)
- **Optional:** [CloudSat 2B-GEOPROF-LIDAR P2_R04 products (2006-2011)](http://www.cloudsat.cira.colostate.edu/data-products/level-2b/2b-geoprof-lidar?term=48)

You can download the complete datasets from the
CloudSat DPC FTP server
at [ftp://ftp.cloudsat.cira.colostate.edu](ftp://ftp.cloudsat.cira.colostate.edu)
after creating an account on [CloudSat DPC](http://www.cloudsat.cira.colostate.edu/).

The product files do not need to be unpacked, the code expects the directory
structure "as is".

## Figures and Tables

The following sections list scripts names used to produce figures and tables
in the paper. Please see the reference section below for a full description
of the scripts. **Scripts** is a list of scripts which need to be run in order to
produce the figure or table.

This repository also contains scripts which may
be useful for additional analysis, but were not used directly to produce
results presented in the paper.

### Figure 1

[![](img/map.png)](plots/map.pdf)

Topographic map of the RIS and Ross Sea showing boundary of the study area
(thick blue line) and border between the RIS and Ross Sea sectors. (Map is based
on the SCAR Antarctic Digital Database.)

**Scripts:** [map.R](scripts/map.R)

### Figure 2

[![](img/cloud_incidence_by_phase_season.png)](plots/cloud_incidence_by_phase_season.png)

Mean vertical profiles of cumulative cloud occurrence for different cloud phases
derived from 2B-CLDCLASS-LIDAR data for the Ross Sea (a–d) and Ross Ice Shelf
regions (e–h) for different seasons.

**Scripts:** [ross_area_files.py](scripts/ross_area_files.py), [extract_area.py](scripts/extract_area.py), [cloud_incidence.py](scripts/cloud_incidence.py),
[plot_cloud_incidence_summary_by_phase.py](plot_cloud_incidence_summary_by_phase.py)

### Figure 3

[![](img/cloud_incidence_by_phase_regime.png)](plots/cloud_incidence_by_phase_regime.png)

Mean vertical profiles of cumulative cloud occurrence for different cloud phases
derived from 2B-CLDCLASS-LIDAR data for the Ross Sea (a–e) and Ross Ice Shelf
regions (f–j) for the Coggins regimes.

**Scripts:** [ross_area_files.py](scripts/ross_area_files.py), [extract_area.py](scripts/extract_area.py), [cloud_incidence.py](scripts/cloud_incidence.py),
[plot_cloud_incidence_summary_by_phase.py](plot_cloud_incidence_summary_by_phase.py)

### Figure 4

[![](img/cloud_layers_hist_cldclass.png)](plots/cloud_layers_hist_cldclass.png)

Distribution of the number of cloud layers over the Ross Sea and Ross Ice Shelf
for all cases, the Coggins regimes and season.

**Scripts:** [ross_area_files.py](scripts/ross_area_files.py), [extract_area.py](scripts/extract_area.py), [cloud_layers_hist.py](scripts/cloud_layers_hist.py), [plot_cloud_layers_hist.py](scripts/cloud_layers_hist.py)

### Figure 5

[![](img/cloud_types_hist_int.png)](plots/cloud_types_hist_int.png)

Percent fraction of cloud types over the Ross Sea and Ross Ice Shelf for all
cases, the Coggins regimes and seasons. The cloud types are identified in
Table 1.

**Scripts:** [ross_area_files.py](scripts/ross_area_files.py), [extract_area.py](scripts/extract_area.py), [cloud_types_hist_int.py](scripts/cloud_types_hist_int.py) [plot_cloud_types_hist_int.py](scripts/plot_cloud_types_hist_int.py)

### Figure 6

[![](img/cloud_top_thickness_composite_regime.png)](plots/cloud_top_thickness_composite_regime.png)

Joint histogram of the cloud top height vs. geometric cloud thickness over the Ross Sea and RIS for the entire year on a logarithmic scale (a, f) and the difference from the annual mean over the respective region (RS and RIS) for each season on a linear scale (b-e, g-j).

**Scripts:** [ross_area_files.py](scripts/ross_area_files.py), [extract_area.py](scripts/extract_area.py), [cloud_top_thickness_hist.py](scripts/cloud_top_thickness_hist.py), [plot_cloud_top_thickness_composite.py](scripts/plot_cloud_top_thickness_composite.py)

### Figure 7

[![](img/cloud_top_thickness_composite_season.png)](plots/cloud_top_thickness_composite_season.png)

Joint histogram of the cloud top height vs. geometric cloud thickness over the Ross Sea and RIS for the entire year on a logarithmic scale (a, f) and the difference from the annual mean over the respective region (RS and RIS) for each Coggins regime on a linear scale (b-e, g-j).

**Scripts:** [ross_area_files.py](scripts/ross_area_files.py), [extract_area.py](scripts/extract_area.py), [cloud_top_thickness_hist.py](scripts/cloud_top_thickness_hist.py), [plot_cloud_top_thickness_composite.py](scripts/plot_cloud_top_thickness_composite.py)

### Table 2

The relative frequency of occurrence of the Coggins regimes annually and
seasonally in the observational data (%). Values for seasons are normalized so
that rows sum to 100 %.

**Scripts:** [ross_area_files.py](scripts/ross_area_files.py), [extract_area.py](scripts/extract_area.py), [regime_season_hist.py](regime_season_hist.py), [print_regime_season_table.py](scripts/print_regime_season_table.py)

## Repository Content

- `config` - configuration files needed by the scripts
- `data` - intermediate data files
- `img` - figure images
- `lib` - additional python modules used by the scripts
- `plots` - plots
- `scripts` - data processing and plotting scripts

## Usage

To produce all plots and intermediate data from the CloudSat products, use:

    make

You can also specify a target to produce subset of results with:

    make <target>

or

    make plots/<name>.pdf

where `<name>` is the name of the plot and `<target>` is one of:

- `map` - the map
- `cloud_top_hist`
- `profile_sample`
- `cloud_top_base_scatter`

Targets correspond to the scripts described in the reference section.

## Reference

Use `spark-submit scripts/<script>.py --help` for more information about how
to submit the scripts. The Spark cluster does not need to be running,
`spark-submit` starts a local instance as needed (you only need to make
sure that `spark-submit` is in your `PATH` environmental variable).

Intermediate data files are stored as HDF5 and plots as PNG or PDF.

### map.R

    scripts/map.R plots/map.pdf /data/datasets/add/

### ross_area_files.py

Output a list of CloudSat HDF-EOS2 files containing data over the
Ross Sea/Ross Ice Shelf area.

    spark-submit scripts/ross_area_files.py '/data/datasets/cloudsat/2b-geoprof-lidar/*/*/*.zip' 2>/dev/null > plots/ross_area_files
    spark-submit scripts/ross_area_files.py '/data/datasets/cloudsat/2b-cldclass-lidar.p_r04/*/*/*.zip' 2>/dev/null > plots/ross_area_cldclass_files

### extract_area.py

Extract profile columns from CloudSat HDF-EOS2 files in a given area.

    spark-submit scripts/extract_area.py -o data/ross_sea.h5 -a ross_sea -f plots/ross_area_files 2>/dev/null
    spark-submit scripts/extract_area.py -o data/ross_ice_shelf.h5 -a ross_ice_shelf -f plots/ross_area_files 2>/dev/null

    spark-submit scripts/extract_area.py -o data/ross_sea_cldclass.h5 -p 2b-cldclass-lidar -a ross_sea -f plots/ross_area_cldclass_files 2>/dev/null
    spark-submit scripts/extract_area.py -o data/ross_ice_shelf_cldclass.h5 -p 2b-cldclass-lidar -a ross_ice_shelf -f plots/ross_area_cldclass_files 2>/dev/null

### cloud_top_hist.py

Produce a histogram of the topmost cloud top height.

    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR)" -o plots/cloud_top_hist_rs.pdf data/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR)" -o plots/cloud_top_hist_ris.pdf data/ross_ice_shelf.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, CPR)" -i 1 -o plots/cloud_top_hist_rs_cpr.pdf data/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, CALIOP)" -i 2 -o plots/cloud_top_hist_rs_caliop.pdf data/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, CPR)" -i 1 -o plots/cloud_top_hist_ris_cpr.pdf data/ross_ice_shelf.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, CALIOP)" -i 2 -o plots/cloud_top_hist_ris_caliop.pdf data/ross_ice_shelf.h5 2>/dev/null

    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_top_hist_rs_cldclass.pdf data/ross_sea_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_top_hist_ris_cldclass.pdf data/ross_ice_shelf_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, ${regime^^}, 2006-2011, 2B-GEOPROF-LIDAR)" -o "plots/cloud_top_hist_rs_$regime.pdf" -r "$regime" data/ross_sea.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, ${regime^^}, 2006-2011, 2B-GEOPROF-LIDAR)" -o "plots/cloud_top_hist_ris_$regime.pdf" -r "$regime" data/ross_ice_shelf.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, ${regime^^}, 2006-2011, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_hist_rs_${regime}_cldclass.pdf" -r "$regime" data/ross_sea_cldclass.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, ${regime^^}, 2006-2011, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_hist_ris_${regime}_cldclass.pdf" -r "$regime" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

### profile_sample.py

Plot a profile sample.

    spark-submit scripts/profile_sample.py -o plots/profile_sample_rs.pdf data/ross_sea.h5 2>/dev/null
    spark-submit scripts/profile_sample.py -o plots/profile_sample_ris.pdf data/ross_ice_shelf.h5 2>/dev/null

### cloud_top_base_scatter.py

Plot cloud top vs. cloud base scatter plot from a sample of data.

    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Sea, 2B-GEOPROF-LIDAR)' -o plots/cloud_top_base_scatter_rs.png data/ross_sea.h5 2>/dev/null
    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Ice Shelf, 2B-GEOPROF-LIDAR)' -o plots/cloud_top_base_scatter_ris.png data/ross_ice_shelf.h5 2>/dev/null

    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Sea, 2B-CLDCLASS-LIDAR)' -o plots/cloud_top_base_scatter_rs_cldclass.png data/ross_sea_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Ice Shelf, 2B-CLDCLASS-LIDAR)' -o plots/cloud_top_base_scatter_ris_cldclass.png data/ross_ice_shelf_cldclass.h5 2>/dev/null

### cloud_top_base_scatter_multi.py

Plot cloud top vs. cloud base scatter plot from a sample of data
(multiple panels).

    spark-submit scripts/cloud_top_base_scatter_multi.py -c config/cloud_top_base_scatter_multi.json -o $@ 2>/dev/null

### cloud_incidence.py

Produce cloud incidence histogram.

    spark-submit scripts/cloud_incidence.py data/ross_sea.h5 -o data/cloud_incidence_rs.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 0 data/ross_sea.h5 -o data/cloud_incidence_rs_night.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 1 data/ross_sea.h5 -o data/cloud_incidence_rs_day.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py data/ross_ice_shelf.h5 -o data/cloud_incidence_ris.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 0 data/ross_ice_shelf.h5 -o data/cloud_incidence_ris_night.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -n 1 data/ross_ice_shelf.h5 -o data/cloud_incidence_ris_day.h5 2>/dev/null

    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar data/ross_sea_cldclass.h5 -o data/cloud_incidence_rs_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar data/ross_sea_cldclass.h5 -a ross_sea_east -o data/cloud_incidence_rs-e_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar data/ross_sea_cldclass.h5 -a ross_sea_west -o data/cloud_incidence_rs-w_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar data/ross_ice_shelf_cldclass.h5 -o data/cloud_incidence_ris_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar data/ross_ice_shelf_cldclass.h5 -a ross_ice_shelf_east -o data/cloud_incidence_ris-e_cldclass.h5 2>/dev/null\
    spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar data/ross_ice_shelf_cldclass.h5 -a ross_ice_shelf_west -o data/cloud_incidence_ris-w_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" data/ross_sea_cldclass.h5 -o "data/cloud_incidence_rs_${regime}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" data/ross_sea_cldclass.h5 -a ross_sea_east -o "data/cloud_incidence_rs-e_${regime}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" data/ross_sea_cldclass.h5 -a ross_sea_west -o "data/cloud_incidence_rs-w_${regime}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" data/ross_ice_shelf_cldclass.h5 -o "data/cloud_incidence_ris_${regime}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" data/ross_ice_shelf_cldclass.h5 -a ross_ice_shelf_east -o "data/cloud_incidence_ris-e_${regime}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r "$regime" data/ross_ice_shelf_cldclass.h5 -a ross_ice_shelf_west -o "data/cloud_incidence_ris-w_${regime}_cldclass.h5" 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" data/ross_sea_cldclass.h5 -o "data/cloud_incidence_rs_${season}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" data/ross_sea_cldclass.h5 -a ross_sea_east -o "data/cloud_incidence_rs-e_${season}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" data/ross_sea_cldclass.h5 -a ross_sea_west -o "data/cloud_incidence_rs-w_${season}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" data/ross_ice_shelf_cldclass.h5 -o "data/cloud_incidence_ris_${season}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" data/ross_ice_shelf_cldclass.h5 -a ross_ice_shelf_east -o "data/cloud_incidence_ris-e_${season}_cldclass.h5" 2>/dev/null
        spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s "$season" data/ross_ice_shelf_cldclass.h5 -a ross_ice_shelf_west -o "data/cloud_incidence_ris-w_${season}_cldclass.h5" 2>/dev/null
    done

### plot_cloud_incidence.py

Plot cloud incidence histogram.

    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR)" -o plots/cloud_incidence_rs.png data/cloud_incidence_rs.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, night)" -o plots/cloud_incidence_rs_night.png data/cloud_incidence_rs_night.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, day)" -o plots/cloud_incidence_rs_day.png data/cloud_incidence_rs_day.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR)" -o plots/cloud_incidence_ris.png data/cloud_incidence_ris.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, night)" -o plots/cloud_incidence_ris_night.png data/cloud_incidence_ris_night.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, day)" -o plots/cloud_incidence_ris_day.png data/cloud_incidence_ris_day.h5

    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_rs_cldclass.png data/cloud_incidence_rs_cldclass.h5
    python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_ris_cldclass.png data/cloud_incidence_ris_cldclass.h5

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_rs_${regime}_cldclass.png data/cloud_incidence_rs_cldclass.h5
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_ris_${regime}_cldclass.png data/cloud_incidence_ris_${regime}_cldclass.h5
    done


### plot_cloud_incidence_by_type.py

Plot cloud incidence by type histogram.

    python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_type_rs_cldclass.png data/cloud_incidence_rs_cldclass.h5
    python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_type_ris_cldclass.png data/cloud_incidence_ris_cldclass.h5

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_type_rs_${regime}_cldclass.png data/cloud_incidence_rs_${regime}_cldclass.h5
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_type_ris_${regime}_cldclass.png data/cloud_incidence_ris_${regime}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_type_rs_${season}_cldclass.png data/cloud_incidence_rs_${season}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_type_ris_${season}_cldclass.png data/cloud_incidence_ris_${season}_cldclass.h5
    done

### plot_cloud_incidence_by_phase.py

Plot cloud incidence by phase histogram.

    python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_phase_rs_cldclass.png data/cloud_incidence_rs_cldclass.h5
    python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_phase_ris_cldclass.png data/cloud_incidence_ris_cldclass.h5

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_phase_rs_${regime}_cldclass.png data/cloud_incidence_rs_${regime}_cldclass.h5
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_phase_ris_${regime}_cldclass.png data/cloud_incidence_ris_${regime}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_phase_rs_${season}_cldclass.png data/cloud_incidence_rs_${season}_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_incidence_by_phase_ris_${season}_cldclass.png data/cloud_incidence_ris_${season}_cldclass.h5
    done

### plot_cloud_incidence_multi.py

Plot cloud incidence as a function of height (multiple datasets).

    python scripts/plot_cloud_incidence_multi.py -o plots/cloud_incidence_multi.pdf -c config/cloud_incidence_multi.json

### cloud_incidence_map_8000_8300

Calculate cloud incidence map for two heights (8000 m and 8300 m).

    spark-submit scripts/cloud_incidence_map_8000_8300.py -o data/cloud_incidence_map_8000_8300.h5 '/data/datasets/cloudsat/2b-geoprof-lidar/*/*/*.zip' 2>/dev/null

### plot_correction_factor.py

Plot a map of cloud incidence correction factor (cloud incidence at 8300 m over
cloud incidence at 8000 m).

    python scripts/plot_correction_factor.py data/cloud_incidence_map_8000_8300.h5 -t 'Cloud incidence correction factor 8000 m vs. 8300 m' -o plots/correction_factor.pdf

    python scripts/plot_correction_factor.py data/cloud_incidence_map_8000_8300_djf.h5 -t 'Cloud incidence correction factor 8000 m vs. 8300 m (DJF)' -o plots/correction_factor_djf.pdf

    python scripts/plot_correction_factor.py data/cloud_incidence_map_8000_8300_jja.h5 -t 'Cloud incidence correction factor 8000 m vs. 8300 m (JJA)' -o plots/correction_factor_jja.pdf

### plot_correction_factor_multi.py

Plot a map of cloud incidence correction factor (cloud incidence at 8300 m over
cloud incidence at 8300 m) (multiple panels).

    python scripts/plot_correction_factor_multi.py -o plots/correction_factor_multi.pdf -c config/correction_factor_multi.json

### plot_regimes.py

Plot regimes distribution by month.

    python scripts/plot_regimes.py -t 'Regimes distribution by month (2007-2010)' -o plots/regimes.pdf

### plot_cloud_incidence_summary_by_phase.py

Plot cloud incidence summary by phase.

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o plots/cloud_incidence_summary_by_phase_rs_seasons.png data/cloud_incidence_rs_djf_cldclass.h5 data/cloud_incidence_rs_mam_cldclass.h5 data/cloud_incidence_rs_jja_cldclass.h5 data/cloud_incidence_rs_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o plots/cloud_incidence_summary_by_phase_ris_seasons.png data/cloud_incidence_ris_djf_cldclass.h5 data/cloud_incidence_ris_mam_cldclass.h5 data/cloud_incidence_ris_jja_cldclass.h5 data/cloud_incidence_ris_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o plots/cloud_incidence_summary_by_phase_rs_regimes.png data/cloud_incidence_rs_wnc_cldclass.h5 data/cloud_incidence_rs_snc_cldclass.h5 data/cloud_incidence_rs_ras_cldclass.h5 data/cloud_incidence_rs_wsc_cldclass.h5 data/cloud_incidence_rs_ws_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o plots/cloud_incidence_summary_by_phase_ris_regimes.png data/cloud_incidence_ris_wnc_cldclass.h5 data/cloud_incidence_ris_snc_cldclass.h5 data/cloud_incidence_ris_ras_cldclass.h5 data/cloud_incidence_ris_wsc_cldclass.h5 data/cloud_incidence_ris_ws_cldclass.h5

### plot_cloud_incidence_summary_by_type.py

Plot cloud incidence summary by type.

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o plots/cloud_incidence_summary_by_type_rs_seasons.png data/cloud_incidence_rs_djf_cldclass.h5 data/cloud_incidence_rs_mam_cldclass.h5 data/cloud_incidence_rs_jja_cldclass.h5 data/cloud_incidence_rs_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o plots/cloud_incidence_summary_by_type_ris_seasons.png data/cloud_incidence_ris_djf_cldclass.h5 data/cloud_incidence_ris_mam_cldclass.h5 data/cloud_incidence_ris_jja_cldclass.h5 data/cloud_incidence_ris_son_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o plots/cloud_incidence_summary_by_type_rs_regimes.png data/cloud_incidence_rs_wnc_cldclass.h5 data/cloud_incidence_rs_snc_cldclass.h5 data/cloud_incidence_rs_ras_cldclass.h5 data/cloud_incidence_rs_wsc_cldclass.h5 data/cloud_incidence_rs_ws_cldclass.h5

    python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o plots/cloud_incidence_summary_by_type_ris_regimes.png data/cloud_incidence_ris_wnc_cldclass.h5 data/cloud_incidence_ris_snc_cldclass.h5 data/cloud_incidence_ris_ras_cldclass.h5 data/cloud_incidence_ris_wsc_cldclass.h5 data/cloud_incidence_ris_ws_cldclass.h5

### plot_cloud_incidence_information_gain.py

Plot cloud incidence information gain.

    python scripts/plot_cloud_incidence_information_gain.py -t "Information gain (Ross Sea, 2007-2010, 2B-CLDCLASS)" -x phase -o plots/cloud_incidence_information_gain_rs_phase.png -c data/classes_rs.json
    python scripts/plot_cloud_incidence_information_gain.py -t "Information gain (Ross Sea, 2007-2010, 2B-CLDCLASS)"  -x type -o plots/cloud_incidence_information_gain_rs_type.png -c data/classes_rs.json

    python scripts/plot_cloud_incidence_information_gain.py -t "Information gain (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS)"  -x phase -o plots/cloud_incidence_information_gain_ris_phase.png -c config/classes_ris.json
    python scripts/plot_cloud_incidence_information_gain.py -t "Information gain (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS)"  -x type -o plots/cloud_incidence_information_gain_ris_type.png -c config/classes_ris.json

### plot_cloud_incidence_by_phase_multiple.py

Plot cloud incidence by phase (multiple panels).

    python scripts/plot_cloud_incidence_by_phase_multiple.py -o plots/cloud_incidence_by_phase_regime.png -c config/cloud_incidence_by_phase_regime.json

    python scripts/plot_cloud_incidence_by_phase_multiple.py -o plots/cloud_incidence_by_phase_season.png -c config/cloud_incidence_by_phase_season.json

### cloud_incidence_summary.py

Print fraction of cloudy profiles.

    python scripts/cloud_incidence_summary.py -o data/cloud_incidence_summary_cldclass.h5 -c config/cloud_incidence_summary_cldclass.json

    sh -c '
        for regime in wnc snc ras wsc ws; do
            echo "RS,${regime^^},$(python scripts/cloud_incidence_cloudy.py data/cloud_incidence_rs_${regime}_cldclass.h5)"
        done

        for regime in wnc snc ras wsc ws; do
            echo "RIS,${regime^^},$(python scripts/cloud_incidence_cloudy.py data/cloud_incidence_ris_${regime}_cldclass.h5)"
        done

        for season in djf mam jja son; do
            echo "RS,${season^^},$(python scripts/cloud_incidence_cloudy.py data/cloud_incidence_rs_${season}_cldclass.h5)"
        done

        for season in djf mam jja son; do
            echo "RIS,${season^^},$(python scripts/cloud_incidence_cloudy.py data/cloud_incidence_ris_${season}_cldclass.h5)"
        done
    ' > plots/cloud_incidence_summary_cldclass.csv

### cloud_layers_hist.py

Cloud layers histogram.

    spark-submit scripts/cloud_layers_hist.py -o data/cloud_layers_hist_rs_cldclass.h5 data/ross_sea_cldclass.h5 2>/dev/null
    spark-submit scripts/cloud_layers_hist.py -o data/cloud_layers_hist_ris_cldclass.h5 data/ross_ice_shelf_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_layers_hist.py -o data/cloud_layers_hist_rs_${regime}_cldclass.h5 -r "$regime" data/ross_sea_cldclass.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_layers_hist.py -o data/cloud_layers_hist_ris_${regime}_cldclass.h5 -r "$regime" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_layers_hist.py -o data/cloud_layers_hist_rs_${season}_cldclass.h5 -s "$season" data/ross_sea_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_layers_hist.py -o data/cloud_layers_hist_ris_${season}_cldclass.h5 -s "$season" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

### plot_cloud_layers_hist.py

Plot cloud layers histogram.

    python scripts/plot_cloud_layers_hist.py -o plots/cloud_layers_hist_cldclass.png -c config/cloud_layers_hist_cldclass.json

    python scripts/plot_cloud_layers_hist.py -o plots/cloud_layers_hist_rs_cldclass.png -c config/cloud_layers_hist_rs_cldclass.json

    python scripts/plot_cloud_layers_hist.py -o plots/cloud_layers_hist_ris_cldclass.png -c config/cloud_layers_hist_ris_cldclass.json

### count.py

Count the number of profiles.

    bash -c '
        echo "RS,all,$(spark-submit scripts/count.py data/ross_sea_cldclass.h5 2>/dev/null)"
        echo "RIS,all,$(spark-submit scripts/count.py data/ross_ice_shelf_cldclass.h5 2>/dev/null)"

        for regime in wnc snc ras wsc ws; do
            echo "RS,${regime^^},$(spark-submit scripts/count.py -r "$regime" data/ross_sea_cldclass.h5 2>/dev/null)"
            echo "RS-E,${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_sea_east data/ross_sea_cldclass.h5 2>/dev/null)"
            echo "RS-W,${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_sea_west data/ross_sea_cldclass.h5 2>/dev/null)"
            echo "RIS,${regime^^},$(spark-submit scripts/count.py -r "$regime" data/ross_ice_shelf_cldclass.h5 2>/dev/null)"
            echo "RIS-E,${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_ice_shelf_east data/ross_ice_shelf_cldclass.h5 2>/dev/null)"
            echo "RIS-W,${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_ice_shelf_west data/ross_ice_shelf_cldclass.h5 2>/dev/null)"
        done

        for season in djf mam jja son; do
            echo "RS,${season^^},$(spark-submit scripts/count.py -s "$season" data/ross_sea_cldclass.h5 2>/dev/null)"
            echo "RS-E,${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_sea_east data/ross_sea_cldclass.h5 2>/dev/null)"
            echo "RS-W,${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_sea_west data/ross_sea_cldclass.h5 2>/dev/null)"
            echo "RIS,${season^^},$(spark-submit scripts/count.py -s "$season" data/ross_ice_shelf_cldclass.h5 2>/dev/null)"
            echo "RIS-E,${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_ice_shelf_east data/ross_ice_shelf_cldclass.h5 2>/dev/null)"
            echo "RIS-W,${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_ice_shelf_west data/ross_ice_shelf_cldclass.h5 2>/dev/null)"
        done
    ' > data/counts.csv

### cloud_types_hist.py

Cloud types histogram.

    spark-submit scripts/cloud_types_hist.py -o data/cloud_types_hist_rs_cldclass.h5 data/ross_sea_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_types_hist.py -o "data/cloud_types_hist_rs_${regime}_cldclass.h5" -r "$regime" data/ross_sea_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_types_hist.py -o "data/cloud_types_hist_rs_${season}_cldclass.h5" -s "$season" data/ross_sea_cldclass.h5 2>/dev/null
    done

    spark-submit scripts/cloud_types_hist.py -o data/cloud_types_hist_ris_cldclass.h5 data/ross_ice_shelf_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_types_hist.py -o "data/cloud_types_hist_ris_${regime}_cldclass.h5" -r "$regime" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_types_hist.py -o "data/cloud_types_hist_ris_${season}_cldclass.h5" -s "$season" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

### plot_cloud_types_hist.py

Plot cloud types histogram.

    python scripts/plot_cloud_types_hist.py -o plots/cloud_types_hist_rs_cldclass.png -c config/cloud_types_hist_rs_cldclass.json

    python scripts/plot_cloud_types_hist.py -o plots/cloud_types_hist_ris_cldclass.png -c config/cloud_types_hist_ris_cldclass.json

### cloud_top_thickness_hist.py

Cloud top-thickness histogram.

    spark-submit scripts/cloud_top_thickness_hist.py -o data/cloud_top_thickness_hist_rs_cldclass.h5 data/ross_sea_cldclass.h5 2>/dev/null

    spark-submit scripts/cloud_top_thickness_hist.py -o data/cloud_top_thickness_hist_ris_cldclass.h5 data/ross_ice_shelf_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_thickness_hist.py -o "data/cloud_top_thickness_hist_rs_${regime}_cldclass.h5" -r "$regime" data/ross_sea_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_top_thickness_hist.py -o "data/cloud_top_thickness_hist_rs_${season}_cldclass.h5" -s "$season" data/ross_sea_cldclass.h5 2>/dev/null
    done

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_top_thickness_hist.py -o "data/cloud_top_thickness_hist_ris_${regime}_cldclass.h5" -r "$regime" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_top_thickness_hist.py -o "data/cloud_top_thickness_hist_ris_${season}_cldclass.h5" -s "$season" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done


### plot_cloud_top_thickness_hist.py

Plot cloud top-thickness histogram.

    python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_top_thickness_hist_rs_cldclass.pdf data/cloud_top_thickness_hist_rs_cldclass.h5

    python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o plots/cloud_top_thickness_hist_ris_cldclass.pdf data/cloud_top_thickness_hist_ris_cldclass.h5

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_rs_${regime}_cldclass.pdf" "data/cloud_top_thickness_hist_rs_${regime}_cldclass.h5"
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_rs_${season}_cldclass.pdf" "data/cloud_top_thickness_hist_rs_${season}_cldclass.h5"
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_ris_${regime}_cldclass.pdf" "data/cloud_top_thickness_hist_ris_${regime}_cldclass.h5"
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_ris_${season}_cldclass.pdf" "data/cloud_top_thickness_hist_ris_${season}_cldclass.h5"
    done

    # Relative

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_rs_${regime}_rel_cldclass.pdf" "data/cloud_top_thickness_hist_rs_${regime}_cldclass.h5" data/cloud_top_thickness_hist_rs_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_rs_${season}_rel_cldclass.pdf" "data/cloud_top_thickness_hist_rs_${season}_cldclass.h5" data/cloud_top_thickness_hist_rs_cldclass.h5
    done

    for regime in wnc snc ras wsc ws; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, ${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_ris_${regime}_rel_cldclass.pdf" "data/cloud_top_thickness_hist_ris_${regime}_cldclass.h5" data/cloud_top_thickness_hist_ris_cldclass.h5
    done

    for season in djf mam jja son; do
        python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, ${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o "plots/cloud_top_thickness_hist_ris_${season}_rel_cldclass.pdf" "data/cloud_top_thickness_hist_ris_${season}_cldclass.h5" data/cloud_top_thickness_hist_ris_cldclass.h5
    done

### plot_cloud_top_thickness_hist_multi.py

Plot cloud top-thickness histogram (multiple panels).

    python scripts/plot_cloud_top_thickness_hist.py -o plots/cloud_top_thickness_hist.png -c config/cloud_top_thickness_hist_cldclass.json

### cloud_types_hist_int.py

Cloud types histogram (integrated)

    spark-submit scripts/cloud_types_hist_int.py -o data/cloud_types_hist_int_rs_cldclass.h5 data/ross_sea_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_types_hist_int.py -o "data/cloud_types_hist_int_rs_${regime}_cldclass.h5" -r "$regime" data/ross_sea_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_types_hist_int.py -o "data/cloud_types_hist_int_rs_${season}_cldclass.h5" -s "$season" data/ross_sea_cldclass.h5 2>/dev/null
    done

    spark-submit scripts/cloud_types_hist_int.py -o data/cloud_types_hist_int_ris_cldclass.h5 data/ross_ice_shelf_cldclass.h5 2>/dev/null

    for regime in wnc snc ras wsc ws; do
        spark-submit scripts/cloud_types_hist_int.py -o "data/cloud_types_hist_int_ris_${regime}_cldclass.h5" -r "$regime" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

    for season in djf mam jja son; do
        spark-submit scripts/cloud_types_hist_int.py -o "data/cloud_types_hist_int_ris_${season}_cldclass.h5" -s "$season" data/ross_ice_shelf_cldclass.h5 2>/dev/null
    done

### plot_cloud_types_hist_int.py

Plot cloud types histogram (integrated).

    python scripts/plot_cloud_types_hist_int.py -o plots/cloud_types_hist_int.png -c config/cloud_types_hist_int.json

### plot_cloud_top_thickness_composite.py

Plot cloud top vs. cloud thickness composite plot.

    python scripts/plot_cloud_top_thickness_composite.py -o plots/cloud_top_thickness_composite_regime.pdf -c config/cloud_top_thickness_composite_regime.json

    python scripts/plot_cloud_top_thickness_composite.py -o plots/cloud_top_thickness_composite_season.pdf -c config/cloud_top_thickness_composite_season.json

### regime_season_hist.py

Regime-season histogram.

    spark-submit scripts/regime_season_hist.py -o data/regime_season_hist.h5 data/ross_sea_cldclass.h5 data/ross_ice_shelf_cldclass.h5 2>/dev/null

### print_regime_season_table.py

Print regime-season table.

    python scripts/print_regime_season_table.py data/regime_season_hist.h5
