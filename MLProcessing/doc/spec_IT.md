<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
Entità: Elaborazione MLP    
========================<!-- /10-Header -->    
<!-- 15-License -->    
[Licenza aperta](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLProcessing/LICENSE.md)    
[documento generato automaticamente](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
Descrizione globale: **Modello di dati per la compilazione degli elementi relativi all'esecuzione di un modello di machine learning.**    
versione: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## Elenco delle proprietà    
<sup><sub>[*] Se non c'è un tipo in un attributo è perché potrebbe avere diversi tipi o diversi formati/modelli</sub></sup>.    
- `alternateName[string]`: Un nome alternativo per questa voce  - `connectionParameters[object]`: Parametri per l'esecuzione della connessione con il sistema  	- `port`:       
	- `server`:       
- `dataProvider[string]`: una sequenza di caratteri che identifica il fornitore dell'entità di dati armonizzata  - `dateCreated[date-time]`: Timestamp di creazione dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `dateModified[date-time]`: Timestamp dell'ultima modifica dell'entità. Di solito viene assegnato dalla piattaforma di archiviazione  - `description[string]`: Descrizione dell'articolo  - `dueDate[date-time]`: Dati previsti / tempo di esecuzione dell'elaborazione (per le versioni successive, per consentire elaborazioni pianificate)  - `id[*]`: Identificatore univoco dell'entità  - `name[string]`: Il nome di questo elemento  - `objective[string]`: Obiettivo del trattamento  - `owner[array]`: Un elenco contenente una sequenza di caratteri codificata JSON che fa riferimento agli ID univoci dei proprietari.  - `refMLModel[*]`: Relazione che punta al modello di apprendimento automatico da utilizzare per l'elaborazione  - `refSubscriptionQuery[*]`: Relazione che indirizza la query di sottoscrizione da utilizzare dal modello di apprendimento automatico  - `seeAlso[*]`: elenco di uri che puntano a risorse aggiuntive sull'elemento  - `source[string]`: Una sequenza di caratteri che indica la fonte originale dei dati dell'entità come URL. Si consiglia di utilizzare il nome di dominio completamente qualificato del provider di origine o l'URL dell'oggetto di origine.  - `type[string]`: Tipo di entità NGSI. Deve essere MLProcessing  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
Proprietà richieste    
<!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## Modello di dati descrizione delle proprietà    
Ordinati in ordine alfabetico (clicca per i dettagli)    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
MLProcessing:      
  description: Data model for compilation of the elements about the execution of a machine learning model.      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    connectionParameters:      
      description: Parameters for running the connection with the system      
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
    dueDate:      
      description: 'Expected data / time for running the processing (for later versions, to allow planned processings)'      
      format: date-time      
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
    name:      
      description: The name of this item      
      type: string      
      x-ngsi:      
        type: Property      
    objective:      
      description: Objective of the processing      
      type: string      
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
    refMLModel:      
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
      description: Relationship targeting the Machine Learning model to use for the processing      
      x-ngsi:      
        type: Relationship      
    refSubscriptionQuery:      
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
      description: Relationship targeting the subscription query to use by the Machine Learning model      
      x-ngsi:      
        type: Relationship      
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
      description: NGSI entity type. It has to be MLProcessing      
      enum:      
        - MLProcessing      
      type: string      
      x-ngsi:      
        type: Property      
  required: []      
  type: object      
  x-derived-from: ""      
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
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
## Esempi di payload    
#### Elaborazione MLP dei valori-chiave NGSI-v2 Esempio    
Ecco un esempio di un'elaborazione MLP in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-v2 quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MLProcessing:01",  
  "type": "MLProcessing",  
  "refMLModel": "urn:ngsi-ld:MLModel:01",  
  "refSubscriptionQuery": "urn:ngsi-ld:SubscriptionQuery:01"  
}  
```  
</details>    
#### Elaborazione MLP Esempio normalizzato NGSI-v2    
Ecco un esempio di MLProcessing in formato JSON-LD normalizzato. Questo è compatibile con NGSI-v2 quando non si utilizzano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
  "id": "urn:ngsi-ld:MLProcessing:01",  
  "type": "MLProcessing",  
  "refMLModel": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:MLModel:01"  
  },  
  "refSubscriptionQuery": {  
    "type": "Text",  
    "value": "urn:ngsi-ld:SubscriptionQuery:01"  
  }  
}  
```  
</details>    
#### Elaborazione MLP Valori chiave NGSI-LD Esempio    
Ecco un esempio di un'elaborazione MLP in formato JSON-LD come valori-chiave. Questo è compatibile con NGSI-LD quando si usa `options=keyValues` e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
```json  
{  
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
#### Elaborazione MLP Esempio normalizzato NGSI-LD    
Ecco un esempio di MLProcessing in formato JSON-LD normalizzato. Questo è compatibile con NGSI-LD quando non si usano opzioni e restituisce i dati di contesto di una singola entità.    
<details><summary><strong>show/hide example</strong></summary>      
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
        "https://raw.githubusercontent.com/smart-data-models/dataModel.MachineLearning/master/context.jsonld"  
    ]  
}  
```  
</details><!-- /80-Examples -->    
<!-- 90-FooterNotes -->    
<!-- /90-FooterNotes -->    
<!-- 95-Units -->    
Vedere [FAQ 10](https://smartdatamodels.org/index.php/faqs/) per ottenere una risposta su come gestire le unità di grandezza.    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
