# chicago-crime-outliers

Look for outliers in Chicago's crime statistics.

### Motivation

This repository is my solution to a data science challenge project given by an interviewer.

### Idea

I will attempt to use the database of crimes in Chicago to perform on-line prediction on which crimes are outliers.  For the purposes of this study, a crime is considered an outlier if the type of the crime is significantly mispredicted by a trained, on-line predictor.

In particular, this is the outlier detection procedure.  Off-line the following are performed:

* Train a classifier to predict the class _C_ of a crime given 4 input variables (time of day, longitude, latitude, location description)
* Calculate a windowed running average of the prior proportion of crimes _pC_ for each class _C_.

Then, to predict, the procedure is performed for each incoming data point:

* Predict the probabilities _PC_ from the classifier.
* Define an _outlier score_ for each incident by calculating (_PC_ - _pC_) / _pC_ where _C_ is the true class for this incident.
