# HZB (meta)data schema: operando catalysis

(Meta)data schema for operando catalysis: A datamodel for describing entities and their semantic associations (vocabularies/ontologies) for scientific (particularly catalytic) data at HZB, including operando and in situ characterization of catalytic materials.

At the moment, this schema is organized into 2 separate modules:
* catlabs definitions (catalysis lab-based)
* BESSY definitions (synchrotron-based)
* operandoCatalysis definitions (catalysis + synchrotron-based)
* core (common)

### Mappings to: 
* voc4cat
* Chemical Entities Mixtures and Reactions Ontological Framework
* NeXus definitions?? -

## Website

[https://hzb-ce-dataschemas.github.io/hzb-catalysisLabs-schema/](https://hzb-ce-dataschemas.github.io/hzb-catalysisLabs-schema/)

## Repository Structure

* [examples/](examples/) - example data
* [project/](project/) - project files (do not edit these)
* [src/](src/) - source files (edit these)
  * [hzb_catalysislabs_schema](src/hzb_catalysislabs_schema)
    * [schema](src/hzb_catalysislabs_schema/schema) -- LinkML schema
      (edit this)
    * [datamodel](src/hzb_catalysislabs_schema/datamodel) -- generated
      Python datamodel
* [tests/](tests/) - Python tests

## Developer Documentation

<details>
Use the `make` command to generate project artefacts:

* `make all`: make everything
* `make deploy`: deploys site
</details>

## Credits

This project was made with
[linkml-project-cookiecutter](https://github.com/linkml/linkml-project-cookiecutter).
