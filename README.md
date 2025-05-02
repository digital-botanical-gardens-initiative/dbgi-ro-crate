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

### SIS

People at SIS  have been working on the modelling of [complex xlsx sheets](https://sissource.ethz.ch/sispub/ro-crate/-/blob/main/interoperability/0.1.x/examples/reference-openbis-export/metadata.xlsx?ref_type=heads) through their RO Crate interoperability specs https://sissource.ethz.ch/sispub/ro-crate/-/blob/main/interoperability/0.1.x/examples/ro-crate-1.1/ro-crate-metadata/ro-crate-metadata.json?ref_type=heads.
This has been announced and discussed at https://github.com/ResearchObject/ro-crate/issues/399


### Ideas and tasks

- Chatting with SIS people today (Juan and Andreas), proposed them to add a hash (sha2546 or md5) of the files to ro-crates, I think this could be done also for ROCrate 1.1, wether or not files are described in the schema
- Better examples should be established to showcase the possibilities open by modelling tabular files in the ROCrate metadata.
- Fork https://pypi.org/project/rocrate/ and try to replicate https://sissource.ethz.ch/sispub/ro-crate/-/blob/main/interoperability/0.1.x/

They have shared 

