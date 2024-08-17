from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class Type(Enum):
    MLModel = 'MLModel'


class MLModel(BaseModel):
    acceptableDataSources: Optional[List[str]] = Field(
        None,
        description='Valid type of input data sources for running the Machine Learning Model',
    )
    algorithm: Optional[str] = Field(
        None,
        description='The algorithm used by the underlying Machine Learning model (e.g. linear regression, k-means, SVM, MLP,...)',
    )
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    dataProvider: Optional[str] = Field(
        None,
        description='A sequence of characters identifying the provider of the harmonised data entity',
    )
    dateCreated: Optional[AwareDatetime] = Field(
        None,
        description='Entity creation timestamp. This will usually be allocated by the storage platform',
    )
    dateModified: Optional[AwareDatetime] = Field(
        None,
        description='Timestamp of the last modification of the entity. This will usually be allocated by the storage platform',
    )
    description: Optional[str] = Field(None, description='A description of this item')
    dockerImage: Optional[str] = Field(
        None, description='Docker image containing the Machine Learning model'
    )
    id: Optional[
        Union[
            constr(
                pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!, :\\\\]+$',
                min_length=1,
                max_length=256,
            ),
            AnyUrl,
        ]
    ] = Field(None, description='Unique identifier of the entity')
    inputAttributes: Optional[List[str]] = Field(
        None,
        description='Comma-separated list of attributes names (that should have a given type by definition)',
    )
    mlFramework: Optional[str] = Field(
        None,
        description='The Machine Learning framework that has been used to prepare the model (e.g., scikit-learn, H2O, Spark MLib, etc)',
    )
    name: Optional[str] = Field(None, description='The name of this item')
    outputAttributes: Optional[List[str]] = Field(
        None,
        description='Comma-separated list of attributes names used to publish the results',
    )
    outputDataTypes: Optional[List[str]] = Field(
        None, description='Type of output data produced by the Machine Learning Model'
    )
    owner: Optional[
        List[
            Union[
                constr(
                    pattern=r'^[\\w\\-\\.\\{\\}\\$\\+\\*\\[\\]`|~^@!,:\\\\]+$',
                    min_length=1,
                    max_length=256,
                ),
                AnyUrl,
            ]
        ]
    ] = Field(
        None,
        description='A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)',
    )
    refMLProcessing: Optional[List[AnyUrl]] = Field(None, description='')
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    type: Optional[Type] = Field(
        None, description='NGSI entity type. It has to be MLModel'
    )
    typeOfAlgorithm: Optional[str] = Field(None, description='Enumeration')
    version: Optional[str] = Field(None, description='Version of the model')
