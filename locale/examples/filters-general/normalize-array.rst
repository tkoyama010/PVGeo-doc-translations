
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples/filters-general/normalize-array.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_filters-general_normalize-array.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_filters-general_normalize-array.py:


Normalize Array
~~~~~~~~~~~~~~~

This example will demonstrate how to perform a normalization or any custom
mathematical operation on a single data array for an input data set.

This filter allow the user to select an array from the input data set to be
normalized. The filter will append another array to that data set for the
output. The user can specify how they want to rename the array, can choose a
multiplier, and can choose from two types of common normalizations:
Feature Scaling and Standard Score.

This example demos :class:`PVGeo.filters.NormalizeArray`

.. GENERATED FROM PYTHON SOURCE LINES 17-23

.. code-block:: default

    import numpy as np
    import pyvista
    from pyvista import examples
    import PVGeo
    from PVGeo.filters import NormalizeArray








.. GENERATED FROM PYTHON SOURCE LINES 24-25

Create some input data. this can be any `vtkDataObject`

.. GENERATED FROM PYTHON SOURCE LINES 25-28

.. code-block:: default

    mesh = examples.load_uniform()
    title = 'Spatial Point Data'
    mesh.plot(scalars=title)



.. image:: /examples/filters-general/images/sphx_glr_normalize-array_001.png
    :alt: normalize array
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(21.886664873203234, 21.886664873203234, 21.886664873203234),
     (4.5, 4.5, 4.5),
     (0.0, 0.0, 1.0)]



.. GENERATED FROM PYTHON SOURCE LINES 29-35

.. code-block:: default


    # Apply the filter
    f = NormalizeArray(normalization='feature_scale', new_name='foo')
    output = f.apply(mesh, title)
    print(output)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    UniformGrid (0x7f91dc1df6e0)
      N Cells:      729
      N Points:     1000
      X Bounds:     0.000e+00, 9.000e+00
      Y Bounds:     0.000e+00, 9.000e+00
      Z Bounds:     0.000e+00, 9.000e+00
      Dimensions:   10, 10, 10
      Spacing:      1.000e+00, 1.000e+00, 1.000e+00
      N Arrays:     3





.. GENERATED FROM PYTHON SOURCE LINES 36-37

.. code-block:: default

    output.plot(scalars='foo')



.. image:: /examples/filters-general/images/sphx_glr_normalize-array_002.png
    :alt: normalize array
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(21.886664873203234, 21.886664873203234, 21.886664873203234),
     (4.5, 4.5, 4.5),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.633 seconds)


.. _sphx_glr_download_examples_filters-general_normalize-array.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: normalize-array.py <normalize-array.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: normalize-array.ipynb <normalize-array.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
