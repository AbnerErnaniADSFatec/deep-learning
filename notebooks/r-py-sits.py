import rpy2.robjects
from rpy2.robjects.packages import importr

# R modules
r_utils = importr("utils")
r_sits = importr("sits")

r_array = rpy2.robjects.r["c"]
r_url = rpy2.robjects.r["url"]
r_readRDS = rpy2.robjects.r["readRDS"]
r_sistem_file = rpy2.robjects.r["system.file"]
r_plot = rpy2.robjects.r["plot"]

samples = r_sits.sits_select(rpy2.robjects.r["samples_modis_4bands"], bands = r_array("NDVI", "EVI"))
rfor_model = r_sits.sits_train(samples, r_sits.sits_rfor())

data_dir = r_sistem_file("extdata/raster/mod13q1", package = "sits")
sinop = r_sits.sits_cube(
    source = "LOCAL",
    name = "sinop-2014",
    satellite = "TERRA",
    sensor = "MODIS",
    data_dir = data_dir,
    delim = "_",
    parse_info = r_array("X1", "X2", "band", "date")
)

probs_cube = r_sits.sits_classify(sinop, 
                            ml_model = rfor_model)

# apply a bayesian smoothing to remove outliers
bayes_cube = r_sits.sits_smooth(probs_cube)
# generate a thematic map
label_cube = r_sits.sits_label_classification(bayes_cube)
# plot the the labelled cube
r_plot(label_cube, title = "Labelled image")