
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples/filters-general/append-cell-centers.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_filters-general_append-cell-centers.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_filters-general_append-cell-centers.py:


Append Cell Centers
~~~~~~~~~~~~~~~~~~~

This example will demonstrate how to append a dataset's cell centers as a length 3 tuple array.

This example demonstrates :class:`PVGeo.filters.AppendCellCenters`

.. GENERATED FROM PYTHON SOURCE LINES 9-13

.. code-block:: default


    from pyvista import examples
    from PVGeo.filters import AppendCellCenters








.. GENERATED FROM PYTHON SOURCE LINES 14-15

Use an example mesh from pyvista

.. GENERATED FROM PYTHON SOURCE LINES 15-18

.. code-block:: default

    mesh = examples.load_rectilinear()
    print(mesh)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    RectilinearGrid (0x7f91dc1df280)
      N Cells:      16146
      N Points:     18144
      X Bounds:     -3.500e+02, 1.350e+03
      Y Bounds:     -4.000e+02, 1.350e+03
      Z Bounds:     -8.500e+02, 0.000e+00
      Dimensions:   27, 28, 24
      N Arrays:     1





.. GENERATED FROM PYTHON SOURCE LINES 19-20

Run the PVGeo algorithm

.. GENERATED FROM PYTHON SOURCE LINES 20-23

.. code-block:: default

    centers = AppendCellCenters().apply(mesh)
    print(centers)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    RectilinearGrid (0x7f91dc1df3d0)
      N Cells:      16146
      N Points:     18144
      X Bounds:     -3.500e+02, 1.350e+03
      Y Bounds:     -4.000e+02, 1.350e+03
      Z Bounds:     -8.500e+02, 0.000e+00
      Dimensions:   27, 28, 24
      N Arrays:     2





.. GENERATED FROM PYTHON SOURCE LINES 24-25

.. code-block:: default

    centers.plot()



.. image:: /examples/filters-general/images/sphx_glr_append-cell-centers_001.png
    :alt: append cell centers
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(3381.633746130961, 3356.633746130961, 2456.633746130961),
     (500.0, 475.0, -425.0),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  0.961 seconds)


.. _sphx_glr_download_examples_filters-general_append-cell-centers.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: append-cell-centers.py <append-cell-centers.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: append-cell-centers.ipynb <append-cell-centers.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
