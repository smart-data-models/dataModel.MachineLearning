<!-- 10-Header -->
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  

=======
<!-- 15-License -->


<!-- /15-License -->
<!-- 20-Description -->


<!-- /20-Description -->
<!-- 30-PropertiesList -->




- `alternateName[string]`: 这个项目的一个替代名称  
<!-- 35-RequiredProperties -->

<!-- /35-RequiredProperties -->
<!-- 40-RequiredProperties -->
<!-- /40-RequiredProperties -->
<!-- 50-DataModelHeader -->


<!-- /50-DataModelHeader -->
<!-- 60-ModelYaml -->
<details><summary><strong>full yaml details</strong></summary>    

MLProcessing:    
  description: 'Data model for compilation of the elements about the execution of a machine learning model.'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
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
      type: object    
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
    dueDate:    
      description: 'Expected data / time for running the processing (for later versions, to allow planned processings)'    
      format: date-time    
      type: string    
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    objective:    
      description: 'Objective of the processing'    
      type: string    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *mlprocessing_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
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
      x-ngsi:    
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
      x-ngsi:    
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
      x-ngsi:    
        type: Property    
    source:    
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'NGSI entity type. It has to be MLProcessing'    
      enum:    
        - MLProcessing    
      type: string    
      x-ngsi:    
        type: Property    
  required: []    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MachineLearning/blob/master/MLProcessing/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MLModel/MLModel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->
<!-- 70-MiddleNotes -->
<!-- /70-MiddleNotes -->
<!-- 80-Examples -->



<details><summary><strong>show/hide example</strong></summary>    


  "id":"urn:ngsi-ld:MLProcessing:01",  
  "type":"MLProcessing",  
  "refMLModel": "urn:ngsi-ld:MLModel:01",  
  "refSubscriptionQuery": "urn:ngsi-ld:SubscriptionQuery:01"  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
</details>  


<details><summary><strong>show/hide example</strong></summary>    


    "id": "urn:ngsi-ld:MLProcessing:01",  
    "type": "MLProcessing",  
    "refMLModel": "urn:ngsi-ld:MLModel:01",  
    "refSubscriptionQuery": "urn:ngsi-ld:SubscriptionQuery:01",  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MachineLearning/master/context.jsonld"  
    ]  
}  
```  
</details>  


<details><summary><strong>show/hide example</strong></summary>    


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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MachineLearning/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->
<!-- 90-FooterNotes -->
<!-- /90-FooterNotes -->
<!-- 95-Units -->

<!-- /95-Units -->
<!-- 97-LastFooter -->
---  
