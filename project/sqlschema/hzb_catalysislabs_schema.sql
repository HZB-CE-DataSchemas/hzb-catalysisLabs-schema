-- # Class: "chemical or drug or treatment" Description: ""
--     * Slot: id Description: 
-- # Class: "Entity" Description: "An entity is anything that exists or has existed or will exist.  Model class for all things and informational relationships, real or imagined."
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: name Description: A human-readable name for a thing
-- # Class: "NamedEntity" Description: "a databased entity or concept/class"
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "DataCite" Description: "Represents metadata for datasets according to DataCite standard. Core properties of DataCite standard (basics for citation/publications.) DataCite already considers DublinCore elements. "
--     * Slot: identifier Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: identifierType Description: type of identifier.
--     * Slot: creators Description: Creator(s) of the resource.
--     * Slot: title Description: Title of the resource/dataset.
--     * Slot: Publisher Description: lorem.
--     * Slot: ResourceType Description: lorem.
--     * Slot: Subject Description: lorem.
--     * Slot: Contributor Description: Creator of the resource.
--     * Slot: Date Description: Creator of the resource.
--     * Slot: Language Description: Creator of the resource.
--     * Slot: AlternateIdentifier Description: An identifier other than the primary Identifier applied to the resource being registered. This may be any alphanumeric string which is unique within its domain of issue. May be used for local identifiers, a serial number of an instrument or an inventory number. The AlternateIdentifier should be an additional identifier for the same instance of the resource (i.e., same location, same file).
--     * Slot: RelatedIdentifier Description: Identifiers of related resources. These must be globally unique identifiers.
--     * Slot: Size Description: Size (e.g., bytes, pages, inches, etc.) or duration (extent), e.g., hours, minutes, days, etc., of a resource.
--     * Slot: Format Description: Technical format of the resource.
--     * Slot: Version Description: Creator of the resource.
--     * Slot: Rights Description: Creator of the resource.
--     * Slot: Description Description: Creator of the resource.
--     * Slot: GeoLocation Description: Creator of the resource.
--     * Slot: FundingReference Description: Creator of the resource.
--     * Slot: RelatedItem Description: Creator of the resource.
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Person" Description: "A basic/standard definition of a person, which later can be further defined as scientist, beam scientist, user, etc."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: person_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: orcid_id Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: first_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: last_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: title Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: institution Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: department Description: Department or division the researcher belongs to (e.g., "Chemical Energy").
--     * Slot: role Description: Researcher's role in the department (e.g., "Principal Investigator", "Research Assistant", "Postdoc").
--     * Slot: research_focus Description: Area of expertise (e.g. “Thermo-Catalysis”).
--     * Slot: laboratory_name Description: Working group (e.g. Amkreutz lab).
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Project" Description: "A research activity or initiative with defined objectives, funding, and timelines, involving one or more researchers, designed to generate data, publications, and other outputs. The project may involve multiple experiments, datasets, and contributors, and can be linked to specific funding sources and institutions."
--     * Slot: project_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: project_code Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: project_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: acronym Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: start_date Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: end_date Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: status Description: Department or division the researcher belongs to (e.g., "Chemical Energy").
--     * Slot: institutions Description: Researcher's role in the department (e.g., "Principal Investigator", "Research Assistant", "Postdoc").
--     * Slot: principal_investigator Description: Area of expertise (e.g. “Thermo-Catalysis”).
--     * Slot: assigned_lab Description: Working group (e.g. Amkreutz lab).
--     * Slot: research_area Description: Working group (e.g. Amkreutz lab).
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Device" Description: "A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment."
--     * Slot: device_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: serial_number Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: device_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: device_type Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: manufacturer Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: model_number Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: purchase_date Description: Department or division the researcher belongs to (e.g., "Chemical Energy").
--     * Slot: commission_date Description: Researcher's role in the department (e.g., "Principal Investigator", "Research Assistant", "Postdoc").
--     * Slot: warranty_expiration_date Description: Area of expertise (e.g. “Thermo-Catalysis”).
--     * Slot: operating_system Description: Working group (e.g. Amkreutz lab).
--     * Slot: specifications Description: Working group (e.g. Amkreutz lab).
--     * Slot: input_gases Description: Working group (e.g. Amkreutz lab).
--     * Slot: catalyst_handling_capability Description: Working group (e.g. Amkreutz lab).
--     * Slot: ip_address Description: Working group (e.g. Amkreutz lab).
--     * Slot: mac_address Description: Working group (e.g. Amkreutz lab).
--     * Slot: location Description: Working group (e.g. Amkreutz lab).
--     * Slot: responsible_person Description: Working group (e.g. Amkreutz lab).
--     * Slot: device_status Description: Working group (e.g. Amkreutz lab).
--     * Slot: ownership Description: Working group (e.g. Amkreutz lab).
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Sample" Description: "Core properties of a sample, discipline agnostic."
--     * Slot: sample_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: sample_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_description Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: composition Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: size Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: preparation_method Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: batch_number Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: SampleCollection_id Description: Autocreated FK slot
-- # Class: "SampleCollection" Description: "A holder for Sample objects"
--     * Slot: id Description: 
-- # Class: "Scientist" Description: "An individual involved in research activities, and their details that are important  to be referenced on experiments, projects, publivations, etc."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: person_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: orcid_id Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: first_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: last_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: title Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: institution Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: department Description: Department or division the researcher belongs to (e.g., "Chemical Energy").
--     * Slot: role Description: Researcher's role in the department (e.g., "Principal Investigator", "Research Assistant", "Postdoc").
--     * Slot: research_focus Description: Area of expertise (e.g. “Thermo-Catalysis”).
--     * Slot: laboratory_name Description: Working group (e.g. Amkreutz lab).
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "CatalysisSample" Description: "Core properties of a catalysis sample."
--     * Slot: sample_ELN_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: eln_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_institution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_role Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: laboratory_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: project_sample Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_abbreviation Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_type Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_form Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical__formula Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_components Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: active_site Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: support Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: loading Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: purity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: synthesis_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: characterization_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_area Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: particle_size Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: morphology Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: pore_size_distribution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: crystalline_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical_composition Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_chemistry Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_stability Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_activity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: sample_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_description Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: composition Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: size Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: preparation_method Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: batch_number Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: CatalysisSampleCollection_id Description: Autocreated FK slot
-- # Class: "Catalyst" Description: "A substance or material that increases the rate of a chemical reaction.  Class including core properties of the synthesis characterization, and other experiments. "
--     * Slot: sample_ELN_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: eln_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_institution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_role Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: laboratory_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: project_sample Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_abbreviation Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_type Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_form Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical__formula Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_components Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: active_site Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: support Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: loading Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: purity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: synthesis_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: characterization_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_area Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: particle_size Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: morphology Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: pore_size_distribution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: crystalline_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical_composition Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_chemistry Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_stability Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_activity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: sample_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_description Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: composition Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: size Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: preparation_method Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: batch_number Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "ThinFilmCatalyst" Description: "Catalyst type. Core properties of a thin film."
--     * Slot: sample_ELN_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: eln_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_institution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_role Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: laboratory_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: project_sample Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_abbreviation Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_type Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_form Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical__formula Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_components Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: active_site Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: support Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: loading Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: purity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: synthesis_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: characterization_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_area Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: particle_size Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: morphology Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: pore_size_distribution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: crystalline_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical_composition Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_chemistry Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_stability Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_activity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: sample_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_description Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: composition Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: size Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: preparation_method Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: batch_number Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "PowderCatalyst" Description: "Catalyst type. Core properties of a powder catalyst."
--     * Slot: sample_ELN_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: eln_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_institution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: creator_role Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: laboratory_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: project_sample Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: institution_abbreviation Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_type Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_form Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical__formula Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_components Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: active_site Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: support Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: loading Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: purity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: synthesis_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: characterization_method Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_area Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: particle_size Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: morphology Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: pore_size_distribution Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: crystalline_structure Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: chemical_composition Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: surface_chemistry Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_stability Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst_activity Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: sample_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample_description Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: phase Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: composition Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: size Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: preparation_method Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: batch_number Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Recipe" Description: "A detailed set of instructions outlining the materials, quantities, and procedures  required to perform a specific chemical reaction or experimental process."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Mixture" Description: "A combination of two or more substances that are mixed together,  which may retain their individual properties or interact chemically. "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Workflow" Description: "A structured sequence of tasks, activities, or processes designed to accomplish a  specific research objective or experimental goal."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Process" Description: "A defined series of actions, steps, or operations undertaken to achieve a  specific scientific or experimental outcome (e.g. atomic layer deposition)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Experiment" Description: "A systematic investigation designed to test hypotheses, gather data, or explore  scientific principles through controlled conditions."
--     * Slot: experiment_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: experiment_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: performed_by Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: related_project Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: reaction Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: start_date Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: end_date Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Measurement" Description: "Storing and describing measurements to perform on a sample."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Parameter" Description: "Associates parameters on demand to a certain experiment or measurement."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Reaction" Description: "A chemical process in which one or more substances (reactants) undergo transformation to produce new substances (products). "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "ReactionProduct" Description: "A substance formed as a result of a chemical reaction, representing the end products  generated from the transformation of reactants."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
--     * Slot: ReactionProductCollection_id Description: Autocreated FK slot
-- # Class: "Reactor" Description: "Equipment designed to facilitate and control chemical reactions under specified  conditions, such as temperature, pressure, and flow rates. "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "CatalysisSampleCollection" Description: "A holder for CatalysisSample objects"
--     * Slot: id Description: 
-- # Class: "ReactionProductCollection" Description: "A holder for ReactionProduct objects"
--     * Slot: id Description: 
-- # Class: "Beamline" Description: "System within a facility designed to direct a beam of radiation toward a sample for  the purpose of analysis or experimentation."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "BeamlineExperiment" Description: "An experimental investigation conducted using a beamline."
--     * Slot: experiment_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: experiment_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: performed_by Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: related_project Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: catalyst Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: sample Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: reaction Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: start_date Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: end_date Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "BeamlineScientist" Description: "An expert responsible for the operation and scientific application of beamlines  in a research facility."
--     * Slot: primary_email Description: The main email address of a person
--     * Slot: birth_date Description: Date on which a person is born
--     * Slot: age_in_years Description: Number of years since birth
--     * Slot: gender Description: 
--     * Slot: person_id Description: The Identifier is a unique string that identifies a resource (i.e., DOI).
--     * Slot: orcid_id Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: first_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: last_name Description: The ORCID Identifier is a unique string that identifies a researcher.
--     * Slot: title Description: Academic or professional title of the researcher (e.g., "Dr.", "Professor").
--     * Slot: institution Description: Research institution or university the person is affiliated with (e.g., "HZB").
--     * Slot: department Description: Department or division the researcher belongs to (e.g., "Chemical Energy").
--     * Slot: role Description: Researcher's role in the department (e.g., "Principal Investigator", "Research Assistant", "Postdoc").
--     * Slot: research_focus Description: Area of expertise (e.g. “Thermo-Catalysis”).
--     * Slot: laboratory_name Description: Working group (e.g. Amkreutz lab).
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "mySpot" Description: "Myspot beamline description."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EMIL_Pink" Description: "Pink beamline description."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EMIL_OAESE" Description: "OAESE beamline description."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "SampleEnvironment" Description: "Controlled environment in which the sample is studied (operando research)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "EnvironmentDynamics" Description: "Dynamic or time-resolved environmental conditions during an  experiment (e.g.for in-situ measurements)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "SamplePositioning" Description: "The arrangement or location of samples within an experimental setup,  critical for ensuring accurate data collection and analysis. "
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "File" Description: "Stores data related to the experiment (e.g. images, videos, or other files)."
--     * Slot: name Description: A human-readable name for a thing
--     * Slot: id Description: A unique identifier for a thing
--     * Slot: iri Description: Internationalized Resource Identifier
-- # Class: "Person_has_employment_history" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 
-- # Class: "Person_projects" Description: ""
--     * Slot: Person_id Description: Autocreated FK slot
--     * Slot: projects_id Description: Project(s) that the researcher is involved in (e.g. CatLab)
-- # Class: "Project_collaborators" Description: ""
--     * Slot: Project_id Description: Autocreated FK slot
--     * Slot: collaborators_id Description: Project(s) that the researcher is involved in (e.g. CatLab)
-- # Class: "Scientist_has_employment_history" Description: ""
--     * Slot: Scientist_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 
-- # Class: "Scientist_projects" Description: ""
--     * Slot: Scientist_id Description: Autocreated FK slot
--     * Slot: projects_id Description: Project(s) that the researcher is involved in (e.g. CatLab)
-- # Class: "BeamlineScientist_has_employment_history" Description: ""
--     * Slot: BeamlineScientist_id Description: Autocreated FK slot
--     * Slot: has_employment_history Description: 
-- # Class: "BeamlineScientist_projects" Description: ""
--     * Slot: BeamlineScientist_id Description: Autocreated FK slot
--     * Slot: projects_id Description: Project(s) that the researcher is involved in (e.g. CatLab)

CREATE TABLE "chemical or drug or treatment" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Entity" (
	id TEXT NOT NULL, 
	iri TEXT, 
	name TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "NamedEntity" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Person" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	person_id TEXT, 
	orcid_id TEXT, 
	first_name TEXT, 
	last_name TEXT, 
	title TEXT, 
	institution TEXT, 
	department TEXT, 
	role TEXT, 
	research_focus TEXT, 
	laboratory_name TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Device" (
	device_id TEXT, 
	serial_number TEXT, 
	device_name TEXT, 
	device_type TEXT, 
	manufacturer TEXT, 
	model_number TEXT, 
	purchase_date TEXT, 
	commission_date TEXT, 
	warranty_expiration_date TEXT, 
	operating_system TEXT, 
	specifications TEXT, 
	input_gases TEXT, 
	catalyst_handling_capability TEXT, 
	ip_address TEXT, 
	mac_address TEXT, 
	location TEXT, 
	responsible_person TEXT, 
	device_status TEXT, 
	ownership TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SampleCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Scientist" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	person_id TEXT, 
	orcid_id TEXT, 
	first_name TEXT, 
	last_name TEXT, 
	title TEXT, 
	institution TEXT, 
	department TEXT, 
	role TEXT, 
	research_focus TEXT, 
	laboratory_name TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Recipe" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Mixture" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Workflow" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Process" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Measurement" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Parameter" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Reaction" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "Reactor" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "CatalysisSampleCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "ReactionProductCollection" (
	id INTEGER NOT NULL, 
	PRIMARY KEY (id)
);
CREATE TABLE "Beamline" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "BeamlineScientist" (
	primary_email TEXT, 
	birth_date DATE, 
	age_in_years INTEGER, 
	gender VARCHAR(9), 
	person_id TEXT, 
	orcid_id TEXT, 
	first_name TEXT, 
	last_name TEXT, 
	title TEXT, 
	institution TEXT, 
	department TEXT, 
	role TEXT, 
	research_focus TEXT, 
	laboratory_name TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "mySpot" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EMIL_Pink" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EMIL_OAESE" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SampleEnvironment" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "EnvironmentDynamics" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "SamplePositioning" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "File" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id)
);
CREATE TABLE "DataCite" (
	identifier TEXT, 
	"identifierType" TEXT, 
	creators TEXT, 
	title TEXT, 
	"Publisher" TEXT, 
	"ResourceType" TEXT, 
	"Subject" TEXT, 
	"Contributor" TEXT, 
	"Date" TEXT, 
	"Language" TEXT, 
	"AlternateIdentifier" TEXT, 
	"RelatedIdentifier" TEXT, 
	"Size" TEXT, 
	"Format" TEXT, 
	"Version" TEXT, 
	"Rights" TEXT, 
	"Description" TEXT, 
	"GeoLocation" TEXT, 
	"FundingReference" TEXT, 
	"RelatedItem" TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(creators) REFERENCES "Person" (id)
);
CREATE TABLE "Project" (
	project_id TEXT, 
	project_code TEXT, 
	project_name TEXT, 
	acronym TEXT, 
	start_date TEXT, 
	end_date TEXT, 
	status TEXT, 
	institutions TEXT, 
	principal_investigator TEXT, 
	assigned_lab TEXT, 
	research_area TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(principal_investigator) REFERENCES "Scientist" (id)
);
CREATE TABLE "Sample" (
	sample_id TEXT, 
	sample_name TEXT, 
	sample_description TEXT, 
	phase TEXT, 
	composition TEXT, 
	size TEXT, 
	preparation_method TEXT, 
	batch_number TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"SampleCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("SampleCollection_id") REFERENCES "SampleCollection" (id)
);
CREATE TABLE "ReactionProduct" (
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"ReactionProductCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY("ReactionProductCollection_id") REFERENCES "ReactionProductCollection" (id)
);
CREATE TABLE "Person_has_employment_history" (
	"Person_id" TEXT, 
	has_employment_history TEXT, 
	PRIMARY KEY ("Person_id", has_employment_history), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id)
);
CREATE TABLE "Scientist_has_employment_history" (
	"Scientist_id" TEXT, 
	has_employment_history TEXT, 
	PRIMARY KEY ("Scientist_id", has_employment_history), 
	FOREIGN KEY("Scientist_id") REFERENCES "Scientist" (id)
);
CREATE TABLE "BeamlineScientist_has_employment_history" (
	"BeamlineScientist_id" TEXT, 
	has_employment_history TEXT, 
	PRIMARY KEY ("BeamlineScientist_id", has_employment_history), 
	FOREIGN KEY("BeamlineScientist_id") REFERENCES "BeamlineScientist" (id)
);
CREATE TABLE "CatalysisSample" (
	"sample_ELN_id" TEXT, 
	eln_name TEXT, 
	creator_name TEXT, 
	creator_institution TEXT, 
	creator_role TEXT, 
	laboratory_name TEXT, 
	project_sample TEXT, 
	institution_name TEXT, 
	institution_abbreviation TEXT, 
	catalyst_type TEXT, 
	catalyst_phase TEXT, 
	catalyst_form TEXT, 
	catalyst_name TEXT, 
	chemical__formula TEXT, 
	catalyst_components TEXT, 
	catalyst_structure TEXT, 
	active_site TEXT, 
	support TEXT, 
	loading TEXT, 
	purity TEXT, 
	synthesis_method TEXT, 
	characterization_method TEXT, 
	surface_area TEXT, 
	particle_size TEXT, 
	morphology TEXT, 
	pore_size_distribution TEXT, 
	crystalline_structure TEXT, 
	chemical_composition TEXT, 
	surface_chemistry TEXT, 
	catalyst_stability TEXT, 
	catalyst_activity TEXT, 
	sample_id TEXT, 
	sample_name TEXT, 
	sample_description TEXT, 
	phase TEXT, 
	composition TEXT, 
	size TEXT, 
	preparation_method TEXT, 
	batch_number TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	"CatalysisSampleCollection_id" INTEGER, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_sample) REFERENCES "Project" (id), 
	FOREIGN KEY("CatalysisSampleCollection_id") REFERENCES "CatalysisSampleCollection" (id)
);
CREATE TABLE "Catalyst" (
	"sample_ELN_id" TEXT, 
	eln_name TEXT, 
	creator_name TEXT, 
	creator_institution TEXT, 
	creator_role TEXT, 
	laboratory_name TEXT, 
	project_sample TEXT, 
	institution_name TEXT, 
	institution_abbreviation TEXT, 
	catalyst_type TEXT, 
	catalyst_phase TEXT, 
	catalyst_form TEXT, 
	catalyst_name TEXT, 
	chemical__formula TEXT, 
	catalyst_components TEXT, 
	catalyst_structure TEXT, 
	active_site TEXT, 
	support TEXT, 
	loading TEXT, 
	purity TEXT, 
	synthesis_method TEXT, 
	characterization_method TEXT, 
	surface_area TEXT, 
	particle_size TEXT, 
	morphology TEXT, 
	pore_size_distribution TEXT, 
	crystalline_structure TEXT, 
	chemical_composition TEXT, 
	surface_chemistry TEXT, 
	catalyst_stability TEXT, 
	catalyst_activity TEXT, 
	sample_id TEXT, 
	sample_name TEXT, 
	sample_description TEXT, 
	phase TEXT, 
	composition TEXT, 
	size TEXT, 
	preparation_method TEXT, 
	batch_number TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_sample) REFERENCES "Project" (id)
);
CREATE TABLE "ThinFilmCatalyst" (
	"sample_ELN_id" TEXT, 
	eln_name TEXT, 
	creator_name TEXT, 
	creator_institution TEXT, 
	creator_role TEXT, 
	laboratory_name TEXT, 
	project_sample TEXT, 
	institution_name TEXT, 
	institution_abbreviation TEXT, 
	catalyst_type TEXT, 
	catalyst_phase TEXT, 
	catalyst_form TEXT, 
	catalyst_name TEXT, 
	chemical__formula TEXT, 
	catalyst_components TEXT, 
	catalyst_structure TEXT, 
	active_site TEXT, 
	support TEXT, 
	loading TEXT, 
	purity TEXT, 
	synthesis_method TEXT, 
	characterization_method TEXT, 
	surface_area TEXT, 
	particle_size TEXT, 
	morphology TEXT, 
	pore_size_distribution TEXT, 
	crystalline_structure TEXT, 
	chemical_composition TEXT, 
	surface_chemistry TEXT, 
	catalyst_stability TEXT, 
	catalyst_activity TEXT, 
	sample_id TEXT, 
	sample_name TEXT, 
	sample_description TEXT, 
	phase TEXT, 
	composition TEXT, 
	size TEXT, 
	preparation_method TEXT, 
	batch_number TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_sample) REFERENCES "Project" (id)
);
CREATE TABLE "PowderCatalyst" (
	"sample_ELN_id" TEXT, 
	eln_name TEXT, 
	creator_name TEXT, 
	creator_institution TEXT, 
	creator_role TEXT, 
	laboratory_name TEXT, 
	project_sample TEXT, 
	institution_name TEXT, 
	institution_abbreviation TEXT, 
	catalyst_type TEXT, 
	catalyst_phase TEXT, 
	catalyst_form TEXT, 
	catalyst_name TEXT, 
	chemical__formula TEXT, 
	catalyst_components TEXT, 
	catalyst_structure TEXT, 
	active_site TEXT, 
	support TEXT, 
	loading TEXT, 
	purity TEXT, 
	synthesis_method TEXT, 
	characterization_method TEXT, 
	surface_area TEXT, 
	particle_size TEXT, 
	morphology TEXT, 
	pore_size_distribution TEXT, 
	crystalline_structure TEXT, 
	chemical_composition TEXT, 
	surface_chemistry TEXT, 
	catalyst_stability TEXT, 
	catalyst_activity TEXT, 
	sample_id TEXT, 
	sample_name TEXT, 
	sample_description TEXT, 
	phase TEXT, 
	composition TEXT, 
	size TEXT, 
	preparation_method TEXT, 
	batch_number TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(project_sample) REFERENCES "Project" (id)
);
CREATE TABLE "Person_projects" (
	"Person_id" TEXT, 
	projects_id TEXT, 
	PRIMARY KEY ("Person_id", projects_id), 
	FOREIGN KEY("Person_id") REFERENCES "Person" (id), 
	FOREIGN KEY(projects_id) REFERENCES "Project" (id)
);
CREATE TABLE "Project_collaborators" (
	"Project_id" TEXT, 
	collaborators_id TEXT, 
	PRIMARY KEY ("Project_id", collaborators_id), 
	FOREIGN KEY("Project_id") REFERENCES "Project" (id), 
	FOREIGN KEY(collaborators_id) REFERENCES "Person" (id)
);
CREATE TABLE "Scientist_projects" (
	"Scientist_id" TEXT, 
	projects_id TEXT, 
	PRIMARY KEY ("Scientist_id", projects_id), 
	FOREIGN KEY("Scientist_id") REFERENCES "Scientist" (id), 
	FOREIGN KEY(projects_id) REFERENCES "Project" (id)
);
CREATE TABLE "BeamlineScientist_projects" (
	"BeamlineScientist_id" TEXT, 
	projects_id TEXT, 
	PRIMARY KEY ("BeamlineScientist_id", projects_id), 
	FOREIGN KEY("BeamlineScientist_id") REFERENCES "BeamlineScientist" (id), 
	FOREIGN KEY(projects_id) REFERENCES "Project" (id)
);
CREATE TABLE "Experiment" (
	experiment_id TEXT, 
	experiment_name TEXT, 
	performed_by TEXT, 
	related_project TEXT, 
	catalyst TEXT, 
	sample TEXT, 
	reaction TEXT, 
	start_date TEXT, 
	end_date TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(performed_by) REFERENCES "Scientist" (id), 
	FOREIGN KEY(related_project) REFERENCES "Project" (id), 
	FOREIGN KEY(catalyst) REFERENCES "Catalyst" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (id), 
	FOREIGN KEY(reaction) REFERENCES "Reaction" (id)
);
CREATE TABLE "BeamlineExperiment" (
	experiment_id TEXT, 
	experiment_name TEXT, 
	performed_by TEXT, 
	related_project TEXT, 
	catalyst TEXT, 
	sample TEXT, 
	reaction TEXT, 
	start_date TEXT, 
	end_date TEXT, 
	name TEXT, 
	id TEXT NOT NULL, 
	iri TEXT, 
	PRIMARY KEY (id), 
	FOREIGN KEY(performed_by) REFERENCES "Scientist" (id), 
	FOREIGN KEY(related_project) REFERENCES "Project" (id), 
	FOREIGN KEY(catalyst) REFERENCES "Catalyst" (id), 
	FOREIGN KEY(sample) REFERENCES "Sample" (id), 
	FOREIGN KEY(reaction) REFERENCES "Reaction" (id)
);