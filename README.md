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
* If an outlier score is very low, that means the data point is an outlier data point.
* Alternatively, if an outlier score is very high, the data point is a "most probable" data point.

### Conclusions

I spent around 4-5 hours on this project.  Here are some brief conclusions of the study:

* You can see some HTML pages with sample visualizations of crime locations in results/
* In retrospect, attempting to do the project with on-line learning was difficult given so little available time.  Ready-to-use online methods are not as easy-to-use and available as off-line methods.  As such, mid-way through the project I switched to using an offline method.
* Top outlier and most-probable data points (see results/) all fit into a few crime types (for instance, Arson tends to be highly represented in the top outliers).  This seems to indicate that the normalization in the outlier score is not quite right and uncommon crimes could be leading the outlier table despite attempt at normalization.
* Before switching to off-line random forest, I tried online logistic regression.  As we would expect, with so few features it was highly biased.

### Things that can be improved

Obviously, this is a first stab at the problem.  Plenty of things can be improved:

* More features can be used
* Mapping of qualitative features to numeric values is slightly inappropriate (location type).  Though random forest should handle this better than some other classifiers.
* Visualization (map plotting) presently only plots close-by locations.  It would be good to narrow down on similar time.
* A more formalized approach to outlier detection could be used.