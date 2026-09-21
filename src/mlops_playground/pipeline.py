import numpy as np
import pandas as pd
from sklearn.base import BaseEstimator, TransformerMixin
from sklearn.utils.validation import check_is_fitted


class FeatureSelector(TransformerMixin, BaseEstimator):
    def __init__(self, features):
        self.features = features

    def fit(self, X, y=None):
        self.features_ = list(self.features)
        return self

    def transform(self, X):
        check_is_fitted(self, "features_")
        return pd.DataFrame(X).reindex(columns=self.features_)

    def get_feature_names_out(self, input_features=None):
        check_is_fitted(self, "features_")
        return np.asarray(self.features_, dtype=object)
