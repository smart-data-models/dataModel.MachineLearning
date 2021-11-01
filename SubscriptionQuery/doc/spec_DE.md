Entität: SubscriptionQuery  
==========================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Abonnement-Abfragemodell für Modelle des maschinellen Lernens**  

## Liste der Eigenschaften  

- `alternateName`: Ein alternativer Name für diesen Artikel  - `csf`: Kontextquellen-Filter, der von Kontextquellen-Registrierungen erfüllt werden muss, die Kontextquellen beschreiben, die zum Abrufen von Entitäten verwendet werden sollen. Definiert im NGSI-LD-Standard.  - `dataProvider`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `entities`: Entitäts-IDs, ID-Muster und Entitätstypen, die von Entitäten abgeglichen werden müssen, um abgerufen werden zu können. Definiert im NGSI-LD Standard.  - `expiresAt`: Verfallsdatum für das Abonnement. Definiert im NGSI-LD-Standard.  - `geoQ`: Geo-Query, die von Entitäten abgeglichen werden muss, um abgerufen zu werden. Definiert im NGSI-LD Standard.  - `id`: Eindeutiger Bezeichner der Entität  - `name`: Der Name dieses Artikels.  - `notification`: Parameter der Benachrichtigung für das Abonnement. Definiert im NGSI-LD-Standard.  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `q`: Abfrage, die von Entitäten erfüllt werden muss, um abgerufen werden zu können. Definiert im NGSI-LD-Standard.  - `seeAlso`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `subscriptionName`: Ein (kurzer) Name, der dieser Subskription gegeben wird. Definiert im NGSI-LD-Standard.  - `temporalQ`: Zeitliche Abfrage, die nur für die Operation "Abfrage der zeitlichen Entwicklung von Entitäten" vorhanden ist. Definiert im NGSI-LD-Standard.  - `throttling`: Minimale Zeitspanne in Sekunden, die zwischen zwei aufeinanderfolgenden Benachrichtigungen vergehen muss. Definiert in der NGSI-LD-Norm.  - `type`: Es muss SubscriptionQuery sein. Enum:'SubscriptionQuery'  - `watchedAttributes`: Liste der Attribute, die von Entitäten abgeglichen werden müssen, um abgerufen werden zu können. Falls nicht vorhanden, werden alle Attribute abgerufen. Definiert im NGSI-LD-Standard.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SubscriptionQuery:    
  description: 'Subscription Query model for Machine Learning models'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    csf:    
      description: 'Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: 'A sequence of characters identifying the provider of the harmonised data entity.'    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: 'Entity creation timestamp. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: 'Timestamp of the last modification of the entity. This will usually be allocated by the storage platform.'    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: 'A description of this item'    
      type: string    
      x-ngsi:    
        type: Property    
    entities:    
      description: 'Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard.'    
      items:    
        properties:    
          type:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expiresAt:    
      description: 'Expiration date for the subscription. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    geoQ:    
      description: 'Geo-Query that shall be matched by Entities in order be retrieved. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
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
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *subscriptionquery_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    q:    
      description: 'Query that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    subscriptionName:    
      description: 'A (short) name given to this Subscription. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    temporalQ:    
      description: 'Temporal Query to be present only for ''Query Temporal Evolution of Entities'' operation. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    throttling:    
      description: 'Minimal period of time in seconds which shall elapse between two consecutive notifications. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be SubscriptionQuery. Enum:''SubscriptionQuery'''    
      enum:    
        - SubscriptionQuery    
      type: string    
      x-ngsi:    
        type: Property    
    watchedAttributes:    
      description: 'List of Attributes that shall be matched by Entities in order to be retrieved. If not present all Attributes will be retrieved. Defined in NGSI-LD standard. '    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### SubscriptionQuery NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SubscriptionQuery NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SubscriptionQuery NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
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
#### SubscriptionQuery NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
