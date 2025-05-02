from rocrate.rocrate import ROCrate
from rocrate.model.person import Person
from rocrate.model.contextentity import ContextEntity

crate = ROCrate()
paper = crate.add_file("./docs/input/paper.pdf", properties={
    "name": "manuscript",
    "encodingFormat": "application/pdf"
})
table = crate.add_file("./docs/input/data.csv", properties={
    "name": "experimental data",
    "encodingFormat": "text/csv"
})
diagram = crate.add_file("./docs/input/diagram.svg", dest_path="images/figure.svg", properties={
    "name": "bar chart",
    "encodingFormat": "image/svg+xml"
})

alice_id = "https://orcid.org/0000-0000-0000-0000"
bob_id = "https://orcid.org/0000-0000-0000-0001"
pma_id = "https://orcid.org/0000-0003-3389-2191"



unifr = crate.add(ContextEntity(crate, "https://ror.org/022fs9h90", properties={
    "name": "University of Fribourg",
    "url": "http://www.unifr.ch/home/welcomeE.php"
}))

alice = crate.add(Person(crate, alice_id, properties={
    "name": "Alice Doe",
    "affiliation": "University of Flatland"
}))
bob = crate.add(Person(crate, bob_id, properties={
    "name": "Bob Doe",
    "affiliation": "University of Flatland"
}))

pma = crate.add(Person(crate, pma_id, properties={
    "name": "PMA",
    "affiliation": unifr
}))


paper["author"] = [alice, bob]
table["author"] = [alice, pma]
diagram["author"] = bob

logs = crate.add_dataset("./docs/input/exp/logs")

crate.write("exp_crate")