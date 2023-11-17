<!-- 10-Header -->    
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)    
エンティティサブスクリプションクエリ    
==================<!-- /10-Header -->    
<!-- 15-License -->    
[オープン・ライセンス](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md)    
[文書は自動的に生成される](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)    
<!-- /15-License -->    
<!-- 20-Description -->    
グローバルな説明**機械学習モデルのためのサブスクリプションクエリーモデル**。    
バージョン: 0.0.2    
<!-- /20-Description -->    
<!-- 30-PropertiesList -->    
## プロパティのリスト    
<sup><sub>[*] 属性に型がない場合は、複数の型があるか、異なるフォーマット/パターンがある可能性があるためです</sub></sup>。    
- `alternateName[string]`: この項目の別名  - `csf[string]`: エンティティを検索するために使用されるコンテキストソースを記述するコンテキストソース登録によって適合されなければならないコンテキストソースフィルタ。NGSI-LD 標準で定義されている。  - `dataProvider[string]`: ハーモナイズされたデータ・エンティティの提供者を識別する一連の文字。  - `dateCreated[date-time]`: エンティティの作成タイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられます。  - `dateModified[date-time]`: エンティティの最終変更のタイムスタンプ。これは通常、ストレージプラットフォームによって割り当てられる。  - `description[string]`: この商品の説明  - `entities[array]`: エンティティが検索されるためにマッチしなければならないエンティティ ID、ID パターン、エンティティタイプ。NGSI-LD 標準で定義されている。  - `expiresAt[string]`: サブスクリプションの有効期限。NGSI-LD規格で定義  - `geoQ[string]`: エンティティが検索されるためにマッチしなければならないジオクエリー。NGSI-LD 標準で定義されている。  - `id[*]`: エンティティの一意識別子  - `name[string]`: このアイテムの名前  - `notification[object]`: サブスクリプションの通知のパラメータ。NGSI-LD 標準で定義されている。  	- `attributes`:       
	- `endPoint`:       
- `owner[array]`: 所有者の固有IDを参照するJSONエンコードされた文字列を含むリスト。  - `q[string]`: エンティティが検索されるために一致させなければならないクエリ。NGSI-LD 標準で定義されている。  - `seeAlso[*]`: アイテムに関する追加リソースを指すURIのリスト  - `source[string]`: エンティティ・データの元のソースを URL として示す一連の文字。ソース・プロバイダの完全修飾ドメイン名、またはソース・オブジェクトの URL を推奨する。  - `subscriptionName[string]`: このサブスクリプションに与えられる(短い)名前。NGSI-LD 標準で定義されている。  - `temporalQ[string]`: Temporal Query は、'Query Temporal Evolution of Entities' 操作にのみ存在する。NGSI-LD規格で定義  - `throttling[string]`: 連続する 2 つの通知間の最小経過時間（秒）。NGSI-LD規格で定義  - `type[string]`: SubscriptionQuery でなければなりません。NGSIエンティティタイプ。Enum:'SubscriptionQuery'。  - `watchedAttributes[array]`: Entityが検索するためにマッチさせなければならないAttributesのリスト。存在しない場合、すべての属性が検索される。NGSI-LD 標準で定義されている。  <!-- /30-PropertiesList -->    
<!-- 35-RequiredProperties -->    
必須プロパティ    
- `id`  - `type`  <!-- /35-RequiredProperties -->    
<!-- 40-RequiredProperties -->    
<!-- /40-RequiredProperties -->    
<!-- 50-DataModelHeader -->    
## プロパティのデータモデル記述    
アルファベット順（クリックで詳細表示）    
<!-- /50-DataModelHeader -->    
<!-- 60-ModelYaml -->    
<details><summary><strong>full yaml details</strong></summary>      
```yaml    
SubscriptionQuery:      
  description: Subscription Query model for Machine Learning models      
  properties:      
    alternateName:      
      description: An alternative name for this item      
      type: string      
      x-ngsi:      
        type: Property      
    csf:      
      description: Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities. Defined in NGSI-LD standard      
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
    entities:      
      description: 'Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard'      
      items:      
        properties:      
          type:      
            type: string      
        type: object      
      type: array      
      x-ngsi:      
        type: Property      
    expiresAt:      
      description: Expiration date for the subscription. Defined in NGSI-LD standard      
      type: string      
      x-ngsi:      
        type: Property      
    geoQ:      
      description: Geo-Query that shall be matched by Entities in order be retrieved. Defined in NGSI-LD standard      
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
    notification:      
      description: Parameters of the notification for the subscription. Defined in NGSI-LD standard      
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
          description: Format of the output      
          type: string      
          x-ngsi:      
            type: Property      
      type: object      
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
    q:      
      description: Query that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard      
      type: string      
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
    subscriptionName:      
      description: A (short) name given to this Subscription. Defined in NGSI-LD standard      
      type: string      
      x-ngsi:      
        type: Property      
    temporalQ:      
      description: Temporal Query to be present only for 'Query Temporal Evolution of Entities' operation. Defined in NGSI-LD standard      
      type: string      
      x-ngsi:      
        type: Property      
    throttling:      
      description: Minimal period of time in seconds which shall elapse between two consecutive notifications. Defined in NGSI-LD standard      
      type: string      
      x-ngsi:      
        type: Property      
    type:      
      description: 'It has to be SubscriptionQuery. NGSI entity type. Enum:''SubscriptionQuery'''      
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2022 Contributors to Smart Data Models Program'      
  x-license-url: https://github.com/smart-data-models/dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md      
  x-model-schema: https://smart-data-models.github.io/dataModel.MLModel/SubscriptionQuery/schema.json      
  x-model-tags: ""      
  x-version: 0.0.2      
```    
</details>      
<!-- /60-ModelYaml -->    
<!-- 70-MiddleNotes -->    
<!-- /70-MiddleNotes -->    
<!-- 80-Examples -->    
## ペイロードの例    
#### SubscriptionQuery NGSI-v2 キー値の例    
以下は、JSON-LD フォーマットのキー値としての SubscriptionQuery の例です。これは NGSI-v2 と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返します。    
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
#### SubscriptionQuery NGSI-v2 正規化例    
以下は、正規化された JSON-LD フォーマットの SubscriptionQuery の例です。これは、オプションを使用しない場合に NGSI-v2 と互換性があり、個々のエンティティのコンテキスト・データを返します。    
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
#### SubscriptionQuery NGSI-LD キー値の例    
以下は、JSON-LD フォーマットのキー値としての SubscriptionQuery の例です。これは NGSI-LD と互換性があり、`options=keyValues` を使用すると、個々のエンティティのコンテキストデータを返します。    
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
#### SubscriptionQuery NGSI-LD 正規化例    
以下は、正規化された JSON-LD フォーマットの SubscriptionQuery の例です。これは、オプションを使用しない場合に NGSI-LD と互換性があり、個々のエンティティのコンテキストデータを返します。    
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
マグニチュード単位の扱い方については、[FAQ 10](https://smartdatamodels.org/index.php/faqs/)を参照のこと。    
<!-- /95-Units -->    
<!-- 97-LastFooter -->    
---    
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->    
