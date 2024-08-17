from __future__ import annotations

from enum import Enum
from typing import List, Optional, Union

from pydantic import AnyUrl, AwareDatetime, BaseModel, Field, constr


class Entity(BaseModel):
    type: Optional[str] = None


class EndPoint(BaseModel):
    accept: Optional[str] = None
    uri: Optional[AnyUrl] = None


class Notification(BaseModel):
    attributes: Optional[List[str]] = None
    endPoint: Optional[EndPoint] = None
    format: Optional[str] = Field(None, description='Format of the output')


class Type(Enum):
    SubscriptionQuery = 'SubscriptionQuery'


class SubscriptionQuery(BaseModel):
    alternateName: Optional[str] = Field(
        None, description='An alternative name for this item'
    )
    csf: Optional[str] = Field(
        None,
        description='Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities. Defined in NGSI-LD standard',
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
    entities: Optional[List[Entity]] = Field(
        None,
        description='Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard',
    )
    expiresAt: Optional[str] = Field(
        None,
        description='Expiration date for the subscription. Defined in NGSI-LD standard',
    )
    geoQ: Optional[str] = Field(
        None,
        description='Geo-Query that shall be matched by Entities in order be retrieved. Defined in NGSI-LD standard',
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
    name: Optional[str] = Field(None, description='The name of this item')
    notification: Optional[Notification] = Field(
        None,
        description='Parameters of the notification for the subscription. Defined in NGSI-LD standard',
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
    q: Optional[str] = Field(
        None,
        description='Query that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard',
    )
    seeAlso: Optional[Union[List[AnyUrl], AnyUrl]] = Field(
        None, description='list of uri pointing to additional resources about the item'
    )
    source: Optional[str] = Field(
        None,
        description='A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object',
    )
    subscriptionName: Optional[str] = Field(
        None,
        description='A (short) name given to this Subscription. Defined in NGSI-LD standard',
    )
    temporalQ: Optional[str] = Field(
        None,
        description="Temporal Query to be present only for 'Query Temporal Evolution of Entities' operation. Defined in NGSI-LD standard",
    )
    throttling: Optional[str] = Field(
        None,
        description='Minimal period of time in seconds which shall elapse between two consecutive notifications. Defined in NGSI-LD standard',
    )
    type: Optional[Type] = Field(
        None,
        description="It has to be SubscriptionQuery. NGSI entity type. Enum:'SubscriptionQuery'",
    )
    watchedAttributes: Optional[List[str]] = Field(
        None,
        description='List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved. Defined in NGSI-LD standard. ',
    )
