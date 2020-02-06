
from sklearn.linear_model.coordinate_descent import ElasticNetCV as SKLModel
import lale.helpers
import lale.operators
from numpy import nan, inf

class ElasticNetCVImpl():

    def __init__(self, l1_ratio=0.5, eps=0.001, n_alphas=100, alphas=None, fit_intercept=True, normalize=False, precompute='auto', max_iter=1000, tol=0.0001, cv=3, copy_X=True, verbose=0, n_jobs=None, positive=False, random_state=None, selection='cyclic'):
        self._hyperparams = {
            'l1_ratio': l1_ratio,
            'eps': eps,
            'n_alphas': n_alphas,
            'alphas': alphas,
            'fit_intercept': fit_intercept,
            'normalize': normalize,
            'precompute': precompute,
            'max_iter': max_iter,
            'tol': tol,
            'cv': cv,
            'copy_X': copy_X,
            'verbose': verbose,
            'n_jobs': n_jobs,
            'positive': positive,
            'random_state': random_state,
            'selection': selection}
        self._sklearn_model = SKLModel(**self._hyperparams)

    def fit(self, X, y=None):
        if (y is not None):
            self._sklearn_model.fit(X, y)
        else:
            self._sklearn_model.fit(X)
        return self

    def predict(self, X):
        return self._sklearn_model.predict(X)
_hyperparams_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'inherited docstring for ElasticNetCV    Elastic Net model with iterative fitting along a regularization path.',
    'allOf': [{
        'type': 'object',
        'required': ['l1_ratio', 'eps', 'n_alphas', 'alphas', 'fit_intercept', 'normalize', 'precompute', 'max_iter', 'tol', 'cv', 'copy_X', 'verbose', 'n_jobs', 'positive', 'random_state', 'selection'],
        'relevantToOptimizer': ['eps', 'n_alphas', 'fit_intercept', 'normalize', 'precompute', 'max_iter', 'tol', 'cv', 'copy_X', 'positive', 'selection'],
        'additionalProperties': False,
        'properties': {
            'l1_ratio': {
                'XXX TODO XXX': 'float or array of floats, optional',
                'description': 'float between 0 and 1 passed to ElasticNet (scaling between',
                'type': 'number',
                'default': 0.5},
            'eps': {
                'type': 'number',
                'minimumForOptimizer': 0.001,
                'maximumForOptimizer': 0.1,
                'distribution': 'uniform',
                'default': 0.001,
                'description': 'Length of the path. ``eps=1e-3`` means that'},
            'n_alphas': {
                'type': 'integer',
                'minimumForOptimizer': 100,
                'maximumForOptimizer': 101,
                'distribution': 'uniform',
                'default': 100,
                'description': 'Number of alphas along the regularization path, used for each l1_ratio.'},
            'alphas': {
                'anyOf': [{
                    'type': 'array',
                    'items': {
                        'XXX TODO XXX': 'item type'},
                    'XXX TODO XXX': 'numpy array, optional'}, {
                    'enum': [None]}],
                'default': None,
                'description': 'List of alphas where to compute the models.'},
            'fit_intercept': {
                'type': 'boolean',
                'default': True,
                'description': 'whether to calculate the intercept for this model. If set'},
            'normalize': {
                'type': 'boolean',
                'default': False,
                'description': 'This parameter is ignored when ``fit_intercept`` is set to False.'},
            'precompute': {
                'anyOf': [{
                    'type': 'array',
                    'items': {
                        'XXX TODO XXX': 'item type'},
                    'XXX TODO XXX': "True | False | 'auto' | array-like",
                    'forOptimizer': False}, {
                    'enum': ['auto']}],
                'default': 'auto',
                'description': 'Whether to use a precomputed Gram matrix to speed up'},
            'max_iter': {
                'type': 'integer',
                'minimumForOptimizer': 10,
                'maximumForOptimizer': 1000,
                'distribution': 'uniform',
                'default': 1000,
                'description': 'The maximum number of iterations'},
            'tol': {
                'type': 'number',
                'minimumForOptimizer': 1e-08,
                'maximumForOptimizer': 0.01,
                'distribution': 'loguniform',
                'default': 0.0001,
                'description': 'The tolerance for the optimization: if the updates are'},
            'cv': {
                'XXX TODO XXX': 'int, cross-validation generator or an iterable, optional',
                'description': 'Determines the cross-validation splitting strategy.',
                'type': 'integer',
                'minimumForOptimizer': 3,
                'maximumForOptimizer': 4,
                'distribution': 'uniform',
                'default': 3},
            'copy_X': {
                'type': 'boolean',
                'default': True,
                'description': 'If ``True``, X will be copied; else, it may be overwritten.'},
            'verbose': {
                'anyOf': [{
                    'type': 'boolean'}, {
                    'type': 'integer'}],
                'default': 0,
                'description': 'Amount of verbosity.'},
            'n_jobs': {
                'anyOf': [{
                    'type': 'integer'}, {
                    'enum': [None]}],
                'default': None,
                'description': 'Number of CPUs to use during the cross validation.'},
            'positive': {
                'type': 'boolean',
                'default': False,
                'description': 'When set to ``True``, forces the coefficients to be positive.'},
            'random_state': {
                'anyOf': [{
                    'type': 'integer'}, {
                    'type': 'object'}, {
                    'enum': [None]}],
                'default': None,
                'description': 'The seed of the pseudo random number generator that selects a random'},
            'selection': {
                'enum': ['random', 'cyclic'],
                'default': 'cyclic',
                'description': "If set to 'random', a random coefficient is updated every iteration"},
        }}],
}
_input_fit_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Fit linear model with coordinate descent',
    'type': 'object',
    'required': ['y', 'X'],
    'properties': {
        'X': {
            'XXX TODO XXX': '{array-like}, shape (n_samples, n_features)',
            'description': 'Training data. Pass directly as Fortran-contiguous data'},
        'y': {
            'anyOf': [{
                'type': 'array',
                'items': {
                    'type': 'number'},
            }, {
                'type': 'array',
                'items': {
                    'type': 'array',
                    'items': {
                        'type': 'number'},
                }}],
            'description': 'Target values'},
    },
}
_input_predict_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Predict using the linear model',
    'type': 'object',
    'required': ['X'],
    'properties': {
        'X': {
            'anyOf': [{
                'type': 'array',
                'items': {
                    'XXX TODO XXX': 'item type'},
                'XXX TODO XXX': 'array_like or sparse matrix, shape (n_samples, n_features)'}, {
                'type': 'array',
                'items': {
                    'type': 'array',
                    'items': {
                        'type': 'number'},
                }}],
            'description': 'Samples.'},
    },
}
_output_predict_schema = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Returns predicted values.',
    'type': 'array',
    'items': {
        'type': 'number'},
}
_combined_schemas = {
    '$schema': 'http://json-schema.org/draft-04/schema#',
    'description': 'Combined schema for expected data and hyperparameters.',
    'type': 'object',
    'tags': {
        'pre': [],
        'op': ['estimator'],
        'post': []},
    'properties': {
        'hyperparams': _hyperparams_schema,
        'input_fit': _input_fit_schema,
        'input_predict': _input_predict_schema,
        'output_predict': _output_predict_schema},
}
if (__name__ == '__main__'):
    lale.helpers.validate_is_schema(_combined_schemas)
ElasticNetCV = lale.operators.make_operator(ElasticNetCVImpl, _combined_schemas)

