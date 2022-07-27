[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entità: MLModel  
===============  
[Licenza aperta](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLModel/LICENSE.md)  
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Descrizione globale: **Modello di dati per la compilazione degli elementi di un modello di apprendimento automatico.**  
versione: 0.0.2  

## Elenco delle proprietà  

- `acceptableDataSources`: Tipo valido di fonti di dati di input per l'esecuzione del modello di apprendimento automatico  - `algorithm`: L'algoritmo utilizzato dal modello di apprendimento automatico sottostante (ad es. regressione lineare, k-means, SVM, MLP, ...)  - `alternateName`: Un nome alternativo per questa voce  - `dataProvider`: Una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata.  - `dateCreated`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `dateModified`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione.  - `description`: Descrizione dell'articolo  - `dockerImage`: Immagine Docker contenente il modello di apprendimento automatico  - `id`: Identificatore univoco dell'entità  - `inputAttributes`: Elenco separato da virgole di nomi di attributi (che dovrebbero avere un determinato tipo per definizione).  - `mlFramework`: Il framework di apprendimento automatico utilizzato per preparare il modello (ad esempio, scikit-learn, H2O, Spark MLib, ecc.).  - `name`: Il nome di questo elemento.  - `outputAttributes`: Elenco separato da virgole dei nomi degli attributi usati per pubblicare i risultati.  - `outputDataTypes`: Tipo di dati in uscita prodotti dal modello di apprendimento automatico  - `owner`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refMLProcessing`:   - `seeAlso`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type`: Tipo di entità NGSI. Deve essere MLModel  - `typeOfAlgorithm`: Enumerazione  - `version`: Versione del modello.    
Proprietà richieste  
- `id`  - `type`  ## Modello di dati descrizione delle proprietà  
Ordinati in ordine alfabetico (clicca per i dettagli)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MLModel:    
  description: 'Data model for compilation of the elements of a machine learning model.'    
  properties:    
    acceptableDataSources:    
      description: 'Valid type of input data sources for running the Machine Learning Model'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    algorithm:    
      description: 'The algorithm used by the underlying Machine Learning model (e.g. linear regression, k-means, SVM, MLP,...)'    
      type: string    
      x-ngsi:    
        type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
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
    dockerImage:    
      description: 'Docker image containing the Machine Learning model'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &mlmodel_-_properties_-_owner_-_items_-_anyof    
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
    inputAttributes:    
      description: 'Comma-separated list of attributes names (that should have a given type by definition).'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    mlFramework:    
      description: 'The Machine Learning framework that has been used to prepare the model (e.g., scikit-learn, H2O, Spark MLib, etc)'    
      type: string    
      x-ngsi:    
        type: Property    
    name:    
      description: 'The name of this item.'    
      type: string    
      x-ngsi:    
        type: Property    
    outputAttributes:    
      description: 'Comma-separated list of attributes names used to publish the results.'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    outputDataTypes:    
      description: 'Type of output data produced by the Machine Learning Model'    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *mlmodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    refMLProcessing:    
      description: ""    
      items:    
        format: uri    
        type: string    
      type: array    
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
    type:    
      description: 'NGSI entity type. It has to be MLModel'    
      enum:    
        - MLModel    
      type: string    
      x-ngsi:    
        type: Property    
    typeOfAlgorithm:    
      description: Enumeration    
      type: string    
      x-ngsi:    
        model: https://schema.org/Text    
        type: Property    
    version:    
      description: 'Version of the model.'    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MachineLearning/blob/master/MLModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MLModel/MLModel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
## Esempi di payload  
#### MLModel NGSI-v2 valori-chiave Esempio  
Ecco un esempio di MLModel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "MLModel.01",  
  "type": "MLModel",  
  "name": "Water consumption prediction",  
  "description": "Predicts water consumption based on …",  
  "dockerImage": "Docker image containing the model",  
  "algorithm": "k-means",  
  "version": "12",  
  "inputAttributes": [  
    "minFlow",  
    "maxFlow",  
    "waterConsumption"  
  ],  
  "outputAttributes": [  
    "consumptionNextDay",  
    "consumptionNextWeek"  
  ]  
}  
```  
#### MLModello NGSI-v2 normalizzato Esempio  
Ecco un esempio di MLModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
  "id": "MLModel.01",  
  "type": "MLModel",  
  "name": {  
    "type": "Text",  
    "value": "Water consumption prediction"  
  },  
  "description": {  
    "type": "Text",  
    "value": "Predicts water consumption based "  
  },  
  "dockerImage": {  
    "type": "Text",  
    "value": "Docker image containing the model"  
  },  
  "algorithm": {  
    "type": "Text",  
    "value": "k-means"  
  },  
  "version": {  
    "type": "Text",  
    "value": "12"  
  },  
  "inputAttributes": {  
    "type": "StructuredValue",  
    "value": [  
      "minFlow",  
      "maxFlow",  
      "waterConsumption"  
    ]  
  },  
  "outputAttributes": {  
    "type": "StructuredValue",  
    "value": [  
      "consumptionNextDay",  
      "consumptionNextWeek"  
    ]  
  }  
}  
```  
#### MLModel NGSI-LD valori-chiave Esempio  
Ecco un esempio di MLModel in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi-ld:MLModel:01",  
    "type": "MLModel",  
    "algorithm": "k-means",  
    "description": "Predicts water consumption based on \u2026",  
    "dockerImage": "Docker image containing the model",  
    "inputAttributes": [  
        "minFlow",  
        "maxFlow",  
        "waterConsumption"  
    ],  
    "name": "Water consumption prediction",  
    "outputAttributes": [  
        "consumptionNextDay",  
        "consumptionNextWeek"  
    ],  
    "version": 12,  
    "@context": [  
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MachineLearning/master/context.jsonld"  
    ]  
}  
```  
#### MLModello NGSI-LD normalizzato Esempio  
Ecco un esempio di MLModel in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.  
```json  
{  
    "id": "urn:ngsi-ld:MLModel:01",  
    "type": "MLModel",  
    "algorithm": {  
        "type": "Property",  
        "value": "k-means"  
    },  
    "description": {  
        "type": "Property",  
        "value": "Predicts water consumption based "  
    },  
    "dockerImage": {  
        "type": "Property",  
        "value": "Docker image containing the model"  
    },  
    "inputAttributes": {  
        "type": "Property",  
        "value": [  
            "minFlow",  
            "maxFlow",  
            "waterConsumption"  
        ]  
    },  
    "name": {  
        "type": "Property",  
        "value": "Water consumption prediction"  
    },  
    "outputAttributes": {  
        "type": "Property",  
        "value": [  
            "consumptionNextDay",  
            "consumptionNextWeek"  
        ]  
    },  
    "version": {  
        "type": "Property",  
        "value": "12"  
    },  
    "@context": []  
}  
```  
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.  
