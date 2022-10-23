<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
エンティティMLModel  
=============<!-- /10-Header -->  
<!-- 15-License -->  
[オープンライセンス](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLModel/LICENSE.md)  
[ドキュメント自動生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
グローバルな記述です。**機械学習モデルの要素をまとめるためのデータモデル。  
バージョン: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## プロパティ一覧  

<sup><sub>[*] 属性にタイプがない場合、複数のタイプまたは異なるフォーマット/パターンを持つ可能性があるためです</sub></sup>。  
- `acceptableDataSources[array]`: 機械学習モデルを実行するために有効な入力データソースの種類  - `algorithm[string]`: 基礎となる機械学習モデルで使用されるアルゴリズム（例：線形回帰，k-means，SVM，MLP，...）．  - `alternateName[string]`: この項目の別称  - `dataProvider[string]`: 調和されたデータエンティティの提供者を識別する一連の文字。  - `dateCreated[string]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `dateModified[string]`: エンティティの最終更新のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: このアイテムの説明  - `dockerImage[string]`: 機械学習モデルを格納したDockerイメージ  - `id[*]`: エンティティの一意な識別子  - `inputAttributes[array]`: カンマで区切られた属性名のリスト（定義上、指定された型を持つ必要があります）。  - `mlFramework[string]`: モデルを準備するために使用した機械学習フレームワーク（例：scikit-learn、H2O、Spark MLib、など）  - `name[string]`: このアイテムの名称です。  - `outputAttributes[array]`: 結果を公開するために使用される属性名のカンマ区切りリスト。  - `outputDataTypes[array]`: 機械学習モデルが生成する出力データの種類  - `owner[array]`: 所有者の一意のIDを参照するJSONエンコードされた文字列を含むリストです。  - `refMLProcessing[array]`:   - `seeAlso[*]`: 項目に関する追加リソースを指すURIのリスト。  - `source[string]`: エンティティデータの元のソースをURLで示す一連の文字。ソースプロバイダの完全修飾ドメイン名、またはソースオブジェクトのURLであることが推奨されます。  - `type[string]`: NGSI エンティティタイプ。MLModelでなければならない。  - `typeOfAlgorithm[string]`: 列挙  . Model: [https://schema.org/Text](https://schema.org/Text)- `version[string]`: モデルのバージョン。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
必要なプロパティ  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## プロパティのデータモデル記述  
アルファベット順に並びます（クリックで詳細へ）  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
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
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ペイロードの例  
#### MLModel NGSI-v2 key-value の例。  
ここでは、MLModelをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合、NGSI-v2と互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### MLModel NGSI-v2 正規化例  
以下は、MLModel を JSON-LD 形式で正規化した例である。これはオプションを使用しない場合，NGSI-v2と互換性があり，個々のエンティティのコンテクストデータを返す。  
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
#### MLModel NGSI-LD key-value 例  
ここでは、MLModelをJSON-LD形式でkey-valuesとした例を示します。これは、`options=keyValues`を使用した場合、NGSI-LDと互換性があり、個々のエンティティのコンテキストデータを返します。  
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
#### MLModel NGSI-LD 正規化例  
MLModel を JSON-LD 形式で正規化した例を示す。これはオプションを使用しない場合，NGSI-LDと互換性があり，個々のエンティティのコンテクストデータを返す。  
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
マグニチュード単位の扱いについては、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照してください。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
