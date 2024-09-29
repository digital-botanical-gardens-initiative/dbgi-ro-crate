Following https://www.researchobject.org/packaging_data_with_ro-crate/

The RO crate has been created and is observable at http://www.dbgi.org/dbgi-ro-crate/crate1/ro-crate-preview.html

Now what would be great would be to understand mechanisms available to describe the data at a finer granularity. E.g. describe the headers in docs/crate1/data.csv

FrictionLess data seems to be a good candidate for this. It would howevere be simpler to have everything under the same framework. Their is a discussion on the topic at https://github.com/ResearchObject/ro-crate/issues/27. It is still Open.

Dig arcp https://pure.manchester.ac.uk/ws/portalfiles/portal/76956641/arcp.html


### FrictionLess data

A FrictionLess data schemas (is that a [TableSchema](https://specs.frictionlessdata.io/table-schema/#types-and-formats) of a [Data Resource](https://specs.frictionlessdata.io/data-resource/#examples) ? ) is created using the following command 

```bash
frictionless describe docs/crate1/data.csv --yaml > docs
/crate1/data.resource.yaml
```

