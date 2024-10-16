# Auto generated from hzb_catalysislabs_schema.yaml by pythongen.py version: 0.0.1
# Generation date: 2024-10-16T11:38:38
# Schema: hzb-catalysisLabs-schema
#
# id: https://w3id.org/https://github.com/HZB-CE-DataSchemas//hzb-catalysisLabs-schema
# description: A datamodel for describing entities and their semantic associations (vocabularies/ontologies) for scientific (particularly catalytic) data at HZB, particularly for operando and in situ characterization of catalytic materials.
# license: MIT

import dataclasses
import re
from jsonasobj2 import JsonObj, as_dict
from typing import Optional, List, Union, Dict, ClassVar, Any
from dataclasses import dataclass
from datetime import date, datetime, time
from linkml_runtime.linkml_model.meta import EnumDefinition, PermissibleValue, PvFormulaOptions

from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.metamodelcore import empty_list, empty_dict, bnode
from linkml_runtime.utils.yamlutils import YAMLRoot, extended_str, extended_float, extended_int
from linkml_runtime.utils.dataclass_extensions_376 import dataclasses_init_fn_with_kwargs
from linkml_runtime.utils.formatutils import camelcase, underscore, sfx
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from rdflib import Namespace, URIRef
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.linkml_model.types import Date, Float, Integer, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE, XSDDate

metamodel_version = "1.7.0"
version = None

# Overwrite dataclasses _init_fn to add **kwargs in __init__
dataclasses._init_fn = dataclasses_init_fn_with_kwargs

# Namespaces
BFO = CurieNamespace('BFO', 'http://purl.obolibrary.org/obo/BFO_')
GSSO = CurieNamespace('GSSO', 'http://purl.bioontology.org/ontology/GSSO/')
PATO = CurieNamespace('PATO', 'http://purl.obolibrary.org/obo/PATO_')
STY = CurieNamespace('STY', 'http://example.org/UNKNOWN/STY/')
UMLSSG = CurieNamespace('UMLSSG', 'http://example.org/UNKNOWN/UMLSSG/')
WIKIDATA = CurieNamespace('WIKIDATA', 'http://example.org/UNKNOWN/WIKIDATA/')
BIOLINK = CurieNamespace('biolink', 'https://w3id.org/biolink/')
DCID = CurieNamespace('dcid', 'http://example.org/UNKNOWN/dcid/')
HZB_METADATA_SCHEMA = CurieNamespace('hzb_metadata_schema', 'https://w3id.org/anak-velazquez/hzb-metadata-schema/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = HZB_METADATA_SCHEMA


# Types
class ChemicalFormulaValue(str):
    """ A chemical formula """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "chemical formula value"
    type_model_uri = HZB_METADATA_SCHEMA.ChemicalFormulaValue


# Class references
class EntityId(URIorCURIE):
    pass


class NamedEntityId(EntityId):
    pass


class DataCiteId(NamedEntityId):
    pass


class PersonId(NamedEntityId):
    pass


class ProjectId(NamedEntityId):
    pass


class DeviceId(NamedEntityId):
    pass


class SampleId(NamedEntityId):
    pass


class ScientistId(PersonId):
    pass


class CatalysisSampleId(SampleId):
    pass


class CatalystId(CatalysisSampleId):
    pass


class ThinFilmCatalystId(CatalystId):
    pass


class PowderCatalystId(CatalystId):
    pass


class RecipeId(NamedEntityId):
    pass


class MixtureId(NamedEntityId):
    pass


class WorkflowId(NamedEntityId):
    pass


class ProcessId(NamedEntityId):
    pass


class SynthesisProcessId(ProcessId):
    pass


class CleaningProcessId(ProcessId):
    pass


class CharacterizationProcessId(ProcessId):
    pass


class CatalyticActivityAssesmentProcessId(ProcessId):
    pass


class AnalyticsProcessId(ProcessId):
    pass


class OzoneCleaningId(CleaningProcessId):
    pass


class ALDId(SynthesisProcessId):
    pass


class ALDBeneQId(ALDId):
    pass


class CVDId(SynthesisProcessId):
    pass


class CVDNanofabId(CVDId):
    pass


class CVDPc1Id(CVDId):
    pass


class CVDPc2Id(CVDId):
    pass


class SputteringId(SynthesisProcessId):
    pass


class SputteringPrevacId(SputteringId):
    pass


class SputteringVonAdenneId(SputteringId):
    pass


class ExperimentId(NamedEntityId):
    pass


class MeasurementId(NamedEntityId):
    pass


class ParameterId(NamedEntityId):
    pass


class ReactionId(NamedEntityId):
    pass


class ReactionProductId(NamedEntityId):
    pass


class ReactorId(NamedEntityId):
    pass


class BeamlineId(NamedEntityId):
    pass


class BeamlineExperimentId(ExperimentId):
    pass


class BeamlineScientistId(PersonId):
    pass


class MySpotId(BeamlineId):
    pass


class EMILPinkId(BeamlineId):
    pass


class EMILOAESEId(BeamlineId):
    pass


class SampleEnvironmentId(NamedEntityId):
    pass


class EnvironmentDynamicsId(NamedEntityId):
    pass


class SamplePositioningId(NamedEntityId):
    pass


class FileId(NamedEntityId):
    pass


class ChemicalOrDrugOrTreatment(YAMLRoot):
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA["ChemicalOrDrugOrTreatment"]
    class_class_curie: ClassVar[str] = "hzb_metadata_schema:ChemicalOrDrugOrTreatment"
    class_name: ClassVar[str] = "chemical or drug or treatment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ChemicalOrDrugOrTreatment


@dataclass(repr=False)
class Entity(YAMLRoot):
    """
    An entity is anything that exists or has existed or will exist. Model class for all things and informational
    relationships, real or imagined.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Entity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Entity"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Entity

    id: Union[str, EntityId] = None
    iri: Optional[str] = None
    name: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EntityId):
            self.id = EntityId(self.id)

        if self.iri is not None and not isinstance(self.iri, str):
            self.iri = str(self.iri)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedEntity(Entity):
    """
    a databased entity or concept/class
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/NamedEntity")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "NamedEntity"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.NamedEntity

    id: Union[str, NamedEntityId] = None
    name: Optional[str] = None
    category: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedEntityId):
            self.id = NamedEntityId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class DataCite(NamedEntity):
    """
    Represents metadata for datasets according to DataCite standard. Core properties of DataCite standard (basics for
    citation/publications.) DataCite already considers DublinCore elements.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/DataCite")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "DataCite"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.DataCite

    id: Union[str, DataCiteId] = None
    identifier: Optional[str] = None
    identifierType: Optional[str] = None
    creators: Optional[Union[str, PersonId]] = None
    title: Optional[str] = None
    Publisher: Optional[str] = None
    ResourceType: Optional[str] = None
    Subject: Optional[str] = None
    Contributor: Optional[str] = None
    Date: Optional[str] = None
    Language: Optional[str] = None
    AlternateIdentifier: Optional[str] = None
    RelatedIdentifier: Optional[str] = None
    Size: Optional[str] = None
    Format: Optional[str] = None
    Version: Optional[str] = None
    Rights: Optional[str] = None
    Description: Optional[str] = None
    GeoLocation: Optional[str] = None
    FundingReference: Optional[str] = None
    RelatedItem: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DataCiteId):
            self.id = DataCiteId(self.id)

        if self.identifier is not None and not isinstance(self.identifier, str):
            self.identifier = str(self.identifier)

        if self.identifierType is not None and not isinstance(self.identifierType, str):
            self.identifierType = str(self.identifierType)

        if self.creators is not None and not isinstance(self.creators, PersonId):
            self.creators = PersonId(self.creators)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.Publisher is not None and not isinstance(self.Publisher, str):
            self.Publisher = str(self.Publisher)

        if self.ResourceType is not None and not isinstance(self.ResourceType, str):
            self.ResourceType = str(self.ResourceType)

        if self.Subject is not None and not isinstance(self.Subject, str):
            self.Subject = str(self.Subject)

        if self.Contributor is not None and not isinstance(self.Contributor, str):
            self.Contributor = str(self.Contributor)

        if self.Date is not None and not isinstance(self.Date, str):
            self.Date = str(self.Date)

        if self.Language is not None and not isinstance(self.Language, str):
            self.Language = str(self.Language)

        if self.AlternateIdentifier is not None and not isinstance(self.AlternateIdentifier, str):
            self.AlternateIdentifier = str(self.AlternateIdentifier)

        if self.RelatedIdentifier is not None and not isinstance(self.RelatedIdentifier, str):
            self.RelatedIdentifier = str(self.RelatedIdentifier)

        if self.Size is not None and not isinstance(self.Size, str):
            self.Size = str(self.Size)

        if self.Format is not None and not isinstance(self.Format, str):
            self.Format = str(self.Format)

        if self.Version is not None and not isinstance(self.Version, str):
            self.Version = str(self.Version)

        if self.Rights is not None and not isinstance(self.Rights, str):
            self.Rights = str(self.Rights)

        if self.Description is not None and not isinstance(self.Description, str):
            self.Description = str(self.Description)

        if self.GeoLocation is not None and not isinstance(self.GeoLocation, str):
            self.GeoLocation = str(self.GeoLocation)

        if self.FundingReference is not None and not isinstance(self.FundingReference, str):
            self.FundingReference = str(self.FundingReference)

        if self.RelatedItem is not None and not isinstance(self.RelatedItem, str):
            self.RelatedItem = str(self.RelatedItem)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Person(NamedEntity):
    """
    A basic/standard definition of a person, which later can be further defined as scientist, beam scientist, user,
    etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Person"]
    class_class_curie: ClassVar[str] = "schema:Person"
    class_name: ClassVar[str] = "Person"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Person

    id: Union[str, PersonId] = None
    primary_email: Optional[str] = None
    birth_date: Optional[Union[str, XSDDate]] = None
    age_in_years: Optional[int] = None
    gender: Optional[Union[str, "GenderEnum"]] = None
    has_employment_history: Optional[Union[str, List[str]]] = empty_list()
    person_id: Optional[str] = None
    orcid_id: Optional[str] = None
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    title: Optional[str] = None
    institution: Optional[str] = None
    department: Optional[str] = None
    role: Optional[str] = None
    research_focus: Optional[str] = None
    laboratory_name: Optional[str] = None
    projects: Optional[Union[Union[str, ProjectId], List[Union[str, ProjectId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PersonId):
            self.id = PersonId(self.id)

        if self.primary_email is not None and not isinstance(self.primary_email, str):
            self.primary_email = str(self.primary_email)

        if self.birth_date is not None and not isinstance(self.birth_date, XSDDate):
            self.birth_date = XSDDate(self.birth_date)

        if self.age_in_years is not None and not isinstance(self.age_in_years, int):
            self.age_in_years = int(self.age_in_years)

        if self.gender is not None and not isinstance(self.gender, GenderEnum):
            self.gender = GenderEnum(self.gender)

        if not isinstance(self.has_employment_history, list):
            self.has_employment_history = [self.has_employment_history] if self.has_employment_history is not None else []
        self.has_employment_history = [v if isinstance(v, str) else str(v) for v in self.has_employment_history]

        if self.person_id is not None and not isinstance(self.person_id, str):
            self.person_id = str(self.person_id)

        if self.orcid_id is not None and not isinstance(self.orcid_id, str):
            self.orcid_id = str(self.orcid_id)

        if self.first_name is not None and not isinstance(self.first_name, str):
            self.first_name = str(self.first_name)

        if self.last_name is not None and not isinstance(self.last_name, str):
            self.last_name = str(self.last_name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.institution is not None and not isinstance(self.institution, str):
            self.institution = str(self.institution)

        if self.department is not None and not isinstance(self.department, str):
            self.department = str(self.department)

        if self.role is not None and not isinstance(self.role, str):
            self.role = str(self.role)

        if self.research_focus is not None and not isinstance(self.research_focus, str):
            self.research_focus = str(self.research_focus)

        if self.laboratory_name is not None and not isinstance(self.laboratory_name, str):
            self.laboratory_name = str(self.laboratory_name)

        if not isinstance(self.projects, list):
            self.projects = [self.projects] if self.projects is not None else []
        self.projects = [v if isinstance(v, ProjectId) else ProjectId(v) for v in self.projects]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Project(NamedEntity):
    """
    A research activity or initiative with defined objectives, funding, and timelines, involving one or more
    researchers, designed to generate data, publications, and other outputs. The project may involve multiple
    experiments, datasets, and contributors, and can be linked to specific funding sources and institutions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Project")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Project"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Project

    id: Union[str, ProjectId] = None
    project_id: Optional[str] = None
    project_code: Optional[str] = None
    project_name: Optional[str] = None
    acronym: Optional[str] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None
    status: Optional[str] = None
    institutions: Optional[str] = None
    principal_investigator: Optional[Union[str, ScientistId]] = None
    assigned_lab: Optional[str] = None
    research_area: Optional[str] = None
    collaborators: Optional[Union[Union[str, PersonId], List[Union[str, PersonId]]]] = empty_list()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProjectId):
            self.id = ProjectId(self.id)

        if self.project_id is not None and not isinstance(self.project_id, str):
            self.project_id = str(self.project_id)

        if self.project_code is not None and not isinstance(self.project_code, str):
            self.project_code = str(self.project_code)

        if self.project_name is not None and not isinstance(self.project_name, str):
            self.project_name = str(self.project_name)

        if self.acronym is not None and not isinstance(self.acronym, str):
            self.acronym = str(self.acronym)

        if self.start_date is not None and not isinstance(self.start_date, str):
            self.start_date = str(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, str):
            self.end_date = str(self.end_date)

        if self.status is not None and not isinstance(self.status, str):
            self.status = str(self.status)

        if self.institutions is not None and not isinstance(self.institutions, str):
            self.institutions = str(self.institutions)

        if self.principal_investigator is not None and not isinstance(self.principal_investigator, ScientistId):
            self.principal_investigator = ScientistId(self.principal_investigator)

        if self.assigned_lab is not None and not isinstance(self.assigned_lab, str):
            self.assigned_lab = str(self.assigned_lab)

        if self.research_area is not None and not isinstance(self.research_area, str):
            self.research_area = str(self.research_area)

        if not isinstance(self.collaborators, list):
            self.collaborators = [self.collaborators] if self.collaborators is not None else []
        self.collaborators = [v if isinstance(v, PersonId) else PersonId(v) for v in self.collaborators]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Device(NamedEntity):
    """
    A thing made or adapted for a particular purpose, especially a piece of mechanical or electronic equipment.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Device")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Device"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Device

    id: Union[str, DeviceId] = None
    device_id: Optional[str] = None
    serial_number: Optional[str] = None
    device_name: Optional[str] = None
    device_type: Optional[str] = None
    manufacturer: Optional[str] = None
    model_number: Optional[str] = None
    purchase_date: Optional[str] = None
    commission_date: Optional[str] = None
    warranty_expiration_date: Optional[str] = None
    operating_system: Optional[str] = None
    specifications: Optional[str] = None
    input_gases: Optional[str] = None
    catalyst_handling_capability: Optional[str] = None
    ip_address: Optional[str] = None
    mac_address: Optional[str] = None
    location: Optional[str] = None
    responsible_person: Optional[str] = None
    device_status: Optional[str] = None
    ownership: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, DeviceId):
            self.id = DeviceId(self.id)

        if self.device_id is not None and not isinstance(self.device_id, str):
            self.device_id = str(self.device_id)

        if self.serial_number is not None and not isinstance(self.serial_number, str):
            self.serial_number = str(self.serial_number)

        if self.device_name is not None and not isinstance(self.device_name, str):
            self.device_name = str(self.device_name)

        if self.device_type is not None and not isinstance(self.device_type, str):
            self.device_type = str(self.device_type)

        if self.manufacturer is not None and not isinstance(self.manufacturer, str):
            self.manufacturer = str(self.manufacturer)

        if self.model_number is not None and not isinstance(self.model_number, str):
            self.model_number = str(self.model_number)

        if self.purchase_date is not None and not isinstance(self.purchase_date, str):
            self.purchase_date = str(self.purchase_date)

        if self.commission_date is not None and not isinstance(self.commission_date, str):
            self.commission_date = str(self.commission_date)

        if self.warranty_expiration_date is not None and not isinstance(self.warranty_expiration_date, str):
            self.warranty_expiration_date = str(self.warranty_expiration_date)

        if self.operating_system is not None and not isinstance(self.operating_system, str):
            self.operating_system = str(self.operating_system)

        if self.specifications is not None and not isinstance(self.specifications, str):
            self.specifications = str(self.specifications)

        if self.input_gases is not None and not isinstance(self.input_gases, str):
            self.input_gases = str(self.input_gases)

        if self.catalyst_handling_capability is not None and not isinstance(self.catalyst_handling_capability, str):
            self.catalyst_handling_capability = str(self.catalyst_handling_capability)

        if self.ip_address is not None and not isinstance(self.ip_address, str):
            self.ip_address = str(self.ip_address)

        if self.mac_address is not None and not isinstance(self.mac_address, str):
            self.mac_address = str(self.mac_address)

        if self.location is not None and not isinstance(self.location, str):
            self.location = str(self.location)

        if self.responsible_person is not None and not isinstance(self.responsible_person, str):
            self.responsible_person = str(self.responsible_person)

        if self.device_status is not None and not isinstance(self.device_status, str):
            self.device_status = str(self.device_status)

        if self.ownership is not None and not isinstance(self.ownership, str):
            self.ownership = str(self.ownership)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sample(NamedEntity):
    """
    Core properties of a sample, discipline agnostic.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/Sample")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Sample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Sample

    id: Union[str, SampleId] = None
    sample_id: Optional[str] = None
    sample_name: Optional[str] = None
    sample_description: Optional[str] = None
    phase: Optional[str] = None
    composition: Optional[str] = None
    size: Optional[str] = None
    preparation_method: Optional[str] = None
    batch_number: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleId):
            self.id = SampleId(self.id)

        if self.sample_id is not None and not isinstance(self.sample_id, str):
            self.sample_id = str(self.sample_id)

        if self.sample_name is not None and not isinstance(self.sample_name, str):
            self.sample_name = str(self.sample_name)

        if self.sample_description is not None and not isinstance(self.sample_description, str):
            self.sample_description = str(self.sample_description)

        if self.phase is not None and not isinstance(self.phase, str):
            self.phase = str(self.phase)

        if self.composition is not None and not isinstance(self.composition, str):
            self.composition = str(self.composition)

        if self.size is not None and not isinstance(self.size, str):
            self.size = str(self.size)

        if self.preparation_method is not None and not isinstance(self.preparation_method, str):
            self.preparation_method = str(self.preparation_method)

        if self.batch_number is not None and not isinstance(self.batch_number, str):
            self.batch_number = str(self.batch_number)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleCollection(YAMLRoot):
    """
    A holder for Sample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/core/SampleCollection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SampleCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SampleCollection

    entries: Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=Sample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Scientist(Person):
    """
    An individual involved in research activities, and their details that are important to be referenced on
    experiments, projects, publivations, etc.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Scientist")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Scientist"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Scientist

    id: Union[str, ScientistId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ScientistId):
            self.id = ScientistId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalysisSample(Sample):
    """
    Core properties of a catalysis sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CatalysisSample")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CatalysisSample"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CatalysisSample

    id: Union[str, CatalysisSampleId] = None
    sample_ELN_id: Optional[str] = None
    eln_name: Optional[str] = None
    creator_name: Optional[str] = None
    creator_institution: Optional[str] = None
    creator_role: Optional[str] = None
    laboratory_name: Optional[str] = None
    project_sample: Optional[Union[str, ProjectId]] = None
    institution_name: Optional[str] = None
    institution_abbreviation: Optional[str] = None
    catalyst_type: Optional[str] = None
    catalyst_phase: Optional[str] = None
    catalyst_form: Optional[str] = None
    catalyst_name: Optional[str] = None
    chemical__formula: Optional[str] = None
    catalyst_components: Optional[str] = None
    catalyst_structure: Optional[str] = None
    active_site: Optional[str] = None
    support: Optional[str] = None
    loading: Optional[str] = None
    purity: Optional[str] = None
    synthesis_method: Optional[str] = None
    characterization_method: Optional[str] = None
    surface_area: Optional[str] = None
    particle_size: Optional[str] = None
    morphology: Optional[str] = None
    pore_size_distribution: Optional[str] = None
    crystalline_structure: Optional[str] = None
    chemical_composition: Optional[str] = None
    surface_chemistry: Optional[str] = None
    catalyst_stability: Optional[str] = None
    catalyst_activity: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalysisSampleId):
            self.id = CatalysisSampleId(self.id)

        if self.sample_ELN_id is not None and not isinstance(self.sample_ELN_id, str):
            self.sample_ELN_id = str(self.sample_ELN_id)

        if self.eln_name is not None and not isinstance(self.eln_name, str):
            self.eln_name = str(self.eln_name)

        if self.creator_name is not None and not isinstance(self.creator_name, str):
            self.creator_name = str(self.creator_name)

        if self.creator_institution is not None and not isinstance(self.creator_institution, str):
            self.creator_institution = str(self.creator_institution)

        if self.creator_role is not None and not isinstance(self.creator_role, str):
            self.creator_role = str(self.creator_role)

        if self.laboratory_name is not None and not isinstance(self.laboratory_name, str):
            self.laboratory_name = str(self.laboratory_name)

        if self.project_sample is not None and not isinstance(self.project_sample, ProjectId):
            self.project_sample = ProjectId(self.project_sample)

        if self.institution_name is not None and not isinstance(self.institution_name, str):
            self.institution_name = str(self.institution_name)

        if self.institution_abbreviation is not None and not isinstance(self.institution_abbreviation, str):
            self.institution_abbreviation = str(self.institution_abbreviation)

        if self.catalyst_type is not None and not isinstance(self.catalyst_type, str):
            self.catalyst_type = str(self.catalyst_type)

        if self.catalyst_phase is not None and not isinstance(self.catalyst_phase, str):
            self.catalyst_phase = str(self.catalyst_phase)

        if self.catalyst_form is not None and not isinstance(self.catalyst_form, str):
            self.catalyst_form = str(self.catalyst_form)

        if self.catalyst_name is not None and not isinstance(self.catalyst_name, str):
            self.catalyst_name = str(self.catalyst_name)

        if self.chemical__formula is not None and not isinstance(self.chemical__formula, str):
            self.chemical__formula = str(self.chemical__formula)

        if self.catalyst_components is not None and not isinstance(self.catalyst_components, str):
            self.catalyst_components = str(self.catalyst_components)

        if self.catalyst_structure is not None and not isinstance(self.catalyst_structure, str):
            self.catalyst_structure = str(self.catalyst_structure)

        if self.active_site is not None and not isinstance(self.active_site, str):
            self.active_site = str(self.active_site)

        if self.support is not None and not isinstance(self.support, str):
            self.support = str(self.support)

        if self.loading is not None and not isinstance(self.loading, str):
            self.loading = str(self.loading)

        if self.purity is not None and not isinstance(self.purity, str):
            self.purity = str(self.purity)

        if self.synthesis_method is not None and not isinstance(self.synthesis_method, str):
            self.synthesis_method = str(self.synthesis_method)

        if self.characterization_method is not None and not isinstance(self.characterization_method, str):
            self.characterization_method = str(self.characterization_method)

        if self.surface_area is not None and not isinstance(self.surface_area, str):
            self.surface_area = str(self.surface_area)

        if self.particle_size is not None and not isinstance(self.particle_size, str):
            self.particle_size = str(self.particle_size)

        if self.morphology is not None and not isinstance(self.morphology, str):
            self.morphology = str(self.morphology)

        if self.pore_size_distribution is not None and not isinstance(self.pore_size_distribution, str):
            self.pore_size_distribution = str(self.pore_size_distribution)

        if self.crystalline_structure is not None and not isinstance(self.crystalline_structure, str):
            self.crystalline_structure = str(self.crystalline_structure)

        if self.chemical_composition is not None and not isinstance(self.chemical_composition, str):
            self.chemical_composition = str(self.chemical_composition)

        if self.surface_chemistry is not None and not isinstance(self.surface_chemistry, str):
            self.surface_chemistry = str(self.surface_chemistry)

        if self.catalyst_stability is not None and not isinstance(self.catalyst_stability, str):
            self.catalyst_stability = str(self.catalyst_stability)

        if self.catalyst_activity is not None and not isinstance(self.catalyst_activity, str):
            self.catalyst_activity = str(self.catalyst_activity)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Catalyst(CatalysisSample):
    """
    A substance or material that increases the rate of a chemical reaction. Class including core properties of the
    synthesis characterization, and other experiments.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Catalyst")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Catalyst"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Catalyst

    id: Union[str, CatalystId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalystId):
            self.id = CatalystId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ThinFilmCatalyst(Catalyst):
    """
    Catalyst type. Core properties of a thin film.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ThinFilmCatalyst")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ThinFilmCatalyst"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ThinFilmCatalyst

    id: Union[str, ThinFilmCatalystId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ThinFilmCatalystId):
            self.id = ThinFilmCatalystId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PowderCatalyst(Catalyst):
    """
    Catalyst type. Core properties of a powder catalyst.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/PowderCatalyst")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "PowderCatalyst"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.PowderCatalyst

    id: Union[str, PowderCatalystId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PowderCatalystId):
            self.id = PowderCatalystId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Recipe(NamedEntity):
    """
    A detailed set of instructions outlining the materials, quantities, and procedures required to perform a specific
    chemical reaction or experimental process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Recipe")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Recipe"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Recipe

    id: Union[str, RecipeId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RecipeId):
            self.id = RecipeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Mixture(NamedEntity):
    """
    A combination of two or more substances that are mixed together, which may retain their individual properties or
    interact chemically.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Mixture")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Mixture"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Mixture

    id: Union[str, MixtureId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MixtureId):
            self.id = MixtureId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Workflow(NamedEntity):
    """
    A structured sequence of tasks, activities, or processes designed to accomplish a specific research objective or
    experimental goal.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Workflow")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Workflow"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Workflow

    id: Union[str, WorkflowId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, WorkflowId):
            self.id = WorkflowId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Process(NamedEntity):
    """
    A defined series of actions, steps, or operations undertaken to achieve a specific scientific or experimental
    outcome (e.g. atomic layer deposition).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Process")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Process"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Process

    id: Union[str, ProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ProcessId):
            self.id = ProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SynthesisProcess(Process):
    """
    A defined series of actions, steps, or operations undertaken to achieve a synthesis process. Update this
    definition.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/SynthesisProcess")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SynthesisProcess"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SynthesisProcess

    id: Union[str, SynthesisProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SynthesisProcessId):
            self.id = SynthesisProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CleaningProcess(Process):
    """
    A defined series of actions, steps, or operations undertaken to achieve a  cleaning process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CleaningProcess")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CleaningProcess"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CleaningProcess

    id: Union[str, CleaningProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CleaningProcessId):
            self.id = CleaningProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CharacterizationProcess(Process):
    """
    A defined series of actions, steps, or operations undertaken to achieve a  analysis of a Catalysis sample process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CharacterizationProcess")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CharacterizationProcess"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CharacterizationProcess

    id: Union[str, CharacterizationProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CharacterizationProcessId):
            self.id = CharacterizationProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalyticActivityAssesmentProcess(Process):
    """
    A defined series of actions, steps, or operations undertaken to achieve a  analysis of a Catalysis sample process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CatalyticActivityAssesmentProcess")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CatalyticActivityAssesmentProcess"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CatalyticActivityAssesmentProcess

    id: Union[str, CatalyticActivityAssesmentProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CatalyticActivityAssesmentProcessId):
            self.id = CatalyticActivityAssesmentProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AnalyticsProcess(Process):
    """
    A defined series of actions, steps, or operations undertaken to achieve a  analysis of a Catalysis sample process.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/AnalyticsProcess")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "AnalyticsProcess"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.AnalyticsProcess

    id: Union[str, AnalyticsProcessId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AnalyticsProcessId):
            self.id = AnalyticsProcessId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class OzoneCleaning(CleaningProcess):
    """
    Surface treatment technique used in thin-film catalysis, especially for preparing or regenerating catalyst
    surfaces. It involves using ozone (O₃), a highly reactive form of oxygen, to clean and modify the surface
    properties of thin films.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/OzoneCleaning")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "OzoneCleaning"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.OzoneCleaning

    id: Union[str, OzoneCleaningId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, OzoneCleaningId):
            self.id = OzoneCleaningId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALD(SynthesisProcess):
    """
    Atomic Layer Deposition (ALD) is a thin-film deposition technique that enables precise control over film thickness
    at the atomic level. This method is highly valued for its ability to deposit ultra-thin, conformal films with
    excellent uniformity, even on complex 3D surfaces.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ALD")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ALD"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ALD

    id: Union[str, ALDId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ALDId):
            self.id = ALDId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ALDBeneQ(ALD):
    """
    Atomic Layer Deposition (ALD) performed in BeneQ device.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ALDBeneQ")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ALD_BeneQ"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ALDBeneQ

    id: Union[str, ALDBeneQId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ALDBeneQId):
            self.id = ALDBeneQId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CVD(SynthesisProcess):
    """
    Chemical Vapor Deposition (CVD) is a process used to produce thin films and coatings by depositing material onto a
    substrate through chemical reactions of vapor-phase precursors.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CVD")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CVD"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CVD

    id: Union[str, CVDId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CVDId):
            self.id = CVDId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CVDNanofab(CVD):
    """
    Chemical Vapor Deposition (CVD) performed in the Nanofab chamber from the Oxford Cluster.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CVDNanofab")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CVD_nanofab"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CVDNanofab

    id: Union[str, CVDNanofabId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CVDNanofabId):
            self.id = CVDNanofabId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CVDPc1(CVD):
    """
    Chemical Vapor Deposition (CVD) performed in the pc1 chamber from the von Adenne cluster.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CVDPc1")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CVD_pc1"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CVDPc1

    id: Union[str, CVDPc1Id] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CVDPc1Id):
            self.id = CVDPc1Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CVDPc2(CVD):
    """
    Chemical Vapor Deposition (CVD) performed in the pc2 chamber from the von Adenne cluster.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CVDPc2")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CVD_pc2"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CVDPc2

    id: Union[str, CVDPc2Id] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CVDPc2Id):
            self.id = CVDPc2Id(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Sputtering(SynthesisProcess):
    """
    Physical vapor deposition (PVD) technique used to deposit thin films onto a substrate. In sputtering, high-energy
    ions (usually from a plasma) bombard a target material, causing atoms from the target to be ejected. These ejected
    atoms then travel through a vacuum chamber and settle on a substrate, forming a thin film.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Sputtering")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Sputtering"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Sputtering

    id: Union[str, SputteringId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SputteringId):
            self.id = SputteringId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SputteringPrevac(Sputtering):
    """
    Physical vapor deposition (PVD) technique used to deposit thin films onto a substrate, particularly with the
    Prevac sputtering machine. In sputtering, high-energy ions (usually from a plasma) bombard a target material,
    causing atoms from the target to be ejected. These ejected atoms then travel through a vacuum chamber and settle
    on a substrate, forming a thin film.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/SputteringPrevac")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Sputtering_prevac"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SputteringPrevac

    id: Union[str, SputteringPrevacId] = None
    sputtering_prevac_id: Optional[str] = None
    substrate_id: Optional[str] = None
    sample_owner: Optional[str] = None
    process_user: Optional[str] = None
    date: Optional[str] = None
    holder: Optional[str] = None
    notes: Optional[str] = None
    step_number: Optional[int] = None
    orientation: Optional[str] = None
    sputter_pressure: Optional[float] = None
    substrate_temperature: Optional[float] = None
    ramp: Optional[float] = None
    rotation: Optional[float] = None
    z_position: Optional[float] = None
    gas: Optional[str] = None
    flow_rate: Optional[float] = None
    target_position: Optional[int] = None
    target: Optional[str] = None
    target_power: Optional[float] = None
    DC_RF: Optional[str] = None
    time: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SputteringPrevacId):
            self.id = SputteringPrevacId(self.id)

        if self.sputtering_prevac_id is not None and not isinstance(self.sputtering_prevac_id, str):
            self.sputtering_prevac_id = str(self.sputtering_prevac_id)

        if self.substrate_id is not None and not isinstance(self.substrate_id, str):
            self.substrate_id = str(self.substrate_id)

        if self.sample_owner is not None and not isinstance(self.sample_owner, str):
            self.sample_owner = str(self.sample_owner)

        if self.process_user is not None and not isinstance(self.process_user, str):
            self.process_user = str(self.process_user)

        if self.date is not None and not isinstance(self.date, str):
            self.date = str(self.date)

        if self.holder is not None and not isinstance(self.holder, str):
            self.holder = str(self.holder)

        if self.notes is not None and not isinstance(self.notes, str):
            self.notes = str(self.notes)

        if self.step_number is not None and not isinstance(self.step_number, int):
            self.step_number = int(self.step_number)

        if self.orientation is not None and not isinstance(self.orientation, str):
            self.orientation = str(self.orientation)

        if self.sputter_pressure is not None and not isinstance(self.sputter_pressure, float):
            self.sputter_pressure = float(self.sputter_pressure)

        if self.substrate_temperature is not None and not isinstance(self.substrate_temperature, float):
            self.substrate_temperature = float(self.substrate_temperature)

        if self.ramp is not None and not isinstance(self.ramp, float):
            self.ramp = float(self.ramp)

        if self.rotation is not None and not isinstance(self.rotation, float):
            self.rotation = float(self.rotation)

        if self.z_position is not None and not isinstance(self.z_position, float):
            self.z_position = float(self.z_position)

        if self.gas is not None and not isinstance(self.gas, str):
            self.gas = str(self.gas)

        if self.flow_rate is not None and not isinstance(self.flow_rate, float):
            self.flow_rate = float(self.flow_rate)

        if self.target_position is not None and not isinstance(self.target_position, int):
            self.target_position = int(self.target_position)

        if self.target is not None and not isinstance(self.target, str):
            self.target = str(self.target)

        if self.target_power is not None and not isinstance(self.target_power, float):
            self.target_power = float(self.target_power)

        if self.DC_RF is not None and not isinstance(self.DC_RF, str):
            self.DC_RF = str(self.DC_RF)

        if self.time is not None and not isinstance(self.time, str):
            self.time = str(self.time)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SputteringVonAdenne(Sputtering):
    """
    Physical vapor deposition (PVD) technique used to deposit thin films onto a substrate, particularly with the von
    Adenne (PC3 chamber) machine.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/SputteringVonAdenne")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "sputtering_vonAdenne"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SputteringVonAdenne

    id: Union[str, SputteringVonAdenneId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SputteringVonAdenneId):
            self.id = SputteringVonAdenneId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Experiment(NamedEntity):
    """
    A systematic investigation designed to test hypotheses, gather data, or explore scientific principles through
    controlled conditions.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Experiment")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Experiment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Experiment

    id: Union[str, ExperimentId] = None
    experiment_id: Optional[str] = None
    experiment_name: Optional[str] = None
    performed_by: Optional[Union[str, ScientistId]] = None
    related_project: Optional[Union[str, ProjectId]] = None
    catalyst: Optional[Union[str, CatalystId]] = None
    sample: Optional[Union[str, SampleId]] = None
    reaction: Optional[Union[str, ReactionId]] = None
    start_date: Optional[str] = None
    end_date: Optional[str] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ExperimentId):
            self.id = ExperimentId(self.id)

        if self.experiment_id is not None and not isinstance(self.experiment_id, str):
            self.experiment_id = str(self.experiment_id)

        if self.experiment_name is not None and not isinstance(self.experiment_name, str):
            self.experiment_name = str(self.experiment_name)

        if self.performed_by is not None and not isinstance(self.performed_by, ScientistId):
            self.performed_by = ScientistId(self.performed_by)

        if self.related_project is not None and not isinstance(self.related_project, ProjectId):
            self.related_project = ProjectId(self.related_project)

        if self.catalyst is not None and not isinstance(self.catalyst, CatalystId):
            self.catalyst = CatalystId(self.catalyst)

        if self.sample is not None and not isinstance(self.sample, SampleId):
            self.sample = SampleId(self.sample)

        if self.reaction is not None and not isinstance(self.reaction, ReactionId):
            self.reaction = ReactionId(self.reaction)

        if self.start_date is not None and not isinstance(self.start_date, str):
            self.start_date = str(self.start_date)

        if self.end_date is not None and not isinstance(self.end_date, str):
            self.end_date = str(self.end_date)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Measurement(NamedEntity):
    """
    Storing and describing measurements to perform on a sample.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Measurement")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Measurement"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Measurement

    id: Union[str, MeasurementId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MeasurementId):
            self.id = MeasurementId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Parameter(NamedEntity):
    """
    Associates parameters on demand to a certain experiment or measurement.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Parameter")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Parameter"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Parameter

    id: Union[str, ParameterId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ParameterId):
            self.id = ParameterId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reaction(NamedEntity):
    """
    A chemical process in which one or more substances (reactants) undergo transformation to produce new substances
    (products).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Reaction")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reaction"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Reaction

    id: Union[str, ReactionId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionId):
            self.id = ReactionId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactionProduct(NamedEntity):
    """
    A substance formed as a result of a chemical reaction, representing the end products generated from the
    transformation of reactants.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ReactionProduct")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReactionProduct"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ReactionProduct

    id: Union[str, ReactionProductId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactionProductId):
            self.id = ReactionProductId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Reactor(NamedEntity):
    """
    Equipment designed to facilitate and control chemical reactions under specified conditions, such as temperature,
    pressure, and flow rates.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/Reactor")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Reactor"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Reactor

    id: Union[str, ReactorId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ReactorId):
            self.id = ReactorId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class CatalysisSampleCollection(YAMLRoot):
    """
    A holder for CatalysisSample objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/CatalysisSampleCollection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "CatalysisSampleCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.CatalysisSampleCollection

    entries: Optional[Union[Dict[Union[str, CatalysisSampleId], Union[dict, CatalysisSample]], List[Union[dict, CatalysisSample]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=CatalysisSample, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ReactionProductCollection(YAMLRoot):
    """
    A holder for ReactionProduct objects
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/catlabs/ReactionProductCollection")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "ReactionProductCollection"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.ReactionProductCollection

    entries: Optional[Union[Dict[Union[str, ReactionProductId], Union[dict, ReactionProduct]], List[Union[dict, ReactionProduct]]]] = empty_dict()

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        self._normalize_inlined_as_dict(slot_name="entries", slot_type=ReactionProduct, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Beamline(NamedEntity):
    """
    System within a facility designed to direct a beam of radiation toward a sample for the purpose of analysis or
    experimentation.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/Beamline")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "Beamline"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.Beamline

    id: Union[str, BeamlineId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineId):
            self.id = BeamlineId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BeamlineExperiment(Experiment):
    """
    An experimental investigation conducted using a beamline.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/BeamlineExperiment")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BeamlineExperiment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.BeamlineExperiment

    id: Union[str, BeamlineExperimentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineExperimentId):
            self.id = BeamlineExperimentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class BeamlineScientist(Person):
    """
    An expert responsible for the operation and scientific application of beamlines  in a research facility.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/BeamlineScientist")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "BeamlineScientist"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.BeamlineScientist

    id: Union[str, BeamlineScientistId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BeamlineScientistId):
            self.id = BeamlineScientistId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class MySpot(Beamline):
    """
    Myspot beamline description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/MySpot")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "mySpot"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.MySpot

    id: Union[str, MySpotId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, MySpotId):
            self.id = MySpotId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EMILPink(Beamline):
    """
    Pink beamline description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/EMILPink")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMIL_Pink"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.EMILPink

    id: Union[str, EMILPinkId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EMILPinkId):
            self.id = EMILPinkId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EMILOAESE(Beamline):
    """
    OAESE beamline description.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/BESSY/EMILOAESE")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EMIL_OAESE"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.EMILOAESE

    id: Union[str, EMILOAESEId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EMILOAESEId):
            self.id = EMILOAESEId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SampleEnvironment(NamedEntity):
    """
    Controlled environment in which the sample is studied (operando research).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/SampleEnvironment")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SampleEnvironment"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SampleEnvironment

    id: Union[str, SampleEnvironmentId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SampleEnvironmentId):
            self.id = SampleEnvironmentId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class EnvironmentDynamics(NamedEntity):
    """
    Dynamic or time-resolved environmental conditions during an  experiment (e.g.for in-situ measurements).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/EnvironmentDynamics")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "EnvironmentDynamics"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.EnvironmentDynamics

    id: Union[str, EnvironmentDynamicsId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, EnvironmentDynamicsId):
            self.id = EnvironmentDynamicsId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SamplePositioning(NamedEntity):
    """
    The arrangement or location of samples within an experimental setup, critical for ensuring accurate data
    collection and analysis.
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/SamplePositioning")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "SamplePositioning"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.SamplePositioning

    id: Union[str, SamplePositioningId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SamplePositioningId):
            self.id = SamplePositioningId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class File(NamedEntity):
    """
    Stores data related to the experiment (e.g. images, videos, or other files).
    """
    _inherited_slots: ClassVar[List[str]] = []

    class_class_uri: ClassVar[URIRef] = URIRef("https://w3id.org/anak-velazquez/operandoCatalysis/File")
    class_class_curie: ClassVar[str] = None
    class_name: ClassVar[str] = "File"
    class_model_uri: ClassVar[URIRef] = HZB_METADATA_SCHEMA.File

    id: Union[str, FileId] = None

    def __post_init__(self, *_: List[str], **kwargs: Dict[str, Any]):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FileId):
            self.id = FileId(self.id)

        super().__post_init__(**kwargs)


# Enumerations
class PersonStatus(EnumDefinitionImpl):

    ALIVE = PermissibleValue(
        text="ALIVE",
        description="the person is living",
        meaning=PATO["0001421"])
    DEAD = PermissibleValue(
        text="DEAD",
        description="the person is deceased",
        meaning=PATO["0001422"])
    UNKNOWN = PermissibleValue(
        text="UNKNOWN",
        description="the vital status is not known")

    _defn = EnumDefinition(
        name="PersonStatus",
    )

class GenderEnum(EnumDefinitionImpl):

    Woman = PermissibleValue(
        text="Woman",
        description="identified as woman",
        meaning=GSSO["000369"])
    Masculine = PermissibleValue(
        text="Masculine",
        description="masculine")
    Diverse = PermissibleValue(
        text="Diverse",
        description="other")

    _defn = EnumDefinition(
        name="GenderEnum",
    )

# Slots
class slots:
    pass

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=HZB_METADATA_SCHEMA.id, domain=None, range=URIRef)

slots.iri = Slot(uri="str(uriorcurie)", name="iri", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.iri, domain=None, range=Optional[str])

slots.category = Slot(uri="str(uriorcurie)", name="category", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.category, domain=None, range=Optional[str])

slots.name = Slot(uri=SCHEMA.name, name="name", curie=SCHEMA.curie('name'),
                   model_uri=HZB_METADATA_SCHEMA.name, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=HZB_METADATA_SCHEMA.description, domain=None, range=Optional[str])

slots.primary_email = Slot(uri=SCHEMA.email, name="primary_email", curie=SCHEMA.curie('email'),
                   model_uri=HZB_METADATA_SCHEMA.primary_email, domain=None, range=Optional[str])

slots.birth_date = Slot(uri=SCHEMA.birthDate, name="birth_date", curie=SCHEMA.curie('birthDate'),
                   model_uri=HZB_METADATA_SCHEMA.birth_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.age_in_years = Slot(uri="str(uriorcurie)", name="age_in_years", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.age_in_years, domain=None, range=Optional[int])

slots.vital_status = Slot(uri="str(uriorcurie)", name="vital_status", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.vital_status, domain=None, range=Optional[Union[str, "PersonStatus"]])

slots.gender = Slot(uri=SCHEMA.gender, name="gender", curie=SCHEMA.curie('gender'),
                   model_uri=HZB_METADATA_SCHEMA.gender, domain=None, range=Optional[Union[str, "GenderEnum"]])

slots.has_employment_history = Slot(uri="str(uriorcurie)", name="has_employment_history", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.has_employment_history, domain=None, range=Optional[Union[str, List[str]]])

slots.current_address = Slot(uri="str(uriorcurie)", name="current_address", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.current_address, domain=None, range=Optional[str])

slots.dataCite__identifier = Slot(uri="str(uriorcurie)", name="dataCite__identifier", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__identifier, domain=None, range=Optional[str])

slots.dataCite__identifierType = Slot(uri="str(uriorcurie)", name="dataCite__identifierType", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__identifierType, domain=None, range=Optional[str])

slots.dataCite__creators = Slot(uri="str(uriorcurie)", name="dataCite__creators", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__creators, domain=None, range=Optional[Union[str, PersonId]])

slots.dataCite__title = Slot(uri="str(uriorcurie)", name="dataCite__title", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__title, domain=None, range=Optional[str])

slots.dataCite__Publisher = Slot(uri="str(uriorcurie)", name="dataCite__Publisher", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Publisher, domain=None, range=Optional[str])

slots.dataCite__ResourceType = Slot(uri="str(uriorcurie)", name="dataCite__ResourceType", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__ResourceType, domain=None, range=Optional[str])

slots.dataCite__Subject = Slot(uri="str(uriorcurie)", name="dataCite__Subject", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Subject, domain=None, range=Optional[str])

slots.dataCite__Contributor = Slot(uri="str(uriorcurie)", name="dataCite__Contributor", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Contributor, domain=None, range=Optional[str])

slots.dataCite__Date = Slot(uri="str(uriorcurie)", name="dataCite__Date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Date, domain=None, range=Optional[str])

slots.dataCite__Language = Slot(uri="str(uriorcurie)", name="dataCite__Language", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Language, domain=None, range=Optional[str])

slots.dataCite__AlternateIdentifier = Slot(uri="str(uriorcurie)", name="dataCite__AlternateIdentifier", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__AlternateIdentifier, domain=None, range=Optional[str])

slots.dataCite__RelatedIdentifier = Slot(uri="str(uriorcurie)", name="dataCite__RelatedIdentifier", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__RelatedIdentifier, domain=None, range=Optional[str])

slots.dataCite__Size = Slot(uri="str(uriorcurie)", name="dataCite__Size", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Size, domain=None, range=Optional[str])

slots.dataCite__Format = Slot(uri="str(uriorcurie)", name="dataCite__Format", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Format, domain=None, range=Optional[str])

slots.dataCite__Version = Slot(uri="str(uriorcurie)", name="dataCite__Version", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Version, domain=None, range=Optional[str])

slots.dataCite__Rights = Slot(uri="str(uriorcurie)", name="dataCite__Rights", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Rights, domain=None, range=Optional[str])

slots.dataCite__Description = Slot(uri="str(uriorcurie)", name="dataCite__Description", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__Description, domain=None, range=Optional[str])

slots.dataCite__GeoLocation = Slot(uri="str(uriorcurie)", name="dataCite__GeoLocation", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__GeoLocation, domain=None, range=Optional[str])

slots.dataCite__FundingReference = Slot(uri="str(uriorcurie)", name="dataCite__FundingReference", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__FundingReference, domain=None, range=Optional[str])

slots.dataCite__RelatedItem = Slot(uri="str(uriorcurie)", name="dataCite__RelatedItem", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.dataCite__RelatedItem, domain=None, range=Optional[str])

slots.person__person_id = Slot(uri="str(uriorcurie)", name="person__person_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__person_id, domain=None, range=Optional[str])

slots.person__orcid_id = Slot(uri="str(uriorcurie)", name="person__orcid_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__orcid_id, domain=None, range=Optional[str])

slots.person__first_name = Slot(uri="str(uriorcurie)", name="person__first_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__first_name, domain=None, range=Optional[str])

slots.person__last_name = Slot(uri="str(uriorcurie)", name="person__last_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__last_name, domain=None, range=Optional[str])

slots.person__title = Slot(uri="str(uriorcurie)", name="person__title", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__title, domain=None, range=Optional[str])

slots.person__institution = Slot(uri="str(uriorcurie)", name="person__institution", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__institution, domain=None, range=Optional[str])

slots.person__department = Slot(uri="str(uriorcurie)", name="person__department", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__department, domain=None, range=Optional[str])

slots.person__role = Slot(uri="str(uriorcurie)", name="person__role", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__role, domain=None, range=Optional[str])

slots.person__research_focus = Slot(uri="str(uriorcurie)", name="person__research_focus", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__research_focus, domain=None, range=Optional[str])

slots.person__laboratory_name = Slot(uri="str(uriorcurie)", name="person__laboratory_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__laboratory_name, domain=None, range=Optional[str])

slots.person__projects = Slot(uri="str(uriorcurie)", name="person__projects", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.person__projects, domain=None, range=Optional[Union[Union[str, ProjectId], List[Union[str, ProjectId]]]])

slots.project__project_id = Slot(uri="str(uriorcurie)", name="project__project_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__project_id, domain=None, range=Optional[str])

slots.project__project_code = Slot(uri="str(uriorcurie)", name="project__project_code", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__project_code, domain=None, range=Optional[str])

slots.project__project_name = Slot(uri="str(uriorcurie)", name="project__project_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__project_name, domain=None, range=Optional[str])

slots.project__acronym = Slot(uri="str(uriorcurie)", name="project__acronym", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__acronym, domain=None, range=Optional[str])

slots.project__start_date = Slot(uri="str(uriorcurie)", name="project__start_date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__start_date, domain=None, range=Optional[str])

slots.project__end_date = Slot(uri="str(uriorcurie)", name="project__end_date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__end_date, domain=None, range=Optional[str])

slots.project__status = Slot(uri="str(uriorcurie)", name="project__status", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__status, domain=None, range=Optional[str])

slots.project__institutions = Slot(uri="str(uriorcurie)", name="project__institutions", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__institutions, domain=None, range=Optional[str])

slots.project__principal_investigator = Slot(uri="str(uriorcurie)", name="project__principal_investigator", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__principal_investigator, domain=None, range=Optional[Union[str, ScientistId]])

slots.project__assigned_lab = Slot(uri="str(uriorcurie)", name="project__assigned_lab", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__assigned_lab, domain=None, range=Optional[str])

slots.project__research_area = Slot(uri="str(uriorcurie)", name="project__research_area", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__research_area, domain=None, range=Optional[str])

slots.project__collaborators = Slot(uri="str(uriorcurie)", name="project__collaborators", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.project__collaborators, domain=None, range=Optional[Union[Union[str, PersonId], List[Union[str, PersonId]]]])

slots.device__device_id = Slot(uri="str(uriorcurie)", name="device__device_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__device_id, domain=None, range=Optional[str])

slots.device__serial_number = Slot(uri="str(uriorcurie)", name="device__serial_number", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__serial_number, domain=None, range=Optional[str])

slots.device__device_name = Slot(uri="str(uriorcurie)", name="device__device_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__device_name, domain=None, range=Optional[str])

slots.device__device_type = Slot(uri="str(uriorcurie)", name="device__device_type", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__device_type, domain=None, range=Optional[str])

slots.device__manufacturer = Slot(uri="str(uriorcurie)", name="device__manufacturer", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__manufacturer, domain=None, range=Optional[str])

slots.device__model_number = Slot(uri="str(uriorcurie)", name="device__model_number", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__model_number, domain=None, range=Optional[str])

slots.device__purchase_date = Slot(uri="str(uriorcurie)", name="device__purchase_date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__purchase_date, domain=None, range=Optional[str])

slots.device__commission_date = Slot(uri="str(uriorcurie)", name="device__commission_date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__commission_date, domain=None, range=Optional[str])

slots.device__warranty_expiration_date = Slot(uri="str(uriorcurie)", name="device__warranty_expiration_date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__warranty_expiration_date, domain=None, range=Optional[str])

slots.device__operating_system = Slot(uri="str(uriorcurie)", name="device__operating_system", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__operating_system, domain=None, range=Optional[str])

slots.device__specifications = Slot(uri="str(uriorcurie)", name="device__specifications", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__specifications, domain=None, range=Optional[str])

slots.device__input_gases = Slot(uri="str(uriorcurie)", name="device__input_gases", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__input_gases, domain=None, range=Optional[str])

slots.device__catalyst_handling_capability = Slot(uri="str(uriorcurie)", name="device__catalyst_handling_capability", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__catalyst_handling_capability, domain=None, range=Optional[str])

slots.device__ip_address = Slot(uri="str(uriorcurie)", name="device__ip_address", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__ip_address, domain=None, range=Optional[str])

slots.device__mac_address = Slot(uri="str(uriorcurie)", name="device__mac_address", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__mac_address, domain=None, range=Optional[str])

slots.device__location = Slot(uri="str(uriorcurie)", name="device__location", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__location, domain=None, range=Optional[str])

slots.device__responsible_person = Slot(uri="str(uriorcurie)", name="device__responsible_person", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__responsible_person, domain=None, range=Optional[str])

slots.device__device_status = Slot(uri="str(uriorcurie)", name="device__device_status", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__device_status, domain=None, range=Optional[str])

slots.device__ownership = Slot(uri="str(uriorcurie)", name="device__ownership", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.device__ownership, domain=None, range=Optional[str])

slots.sample__sample_id = Slot(uri="str(uriorcurie)", name="sample__sample_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__sample_id, domain=None, range=Optional[str])

slots.sample__sample_name = Slot(uri="str(uriorcurie)", name="sample__sample_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__sample_name, domain=None, range=Optional[str])

slots.sample__sample_description = Slot(uri="str(uriorcurie)", name="sample__sample_description", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__sample_description, domain=None, range=Optional[str])

slots.sample__phase = Slot(uri="str(uriorcurie)", name="sample__phase", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__phase, domain=None, range=Optional[str])

slots.sample__composition = Slot(uri="str(uriorcurie)", name="sample__composition", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__composition, domain=None, range=Optional[str])

slots.sample__size = Slot(uri="str(uriorcurie)", name="sample__size", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__size, domain=None, range=Optional[str])

slots.sample__preparation_method = Slot(uri="str(uriorcurie)", name="sample__preparation_method", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__preparation_method, domain=None, range=Optional[str])

slots.sample__batch_number = Slot(uri="str(uriorcurie)", name="sample__batch_number", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sample__batch_number, domain=None, range=Optional[str])

slots.sampleCollection__entries = Slot(uri="str(uriorcurie)", name="sampleCollection__entries", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, SampleId], Union[dict, Sample]], List[Union[dict, Sample]]]])

slots.catalysisSample__sample_ELN_id = Slot(uri="str(uriorcurie)", name="catalysisSample__sample_ELN_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__sample_ELN_id, domain=None, range=Optional[str])

slots.catalysisSample__eln_name = Slot(uri="str(uriorcurie)", name="catalysisSample__eln_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__eln_name, domain=None, range=Optional[str])

slots.catalysisSample__creator_name = Slot(uri="str(uriorcurie)", name="catalysisSample__creator_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__creator_name, domain=None, range=Optional[str])

slots.catalysisSample__creator_institution = Slot(uri="str(uriorcurie)", name="catalysisSample__creator_institution", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__creator_institution, domain=None, range=Optional[str])

slots.catalysisSample__creator_role = Slot(uri="str(uriorcurie)", name="catalysisSample__creator_role", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__creator_role, domain=None, range=Optional[str])

slots.catalysisSample__laboratory_name = Slot(uri="str(uriorcurie)", name="catalysisSample__laboratory_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__laboratory_name, domain=None, range=Optional[str])

slots.catalysisSample__project_sample = Slot(uri="str(uriorcurie)", name="catalysisSample__project_sample", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__project_sample, domain=None, range=Optional[Union[str, ProjectId]])

slots.catalysisSample__institution_name = Slot(uri="str(uriorcurie)", name="catalysisSample__institution_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__institution_name, domain=None, range=Optional[str])

slots.catalysisSample__institution_abbreviation = Slot(uri="str(uriorcurie)", name="catalysisSample__institution_abbreviation", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__institution_abbreviation, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_type = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_type", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_type, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_phase = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_phase", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_phase, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_form = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_form", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_form, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_name = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_name, domain=None, range=Optional[str])

slots.catalysisSample__chemical__formula = Slot(uri="str(uriorcurie)", name="catalysisSample__chemical__formula", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__chemical__formula, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_components = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_components", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_components, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_structure = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_structure", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_structure, domain=None, range=Optional[str])

slots.catalysisSample__active_site = Slot(uri="str(uriorcurie)", name="catalysisSample__active_site", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__active_site, domain=None, range=Optional[str])

slots.catalysisSample__support = Slot(uri="str(uriorcurie)", name="catalysisSample__support", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__support, domain=None, range=Optional[str])

slots.catalysisSample__loading = Slot(uri="str(uriorcurie)", name="catalysisSample__loading", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__loading, domain=None, range=Optional[str])

slots.catalysisSample__purity = Slot(uri="str(uriorcurie)", name="catalysisSample__purity", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__purity, domain=None, range=Optional[str])

slots.catalysisSample__synthesis_method = Slot(uri="str(uriorcurie)", name="catalysisSample__synthesis_method", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__synthesis_method, domain=None, range=Optional[str])

slots.catalysisSample__characterization_method = Slot(uri="str(uriorcurie)", name="catalysisSample__characterization_method", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__characterization_method, domain=None, range=Optional[str])

slots.catalysisSample__surface_area = Slot(uri="str(uriorcurie)", name="catalysisSample__surface_area", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__surface_area, domain=None, range=Optional[str])

slots.catalysisSample__particle_size = Slot(uri="str(uriorcurie)", name="catalysisSample__particle_size", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__particle_size, domain=None, range=Optional[str])

slots.catalysisSample__morphology = Slot(uri="str(uriorcurie)", name="catalysisSample__morphology", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__morphology, domain=None, range=Optional[str])

slots.catalysisSample__pore_size_distribution = Slot(uri="str(uriorcurie)", name="catalysisSample__pore_size_distribution", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__pore_size_distribution, domain=None, range=Optional[str])

slots.catalysisSample__crystalline_structure = Slot(uri="str(uriorcurie)", name="catalysisSample__crystalline_structure", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__crystalline_structure, domain=None, range=Optional[str])

slots.catalysisSample__chemical_composition = Slot(uri="str(uriorcurie)", name="catalysisSample__chemical_composition", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__chemical_composition, domain=None, range=Optional[str])

slots.catalysisSample__surface_chemistry = Slot(uri="str(uriorcurie)", name="catalysisSample__surface_chemistry", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__surface_chemistry, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_stability = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_stability", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_stability, domain=None, range=Optional[str])

slots.catalysisSample__catalyst_activity = Slot(uri="str(uriorcurie)", name="catalysisSample__catalyst_activity", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSample__catalyst_activity, domain=None, range=Optional[str])

slots.sputteringPrevac__sputtering_prevac_id = Slot(uri="str(uriorcurie)", name="sputteringPrevac__sputtering_prevac_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__sputtering_prevac_id, domain=None, range=Optional[str])

slots.sputteringPrevac__substrate_id = Slot(uri="str(uriorcurie)", name="sputteringPrevac__substrate_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__substrate_id, domain=None, range=Optional[str])

slots.sputteringPrevac__sample_owner = Slot(uri="str(uriorcurie)", name="sputteringPrevac__sample_owner", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__sample_owner, domain=None, range=Optional[str])

slots.sputteringPrevac__process_user = Slot(uri="str(uriorcurie)", name="sputteringPrevac__process_user", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__process_user, domain=None, range=Optional[str])

slots.sputteringPrevac__date = Slot(uri="str(uriorcurie)", name="sputteringPrevac__date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__date, domain=None, range=Optional[str])

slots.sputteringPrevac__holder = Slot(uri="str(uriorcurie)", name="sputteringPrevac__holder", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__holder, domain=None, range=Optional[str])

slots.sputteringPrevac__notes = Slot(uri="str(uriorcurie)", name="sputteringPrevac__notes", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__notes, domain=None, range=Optional[str])

slots.sputteringPrevac__step_number = Slot(uri="str(uriorcurie)", name="sputteringPrevac__step_number", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__step_number, domain=None, range=Optional[int])

slots.sputteringPrevac__orientation = Slot(uri="str(uriorcurie)", name="sputteringPrevac__orientation", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__orientation, domain=None, range=Optional[str])

slots.sputteringPrevac__sputter_pressure = Slot(uri="str(uriorcurie)", name="sputteringPrevac__sputter_pressure", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__sputter_pressure, domain=None, range=Optional[float])

slots.sputteringPrevac__substrate_temperature = Slot(uri="str(uriorcurie)", name="sputteringPrevac__substrate_temperature", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__substrate_temperature, domain=None, range=Optional[float])

slots.sputteringPrevac__ramp = Slot(uri="str(uriorcurie)", name="sputteringPrevac__ramp", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__ramp, domain=None, range=Optional[float])

slots.sputteringPrevac__rotation = Slot(uri="str(uriorcurie)", name="sputteringPrevac__rotation", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__rotation, domain=None, range=Optional[float])

slots.sputteringPrevac__z_position = Slot(uri="str(uriorcurie)", name="sputteringPrevac__z_position", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__z_position, domain=None, range=Optional[float])

slots.sputteringPrevac__gas = Slot(uri="str(uriorcurie)", name="sputteringPrevac__gas", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__gas, domain=None, range=Optional[str])

slots.sputteringPrevac__flow_rate = Slot(uri="str(uriorcurie)", name="sputteringPrevac__flow_rate", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__flow_rate, domain=None, range=Optional[float])

slots.sputteringPrevac__target_position = Slot(uri="str(uriorcurie)", name="sputteringPrevac__target_position", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__target_position, domain=None, range=Optional[int])

slots.sputteringPrevac__target = Slot(uri="str(uriorcurie)", name="sputteringPrevac__target", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__target, domain=None, range=Optional[str])

slots.sputteringPrevac__target_power = Slot(uri="str(uriorcurie)", name="sputteringPrevac__target_power", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__target_power, domain=None, range=Optional[float])

slots.sputteringPrevac__DC_RF = Slot(uri="str(uriorcurie)", name="sputteringPrevac__DC_RF", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__DC_RF, domain=None, range=Optional[str])

slots.sputteringPrevac__time = Slot(uri="str(uriorcurie)", name="sputteringPrevac__time", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.sputteringPrevac__time, domain=None, range=Optional[str])

slots.experiment__experiment_id = Slot(uri="str(uriorcurie)", name="experiment__experiment_id", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__experiment_id, domain=None, range=Optional[str])

slots.experiment__experiment_name = Slot(uri="str(uriorcurie)", name="experiment__experiment_name", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__experiment_name, domain=None, range=Optional[str])

slots.experiment__performed_by = Slot(uri="str(uriorcurie)", name="experiment__performed_by", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__performed_by, domain=None, range=Optional[Union[str, ScientistId]])

slots.experiment__related_project = Slot(uri="str(uriorcurie)", name="experiment__related_project", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__related_project, domain=None, range=Optional[Union[str, ProjectId]])

slots.experiment__catalyst = Slot(uri="str(uriorcurie)", name="experiment__catalyst", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__catalyst, domain=None, range=Optional[Union[str, CatalystId]])

slots.experiment__sample = Slot(uri="str(uriorcurie)", name="experiment__sample", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__sample, domain=None, range=Optional[Union[str, SampleId]])

slots.experiment__reaction = Slot(uri="str(uriorcurie)", name="experiment__reaction", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__reaction, domain=None, range=Optional[Union[str, ReactionId]])

slots.experiment__start_date = Slot(uri="str(uriorcurie)", name="experiment__start_date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__start_date, domain=None, range=Optional[str])

slots.experiment__end_date = Slot(uri="str(uriorcurie)", name="experiment__end_date", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.experiment__end_date, domain=None, range=Optional[str])

slots.catalysisSampleCollection__entries = Slot(uri="str(uriorcurie)", name="catalysisSampleCollection__entries", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.catalysisSampleCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, CatalysisSampleId], Union[dict, CatalysisSample]], List[Union[dict, CatalysisSample]]]])

slots.reactionProductCollection__entries = Slot(uri="str(uriorcurie)", name="reactionProductCollection__entries", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.reactionProductCollection__entries, domain=None, range=Optional[Union[Dict[Union[str, ReactionProductId], Union[dict, ReactionProduct]], List[Union[dict, ReactionProduct]]]])

slots.NamedEntity_category = Slot(uri="str(uriorcurie)", name="NamedEntity_category", curie=None,
                   model_uri=HZB_METADATA_SCHEMA.NamedEntity_category, domain=NamedEntity, range=Optional[str])