エンティティMLProcessing  
==================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLProcessing/LICENSE.md)  
[document generated automatically](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述です。**機械学習モデルの実行に関する要素をまとめるためのデータモデルです。  

## プロパティのリスト  

- `alternateName`: このアイテムの別称  - `connectionParameters`: システムとの接続を実行するためのパラメータ  - `dataProvider`: 調和されたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified`: エンティティが最後に変更された時のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `description`: このアイテムの説明  - `dueDate`: 処理を実行する予定のデータ／時間（以降のバージョンでは、計画的な処理を可能にするために  - `id`: エンティティのユニークな識別子  - `name`: このアイテムの名前です。  - `objective`: 処理の目的  - `owner`: オーナーのIDを参照するJSONエンコードされた文字列を含むリスト  - `refMLModel`: 処理に使用する機械学習モデルを対象とした関係  - `refSubscriptionQuery`: 機械学習モデルで使用するサブスクリプション・クエリをターゲットとする関係。  - `seeAlso`: アイテムに関する追加リソースを示すuriのリスト  - `source`: エンティティデータのオリジナルソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。    
必須項目  
## データモデルによるプロパティの記述  
アルファベット順（クリックすると詳細が表示されます  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
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
  required: []    
  type: object    
```  
</details>    
## ペイロードの例  
#### MLProcessing NGSI-v2 key-values の例。  
ここでは、JSON-LD形式でkey-valuesとしてMLProcessingの例を示します。これは`options=keyValues`を使うとNGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返すことができます。  
```json  
{  
  "id":"urn:ngsi-ld:MLProcessing:01",  
  "type":"MLProcessing",  
  "refMLModel": "urn:ngsi-ld:MLModel:01",  
  "refSubscriptionQuery": "urn:ngsi-ld:SubscriptionQuery:01"  
}  
```  
#### MLProcessing NGSI-v2の正規化例  
ここでは、正規化されたJSON-LD形式のMLProcessingの例を示します。これは、オプションを使用しない場合のNGSI-v2との互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### MLProcessing NGSI-LD key-valuesの例。  
ここでは、JSON-LD形式でkey-valuesとしてMLProcessingの例を示します。これは、`options=keyValues`を使うとNGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### MLProcessing NGSI-LDの正規化例  
ここでは、JSON-LD形式のMLProcessingを正規化した例を紹介します。これは、オプションを使わない場合のNGSI-LDとの互換性があり、個々のエンティティのコンテキストデータを返します。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。