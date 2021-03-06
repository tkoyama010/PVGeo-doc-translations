
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples/filters-general/array-math.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_filters-general_array-math.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_filters-general_array-math.py:


Array Math
~~~~~~~~~~

This example will demonstrate how to perform a mathematical operation
between two input arrays for any given source.

This filter allows the user to select two input data arrays on which to perform
math operations. The input arrays are used in their order of selection for the
operations.


This example demos: :class:`PVGeo.filters.ArrayMath`

.. GENERATED FROM PYTHON SOURCE LINES 16-21

.. code-block:: default

    import numpy as np
    import pyvista
    import PVGeo
    from PVGeo.filters import ArrayMath








.. GENERATED FROM PYTHON SOURCE LINES 22-23

Create some input data. This can be any `vtkDataObject`

.. GENERATED FROM PYTHON SOURCE LINES 23-31

.. code-block:: default

    inp = pyvista.UniformGrid((10, 10, 4))
    # Populate the tables
    n = 400
    arr0 = np.random.random(n)
    arr1 = np.random.random(n)
    inp['Array 0'] = arr0
    inp['Array 1'] = arr1








.. GENERATED FROM PYTHON SOURCE LINES 32-33

Use the filter:

.. GENERATED FROM PYTHON SOURCE LINES 33-38

.. code-block:: default

    f = ArrayMath(operation='add', new_name='foo')
    # Now get the result
    output = f.apply(inp, 'Array 0', 'Array 1')
    print(output)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    UniformGrid (0x7f91dc1dfec0)
      N Cells:      243
      N Points:     400
      X Bounds:     0.000e+00, 9.000e+00
      Y Bounds:     0.000e+00, 9.000e+00
      Z Bounds:     0.000e+00, 3.000e+00
      Dimensions:   10, 10, 4
      Spacing:      1.000e+00, 1.000e+00, 1.000e+00
      N Arrays:     3





.. GENERATED FROM PYTHON SOURCE LINES 39-40

Note that the output now has three arrays

.. GENERATED FROM PYTHON SOURCE LINES 40-42

.. code-block:: default

    arr = output['foo']
    assert np.allclose(arr, arr0 + arr1)







.. GENERATED FROM PYTHON SOURCE LINES 45-46

Use a custom math operation:

.. GENERATED FROM PYTHON SOURCE LINES 46-58

.. code-block:: default

    def power(arr0, arr1):
        return arr0 ** arr1


    # Use filter generated above
    f.set_operation(power)
    f.set_new_array_name('powered')
    f.update()

    # Now get the result
    output = f.get_output()
    print(output)




.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    UniformGrid (0x7f91dc1df4b0)
      N Cells:      243
      N Points:     400
      X Bounds:     0.000e+00, 9.000e+00
      Y Bounds:     0.000e+00, 9.000e+00
      Z Bounds:     0.000e+00, 3.000e+00
      Dimensions:   10, 10, 4
      Spacing:      1.000e+00, 1.000e+00, 1.000e+00
      N Arrays:     3





.. GENERATED FROM PYTHON SOURCE LINES 59-62

.. code-block:: default

    arr = output['powered']
    assert np.allclose(arr, arr0 ** arr1)








.. GENERATED FROM PYTHON SOURCE LINES 63-64

.. code-block:: default

    output.plot(scalars='powered')



.. image:: /examples/filters-general/images/sphx_glr_array-math_001.png
    :alt: array math
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(19.085160130469124, 19.085160130469124, 16.085160130469124),
     (4.5, 4.5, 1.5),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.543 seconds)


.. _sphx_glr_download_examples_filters-general_array-math.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: array-math.py <array-math.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: array-math.ipynb <array-math.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
