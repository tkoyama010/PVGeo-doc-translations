
.. DO NOT EDIT.
.. THIS FILE WAS AUTOMATICALLY GENERATED BY SPHINX-GALLERY.
.. TO MAKE CHANGES, EDIT THE SOURCE PYTHON FILE:
.. "examples/ubc/read-tensor-mesh.py"
.. LINE NUMBERS ARE GIVEN BELOW.

.. only:: html

    .. note::
        :class: sphx-glr-download-link-note

        Click :ref:`here <sphx_glr_download_examples_ubc_read-tensor-mesh.py>`
        to download the full example code

.. rst-class:: sphx-glr-example-title

.. _sphx_glr_examples_ubc_read-tensor-mesh.py:


Read Tensor Mesh
~~~~~~~~~~~~~~~~

Read a UBC tensor mesh file

.. GENERATED FROM PYTHON SOURCE LINES 7-12

.. code-block:: default

    # sphinx_gallery_thumbnail_number = 1
    import PVGeo
    import pyvista
    from pyvista import examples








.. GENERATED FROM PYTHON SOURCE LINES 13-14

Download sample data files and keep track of names:

.. GENERATED FROM PYTHON SOURCE LINES 14-19

.. code-block:: default

    url = 'https://github.com/OpenGeoVis/PVGeo/raw/master/tests/data/Craig-Chile/craig_chile.msh'
    mesh_file, _ = examples.downloads._retrieve_file(url, 'craig_chile.msh')
    url = 'https://github.com/OpenGeoVis/PVGeo/raw/master/tests/data/Craig-Chile/Lpout.mod'
    model_file, _ = examples.downloads._retrieve_file(url, 'Lpout.mod')








.. GENERATED FROM PYTHON SOURCE LINES 20-21

Read the mesh and model

.. GENERATED FROM PYTHON SOURCE LINES 21-27

.. code-block:: default

    reader = PVGeo.ubc.TensorMeshReader()
    reader.set_mesh_filename(mesh_file)
    reader.add_model_file_name(model_file)
    mesh = reader.apply()
    print(mesh)





.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none

    RectilinearGrid (0x7f91c00ce910)
      N Cells:      190440
      N Points:     200900
      X Bounds:     3.550e+05, 3.722e+05
      Y Bounds:     5.999e+06, 6.016e+06
      Z Bounds:     -5.250e+03, 3.000e+03
      Dimensions:   70, 70, 41
      N Arrays:     1





.. GENERATED FROM PYTHON SOURCE LINES 28-29

Use a `PyVista` ``threshold`` filter to remove ``NaN`` data values

.. GENERATED FROM PYTHON SOURCE LINES 29-32

.. code-block:: default

    mesh.threshold().plot()





.. image:: /examples/ubc/images/sphx_glr_read-tensor-mesh_001.png
    :alt: read tensor mesh
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(392348.1001399256, 6036348.100139925, 27598.10013992562),
     (363625.0, 6007625.0, -1125.0),
     (0.0, 0.0, 1.0)]



.. GENERATED FROM PYTHON SOURCE LINES 33-34

Or inspect slices of the model

.. GENERATED FROM PYTHON SOURCE LINES 34-37

.. code-block:: default

    mesh.slice_orthogonal().plot()





.. image:: /examples/ubc/images/sphx_glr_read-tensor-mesh_002.png
    :alt: read tensor mesh
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(392348.1001399256, 6036348.100139925, 27598.10013992562),
     (363625.0, 6007625.0, -1125.0),
     (0.0, 0.0, 1.0)]



.. GENERATED FROM PYTHON SOURCE LINES 38-39

Or threshold a data range

.. GENERATED FROM PYTHON SOURCE LINES 39-40

.. code-block:: default

    mesh.threshold([-0.6, -0.3]).plot(clim=[-0.6, 0.3])



.. image:: /examples/ubc/images/sphx_glr_read-tensor-mesh_003.png
    :alt: read tensor mesh
    :class: sphx-glr-single-img


.. rst-class:: sphx-glr-script-out

 Out:

 .. code-block:: none


    [(384737.1076481045, 6027487.107648104, 19892.107648104513),
     (363875.0, 6006625.0, -970.0),
     (0.0, 0.0, 1.0)]




.. rst-class:: sphx-glr-timing

   **Total running time of the script:** ( 0 minutes  3.009 seconds)


.. _sphx_glr_download_examples_ubc_read-tensor-mesh.py:


.. only :: html

 .. container:: sphx-glr-footer
    :class: sphx-glr-footer-example



  .. container:: sphx-glr-download sphx-glr-download-python

     :download:`Download Python source code: read-tensor-mesh.py <read-tensor-mesh.py>`



  .. container:: sphx-glr-download sphx-glr-download-jupyter

     :download:`Download Jupyter notebook: read-tensor-mesh.ipynb <read-tensor-mesh.ipynb>`


.. only:: html

 .. rst-class:: sphx-glr-signature

    `Gallery generated by Sphinx-Gallery <https://sphinx-gallery.github.io>`_
