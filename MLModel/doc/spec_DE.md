Entität: MLModel  
================  
[Offene Lizenz](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLModel/LICENSE.md)  
[Dokument automatisch generiert](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
Globale Beschreibung: **Datenmodell zur Zusammenstellung der Elemente eines maschinellen Lernmodells.**  

## Liste der Eigenschaften  

- `acceptableDataSources`: Gültiger Typ der Eingangsdatenquellen für die Ausführung des Machine-Learning-Modells  - `algorithm`: Der vom zugrundeliegenden Machine Learning-Modell verwendete Algorithmus (z. B. lineare Regression, k-means, SVM, MLP,...)  - `alternateName`: Ein alternativer Name für diesen Artikel  - `dataProvider`: Eine Folge von Zeichen, die den Anbieter der harmonisierten Dateneinheit identifiziert.  - `dateCreated`: Zeitstempel der Entitätserstellung. Dieser wird normalerweise von der Speicherplattform zugewiesen.  - `dateModified`: Zeitstempel der letzten Änderung der Entität. Dieser wird in der Regel von der Speicherplattform vergeben.  - `description`: Eine Beschreibung dieses Artikels  - `dockerImage`: Docker-Image, das das Machine Learning-Modell enthält  - `id`: Eindeutiger Bezeichner der Entität  - `inputAttributes`: Komma-getrennte Liste von Attributnamen (die per Definition einen bestimmten Typ haben sollten).  - `mlFramework`: Das Framework für maschinelles Lernen, das zur Erstellung des Modells verwendet wurde (z. B. scikit-learn, H2O, Spark MLib, usw.)  - `name`: Der Name dieses Elements.  - `outputAttributes`: Durch Kommata getrennte Liste der Attributnamen, die zur Veröffentlichung der Ergebnisse verwendet werden.  - `outputDataTypes`: Typ der Ausgabedaten, die vom Machine Learning Model erzeugt werden  - `owner`: Eine Liste mit einer JSON-kodierten Zeichenfolge, die auf die eindeutigen Ids der Eigentümer verweist  - `refMLProcessing`:   - `seeAlso`: Liste von uri, die auf zusätzliche Ressourcen über das Element verweist  - `source`: Eine Folge von Zeichen, die die ursprüngliche Quelle der Entitätsdaten als URL angibt. Empfohlen wird der voll qualifizierte Domänenname des Quellanbieters oder die URL zum Quellobjekt.  - `typeOfAlgorithm`: Aufzählung  - `version`: Version des Modells.    
Erforderliche Eigenschaften  
- `id`  - `type`  ## Datenmodell Beschreibung der Eigenschaften  
Alphabetisch sortiert (für Details anklicken)  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
MLModel:    
  description: 'Data model for compilation of the elements of a machine learning model.'    
  properties:    
    acceptableDataSources:    
      description: 'Valid type of input data sources for running the Machine Learning Model'    
      items:    
        type: string    
      type: Property    
    algorithm:    
      description: 'The algorithm used by the underlying Machine Learning model (e.g. linear regression, k-means, SVM, MLP,...)'    
      type: Property    
    alternateName:    
      description: 'An alternative name for this item'    
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
    dockerImage:    
      description: 'Docker image containing the Machine Learning model'    
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
      type: Property    
    inputAttributes:    
      description: 'Comma-separated list of attributes names (that should have a given type by definition).'    
      items:    
        type: string    
      type: Property    
    mlFramework:    
      description: 'The Machine Learning framework that has been used to prepare the model (e.g., scikit-learn, H2O, Spark MLib, etc)'    
      type: Property    
    name:    
      description: 'The name of this item.'    
      type: Property    
    outputAttributes:    
      description: 'Comma-separated list of attributes names used to publish the results.'    
      items:    
        type: string    
      type: Property    
    outputDataTypes:    
      description: 'Type of output data produced by the Machine Learning Model'    
      items:    
        type: string    
      type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *mlmodel_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: Property    
    refMLProcessing:    
      description: ""    
      items:    
        format: uri    
        type: string    
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
    typeOfAlgorithm:    
      description: enumeration    
      type: Property    
      x-ngsi:    
        model: https://schema.org/Text    
    version:    
      description: 'Version of the model.'    
      type: Property    
  required:    
    - id    
    - type    
  type: object    
```  
</details>    
## Beispiel-Nutzlasten  
#### MLModel NGSI-v2 Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-v2 bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "MLModel.01",  
  "type": "MLModel",  
  "name": "Water consumption prediction",  
  "description": "Predicts water consumption based on …",  
  "dockerImage": "Docker image containing the model",  
  "algorithm": "k-means",  
  "version": 12,  
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
#### MLModel NGSI-v2 normalisiert Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-v2, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
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
#### MLModel NGSI-LD Schlüsselwerte Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format als Key-Values. Dies ist kompatibel mit NGSI-LD bei Verwendung von `options=keyValues` und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:MLModel:01",  
  "type": "MLModel",  
  "name": "Water consumption prediction",  
  "description": "Predicts water consumption based on â€¦",  
  "dockerImage": "Docker image containing the model",  
  "algorithm": "k-means",  
  "version": 12,  
  "inputAttributes": [  
    "minFlow",  
    "maxFlow",  
    "waterConsumption"  
  ],  
  "outputAttributes": [  
    "consumptionNextDay",  
    "consumptionNextWeek"  
  ],  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
#### MLModell NGSI-LD normalisiert Beispiel  
Hier ist ein Beispiel für ein MLModel im JSON-LD-Format wie normalisiert. Dies ist kompatibel mit NGSI-LD, wenn keine Optionen verwendet werden, und liefert die Kontextdaten einer einzelnen Entität.  
```json  
{  
  "id": "urn:ngsi-ld:MLModel:01",  
  "type": "MLModel",  
  "name": {  
    "type": "Property",  
    "value": "Water consumption prediction"  
  },  
  "description": {  
    "type": "Property",  
    "value": "Predicts water consumption based "  
  },  
  "dockerImage": {  
    "type": "Property",  
    "value": "Docker image containing the model"  
  },  
  "algorithm": {  
    "type": "Property",  
    "value": "k-means"  
  },  
  "version": {  
    "type": "Property",  
    "value": "12"  
  },  
  "inputAttributes": {  
    "type": "Property",  
    "value": [  
      "minFlow",  
      "maxFlow",  
      "waterConsumption"  
    ]  
  },  
  "outputAttributes": {  
    "type": "Property",  
    "value": [  
      "consumptionNextDay",  
      "consumptionNextWeek"  
    ]  
  },  
  "@context": [  
    "https://smartdatamodels.org/context.jsonld"  
  ]  
}  
```  
