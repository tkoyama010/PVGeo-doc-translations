# PVGeo-doc on the Read The Docs.
translated docs for PVGeo-doc official document

:jp:

[![Documentation Status](https://readthedocs.org/projects/pvgeo-doc-ja/badge/?version=latest)](https://pvgeo-doc-ja.readthedocs.io/ja/latest/?badge=latest)

This is a project to provide PVGeo-doc official documentation with multiple versions and multiple languages on Read The Docs site.

Current procedure is bit tricky because Read The Docs doesn't have a way to specify options for sphinx-build command.
conf.py files for each languages have 'language' and 'locale_dirs' values without having full copy of conf.py of sphinx doc. If we want to specify conf.py file that is out of source directory, we will use '-c' option for sphinx-build command. Unfortunately Read the Docs can't. If there are any better way, please let me know.

## URLs

* RTD project pages for Sphinx:

  * https://readthedocs.org/projects/PVGeo-doc/  (Master)
  * https://readthedocs.org/projects/PVGeo-doc-ja/

* Documentation pages for each languages:

  * https://PVGeo-doc.readthedocs.io/en/latest/
  * https://PVGeo-doc.readthedocs.io/ja/latest/

## How to setup a translated documentation project on RTD

Detail is here: https://docs.readthedocs.org/en/latest/localization.html#project-with-multiple-translations

Points are:

* We must have RTD projects for each languages.
* Each projects must have correct Language setting on "Settings" page.
* Master project has connections to each translated projects on "translations settings" page.


## How to update po files

```
sh ./locale/update.sh
```

After that, you should commit updated po files.


## How to add a language

1. add language to locale/update.sh:

   ```
   - rm -R ja
   - tx pull -l ja
   + rm -R ja de
   + tx pull -l ja,de
   ```

2. update po files

3. commit them

4. add new project on Read The Docs like:

   https://readthedocs.org/projects/PVGeo-doc-ja/

5. add translation project to parent project like:

   https://readthedocs.org/dashboard/PVGeo-doc/translations/
