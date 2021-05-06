Entité : MLProcessing  
=====================  
[Licence ouverte] (https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLProcessing/LICENSE.md)  
Description globale : **Modèle de données pour la compilation des éléments d'un modèle d'apprentissage automatique.**  

## Liste des propriétés  

- `alternateName`: Un nom alternatif pour cet élément  - `connectionParameters`: Paramètres d'exécution de la connexion avec le système  - `dataProvider`: Une séquence de caractères identifiant le fournisseur de l'entité de données harmonisées.  - `dateCreated`: Horodatage de la création de l'entité. Celui-ci sera généralement attribué par la plateforme de stockage.  - `dateModified`: Horodatage de la dernière modification de l'entité. Il sera généralement attribué par la plateforme de stockage.  - `description`: Une description de cet article  - `dueDate`: Données/temps prévus pour l'exécution du traitement (pour les versions ultérieures, afin de permettre des traitements planifiés)  - `id`: Identifiant unique de l'entité  - `name`: Le nom de cet élément.  - `objective`: Objectif du traitement  - `owner`: Une liste contenant une séquence de caractères codée en JSON référençant les identifiants uniques du ou des propriétaires.  - `refMLModel`: Relation ciblant le modèle d'apprentissage automatique à utiliser pour le traitement.  - `refSubscriptionQuery`: Relation ciblant la requête d'abonnement à utiliser par le modèle d'apprentissage automatique.  - `seeAlso`: liste d'uri pointant vers des ressources supplémentaires sur l'élément  - `source`: Une séquence de caractères donnant la source originale des données de l'entité sous forme d'URL. Il est recommandé d'utiliser le nom de domaine entièrement qualifié du fournisseur source ou l'URL de l'objet source.    
Propriétés requises  
## Description des propriétés du modèle de données  
Classés par ordre alphabétique (cliquez pour plus de détails)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MLProcessing:    
  description: 'Data model for compilation of the elements of a machine learning model.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: Property    
    connectionParameters:    
      description: 'Parameters for running the connection with the system'    
      properties:    
        port:    
          type: number    
        server:    
          type: string    
        user:    
          type: string    
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
    dueDate:    
      description: 'Expected data / time for running the processing (for later versions, to allow planned processings)'    
      format: date-time    
      type: Property    
    id:    
      anyOf: &mlprocessing_-_properties_-_owner_-_items_-_anyof    
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
    objective:    
      description: 'Objective of the processing'    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *mlprocessing_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refMLModel:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Relationship targeting the Machine Learning model to use for the processing'    
      type: Relationship    
    refSubscriptionQuery:    
      anyOf:    
        - description: 'Property. Identifier format of any NGSI entity'    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
        - description: 'Property. Identifier format of any NGSI entity'    
          format: uri    
          type: string    
      description: 'Relationship targeting the subscription query to use by the Machine Learning model.'    
      type: Relationship    
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
  required: []    
  type: object    
```  
</details>    
## Exemples de charges utiles  
#### MLProcessing NGSI-v2 key-values Exemple  
Voici un exemple d'un traitement ML au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-v2 lorsque l'on utilise `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id":"urn:ngsi-ld:MLProcessing:01",  
  "type":"MLProcessing",  
  "refMLModel": "urn:ngsi-ld:MLModel:01",  
  "refSubscriptionQuery": "urn:ngsi-ld:SubscriptionQuery:01"  
}  
```  
#### MLProcessing NGSI-v2 normalisé Exemple  
Voici un exemple d'un traitement ML au format JSON-LD tel que normalisé. Il est compatible avec NGSI-v2 lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:MLProcessing:01",  
  "type": "MLProcessing",  
  "refMLModel": {  
    "type": "object",  
    "value": "urn:ngsi-ld:MLModel:01"  
  },  
  "refSubscriptionQuery": {  
    "type": "object",  
    "value": "urn:ngsi-ld:SubscriptionQuery:01"  
  }  
}  
```  
#### MLProcessing NGSI-LD key-values Exemple  
Voici un exemple d'un traitement ML au format JSON-LD en tant que valeurs-clés. Ceci est compatible avec NGSI-LD en utilisant `options=keyValues` et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:MLProcessing:01",  
  "type": "MLProcessing",  
  "refMLModel": "urn:ngsi-ld:MLModel:01",  
  "refSubscriptionQuery": "urn:ngsi-ld:SubscriptionQuery:01",  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### MLProcessing NGSI-LD normalisé Exemple  
Voici un exemple d'un traitement ML au format JSON-LD tel que normalisé. Il est compatible avec NGSI-LD lorsqu'il n'utilise pas d'options et renvoie les données contextuelles d'une entité individuelle.  
```json  
{  
  "id": "urn:ngsi-ld:MLProcessing:01",  
  "type": "MLProcessing",  
  "refMLModel": {  
    "type": "string",  
    "value": "urn:ngsi-ld:MLModel:01"  
  },  
  "refSubscriptionQuery": {  
    "type": "string",  
    "value": "urn:ngsi-ld:SubscriptionQuery:01"  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
