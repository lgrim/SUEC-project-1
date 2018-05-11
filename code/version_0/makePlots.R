# Logan Grim

# Get the command line arguments
# args will be a vector of strings
# Assume that the name of the file is the first argument and the name of the individual is the second argument. i.e "LoganGrim"
args <- commandArgs(trailingOnly = TRUE)

# Set the working directory
setwd("~/Documents/GitHub/SUEC-project-1/code/")

# Load ggplot2
library(ggplot2)

# Read in the data file
data <- read.csv(args[1], header = FALSE, sep = ",")

# Determine if we are working with a biking file or a running file
isRunningFile <- substring(args[1], 1, 1) == 'r'

# Create a histogram of the pace data and save it as "(running or biking)Pace_FirstNameLastName.png"
# The pace data in both types of files is in the second column
paceHist <- ggplot(data.frame(data$V2), aes(data$V2)) + geom_bar(width = 0.5) + labs(title = "Histogram of Pace Data", x = "Pace") + theme(plot.title = element_text(hjust = 0.5)) + ggsave(paste((if (isRunningFile) "running" else "biking"), "Pace_", args[2], ".png", sep = ""),width=6, height=4,dpi=300)



