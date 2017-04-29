SHELL := bash

dataset_2b_geoprof_lidar := /data/datasets/cloudsat/2b-geoprof-lidar
dataset_2b_cldclass_lidar := /cloudsat/2b-cldclass-lidar.p_r04
dataset_add := /data/datasets/add

cloud_top_hist_plots := \
	plots/cloud_top_hist_rs.pdf \
	plots/cloud_top_hist_ris.pdf \
	plots/cloud_top_hist_rs_cpr.pdf \
	plots/cloud_top_hist_rs_caliop.pdf \
	plots/cloud_top_hist_ris_cpr.pdf \
	plots/cloud_top_hist_ris_caliop.pdf \
	plots/cloud_top_hist_rs_cldclass.pdf \
	plots/cloud_top_hist_ris_cldclass.pdf \
	plots/cloud_top_hist_rs_wnc.pdf \
	plots/cloud_top_hist_rs_snc.pdf \
	plots/cloud_top_hist_rs_ras.pdf \
	plots/cloud_top_hist_rs_wsc.pdf \
	plots/cloud_top_hist_rs_ws.pdf \
	plots/cloud_top_hist_ris_wnc.pdf \
	plots/cloud_top_hist_ris_snc.pdf \
	plots/cloud_top_hist_ris_ras.pdf \
	plots/cloud_top_hist_ris_wsc.pdf \
	plots/cloud_top_hist_ris_ws.pdf \
	plots/cloud_top_hist_rs_wnc_cldclass.pdf \
	plots/cloud_top_hist_rs_snc_cldclass.pdf \
	plots/cloud_top_hist_rs_ras_cldclass.pdf \
	plots/cloud_top_hist_rs_wsc_cldclass.pdf \
	plots/cloud_top_hist_rs_ws_cldclass.pdf \
	plots/cloud_top_hist_ris_wnc_cldclass.pdf \
	plots/cloud_top_hist_ris_snc_cldclass.pdf \
	plots/cloud_top_hist_ris_ras_cldclass.pdf \
	plots/cloud_top_hist_ris_wsc_cldclass.pdf \
	plots/cloud_top_hist_ris_ws_cldclass.pdf

cloud_top_base_scatter_plots := \
	plots/cloud_top_base_scatter_rs.pdf \
	plots/cloud_top_base_scatter_ris.pdf \
	plots/cloud_top_base_scatter_rs_cldclass.pdf \
	plots/cloud_top_base_scatter_ris_cldclass.pdf

cloud_incidence_files := \
	data/cloud_incidence_rs.h5 \
	data/cloud_incidence_rs_night.h5 \
	data/cloud_incidence_rs_day.h5 \
	data/cloud_incidence_ris.h5 \
	data/cloud_incidence_ris_night.h5 \
	data/cloud_incidence_ris_day.h5 \
	data/cloud_incidence_rs_cldclass.h5 \
	data/cloud_incidence_rs-e_cldclass.h5 \
	data/cloud_incidence_rs-w_cldclass.h5 \
	data/cloud_incidence_ris_cldclass.h5 \
	data/cloud_incidence_ris-e_cldclass.h5 \
	data/cloud_incidence_ris-w_cldclass.h5 \
	data/cloud_incidence_rs_wnc_cldclass.h5 \
	data/cloud_incidence_rs_snc_cldclass.h5 \
	data/cloud_incidence_rs_ras_cldclass.h5 \
	data/cloud_incidence_rs_wsc_cldclass.h5 \
	data/cloud_incidence_rs_ws_cldclass.h5 \
	data/cloud_incidence_ris_wnc_cldclass.h5 \
	data/cloud_incidence_ris_snc_cldclass.h5 \
	data/cloud_incidence_ris_ras_cldclass.h5 \
	data/cloud_incidence_ris_wsc_cldclass.h5 \
	data/cloud_incidence_ris_ws_cldclass.h5 \
	data/cloud_incidence_rs_djf_cldclass.h5 \
	data/cloud_incidence_rs_mam_cldclass.h5 \
	data/cloud_incidence_rs_jja_cldclass.h5 \
	data/cloud_incidence_rs_son_cldclass.h5 \
	data/cloud_incidence_ris_djf_cldclass.h5 \
	data/cloud_incidence_ris_mam_cldclass.h5 \
	data/cloud_incidence_ris_jja_cldclass.h5 \
	data/cloud_incidence_ris_son_cldclass.h5

cloud_incidence_plots = \
	plots/cloud_incidence_rs.pdf \
	plots/cloud_incidence_rs_night.pdf \
	plots/cloud_incidence_rs_day.pdf \
	plots/cloud_incidence_ris.pdf \
	plots/cloud_incidence_ris_night.pdf \
	plots/cloud_incidence_ris_day.pdf \
	plots/cloud_incidence_rs_cldclass.pdf \
	plots/cloud_incidence_ris_cldclass.pdf \
	plots/cloud_incidence_rs_wnc_cldclass.pdf \
	plots/cloud_incidence_rs_snc_cldclass.pdf \
	plots/cloud_incidence_rs_ras_cldclass.pdf \
	plots/cloud_incidence_rs_wsc_cldclass.pdf \
	plots/cloud_incidence_rs_ws_cldclass.pdf \
	plots/cloud_incidence_ris_wnc_cldclass.pdf \
	plots/cloud_incidence_ris_snc_cldclass.pdf \
	plots/cloud_incidence_ris_ras_cldclass.pdf \
	plots/cloud_incidence_ris_wsc_cldclass.pdf \
	plots/cloud_incidence_ris_ws_cldclass.pdf

cloud_incidence_by_type_plots = \
	plots/cloud_incidence_by_type_rs_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_wnc_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_snc_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_ras_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_wsc_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_ws_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_wnc_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_snc_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_ras_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_wsc_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_ws_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_djf_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_mam_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_jja_cldclass.pdf \
	plots/cloud_incidence_by_type_rs_son_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_djf_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_mam_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_jja_cldclass.pdf \
	plots/cloud_incidence_by_type_ris_son_cldclass.pdf

cloud_incidence_by_phase_plots := \
	plots/cloud_incidence_by_phase_rs_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_wnc_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_snc_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_ras_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_wsc_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_ws_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_wnc_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_snc_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_ras_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_wsc_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_ws_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_djf_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_mam_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_jja_cldclass.pdf \
	plots/cloud_incidence_by_phase_rs_son_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_djf_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_mam_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_jja_cldclass.pdf \
	plots/cloud_incidence_by_phase_ris_son_cldclass.pdf

correction_factor_plots := \
	plots/correction_factor.pdf \
	plots/correction_factor_djf.pdf \
	plots/correction_factor_jja.pdf \
	plots/correction_factor_multi.pdf

cloud_incidence_summary_by_phase_plots := \
	plots/cloud_incidence_summary_by_phase_rs_seasons.pdf \
	plots/cloud_incidence_summary_by_phase_ris_seasons.pdf \
	plots/cloud_incidence_summary_by_phase_rs_regimes.pdf \
	plots/cloud_incidence_summary_by_phase_ris_regimes.pdf

cloud_incidence_summary_by_type_plots := \
	plots/cloud_incidence_summary_by_type_rs_seasons.pdf \
	plots/cloud_incidence_summary_by_type_ris_seasons.pdf \
	plots/cloud_incidence_summary_by_type_rs_regimes.pdf \
	plots/cloud_incidence_summary_by_type_ris_regimes.pdf

cloud_incidence_information_gain_plots := \
	plots/cloud_incidence_information_gain_rs_type.pdf \
	plots/cloud_incidence_information_gain_rs_phase.pdf \
	plots/cloud_incidence_information_gain_ris_type.pdf \
	plots/cloud_incidence_information_gain_ris_phase.pdf

cloud_incidence_by_phase_regime_plots := \
	plots/cloud_incidence_by_phase_regime.pdf \
	plots/cloud_incidence_by_phase_season.pdf

cloud_types_histogram_files := \
	data/cloud_types_hist_rs_cldclass.h5 \
	data/cloud_types_hist_rs_regime_wnc_cldclass.h5 \
	data/cloud_types_hist_rs_regime_snc_cldclass.h5 \
	data/cloud_types_hist_rs_regime_ras_cldclass.h5 \
	data/cloud_types_hist_rs_regime_wsc_cldclass.h5 \
	data/cloud_types_hist_rs_regime_ws_cldclass.h5 \
	data/cloud_types_hist_rs_season_djf_cldclass.h5 \
	data/cloud_types_hist_rs_season_mam_cldclass.h5 \
	data/cloud_types_hist_rs_season_jja_cldclass.h5 \
	data/cloud_types_hist_rs_season_son_cldclass.h5 \
	data/cloud_types_hist_ris_cldclass.h5 \
	data/cloud_types_hist_ris_regime_wnc_cldclass.h5 \
	data/cloud_types_hist_ris_regime_snc_cldclass.h5 \
	data/cloud_types_hist_ris_regime_ras_cldclass.h5 \
	data/cloud_types_hist_ris_regime_wsc_cldclass.h5 \
	data/cloud_types_hist_ris_regime_ws_cldclass.h5 \
	data/cloud_types_hist_ris_season_djf_cldclass.h5 \
	data/cloud_types_hist_ris_season_mam_cldclass.h5 \
	data/cloud_types_hist_ris_season_jja_cldclass.h5 \
	data/cloud_types_hist_ris_season_son_cldclass.h5

cloud_types_hist_plots := \
	plots/cloud_types_hist_rs_cldclass.pdf \
	plots/cloud_types_hist_ris_cldclass.pdf

cloud_top_thickness_hist_files := \
	data/cloud_top_thickness_hist_rs_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_regime_wnc_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_regime_snc_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_regime_ras_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_regime_wsc_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_regime_ws_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_season_djf_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_season_mam_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_season_jja_cldclass.h5 \
	data/cloud_top_thickness_hist_rs_season_son_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_regime_wnc_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_regime_snc_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_regime_ras_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_regime_wsc_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_regime_ws_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_season_djf_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_season_mam_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_season_jja_cldclass.h5 \
	data/cloud_top_thickness_hist_ris_season_son_cldclass.h5

cloud_top_thickness_plots := \
	plots/cloud_top_thickness_hist_rs_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_wnc_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_snc_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_ras_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_wsc_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_ws_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_djf_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_mam_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_jja_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_son_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_wnc_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_snc_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_ras_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_wsc_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_ws_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_djf_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_mam_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_jja_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_son_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_wnc_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_snc_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_ras_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_wsc_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_regime_ws_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_djf_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_mam_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_jja_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_rs_season_son_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_wnc_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_snc_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_ras_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_wsc_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_regime_ws_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_djf_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_mam_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_jja_rel_cldclass.pdf \
	plots/cloud_top_thickness_hist_ris_season_son_rel_cldclass.pdf

cloud_types_hist_int_files := \
	data/cloud_types_hist_int_rs_cldclass.h5 \
	data/cloud_types_hist_int_rs_regime_wnc_cldclass.h5 \
	data/cloud_types_hist_int_rs_regime_snc_cldclass.h5 \
	data/cloud_types_hist_int_rs_regime_ras_cldclass.h5 \
	data/cloud_types_hist_int_rs_regime_wsc_cldclass.h5 \
	data/cloud_types_hist_int_rs_regime_ws_cldclass.h5 \
	data/cloud_types_hist_int_rs_season_djf_cldclass.h5 \
	data/cloud_types_hist_int_rs_season_mam_cldclass.h5 \
	data/cloud_types_hist_int_rs_season_jja_cldclass.h5 \
	data/cloud_types_hist_int_rs_season_son_cldclass.h5 \
	data/cloud_types_hist_int_ris_cldclass.h5 \
	data/cloud_types_hist_int_ris_regime_wnc_cldclass.h5 \
	data/cloud_types_hist_int_ris_regime_snc_cldclass.h5 \
	data/cloud_types_hist_int_ris_regime_ras_cldclass.h5 \
	data/cloud_types_hist_int_ris_regime_wsc_cldclass.h5 \
	data/cloud_types_hist_int_ris_regime_ws_cldclass.h5 \
	data/cloud_types_hist_int_ris_season_djf_cldclass.h5 \
	data/cloud_types_hist_int_ris_season_mam_cldclass.h5 \
	data/cloud_types_hist_int_ris_season_jja_cldclass.h5 \
	data/cloud_types_hist_int_ris_season_son_cldclass.h5

cloud_top_thickness_composite_plots := \
	plots/cloud_top_thickness_composite_regime.pdf \
	plots/cloud_top_thickness_composite_season.pdf

plots := \
	$(cloud_top_hist_plots) \
	$(cloud_top_base_scatter_plots) \
	plots/cloud_top_base_scatter_multi.pdf \
	$(cloud_incidence_plots) \
	$(cloud_incidence_by_type_plots) \
	$(cloud_incidence_by_phase_plots) \
	plots/regimes.pdf \
	$(correction_factor_plots) \
	$(cloud_incidence_summary_by_phase_plots) \
	$(cloud_incidence_summary_by_type_plots) \
	$(cloud_incidence_information_gain_plots) \
	$(cloud_incidence_by_phase_regime_plots) \
	plots/cloud_incidence_multi.pdf \
	plots/cloud_layers_hist_cldclass.pdf \
	$(cloud_types_hist_plots) \
	$(cloud_top_thickness_plots) \
	plots/cloud_top_thickness_hist.pdf \
	plots/cloud_types_hist_int.pdf \
	plots/cloud_types_hist_int_with_cs.pdf \
	$(cloud_top_thickness_composite_plots) \
	plots/map.pdf

all: plots png img README.html

README.html: README.md
	pandoc -o README.html README.md --css github.css

# Plots

.PHONY: plots
plots: $(plots)

# PNG

.PHONY: png
png: $(plots:plots/%.pdf=plots/png/%.png)

plots/png/%.png: plots/%.pdf
	convert -density 300 $^ $@

# Map

.PHONY: map
map: plots/map.pdf

plots/map.pdf:
	scripts/map.R $@ "$(dataset_add)"

# List of files

data/ross_area_files:
	spark-submit scripts/ross_area_files.py '$(dataset_2b_geoprof_lidar)/*/*/*.zip' 2>/dev/null > data/ross_area_files

data/ross_area_cldclass_files:
	spark-submit scripts/ross_area_files.py '$(dataset_2b_cldclass_lidar)/*/*/*.zip' 2>/dev/null > data/ross_area_cldclass_files

# Extract area

data/ross_sea.h5: data/ross_area_files
	spark-submit scripts/extract_area.py -o $@ -a ross_sea -f $^ 2>/dev/null

data/ross_ice_shelf.h5: data/ross_area_files
	spark-submit scripts/extract_area.py -o $@ -a ross_ice_shelf -f $^ 2>/dev/null

data/ross_sea_cldclass.h5: data/ross_area_cldclass_files
	spark-submit scripts/extract_area.py -o $@ -p 2b-cldclass-lidar -a ross_sea -f $^ 2>/dev/null

data/ross_ice_shelf_cldclass.h5: data/ross_area_cldclass_files
	spark-submit scripts/extract_area.py -o $@ -p 2b-cldclass-lidar -a ross_ice_shelf -f $^ 2>/dev/null

# Cloud top histogram

.PHONY: cloud_top_hist
cloud_top_hist: $(cloud_top_hist_plots)

plots/cloud_top_hist_rs.pdf: data/ross_sea.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR)" -o $@ $^ 2>/dev/null

plots/cloud_top_hist_ris.pdf: data/ross_ice_shelf.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR)" -o $@ $^ 2>/dev/null

plots/cloud_top_hist_rs_cpr.pdf: data/ross_sea.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, CPR)" -i 1 -o $@ $^ 2>/dev/null

plots/cloud_top_hist_rs_caliop.pdf: data/ross_sea.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, CALIOP)" -i 2 -o $@ $^ 2>/dev/null

plots/cloud_top_hist_ris_cpr.pdf: data/ross_ice_shelf.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, CPR)" -i 1 -o $@ $^ 2>/dev/null

plots/cloud_top_hist_ris_caliop.pdf: data/ross_ice_shelf.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, CALIOP)" -i 2 -o $@ $^ 2>/dev/null

plots/cloud_top_hist_rs_cldclass.pdf: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^ 2>/dev/null

plots/cloud_top_hist_ris_cldclass.pdf: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^ 2>/dev/null

plots/cloud_top_hist_rs_%.pdf: data/ross_sea.h5
	regime=$*; \
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, $${regime^^}, 2006-2011, 2B-GEOPROF-LIDAR)" -o $@ -r $* $^ 2>/dev/null

plots/cloud_top_hist_ris_%.pdf: data/ross_ice_shelf.h5
	regime=$*; \
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, $${regime^^}, 2006-2011, 2B-GEOPROF-LIDAR)" -o $@ -r $* $^ 2>/dev/null

plots/cloud_top_hist_rs_%_cldclass.pdf: data/ross_sea_cldclass.h5
	regime=$*; \
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Sea, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ -r $* $^ 2>/dev/null

plots/cloud_top_hist_ris_%_cldclass.pdf: data/ross_ice_shelf_cldclass.h5
	regime=$*; \
	spark-submit scripts/cloud_top_hist.py -t "Cloud top (Ross Ice Shelf, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ -r $* $^ 2>/dev/null

# Profile sample

.PHONY: profile_sample
profile_sample: \
	plots/profile_sample_rs.pdf \
	plots/profile_sample_ris.pdf

plots/profile_sample_rs.pdf: data/ross_sea.h5
	spark-submit scripts/profile_sample.py -o $@ $^ 2>/dev/null

plots/profile_sample_ris.pdf: data/ross_ice_shelf.h5
	spark-submit scripts/profile_sample.py -o $@ $^ 2>/dev/null

# Cloud top-base scatter plot

.PHONY: cloud_top_base_scatter
cloud_top_base_scatter: $(cloud_top_base_scatter_plots)

plots/cloud_top_base_scatter_rs.pdf: data/ross_sea.h5
	spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Sea, 2B-GEOPROF-LIDAR)' -o $@ $^ 2>/dev/null

plots/cloud_top_base_scatter_ris.pdf: data/ross_ice_shelf.h5
	spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Ice Shelf, 2B-GEOPROF-LIDAR)' -o $@ $^ 2>/dev/null

plots/cloud_top_base_scatter_rs_cldclass.pdf: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Sea, 2B-CLDCLASS-LIDAR)' -o $@ $^ 2>/dev/null

plots/cloud_top_base_scatter_ris_cldclass.pdf: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_top_base_scatter.py -t 'Cloud top/base scatter plot (Ross Ice Shelf, 2B-CLDCLASS-LIDAR)' -o $@ $^ 2>/dev/null

# Cloud top-base scatter plot (multi)

plots/cloud_top_base_scatter_multi.pdf: \
		scripts/cloud_top_base_scatter_multi.py \
		data/ross_sea_cldclass.h5 \
		data/ross_ice_shelf.h5 \
		data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_top_base_scatter_multi.py -c config/cloud_top_base_scatter_multi.json -o $@ 2>/dev/null

# Cloud incidence

.PHONY: cloud_incidence
cloud_incidence: $(cloud_incidence_files)

data/cloud_incidence_rs.h5: data/ross_sea.h5
	spark-submit scripts/cloud_incidence.py $^ -o $@ 2>/dev/null

data/cloud_incidence_rs_night.h5: data/ross_sea.h5
	spark-submit scripts/cloud_incidence.py -n 0 $^ -o $@ 2>/dev/null

data/cloud_incidence_rs_day.h5: data/ross_sea.h5
	spark-submit scripts/cloud_incidence.py -n 1 $^ -o $@ 2>/dev/null

data/cloud_incidence_ris.h5: data/ross_ice_shelf.h5
	spark-submit scripts/cloud_incidence.py $^ -o $@ 2>/dev/null

data/cloud_incidence_ris_night.h5: data/ross_ice_shelf.h5
	spark-submit scripts/cloud_incidence.py -n 0 $^ -o $@ 2>/dev/null

data/cloud_incidence_ris_day.h5: data/ross_ice_shelf.h5
	spark-submit scripts/cloud_incidence.py -n 1 $^ -o $@ 2>/dev/null

data/cloud_incidence_rs_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar $^ -o $@ 2>/dev/null

data/cloud_incidence_rs-e_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar $^ -a ross_sea_east -o $@ 2>/dev/null

data/cloud_incidence_rs-w_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar $^ -a ross_sea_west -o $@ 2>/dev/null

data/cloud_incidence_ris_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar $^ -o $@ 2>/dev/null

data/cloud_incidence_ris-e_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar $^ -a ross_ice_shelf_east -o $@ 2>/dev/null

data/cloud_incidence_ris-w_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar $^ -a ross_ice_shelf_west -o $@ 2>/dev/null

data/cloud_incidence_rs_regime_%_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r $* $^ -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r $* $^ -a ross_sea_east -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r $* $^ -a ross_sea_west -o $@ 2>/dev/null

data/cloud_incidence_ris_regime_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r $* $^ -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r $* $^ -a ross_ice_shelf_east -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -r $* $^ -a ross_ice_shelf_west -o $@ 2>/dev/null

data/cloud_incidence_rs_season_%_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s $* $^ -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s $* $^ -a ross_sea_east -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s $* $^ -a ross_sea_west -o $@ 2>/dev/null

data/cloud_incidence_ris_season_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s $* $^ -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s $* $^ -a ross_ice_shelf_east -o $@ 2>/dev/null; \
	spark-submit scripts/cloud_incidence.py -p 2b-cldclass-lidar -s $* $^ -a ross_ice_shelf_west -o $@ 2>/dev/null

# Plot cloud incidence

.PHONY: plot_cloud_incidence
plot_cloud_incidence: $(cloud_incidence_plots)

plots/cloud_incidence_rs.pdf: data/cloud_incidence_rs.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR)" -o $@ $^

plots/cloud_incidence_rs_night.pdf: data/cloud_incidence_rs_night.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, night)" -o $@ $^

plots/cloud_incidence_rs_day.pdf: data/cloud_incidence_rs_day.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2006-2011, 2B-GEOPROF-LIDAR, day)" -o $@ $^

plots/cloud_incidence_ris.pdf: data/cloud_incidence_ris.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR)" -o $@ $^

plots/cloud_incidence_ris_night.pdf: data/cloud_incidence_ris_night.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, night)" -o $@ $^

plots/cloud_incidence_ris_day.pdf: data/cloud_incidence_ris_day.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2006-2011, 2B-GEOPROF-LIDAR, day)" -o $@ $^

plots/cloud_incidence_rs_cldclass.pdf: data/cloud_incidence_rs_cldclass.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_incidence_ris_cldclass.pdf: data/cloud_incidence_ris_cldclass.h5
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_incidence_rs_%_cldclass.pdf: data/cloud_incidence_rs_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Sea, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_incidence_ris_%_cldclass.pdf: data/cloud_incidence_ris_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_incidence.py -t "Cloud incidence (Ross Ice Shelf, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

# Plot cloud incidence by type

.PHONY: plot_cloud_incidence_by_type
plot_cloud_incidence_by_type: $(cloud_incidence_by_type_plots)

plots/cloud_incidence_by_type_rs_cldclass.pdf: data/cloud_incidence_rs_cldclass.h5
	python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_incidence_by_type_ris_cldclass.pdf: data/cloud_incidence_ris_cldclass.h5
	python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_incidence_by_type_rs_%_cldclass.pdf: data/cloud_incidence_rs_%_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Sea, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_incidence_by_type_ris_%_cldclass.pdf: data/cloud_incidence_ris_%_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_incidence_by_type.py -t "Cloud incidence by type (Ross Ice Shelf, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

# Plot cloud incidence by phase

.PHONY: plot_cloud_incidence_by_phase
plot_cloud_incidence_by_phase: $(cloud_incidence_by_phase_plots)

plots/cloud_incidence_by_phase_rs_cldclass.pdf: data/cloud_incidence_rs_cldclass.h5 scripts/plot_cloud_incidence_by_phase.py
	python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $<

plots/cloud_incidence_by_phase_ris_cldclass.pdf: data/cloud_incidence_ris_cldclass.h5 scripts/plot_cloud_incidence_by_phase.py
	python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $<

plots/cloud_incidence_by_phase_rs_%_cldclass.pdf: data/cloud_incidence_rs_%_cldclass.h5 scripts/plot_cloud_incidence_by_phase.py
	regime=$*; \
	python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Sea, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $<

plots/cloud_incidence_by_phase_ris_%_cldclass.pdf: data/cloud_incidence_ris_%_cldclass.h5 scripts/plot_cloud_incidence_by_phase.py
	regime=$*; \
	python scripts/plot_cloud_incidence_by_phase.py -t "Cloud incidence by phase (Ross Ice Shelf, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $<

# Cloud incidence map 8000 vs. 8300

data/cloud_incidence_map_8000_8300.h5:
	spark-submit scripts/cloud_incidence_map_8000_8300.py -o data/cloud_incidence_map_8000_8300.h5 '/data/datasets/cloudsat/2b-geoprof-lidar/*/*/*.zip' 2>/dev/null

# Plot correction factor

.PHONY: plot_correction_factor
plot_correction_factor: $(correction_factor_plots)

plots/correction_factor.pdf: data/cloud_incidence_map_8000_8300.h5
	python scripts/plot_correction_factor.py $^ -t 'Cloud incidence correction factor 8000 m vs. 8300 m' -o $@

plots/correction_factor_djf.pdf: data/cloud_incidence_map_8000_8300_djf.h5
	python scripts/plot_correction_factor.py $^ -t 'Cloud incidence correction factor 8000 m vs. 8300 m (DJF)' -o $@

plots/correction_factor_jja.pdf: data/cloud_incidence_map_8000_8300_jja.h5
	python scripts/plot_correction_factor.py $^ -t 'Cloud incidence correction factor 8000 m vs. 8300 m (JJA)' -o $@

plots/correction_factor_multi.pdf: \
		scripts/plot_correction_factor_multi.py \
		data/cloud_incidence_map_8000_8300.h5 \
		data/cloud_incidence_map_8000_8300_djf.h5 \
		data/cloud_incidence_map_8000_8300_jja.h5
	python scripts/plot_correction_factor_multi.py -o $@ -c config/correction_factor_multi.json

# Plot regimes

plots/regimes.pdf:
	python scripts/plot_regimes.py -t 'Regimes distribution by month (2007-2010)' -o $@

# Plot cloud incidence summary by phase

.PHONY: plot_cloud_incidence_summary_by_phase
.plot_cloud_incidence_summary_by_phase: $(cloud_incidence_summary_by_phase_plots)

plots/cloud_incidence_summary_by_phase_rs_seasons.pdf: \
		data/cloud_incidence_rs_djf_cldclass.h5 \
		data/cloud_incidence_rs_mam_cldclass.h5 \
		data/cloud_incidence_rs_jja_cldclass.h5 \
		data/cloud_incidence_rs_son_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o $@ $^

plots/cloud_incidence_summary_by_phase_ris_seasons.pdf: \
		data/cloud_incidence_ris_djf_cldclass.h5 \
		data/cloud_incidence_ris_mam_cldclass.h5 \
		data/cloud_incidence_ris_jja_cldclass.h5 \
		data/cloud_incidence_ris_son_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o $@ $^

plots/cloud_incidence_summary_by_phase_rs_regimes.pdf: \
	 	data/cloud_incidence_rs_wnc_cldclass.h5 \
	 	data/cloud_incidence_rs_snc_cldclass.h5 \
	 	data/cloud_incidence_rs_ras_cldclass.h5 \
	 	data/cloud_incidence_rs_wsc_cldclass.h5 \
	 	data/cloud_incidence_rs_ws_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o $@ $^

plots/cloud_incidence_summary_by_phase_ris_regimes.pdf: \
		data/cloud_incidence_ris_wnc_cldclass.h5 \
		data/cloud_incidence_ris_snc_cldclass.h5 \
		data/cloud_incidence_ris_ras_cldclass.h5 \
		data/cloud_incidence_ris_wsc_cldclass.h5 \
		data/cloud_incidence_ris_ws_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_phase.py -t 'Clouds incidence by phase (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o $@ $^

# Plot cloud incidence summary by type

.PHONY: plot_cloud_incidence_summary_by_type
plot_cloud_incidence_summary_by_type: $(cloud_incidence_summary_by_type_plots)

plots/cloud_incidence_summary_by_type_rs_seasons.pdf: \
		data/cloud_incidence_rs_djf_cldclass.h5 \
		data/cloud_incidence_rs_mam_cldclass.h5 \
		data/cloud_incidence_rs_jja_cldclass.h5 \
		data/cloud_incidence_rs_son_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o $@ $^

plots/cloud_incidence_summary_by_type_ris_seasons.pdf: \
		data/cloud_incidence_ris_djf_cldclass.h5 \
		data/cloud_incidence_ris_mam_cldclass.h5 \
		data/cloud_incidence_ris_jja_cldclass.h5 \
		data/cloud_incidence_ris_son_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l DJF,MAM,JJA,SON -o $@ $^

plots/cloud_incidence_summary_by_type_rs_regimes.pdf: \
		data/cloud_incidence_rs_wnc_cldclass.h5 \
		data/cloud_incidence_rs_snc_cldclass.h5 \
		data/cloud_incidence_rs_ras_cldclass.h5 \
		data/cloud_incidence_rs_wsc_cldclass.h5 \
		data/cloud_incidence_rs_ws_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o $@ $^

plots/cloud_incidence_summary_by_type_ris_regimes.pdf: \
		data/cloud_incidence_ris_wnc_cldclass.h5 \
		data/cloud_incidence_ris_snc_cldclass.h5 \
		data/cloud_incidence_ris_ras_cldclass.h5 \
		data/cloud_incidence_ris_wsc_cldclass.h5 \
		data/cloud_incidence_ris_ws_cldclass.h5
	python scripts/plot_cloud_incidence_summary_by_type.py -t 'Clouds incidence by type (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)' -l WNC,SNC,RAS,WSC,WS -o $@ $^

# Plot information gain

.PHONY: plot_cloud_incidence_information_gain
plot_cloud_incidence_information_gain: $(cloud_incidence_information_gain_plots)

plots/cloud_incidence_information_gain_rs_%.pdf: \
		config/classes_rs.json \
		data/cloud_incidence_rs_wnc_cldclass.h5 \
		data/cloud_incidence_rs_snc_cldclass.h5 \
		data/cloud_incidence_rs_ras_cldclass.h5 \
		data/cloud_incidence_rs_wsc_cldclass.h5 \
		data/cloud_incidence_rs_ws_cldclass.h5 \
		data/cloud_incidence_rs_djf_cldclass.h5 \
		data/cloud_incidence_rs_mam_cldclass.h5 \
		data/cloud_incidence_rs_jja_cldclass.h5 \
		data/cloud_incidence_rs_son_cldclass.h5
	python scripts/plot_cloud_incidence_information_gain.py -t "Information gain (Ross Sea, 2007-2010, 2B-CLDCLASS)" -x $* -o $@ -c config/classes_rs.json

plots/cloud_incidence_information_gain_ris_%.pdf: \
		config/classes_ris.json \
		data/cloud_incidence_ris_wnc_cldclass.h5 \
            	data/cloud_incidence_ris_snc_cldclass.h5 \
            	data/cloud_incidence_ris_ras_cldclass.h5 \
            	data/cloud_incidence_ris_wsc_cldclass.h5 \
            	data/cloud_incidence_ris_ws_cldclass.h5 \
            	data/cloud_incidence_ris_djf_cldclass.h5 \
            	data/cloud_incidence_ris_mam_cldclass.h5 \
            	data/cloud_incidence_ris_jja_cldclass.h5 \
            	data/cloud_incidence_ris_son_cldclass.h5
	python scripts/plot_cloud_incidence_information_gain.py -t "Information gain (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS)"  -x $* -o $@ -c config/classes_ris.json

# Plot cloud incidence by phase (multiple panels)

.PHONY: plot_cloud_incidence_by_phase_regime
plot_cloud_incidence_by_phase_regime: $(cloud_incidence_by_phase_regime_plots)

plots/cloud_incidence_by_phase_regime.pdf: \
		scripts/plot_cloud_incidence_by_phase_multiple.py \
		config/cloud_incidence_by_phase_regime.json \
		data/cloud_incidence_rs_wnc_cldclass.h5 \
		data/cloud_incidence_rs_snc_cldclass.h5 \
		data/cloud_incidence_rs_ras_cldclass.h5 \
		data/cloud_incidence_rs_wsc_cldclass.h5 \
		data/cloud_incidence_rs_ws_cldclass.h5 \
		data/cloud_incidence_ris_wnc_cldclass.h5 \
		data/cloud_incidence_ris_snc_cldclass.h5 \
		data/cloud_incidence_ris_ras_cldclass.h5 \
		data/cloud_incidence_ris_wsc_cldclass.h5 \
		data/cloud_incidence_ris_ws_cldclass.h5 \
		data/cloud_incidence_rs-e_wnc_cldclass.h5 \
		data/cloud_incidence_rs-w_wnc_cldclass.h5 \
		data/cloud_incidence_rs-e_snc_cldclass.h5 \
		data/cloud_incidence_rs-w_snc_cldclass.h5 \
		data/cloud_incidence_rs-e_ras_cldclass.h5 \
		data/cloud_incidence_rs-w_ras_cldclass.h5 \
		data/cloud_incidence_rs-e_wsc_cldclass.h5 \
		data/cloud_incidence_rs-w_wsc_cldclass.h5 \
		data/cloud_incidence_rs-e_ws_cldclass.h5 \
		data/cloud_incidence_rs-w_ws_cldclass.h5 \
		data/cloud_incidence_ris-e_wnc_cldclass.h5 \
		data/cloud_incidence_ris-w_wnc_cldclass.h5 \
		data/cloud_incidence_ris-e_snc_cldclass.h5 \
		data/cloud_incidence_ris-w_snc_cldclass.h5 \
		data/cloud_incidence_ris-e_ras_cldclass.h5 \
		data/cloud_incidence_ris-w_ras_cldclass.h5 \
		data/cloud_incidence_ris-e_wsc_cldclass.h5 \
		data/cloud_incidence_ris-w_wsc_cldclass.h5 \
		data/cloud_incidence_ris-e_ws_cldclass.h5 \
		data/cloud_incidence_ris-w_ws_cldclass.h5
	python scripts/plot_cloud_incidence_by_phase_multiple.py -o $@ -c config/cloud_incidence_by_phase_regime.json

plots/cloud_incidence_by_phase_season.pdf: \
		scripts/plot_cloud_incidence_by_phase_multiple.py \
		config/cloud_incidence_by_phase_season.json \
            	data/cloud_incidence_rs_djf_cldclass.h5 \
            	data/cloud_incidence_rs_mam_cldclass.h5 \
            	data/cloud_incidence_rs_jja_cldclass.h5 \
            	data/cloud_incidence_rs_son_cldclass.h5 \
            	data/cloud_incidence_ris_djf_cldclass.h5 \
            	data/cloud_incidence_ris_mam_cldclass.h5 \
            	data/cloud_incidence_ris_jja_cldclass.h5 \
            	data/cloud_incidence_ris_son_cldclass.h5 \
            	data/cloud_incidence_rs-e_djf_cldclass.h5 \
            	data/cloud_incidence_rs-w_djf_cldclass.h5 \
            	data/cloud_incidence_rs-e_mam_cldclass.h5 \
            	data/cloud_incidence_rs-w_mam_cldclass.h5 \
            	data/cloud_incidence_rs-e_jja_cldclass.h5 \
            	data/cloud_incidence_rs-w_jja_cldclass.h5 \
            	data/cloud_incidence_rs-e_son_cldclass.h5 \
            	data/cloud_incidence_rs-w_son_cldclass.h5 \
            	data/cloud_incidence_ris-e_djf_cldclass.h5 \
            	data/cloud_incidence_ris-w_djf_cldclass.h5 \
            	data/cloud_incidence_ris-e_mam_cldclass.h5 \
            	data/cloud_incidence_ris-w_mam_cldclass.h5 \
            	data/cloud_incidence_ris-e_jja_cldclass.h5 \
            	data/cloud_incidence_ris-w_jja_cldclass.h5 \
            	data/cloud_incidence_ris-e_son_cldclass.h5 \
            	data/cloud_incidence_ris-w_son_cldclass.h5
	python scripts/plot_cloud_incidence_by_phase_multiple.py -o $@ -c config/cloud_incidence_by_phase_season.json

# Cloud layers histogram

data/cloud_layers_hist_rs_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_layers_hist.py -o $@ $^ 2>/dev/null

data/cloud_layers_hist_ris_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_layers_hist.py -o $@ $^ 2>/dev/null

data/cloud_layers_hist_rs_%_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_layers_hist.py -o $@ -r $* $^ 2>/dev/null

data/cloud_layers_hist_ris_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_layers_hist.py -o $@ -r $* $^ 2>/dev/null

# Plot cloud incidence (multi)

plots/cloud_incidence_multi.pdf: \
		scripts/plot_cloud_incidence_multi.py \
		config/cloud_incidence_multi.json \
		data/cloud_incidence_rs.h5 \
		data/cloud_incidence_ris.h5 \
		data/cloud_incidence_rs_cldclass.h5 \
		data/cloud_incidence_ris.h5
	python scripts/plot_cloud_incidence_multi.py -o $@ -c config/cloud_incidence_multi.json

# Plot cloud layers histogram

plots/cloud_layers_hist_cldclass.pdf: \
		config/cloud_layers_hist_cldclass.json \
		data/cloud_layers_hist_rs_cldclass.h5 \
		data/cloud_layers_hist_rs_wnc_cldclass.h5 \
		data/cloud_layers_hist_rs_snc_cldclass.h5 \
		data/cloud_layers_hist_rs_ras_cldclass.h5 \
		data/cloud_layers_hist_rs_wsc_cldclass.h5 \
		data/cloud_layers_hist_rs_ws_cldclass.h5 \
		data/cloud_layers_hist_rs_djf_cldclass.h5 \
		data/cloud_layers_hist_rs_mam_cldclass.h5 \
		data/cloud_layers_hist_rs_jja_cldclass.h5 \
		data/cloud_layers_hist_rs_son_cldclass.h5 \
		data/cloud_layers_hist_ris_cldclass.h5 \
		data/cloud_layers_hist_ris_wnc_cldclass.h5 \
		data/cloud_layers_hist_ris_snc_cldclass.h5 \
		data/cloud_layers_hist_ris_ras_cldclass.h5 \
		data/cloud_layers_hist_ris_wsc_cldclass.h5 \
		data/cloud_layers_hist_ris_ws_cldclass.h5 \
		data/cloud_layers_hist_ris_djf_cldclass.h5 \
		data/cloud_layers_hist_ris_mam_cldclass.h5 \
		data/cloud_layers_hist_ris_jja_cldclass.h5 \
		data/cloud_layers_hist_ris_son_cldclass.h5
	python scripts/plot_cloud_layers_hist.py -o $@ -c config/cloud_layers_hist_cldclass.json

# Counts

data/counts.csv: \
		data/ross_sea_cldclass.h5 \
		data/ross_ice_shelf_cldclass.h5
	bash -c ' \
		echo "RS,all,$(spark-submit scripts/count.py data/ross_sea_cldclass.h5 2>/dev/null)"; \
		echo "RIS,all,$(spark-submit scripts/count.py data/ross_ice_shelf_cldclass.h5 2>/dev/null)"; \
		for regime in wnc snc ras wsc ws; do \
			echo "RS,$${regime^^},$(spark-submit scripts/count.py -r "$regime" data/ross_sea_cldclass.h5 2>/dev/null)"; \
			echo "RS-E,$${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_sea_east data/ross_sea_cldclass.h5 2>/dev/null)"; \
			echo "RS-W,$${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_sea_west data/ross_sea_cldclass.h5 2>/dev/null)"; \
			echo "RIS,$${regime^^},$(spark-submit scripts/count.py -r "$regime" data/ross_ice_shelf_cldclass.h5 2>/dev/null)"; \
			echo "RIS-E,$${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_ice_shelf_east data/ross_ice_shelf_cldclass.h5 2>/dev/null)"; \
			echo "RIS-W,$${regime^^},$(spark-submit scripts/count.py -r "$regime" -a ross_ice_shelf_west data/ross_ice_shelf_cldclass.h5 2>/dev/null)"; \
		done; \
		for season in djf mam jja son; do; \
			echo "RS,$${season^^},$(spark-submit scripts/count.py -s "$season" data/ross_sea_cldclass.h5 2>/dev/null)"; \
			echo "RS-E,$${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_sea_east data/ross_sea_cldclass.h5 2>/dev/null)"; \
			echo "RS-W,$${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_sea_west data/ross_sea_cldclass.h5 2>/dev/null)"; \
			echo "RIS,$${season^^},$(spark-submit scripts/count.py -s "$season" data/ross_ice_shelf_cldclass.h5 2>/dev/null)"; \
			echo "RIS-E,$${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_ice_shelf_east data/ross_ice_shelf_cldclass.h5 2>/dev/null)"; \
			echo "RIS-W,$${season^^},$(spark-submit scripts/count.py -s "$season" -a ross_ice_shelf_west data/ross_ice_shelf_cldclass.h5 2>/dev/null)"; \
		done; \
	' > plots/counts.csv

# Cloud types histgoram

.PHONY: cloud_types_histogram
cloud_types_histogram: $(cloud_types_histogram_files)

data/cloud_types_hist_rs_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_types_hist.py -o $@ $^ 2>/dev/null

data/cloud_types_hist_rs_regime_%_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_types_hist.py -o $@ -r $* $^ 2>/dev/null

data/cloud_types_hist_rs_season_%_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_types_hist.py -o $@ -s $* $^ 2>/dev/null

data/cloud_types_hist_ris_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_types_hist.py -o $@ $^

data/cloud_types_hist_ris_regime_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_types_hist.py -o $@ -r $* $^ 2>/dev/null

data/cloud_types_hist_ris_season_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_types_hist.py -o $@ -s $* $^ 2>/dev/null

# Plot cloud types histogram

.PHONY: plot_cloud_types_hist
plot_cloud_types_hist: $(cloud_types_hist_plots)

plots/cloud_types_hist_rs_cldclass.pdf: \
		config/cloud_types_hist_rs_cldclass.json \
		data/cloud_types_hist_rs_cldclass.h5 \
		data/cloud_types_hist_rs_wnc_cldclass.h5 \
		data/cloud_types_hist_rs_snc_cldclass.h5 \
		data/cloud_types_hist_rs_ras_cldclass.h5 \
		data/cloud_types_hist_rs_wsc_cldclass.h5 \
		data/cloud_types_hist_rs_ws_cldclass.h5 \
		data/cloud_types_hist_rs_djf_cldclass.h5 \
		data/cloud_types_hist_rs_mam_cldclass.h5 \
		data/cloud_types_hist_rs_jja_cldclass.h5 \
		data/cloud_types_hist_rs_son_cldclass.h5
	python scripts/plot_cloud_types_hist.py -o $@ -c config/cloud_types_hist_rs_cldclass.json

plots/cloud_types_hist_ris_cldclass.pdf: \
		config/cloud_types_hist_ris_cldclass.json \
		data/cloud_types_hist_ris_cldclass.h5 \
		data/cloud_types_hist_ris_wnc_cldclass.h5 \
		data/cloud_types_hist_ris_snc_cldclass.h5 \
		data/cloud_types_hist_ris_ras_cldclass.h5 \
		data/cloud_types_hist_ris_wsc_cldclass.h5 \
		data/cloud_types_hist_ris_ws_cldclass.h5 \
		data/cloud_types_hist_ris_djf_cldclass.h5 \
		data/cloud_types_hist_ris_mam_cldclass.h5 \
		data/cloud_types_hist_ris_jja_cldclass.h5 \
		data/cloud_types_hist_ris_son_cldclass.h5
	python scripts/plot_cloud_types_hist.py -o $@ -c config/cloud_types_hist_ris_cldclass.json

# Cloud top-thickness histogram

.PHONY: cloud_top_thickness_hist
cloud_top_thickness_hist: $(cloud_top_thickness_hist_files)

data/cloud_top_thickness_hist_rs_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_top_thickness_hist.py -o $@ $^ 2>/dev/null

data/cloud_top_thickness_hist_ris_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_top_thickness_hist.py -o $@ $^ 2>/dev/null

data/cloud_top_thickness_hist_rs_regime_%_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_top_thickness_hist.py -o $@ -r $* $^ 2>/dev/null

data/cloud_top_thickness_hist_rs_season_%_cldclass.h5: data/ross_sea_cldclass.h5
	spark-submit scripts/cloud_top_thickness_hist.py -o $@ -s $* $^ 2>/dev/null

data/cloud_top_thickness_hist_ris_regime_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_top_thickness_hist.py -o $@ -r $* $^ 2>/dev/null

data/cloud_top_thickness_hist_ris_season_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/cloud_top_thickness_hist.py -o $@ -s $* $^ 2>/dev/null

# Plot cloud top-thickness histogram

.PHONY: plot_cloud_top_thickness_hist
plot_cloud_top_thickness_hist: $(cloud_top_thickness_plots)

plots/cloud_top_thickness_hist_rs_cldclass.pdf: data/cloud_top_thickness_hist_rs_cldclass.h5
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_top_thickness_hist_ris_cldclass.pdf: data/cloud_top_thickness_hist_ris_cldclass.h5
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_top_thickness_hist_rs_regime_%_cldclass.pdf: data/cloud_top_thickness_hist_rs_regime_%_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_top_thickness_hist_rs_season_%_cldclass.pdf: data/cloud_top_thickness_hist_rs_season_%_cldclass.h5
	season=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, $${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_top_thickness_hist_ris_regime_%_cldclass.pdf: data/cloud_top_thickness_hist_ris_regime_%_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_top_thickness_hist_ris_season_%_cldclass.pdf: data/cloud_top_thickness_hist_ris_season_%_cldclass.h5
	season=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, $${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $^

plots/cloud_top_thickness_hist_rs_regime_%_rel_cldclass.pdf: data/cloud_top_thickness_hist_rs_regime_%_cldclass.h5 data/cloud_top_thickness_hist_rs_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $< data/cloud_top_thickness_hist_rs_cldclass.h5

plots/cloud_top_thickness_hist_rs_season_%_rel_cldclass.pdf: data/cloud_top_thickness_hist_rs_season_%_cldclass.h5 data/cloud_top_thickness_hist_rs_cldclass.h5
	season=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Sea, $${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $< data/cloud_top_thickness_hist_rs_cldclass.h5

plots/cloud_top_thickness_hist_ris_regime_%_rel_cldclass.pdf: data/cloud_top_thickness_hist_ris_regime_%_cldclass.h5 data/cloud_top_thickness_hist_ris_cldclass.h5
	regime=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, $${regime^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $< data/cloud_top_thickness_hist_ris_cldclass.h5

plots/cloud_top_thickness_hist_ris_season_%_rel_cldclass.pdf: data/cloud_top_thickness_hist_ris_season_%_cldclass.h5 data/cloud_top_thickness_hist_ris_cldclass.h5
	season=$*; \
	python scripts/plot_cloud_top_thickness_hist.py -t "Cloud top-thickness histogram (Ross Ice Shelf, $${season^^}, 2007-2010, 2B-CLDCLASS-LIDAR)" -o $@ $< data/cloud_top_thickness_hist_ris_cldclass.h5

# Plot cloud top-thickness histogram (multiple panels)

plots/cloud_top_thickness_hist.pdf: \
		config/cloud_top_thickness_hist_cldclass.json \
		data/cloud_top_thickness_hist_rs_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_wnc_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_snc_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_ras_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_wsc_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_ws_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_djf_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_mam_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_jja_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_son_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_wnc_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_snc_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_ras_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_wsc_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_ws_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_djf_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_mam_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_jja_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_son_cldclass.h5
	python scripts/plot_cloud_top_thickness_hist_multi.py -o $@ -c config/cloud_top_thickness_hist_cldclass.json

# Cloud types histogram (integrated)

.PHONY: cloud_types_hist_int
cloud_types_hist_int: $(cloud_types_hist_int_files)

data/cloud_types_hist_int_rs_cldclass.h5: data/ross_sea_cldclass.h5 scripts/cloud_types_hist_int.py
	spark-submit scripts/cloud_types_hist_int.py -o $@ $< 2>/dev/null

data/cloud_types_hist_int_rs_regime_%_cldclass.h5: data/ross_sea_cldclass.h5 scripts/cloud_types_hist_int.py
	spark-submit scripts/cloud_types_hist_int.py -o $@ -r $* $< 2>/dev/null

data/cloud_types_hist_int_rs_season_%_cldclass.h5: data/ross_sea_cldclass.h5 scripts/cloud_types_hist_int.py
	spark-submit scripts/cloud_types_hist_int.py -o $@ -s $* $< 2>/dev/null

data/cloud_types_hist_int_ris_cldclass.h5: data/ross_ice_shelf_cldclass.h5 scripts/cloud_types_hist_int.py
	spark-submit scripts/cloud_types_hist_int.py -o $@ $< 2>/dev/null

data/cloud_types_hist_int_ris_regime_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5 scripts/cloud_types_hist_int.py
	spark-submit scripts/cloud_types_hist_int.py -o $@ -r $* $< 2>/dev/null

data/cloud_types_hist_int_ris_season_%_cldclass.h5: data/ross_ice_shelf_cldclass.h5 scripts/cloud_types_hist_int.py
	spark-submit scripts/cloud_types_hist_int.py -o $@ -s $* $< 2>/dev/null

# Plot cloud types histogram (integrated)

plots/cloud_types_hist_int.pdf: \
		scripts/plot_cloud_types_hist_int.py \
		config/cloud_types_hist_int.json \
		data/cloud_types_hist_int_rs_cldclass.h5 \
		data/cloud_types_hist_int_rs_wnc_cldclass.h5 \
		data/cloud_types_hist_int_rs_snc_cldclass.h5 \
		data/cloud_types_hist_int_rs_ras_cldclass.h5 \
		data/cloud_types_hist_int_rs_wsc_cldclass.h5 \
		data/cloud_types_hist_int_rs_ws_cldclass.h5 \
		data/cloud_types_hist_int_rs_djf_cldclass.h5 \
		data/cloud_types_hist_int_rs_mam_cldclass.h5 \
		data/cloud_types_hist_int_rs_jja_cldclass.h5 \
		data/cloud_types_hist_int_rs_son_cldclass.h5 \
		data/cloud_types_hist_int_ris_cldclass.h5 \
		data/cloud_types_hist_int_ris_wnc_cldclass.h5 \
		data/cloud_types_hist_int_ris_snc_cldclass.h5 \
		data/cloud_types_hist_int_ris_ras_cldclass.h5 \
		data/cloud_types_hist_int_ris_wsc_cldclass.h5 \
		data/cloud_types_hist_int_ris_ws_cldclass.h5 \
		data/cloud_types_hist_int_ris_djf_cldclass.h5 \
		data/cloud_types_hist_int_ris_mam_cldclass.h5 \
		data/cloud_types_hist_int_ris_jja_cldclass.h5 \
		data/cloud_types_hist_int_ris_son_cldclass.h5
	python scripts/plot_cloud_types_hist_int.py -o $@ -c config/cloud_types_hist_int.json

plots/cloud_types_hist_int_with_cs.pdf: \
		scripts/plot_cloud_types_hist_int.py \
		config/cloud_types_hist_int.json \
		data/cloud_types_hist_int_rs_cldclass.h5 \
		data/cloud_types_hist_int_rs_wnc_cldclass.h5 \
		data/cloud_types_hist_int_rs_snc_cldclass.h5 \
		data/cloud_types_hist_int_rs_ras_cldclass.h5 \
		data/cloud_types_hist_int_rs_wsc_cldclass.h5 \
		data/cloud_types_hist_int_rs_ws_cldclass.h5 \
		data/cloud_types_hist_int_rs_djf_cldclass.h5 \
		data/cloud_types_hist_int_rs_mam_cldclass.h5 \
		data/cloud_types_hist_int_rs_jja_cldclass.h5 \
		data/cloud_types_hist_int_rs_son_cldclass.h5 \
		data/cloud_types_hist_int_ris_cldclass.h5 \
		data/cloud_types_hist_int_ris_wnc_cldclass.h5 \
		data/cloud_types_hist_int_ris_snc_cldclass.h5 \
		data/cloud_types_hist_int_ris_ras_cldclass.h5 \
		data/cloud_types_hist_int_ris_wsc_cldclass.h5 \
		data/cloud_types_hist_int_ris_ws_cldclass.h5 \
		data/cloud_types_hist_int_ris_djf_cldclass.h5 \
		data/cloud_types_hist_int_ris_mam_cldclass.h5 \
		data/cloud_types_hist_int_ris_jja_cldclass.h5 \
		data/cloud_types_hist_int_ris_son_cldclass.h5
	python scripts/plot_cloud_types_hist_int.py -o $@ -c config/cloud_types_hist_int.json --with-cs


# Plot cloud top vs. cloud thickness composite plot

.PHONY: plot_cloud_top_thickness_composite
plot_cloud_top_thickness_composite: $(cloud_top_thickness_composite_plots)

plots/cloud_top_thickness_composite_regime.pdf: \
		config/cloud_top_thickness_composite_regime.json \
		data/cloud_top_thickness_hist_rs_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_wnc_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_snc_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_ras_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_wsc_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_ws_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_wnc_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_snc_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_ras_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_wsc_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_ws_cldclass.h5
	python scripts/plot_cloud_top_thickness_composite.py -o $@ -c config/cloud_top_thickness_composite_regime.json

plots/cloud_top_thickness_composite_season.pdf: \
		config/cloud_top_thickness_composite_season.json \
		data/cloud_top_thickness_hist_rs_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_djf_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_mam_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_jja_cldclass.h5 \
		data/cloud_top_thickness_hist_rs_son_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_djf_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_mam_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_jja_cldclass.h5 \
		data/cloud_top_thickness_hist_ris_son_cldclass.h5
	python scripts/plot_cloud_top_thickness_composite.py -o $@ -c config/cloud_top_thickness_composite_season.json

# Regime-season histogram

data/regime_season_hist.h5: data/ross_sea_cldclass.h5 data/ross_ice_shelf_cldclass.h5
	spark-submit scripts/regime_season_hist.py -o $@ $^ 2>/dev/null

# Regime-season table.

data/regime_season_table: data/regime_season_hist.h5
	python scripts/print_regime_season_table.py $^ > $@

# img

.PHONY: img
img: \
	img/map.png \
	img/cloud_incidence_by_phase_season.png \
	img/cloud_incidence_by_phase_regime.png \
	img/cloud_layers_hist_cldclass.png \
	img/cloud_types_hist_int.png \
	img/cloud_top_thickness_composite_season.png \
	img/cloud_top_thickness_composite_regime.png

img/map.png: plots/map.pdf
	convert -resize 512x512 $^ $@

img/cloud_incidence_by_phase_season.png: plots/cloud_incidence_by_phase_season.pdf
	convert -resize 512x512 $^ $@

img/cloud_incidence_by_phase_regime.png: plots/cloud_incidence_by_phase_regime.pdf
	convert -resize 512x512 $^ $@

img/cloud_layers_hist_cldclass.png: plots/cloud_layers_hist_cldclass.pdf
	convert -resize 512x512 $^ $@

img/cloud_types_hist_int.png: plots/cloud_types_hist_int.pdf
	convert -resize 512x512 $^ $@

img/cloud_top_thickness_composite_season.png: plots/cloud_top_thickness_composite_season.pdf
	convert -resize 512x512 $^ $@

img/cloud_top_thickness_composite_regime.png: plots/cloud_top_thickness_composite_regime.pdf
	convert -resize 512x512 $^ $@
