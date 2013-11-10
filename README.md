mpl_styles
==========

mpl_styles provide some decorators to decorate your matplotlib plots. Some styles are included, 
'gg', 'gg2', 'probpro', 'pybo', 'r'.

'gg', 'probpro' and 'r' are adapted from matplotlibrc demo files developed by Ryan Dale.

'gg2' is adapted from matplotlibrc developed by Huy Nguyen.

'pybo' uses the pybonacci logo colors.

It is very easy to include your own style. Just define your rc params in a dictionary and include 
them in a new decorator. Then make a 'Pull Request' to this repo. It would be nice to see a gallery 
of beatiful styles here.

Otherwise, if you don't want to share your beatiful matplotlib configuration you can use your own 
styles using my_style decorator which accepts a dictionary with your rc params.

To use a style you just have to create your function with your plot and decorate the function with the 
decorator you want to use. See some dummy examples in the following link:


