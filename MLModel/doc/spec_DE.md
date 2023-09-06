<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
Entität: MLModel  
================<!-- /10-Header -->  
<!-- 15-License -->  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLModel/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
Globale Beschreibung: **Datenmodell für die Zusammenstellung der Elemente eines Modells für maschinelles Lernen**.  
Version: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## Liste der Eigenschaften  

<sup><sub>[*] Wenn es für ein Attribut keinen Typ gibt, kann es mehrere Typen oder verschiedene Formate/Muster haben</sub></sup>.  
- `acceptableDataSources[array]`: Gültige Art der Eingabedatenquellen für die Ausführung des Modells für maschinelles Lernen  - `algorithm[string]`: Der vom zugrundeliegenden Modell des maschinellen Lernens verwendete Algorithmus (z. B. lineare Regression, k-means, SVM, MLP, ...)  - `alternateName[string]`: Ein alternativer Name für diesen Artikel  - `dataProvider[string]`: Eine Folge von Zeichen zur Identifizierung des Anbieters der harmonisierten Dateneinheit  - `dateCreated[date-time]`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen  - `dateModified[date-time]`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben  - `description[string]`: Eine Beschreibung dieses Artikels  - `dockerImage[string]`: Docker-Image, das das Modell für maschinelles Lernen enthält  - `id[*]`: Eindeutiger Bezeichner der Entität  - `inputAttributes[array]`: Durch Kommata getrennte Liste von Attributnamen (die per Definition einen bestimmten Typ haben sollten)  - `mlFramework[string]`: Das Framework für maschinelles Lernen, das für die Erstellung des Modells verwendet wurde (z. B. scikit-learn, H2O, Spark MLib, usw.)  - `name[string]`: Der Name dieses Artikels  - `outputAttributes[array]`: Durch Kommata getrennte Liste der Attributnamen, die zur Veröffentlichung der Ergebnisse verwendet werden  - `outputDataTypes[array]`: Art der vom Modell für maschinelles Lernen erzeugten Ausgabedaten  - `owner[array]`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Kennungen der Eigentümer verweist  - `refMLProcessing[array]`:   - `seeAlso[*]`: Liste von URLs, die auf zusätzliche Ressourcen zu dem Artikel verweisen  - `source[string]`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL des Quellobjekts.  - `type[string]`: NGSI-Entitätstyp. Es muss MLModel sein  - `typeOfAlgorithm[string]`: Aufzählung  . Model: [https://schema.org/Text](https://schema.org/Text)- `version[string]`: Version des Modells  <!-- /30-PropertiesList -->  
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
MLModel:    
  description: Data model for compilation of the elements of a machine learning model.    
  properties:    
    acceptableDataSources:    
      description: Valid type of input data sources for running the Machine Learning Model    
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
      description: An alternative name for this item    
      type: string    
      x-ngsi:    
        type: Property    
    dataProvider:    
      description: A sequence of characters identifying the provider of the harmonised data entity    
      type: string    
      x-ngsi:    
        type: Property    
    dateCreated:    
      description: Entity creation timestamp. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    dateModified:    
      description: Timestamp of the last modification of the entity. This will usually be allocated by the storage platform    
      format: date-time    
      type: string    
      x-ngsi:    
        type: Property    
    description:    
      description: A description of this item    
      type: string    
      x-ngsi:    
        type: Property    
    dockerImage:    
      description: Docker image containing the Machine Learning model    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf:    
        - description: Identifier format of any NGSI entity    
          maxLength: 256    
          minLength: 1    
          pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
          type: string    
          x-ngsi:    
            type: Property    
        - description: Identifier format of any NGSI entity    
          format: uri    
          type: string    
          x-ngsi:    
            type: Property    
      description: Unique identifier of the entity    
      x-ngsi:    
        type: Property    
    inputAttributes:    
      description: Comma-separated list of attributes names (that should have a given type by definition)    
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
      description: The name of this item    
      type: string    
      x-ngsi:    
        type: Property    
    outputAttributes:    
      description: Comma-separated list of attributes names used to publish the results    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    outputDataTypes:    
      description: Type of output data produced by the Machine Learning Model    
      items:    
        type: string    
      type: array    
      x-ngsi:    
        type: Property    
    owner:    
      description: A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)    
      items:    
        anyOf:    
          - description: Identifier format of any NGSI entity    
            maxLength: 256    
            minLength: 1    
            pattern: ^[\w\-\.\{\}\$\+\*\[\]`|~^@!,:\\]+$    
            type: string    
            x-ngsi:    
              type: Property    
          - description: Identifier format of any NGSI entity    
            format: uri    
            type: string    
            x-ngsi:    
              type: Property    
        description: Unique identifier of the entity    
        x-ngsi:    
          type: Property    
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
      description: list of uri pointing to additional resources about the item    
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
      description: 'A sequence of characters giving the original source of the entity data as a URL. Recommended to be the fully qualified domain name of the source provider, or the URL to the source object'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: NGSI entity type. It has to be MLModel    
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
      description: Version of the model    
      type: string    
      x-ngsi:    
        type: Property    
  required:    
    - id    
    - type    
  type: object    
  x-derived-from: ""    
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MachineLearning/blob/master/MLModel/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MLModel/MLModel/schema.json    
  x-model-tags: ""    
  x-version: 0.0.2    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## Beispiel-Nutzlasten  
#### MLModel NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-v2 kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### MLModel NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### MLModel NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format als Key-Values. Dies ist mit NGSI-LD kompatibel, wenn `options=keyValues` verwendet wird und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
</details>  
#### MLModell NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format in normalisierter Form. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
<details><summary><strong>show/hide example</strong></summary>    
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
