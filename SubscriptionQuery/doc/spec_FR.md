<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entité : SubscriptionQuery  
==========================<!-- /10-Header -->  
<!-- 15-License -->  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md)  
[document généré automatiquement] (https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Description globale : **Modèle de requête d'abonnement pour les modèles d'apprentissage automatique**.  
version : 0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste des propriétés  

<sup><sub>[*] S'il n'y a pas de type dans un attribut, c'est parce qu'il pourrait avoir plusieurs types ou différents formats/modèles</sub></sup>.  
- `alternateName[string]`: Un nom alternatif pour cet élément  - `csf[string]`: Filtre de source contextuelle auquel doivent correspondre les enregistrements de source contextuelle décrivant les sources contextuelles à utiliser pour récupérer les entités. Défini dans la norme NGSI-LD.  - `dataProvider[string]`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated[string]`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified[string]`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description[string]`: Une description de cet article  - `entities[array]`: Les identifiants d'entités, les modèles d'identifiants et les types d'entités que les entités doivent faire correspondre pour pouvoir être récupérées. Défini dans la norme NGSI-LD.  - `expiresAt[string]`: Date d'expiration de l'abonnement. Définie dans la norme NGSI-LD.  - `geoQ[string]`: Requête géographique à laquelle doivent correspondre les entités pour être récupérées. Défini dans la norme NGSI-LD.  - `id[*]`: Identifiant unique de l'entité  - `name[string]`: Le nom de cet élément.  - `notification[object]`: Paramètres de la notification pour l'abonnement. Définis dans la norme NGSI-LD.  - `owner[array]`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `q[string]`: Requête à laquelle les entités doivent correspondre pour pouvoir être récupérées. Définie dans la norme NGSI-LD.  - `seeAlso[*]`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source[string]`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.  - `subscriptionName[string]`: Un nom (court) donné à cet abonnement. Défini dans la norme NGSI-LD.  - `temporalQ[string]`: L'interrogation temporelle doit être présente uniquement pour l'opération "Interroger l'évolution temporelle des entités". Défini dans la norme NGSI-LD.  - `throttling[string]`: Période de temps minimale en secondes qui doit s'écouler entre deux notifications consécutives. Défini dans la norme NGSI-LD.  - `type[string]`: Il doit s'agir de SubscriptionQuery. Enum : "SubscriptionQuery  - `watchedAttributes[array]`: Liste des attributs que les entités doivent faire correspondre afin d'être récupérées. Si elle n'est pas présente, tous les attributs seront récupérés. Défini dans la norme NGSI-LD.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
Propriétés requises  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
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
## Exemples de charges utiles  
#### AbonnementQuery Valeurs-clés NGSI-v2 Exemple  
Voici un exemple d'une SubscriptionQuery au format JSON-LD sous forme de valeurs-clés. Cette requête est compatible avec NGSI-v2 lorsqu'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### AbonnementQuery NGSI-v2 normalisé Exemple  
Voici un exemple d'une SubscriptionQuery au format JSON-LD tel que normalisé. Cette requête est compatible avec la norme NGSI-v2 lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
#### SubscriptionQuery Valeurs-clés NGSI-LD Exemple  
Voici un exemple d'une SubscriptionQuery au format JSON-LD sous forme de valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
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
#### AbonnementQuery NGSI-LD normalisé Exemple  
Voici un exemple d'une SubscriptionQuery au format JSON-LD tel que normalisé. Cette requête est compatible avec NGSI-LD lorsqu'elle n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
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
Voir [FAQ 10](https://smartdatamodels.org/index.php/faqs/) pour obtenir une réponse sur la façon de traiter les unités de magnitude.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
