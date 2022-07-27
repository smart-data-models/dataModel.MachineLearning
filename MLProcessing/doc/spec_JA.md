[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティMLProcessing  
==================  
[オープンライセンス](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLProcessing/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
グローバルな記述。**機械学習モデルの実行に関する要素をまとめたデータモデル**。  
バージョン: 0.0.2  

## プロパティ一覧  

- `alternateName`: この項目の別称  - `connectionParameters`: システムとの接続を実行するためのパラメータ  - `dataProvider`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description`: このアイテムの説明  - `dueDate`: 処理実行予定データ/時間（後のバージョンでは計画的な処理を可能にするため）  - `id`: エンティティの一意な識別子  - `name`: このアイテムの名称です。  - `objective`: 加工の目的  - `owner`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `refMLModel`: 処理に使用する機械学習モデルをターゲットとする関係  - `refSubscriptionQuery`: 機械学習モデルで使用するサブスクリプションクエリをターゲットとするリレーションシップ。  - `seeAlso`: 項目に関する追加リソースを指すURIのリスト。  - `source`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type`: NGSIエンティティタイプ。MLProcessingでなければならない    
必要なプロパティ  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
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
## ペイロードの例  
#### MLProcessing NGSI-v2 key-values の例．  
ここでは，MLP処理をJSON-LD形式でkey-valuesとして表現した例を示します。これは，`options=keyValues` を利用した場合に NGSI-v2 と互換性があり，個々のエンティティのコンテキストデータが返されます．  
```json  
{  
  "id":"urn:ngsi-ld:MLProcessing:01",  
  "type":"MLProcessing",  
  "refMLModel": "urn:ngsi-ld:MLModel:01",  
  "refSubscriptionQuery": "urn:ngsi-ld:SubscriptionQuery:01"  
}  
```  
#### MLProcessing NGSI-v2 正規化例  
以下は，MLProcessing を JSON-LD 形式で正規化した例です。これは，オプションを使用しない場合，NGSI-v2と互換性があり，個々のエンティティのコンテキストデータを返します．  
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
#### MLProcessing NGSI-LD key-value 例  
ここでは，MLP処理をJSON-LD形式でkey-valuesとして表現した例を示します．これは， `options=keyValues` を利用した場合にNGSI-LDと互換性があり，個々のエンティティのコンテキストデータを返します．  
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
#### MLProcessing NGSI-LD 正規化例  
ここでは，MLProcessing を JSON-LD 形式で正規化した例を示します。これは，オプションを使用しない場合のNGSI-LDと互換性があり，個々のエンティティのコンテキストデータを返します．  
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
    "@context": []  
}  
```  
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
