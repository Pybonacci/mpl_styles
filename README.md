mpl-styles
==========

mpl-styles provide some decorators to decorate your matplotlib plots. Some styles are included, 
'gg', 'gg2', 'probpro', 'pybo', 'r'.

'gg', 'probpro' and 'r' are adapted from matplotlibrc demo files developed by [Ryan Dale](https://github.com/daler/matplotlibrc).

'gg2' is adapted from matplotlibrc developed by [Huy Nguyen](https://gist.github.com/huyng/816622).

'pybo' uses the [pybonacci logo colors](https://pybonacci.wordpress.com/2012/11/07/el-pybofractal-el-nuevo-logo-de-pybonacci/).

It is very easy to include your own style. Just define your rc params in a dictionary and include 
them in a new decorator. Then make a 'Pull Request' to this repo. It would be nice to see a gallery 
of beatiful styles here.

Otherwise, if you don't want to share your beatiful matplotlib configuration you can use your own 
styles using my_style decorator which accepts a dictionary with your rc params.

To use a style you just have to create your function with your plot and decorate the function with the 
decorator you want to use. See some dummy examples in the [following link](http://nbviewer.ipython.org/urls/raw.github.com/kikocorreoso/mpl_styles/master/mpl_styles-examples_of_use.ipynb)


