Entidad: SubscriptionQuery  
==========================  
[Licencia abierta](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md)  
Descripción global: **Modelo de consulta para modelos de aprendizaje automático**  

## Lista de propiedades  

- `alternateName`: Un nombre alternativo para este artículo  - `csf`: Filtro de fuente de contexto al que deben ajustarse los registros de fuente de contexto que describen las fuentes de contexto que se utilizarán para recuperar las entidades. Definido en la norma NGSI-LD.  - `dataProvider`: Una secuencia de caracteres que identifica al proveedor de la entidad de datos armonizada.  - `dateCreated`: Marca de tiempo de creación de la entidad. Suele ser asignada por la plataforma de almacenamiento.  - `dateModified`: Marca de tiempo de la última modificación de la entidad. Normalmente será asignada por la plataforma de almacenamiento.  - `description`: Una descripción de este artículo  - `entities`: Id. de entidad, patrón de id. y tipos de entidad que deben coincidir con las entidades para ser recuperadas. Definido en la norma NGSI-LD.  - `expiresAt`: Fecha de caducidad de la suscripción. Definida en la norma NGSI-LD.  - `geoQ`: Geo-Query que debe ser comparada por las Entidades para ser recuperada. Definido en la norma NGSI-LD.  - `id`: Identificador único de la entidad  - `name`: El nombre de este artículo.  - `notification`: Parámetros de la notificación para la suscripción. Definidos en la norma NGSI-LD.  - `owner`: Una lista que contiene una secuencia de caracteres codificada en JSON que hace referencia a los identificadores únicos de los propietarios  - `q`: Consulta que debe ser emparejada por las Entidades para ser recuperada. Definido en la norma NGSI-LD.  - `seeAlso`: lista de uri que apuntan a recursos adicionales sobre el artículo  - `source`: Una secuencia de caracteres que indica la fuente original de los datos de la entidad en forma de URL. Se recomienda que sea el nombre de dominio completo del proveedor de origen, o la URL del objeto de origen.  - `subscriptionName`: Un nombre (corto) dado a esta Suscripción. Definido en la norma NGSI-LD.  - `temporalQ`: La consulta temporal debe estar presente sólo para la operación "Consulta de la evolución temporal de las entidades". Definido en la norma NGSI-LD.  - `throttling`: Período mínimo de tiempo en segundos que debe transcurrir entre dos notificaciones consecutivas. Definido en la norma NGSI-LD.  - `type`: Tiene que ser SubscriptionQuery. Enum:'SubscriptionQuery'  - `watchedAttributes`: Lista de Atributos que deben ser comparados por las Entidades para ser recuperados. Si no está presente, se recuperarán todos los atributos. Definido en la norma NGSI-LD.    
Propiedades requeridas  
- `id`  - `type`  ## Descripción del modelo de datos de las propiedades  
Ordenados alfabéticamente (haga clic para ver los detalles)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SubscriptionQuery:    
  description: 'Subscription Query model for Machine Learning models'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    csf:    
      description: 'Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities. Defined in NGSI-LD standard.'    
      type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: Property    
    description:    
      description: 'A description of this item'    
      type: Property    
    entities:    
      description: 'Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard.'    
      items:    
        properties:    
          type:    
            type: string    
        type: object    
      type: Property    
    expiresAt:    
      description: 'Expiration date for the subscription. Defined in NGSI-LD standard.'    
      type: Property    
    geoQ:    
      description: 'Geo-Query that shall be matched by Entities in order be retrieved. Defined in NGSI-LD standard.'    
      type: Property    
    id:    
      anyOf: &subscriptionquery_-_properties_-_owner_-_items_-_anyof    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Unique identifier of the entity'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    notification:    
      description: 'Parameters of the notification for the subscription. Defined in NGSI-LD standard.'    
      properties:    
        attributes:    
          items:    
            type: string    
          type: array    
        endPoint:    
          properties:    
            accept:    
              type: string    
            uri:    
              format: uri    
              type: string    
          type: object    
        format:    
          description: 'Property. Format of the output'    
          type: string    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *subscriptionquery_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    q:    
      description: 'Query that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard.'    
      type: Property    
    seeAlso:    
      description: 'list of uri pointing to additional resources about the item'    
      oneOf:    
        - items:    
            format: uri    
            type: string    
          minItems: 1    
          type: array    
        - format: uri    
          type: string    
      type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: Property    
    subscriptionName:    
      description: 'A (short) name given to this Subscription. Defined in NGSI-LD standard.'    
      type: Property    
    temporalQ:    
      description: 'Temporal Query to be present only for ''Query Temporal Evolution of Entities'' operation. Defined in NGSI-LD standard.'    
      type: Property    
    throttling:    
      description: 'Minimal period of time in seconds which shall elapse between two consecutive notifications. Defined in NGSI-LD standard.'    
      type: Property    
    type:    
      description: 'It has to be SubscriptionQuery. Enum:''SubscriptionQuery'''    
      enum:    
        - SubscriptionQuery    
      type: Property    
    watchedAttributes:    
      description: 'List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved. Defined in NGSI-LD standard. '    
      items:    
        type: string    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Ejemplo de carga útil  
#### SubscriptionQuery NGSI-v2 key-values Ejemplo  
Aquí hay un ejemplo de una SubscriptionQuery en formato JSON-LD como key-values. Esto es compatible con NGSI-v2 cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Subscription:01",  
  "type": "SubscriptionQuery",  
  "entities": [  
    {  
      "type": "WaterConsumption"  
    }  
  ],  
  "watchedAttributes": [  
    "consumptionNextDay",  
    "consumptionNextWeek"  
  ],  
  "q": "refCity==urn:ngsi-ld:City:Valbonne",  
  "notification": {  
    "attributes": [  
      "consumptionNextDay",  
      "consumptionNextWeek"  
    ],  
    "format": "keyValues",  
    "endpoint": {  
      "uri": "http://my-domain-name",  
      "accept": "application/json"  
    }  
  }  
}  
```  
#### SubscriptionQuery NGSI-v2 normalizado Ejemplo  
He aquí un ejemplo de SubscriptionQuery en formato JSON-LD normalizado. Esto es compatible con NGSI-v2 cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "Subscription.01",  
  "type": "SubscriptionQuery",  
  "entities": {  
    "type": "StructuredValue",  
    "value": [  
      {  
        "type": "WaterConsumption"  
      }  
    ]  
  },  
  "watchedAttributes": {  
    "type": "StructuredValue",  
    "value": [  
      "consumptionNextDay",  
      "consumptionNextWeek"  
    ]  
  },  
  "q": {  
    "type": "Text",  
    "value": "refCity==urn:ngsi-ld:City:Valbonne"  
  },  
  "notification": {  
    "type": "StructuredValue",  
    "value": {  
      "attributes": [  
        "consumptionNextDay",  
        "consumptionNextWeek"  
      ],  
      "format": "keyValues",  
      "endpoint": {  
        "uri": "http://my-domain-name",  
        "accept": "application/json"  
      }  
    }  
  }  
}  
```  
#### SubscriptionQuery NGSI-LD key-values Ejemplo  
Aquí hay un ejemplo de una SubscriptionQuery en formato JSON-LD como key-values. Esto es compatible con NGSI-LD cuando se utiliza `options=keyValues` y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Subscription:01",  
  "type": "SubscriptionQuery",  
  "entities": [  
    {  
      "type": "WaterConsumption"  
    }  
  ],  
  "watchedAttributes": [  
    "consumptionNextDay",  
    "consumptionNextWeek"  
  ],  
  "q": "refCity==urn:ngsi-ld:City:Valbonne",  
  "notification": {  
    "attributes": [  
      "consumptionNextDay",  
      "consumptionNextWeek"  
    ],  
    "format": "keyValues",  
    "endpoint": {  
      "uri": "http://my-domain-name",  
      "accept": "application/json"  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### SubscriptionQuery NGSI-LD normalizado Ejemplo  
He aquí un ejemplo de SubscriptionQuery en formato JSON-LD normalizado. Esto es compatible con NGSI-LD cuando no se utilizan opciones y devuelve los datos de contexto de una entidad individual.  
```json  
{  
  "id": "urn:ngsi-ld:Subscription:01",  
  "type": "SubscriptionQuery",  
  "entities": {  
    "type": "Property",  
    "value": [  
      {  
        "type": "WaterConsumption"  
      }  
    ]  
  },  
  "watchedAttributes": {  
    "type": "Property",  
    "value": [  
      "consumptionNextDay",  
      "consumptionNextWeek"  
    ]  
  },  
  "q": {  
    "type": "Property",  
    "value": "refCity==urn:ngsi-ld:City:Valbonne"  
  },  
  "notification": {  
    "type": "property",  
    "value": {  
      "attributes": [  
        "consumptionNextDay",  
        "consumptionNextWeek"  
      ],  
      "format": "keyValues",  
      "endpoint": {  
        "uri": "http://my-domain-name",  
        "accept": "application/json"  
      }  
    }  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
