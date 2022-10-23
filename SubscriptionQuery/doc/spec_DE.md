<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: SubscriptionQuery  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Abonnement-Abfragemodell für Modelle des maschinellen Lernens**  
Version: 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, liegt das daran, dass es mehrere Typen oder unterschiedliche Formate/Muster haben kann</sub></sup>.  
- `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `csf[string]`: Kontextquellenfilter, der von Kontextquellenregistrierungen, die Kontextquellen beschreiben, die zum Abrufen von Entitäten verwendet werden sollen, abgeglichen werden muss. Definiert im NGSI-LD-Standard.  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit.  - `dateCreated[string]`: Zeitstempel der Entitätserstellung. Dieser wird in der Regel von der Speicherplattform zugewiesen.  - `dateModified[string]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description[string]`: Eine Beschreibung dieses Artikels  - `entities[array]`: Entitäts-IDs, ID-Muster und Entitätsarten, die von Entitäten abgeglichen werden müssen, um abgerufen werden zu können. Definiert im NGSI-LD Standard.  - `expiresAt[string]`: Verfallsdatum für das Abonnement. Definiert im NGSI-LD-Standard.  - `geoQ[string]`: Geo-Query, die von Entitäten abgeglichen werden muss, um abgerufen zu werden. Definiert im NGSI-LD Standard.  - `id[*]`: Eindeutiger Bezeichner der Entität  - `name[string]`: Der Name dieses Artikels.  - `notification[object]`: Parameter der Benachrichtigung für das Abonnement. Definiert im NGSI-LD-Standard.  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `q[string]`: Abfrage, die von Entitäten erfüllt werden muss, um abgerufen werden zu können. Definiert im NGSI-LD-Standard.  - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Es wird empfohlen, den voll qualifizierten Domänennamen des Quellanbieters oder die URL des Quellobjekts zu verwenden.  - `subscriptionName[string]`: Ein (kurzer) Name, der dieser Subskription gegeben wird. Definiert im NGSI-LD-Standard.  - `temporalQ[string]`: Die zeitliche Abfrage ist nur für die Operation "Abfrage der zeitlichen Entwicklung von Entitäten" vorgesehen. Definiert im NGSI-LD-Standard.  - `throttling[string]`: Minimale Zeitspanne in Sekunden, die zwischen zwei aufeinanderfolgenden Meldungen vergehen muss. Definiert in der NGSI-LD-Norm.  - `type[string]`: Es muss SubscriptionQuery sein. Enum:'SubscriptionQuery'  - `watchedAttributes[array]`: Liste der Attribute, die von Entitäten abgeglichen werden müssen, um abgerufen werden zu können. Falls nicht vorhanden, werden alle Attribute abgerufen. Definiert im NGSI-LD-Standard.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Erforderliche Eigenschaften  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MLModel/SubscriptionQuery/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### SubscriptionQuery NGSI-v2 key-values Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SubscriptionQuery NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### SubscriptionQuery NGSI-LD key-values Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
```json  
{  
    "id": "urn:ngsi-ld:Subscription:01",  
    "type": "SubscriptionQuery",  
    "entities": [  
        {  
            "type": "WaterConsumption"  
        }  
    ],  
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
    "q": "refCity==urn:ngsi-ld:City:Valbonne",  
    "watchedAttributes": [  
        "consumptionNextDay",  
        "consumptionNextWeek"  
    ],  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MachineLearning/master/context.jsonld"  
    ]  
}  
```  
</details>  
#### SubscriptionQuery NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für eine SubscriptionQuery im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
    "q": {  
        "type": "Property",  
        "value": "refCity==urn:ngsi-ld:City:Valbonne"  
    },  
    "watchedAttributes": {  
        "type": "Property",  
        "value": [  
            "consumptionNextDay",  
            "consumptionNextWeek"  
        ]  
    },  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MachineLearning/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->  
<!-- 90-FooterNotes -->  
<!-- /90-FooterNotes -->  
<!-- 95-Units -->  
Siehe [FAQ 10] (https://smartdatamodels.org/index.php/faqs/), um eine Antwort auf die Frage zu erhalten, wie man mit Größeneinheiten umgeht  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
