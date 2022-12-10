import numpy as np
import matplotlib.pyplot as plt

def pct_error(true, pred, log=True):
    '''
    Take in two sequences (numpy arrays, pandas series etc.), return a sequence of relative errors.
    Note that (predicted value - true value) not the other way round
    '''
    if log:
        return 100 * (pred - true) / true
    else:
        return 100 * (np.exp(pred) - np.exp(true)) / np.exp(true)

def scatter(true, pred, log=True):

    plt.figure(figsize=(8,8))
    if not log:
        true = np.exp(true)
        pred = np.exp(pred)
    plt.scatter(true, pred)
    plt.xlabel('true')
    plt.ylabel('pred')
    plt.title('price')
    plt.plot(np.arange(true.min(), true.max()+1), np.arange(true.min(), true.max()+1), color='r')

def evaluate(y_train, pred_train, y_dev, pred_dev, y_test, pred_test, log=False):
    train_pct_error = pct_error(y_train, pred_train, log=log)
    dev_pct_error = pct_error(y_dev, pred_dev, log=log)
    test_pct_error = pct_error(y_test, pred_test, log=log)

    print('Training result:')
    print(f'abs mean: {train_pct_error.abs().mean()}, lower: {train_pct_error.quantile(0.025)}, upper: {train_pct_error.quantile(0.975)}')
    print()
    print('Development result:')
    print(f'abs mean: {dev_pct_error.abs().mean()}, lower: {dev_pct_error.quantile(0.025)}, upper: {dev_pct_error.quantile(0.975)}')
    print()
    print('Testing result:')
    print(f'abs mean: {test_pct_error.abs().mean()}, lower: {test_pct_error.quantile(0.025)}, upper: {test_pct_error.quantile(0.975)}')