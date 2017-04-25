all: img README.html

.PHONY img: img/map.png img/cloud_incidence_by_phase_season.png img/cloud_incidence_by_phase_regime.png img/cloud_layers_hist_cldclass.png img/cloud_types_hist_int.png img/cloud_top_thickness_composite_season.png img/cloud_top_thickness_composite_regime.png

img/map.png: out/map.pdf
	convert -resize 512x512 $^ $@ out/map.pdf

img/cloud_incidence_by_phase_season.png: out/cloud_incidence_by_phase_season.png
	convert -resize 512x512 $^ $@

img/cloud_incidence_by_phase_regime.png: out/cloud_incidence_by_phase_regime.png
	convert -resize 512x512 $^ $@

img/cloud_layers_hist_cldclass.png: out/cloud_layers_hist_cldclass.png
	convert -resize 512x512 $^ $@

img/cloud_types_hist_int.png: out/cloud_types_hist_int.png
	convert -resize 512x512 $^ $@

img/cloud_top_thickness_composite_season.png: out/cloud_top_thickness_composite_season.png
	convert -resize 512x512 $^ $@

img/cloud_top_thickness_composite_regime.png: out/cloud_top_thickness_composite_regime.png
	convert -resize 512x512 $^ $@

README.html: README.md
	pandoc -o README.html README.md --css github.css
