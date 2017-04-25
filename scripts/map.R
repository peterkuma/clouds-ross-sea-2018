#!/usr/bin/env Rscript

library(raster)
library(sp)
library(rgdal)
library(rgeos)
library(maptools)
library(geosphere)
library(RColorBrewer)
library(graticule)

args <- commandArgs(TRUE)

if (length(args) != 2) {
    cat('Usage: map.R <output> <add>\n')
    quit('no', 1)
}

output.filename <- args[1]
add.path <- args[2]

font.family <- 'Lato'
proj <- '+proj=stere +lat_0=-90 +lat_ts=-71 +lon_0=180 +k=1 +x_0=0 +y_0=0'

surface.col <- colorRampPalette(c('#dddddd', '#ffffff'))(100)
bathymetry.col <- rev(colorRampPalette(c('#ffffff', '#1F83E0'))(100))

xlim=c(-900000, 1100000)
ylim=c(220000, 2400000)

coastlines.filename <- paste(add.path, '/Coastline_medium_res_polygon/Coastline_medium_res_polygon.shp', sep='')
coastlines.layer <- 'Coastline_medium_res_polygon'
contours.filename <- paste(add.path, '/Contours_low_res_line/Contours_low_res_line.shp', sep='')
contours.layer <- 'Contours_low_res_line'
surface.filename <- paste(add.path, '/Antarctic_surface_dem/surface_dem.tif', sep='')

coastlines <- readOGR(coastlines.filename, layer=coastlines.layer)
contours <- readOGR(contours.filename, layer=contours.layer)
surface <- raster(surface.filename)
ice.shelfs <- coastlines[coastlines@data$surface == 'ice shelf',]

crs.longlat <- CRS('+proj=longlat +ellps=WGS84')
crs <- CRS(proj)

cairo_pdf(output.filename, family=font.family)
par(mar=c(0.5, 0.5, 0.5, 0.5))

bounding.box <- function() {
    pts <- rbind(
        c(xlim[1], ylim[1]),
        c(xlim[2], ylim[1]),
        c(xlim[2], ylim[2]),
        c(xlim[1], ylim[2])
    )
    SpatialPolygons(list(Polygons(list(Polygon(list(pts))), 'bb')), proj4string=crs)
}

plot.map <- function() {
    plot(bb, xlim=xlim, ylim=ylim, ann=FALSE, xaxt='n', yaxt='n', axes=FALSE)
    plot(
        projectRaster(surface, res=10000, crs=crs),
        col=surface.col,
        add=TRUE,
        xlim=xlim,
        ylim=ylim,
        zlim=c(0, 4000),
        ann=FALSE,
        xaxt='n',
        yaxt='n',
        legend=FALSE,
        bty='n',
        axes=FALSE
    )
    plot(
        projectRaster(surface, res=10000, crs=crs),
        add=TRUE,
        col=bathymetry.col,
        xlim=xlim,
        ylim=ylim,
        zlim=c(-5000, 0),
        legend=FALSE
    )
    plot(
        gIntersection(spTransform(gUnaryUnion(ice.shelfs), CRSobj=crs), bb),
        add=TRUE,
        lwd=0.7,
        border='#000000a0',
        col='#ffffff'
    )
    plot(
        gIntersection(spTransform(gUnaryUnion(coastlines), crs), bb),
        add=TRUE,
        lwd=1,
        border='#00000080'
    )
    plot(
        gIntersection(spTransform(contours, crs), bb),
        add=TRUE,
        lwd=0.5,
        col='#00000080'
    )
}

plot.graticules <- function() {
    pts <- SpatialPoints(rbind(
        c(-180, -60),
        c(0, -60),
        c(180, -89),
        c(180, -60)
    ), crs.longlat)
    gl <- gridlines(pts, easts=seq(-180, 160, 20), ndiscr=100)
    lines(gIntersection(spTransform(gl, CRSobj=crs), bb), col='#00000080', lw=0.7)

    plot(
        gIntersection(
            spTransform(SpatialLines(list(Lines(list(Line(cbind(
                seq(0, 360, length.out=1000),
                rep(-78, 1000)
            ))), ID=1)), proj4string=crs.longlat), CRSobj=crs),
            bb
        ),
        add=TRUE,
        col='#00000080',
        lw=0.7,
        lty=2
    )

    plot(
        gIntersection(
            spTransform(SpatialLines(list(Lines(list(Line(cbind(
                seq(0, 360, length.out=1000),
                rep(-82, 1000)
            ))), ID=1)), proj4string=crs.longlat), CRSobj=crs),
            bb
        ),
        add=TRUE,
        col='#00000080',
        lw=0.7,
        lty=2
    )

    plot(
        gIntersection(
            spTransform(SpatialLines(list(Lines(list(Line(cbind(
                rep(210, 1000),
                seq(-90, 0, length.out=1000)
            ))), ID=1)), proj4string=crs.longlat), CRSobj=crs),
            bb
        ),
        add=TRUE,
        col='#00000080',
        lw=0.7,
        lty=2
    )

    # l <- labels(gl, crs.longlat, side=3)
    # l$pos <- NULL
    # text(l, adj=c(0.5, -0.5), cex=1.2, col='#000000')
    # l <- labels(gl, crs.longlat, side=4)
    # l$pos <- NULL
    # text(l, adj=c(-0.2, 2), cex=1.2, col='#000000')
}

plot.graticule.labels <- function() {
    grat.lat.pts <- rbind(
        c(180, -85),
        c(180, -82),
        c(180, -80),
        c(180, -78),
        c(180, -75),
        c(180, -70)
    )

    grat.lat.labels <- c(
        '85° S',
        '82° S',
        '80° S',
        '78° S',
        '75° S',
        '70° S'
    )

    grat.lon.pts <- rbind(
        c(-150, -72.5),
        c(-160, -72.5),
        c(180, -72.5),
        c(160, -72.5)
    )

    grat.lon.labels <- c(
        '150° W',
        '160° W',
        '180°',
        '160° E'
    )

    for(i in 1:nrow(grat.lon.pts)) {
        text(
            coordinates(spTransform(SpatialPoints(rbind(grat.lon.pts[i,]), crs.longlat), crs)),
            labels=grat.lon.labels[i],
            adj=c(1.05, 0.5),
            srt=(180 - grat.lon.pts[i, 1]),
            cex=1.2,
            font=2,
            col='#000000c0'
        )
    }

    text(
        coordinates(spTransform(SpatialPoints(grat.lat.pts, crs.longlat), crs)),
        labels=grat.lat.labels,
        adj=c(1.1, -0.5),
        cex=1.2,
        font=2,
        col='#000000c0'
    )
}

plot.areas <- function() {
    n <- 100
    area.1 <- cbind(
        c(rep(160, n), seq(160, 210, length.out=n), rep(210, n), seq(210, 160, length.out=n)),
        c(seq(-78, -75, length.out=n), rep(-75, n), seq(-75, -78, length.out=n), rep(-78, n))
    )

    area.2 <- cbind(
        c(rep(160, n), seq(160, 210, length.out=n), rep(210, n), seq(210, 160, length.out=n)),
        c(seq(-82, -78, length.out=n), rep(-78, n), seq(-78, -82, length.out=n), rep(-82, n))
    )

    area.1.sp <- SpatialPolygons(list(Polygons(list(Polygon(area.1)), ID=1)), proj4string=crs.longlat)
    area.2.sp <- SpatialPolygons(list(Polygons(list(Polygon(area.2)), ID=2)), proj4string=crs.longlat)

    plot(spTransform(area.1.sp, CRSobj=crs), add=TRUE, border='#0075F3', lwd=5)
    plot(spTransform(area.2.sp, CRSobj=crs), add=TRUE, border='#0075F3', lwd=5)

    plot(
        gIntersection(
            spTransform(SpatialLines(list(Lines(list(Line(cbind(
                rep(-175, 100),
                seq(-82, -75, length.out=100)
            ))), ID=1)), proj4string=crs.longlat), CRSobj=crs),
            bb
        ),
        add=TRUE,
        col='#0075F3',
        lw=2,
        lty=2
    )

    text(
        coordinates(spTransform(SpatialPoints(rbind(c(185, -76.5)), crs.longlat), crs)),
        labels='RS',
        adj=c(0.5, NA),
        col='#0075F3',
        font=2,
        cex=1.8
    )

    text(
        coordinates(spTransform(SpatialPoints(rbind(c(185, -80)), crs.longlat), crs)),
        labels='RIS',
        adj=c(0.5, NA),
        col='#0075F3',
        font=2,
        cex=1.8
    )
}

bb <- bounding.box()

plot.map()

# raster package conflicts with sp
detach(package:raster)

plot.graticules()
plot.graticule.labels()
plot.areas()

plot(bb, add=TRUE, lwd=2.5)
