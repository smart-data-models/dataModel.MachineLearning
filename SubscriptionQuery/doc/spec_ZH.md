<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。订阅查询  
=======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**机器学习模型的订阅查询模型**。  
版本：0.0.1  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `alternateName[string]`: 这个项目的一个替代名称  - `csf[string]`: 上下文源过滤器，应与描述用于检索实体的上下文源的上下文源注册相匹配。在 NGSI-LD 标准中定义。  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `entities[array]`: 实体ID、ID模式和实体类型，实体应与之匹配，以便被检索。在NGSI-LD标准中定义。  - `expiresAt[string]`: 订阅的到期日。在NGSI-LD标准中定义。  - `geoQ[string]`: 应由实体匹配的地理查询，以便进行检索。在NGSI-LD标准中定义。  - `id[*]`: 实体的唯一标识符  - `name[string]`: 这个项目的名称。  - `notification[object]`: 订阅通知的参数。在NGSI-LD标准中定义。  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `q[string]`: 应由实体匹配的查询，以便被检索。在NGSI-LD标准中定义。  - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 一系列的字符，以URL的形式给出实体数据的原始来源。建议为源提供者的完全合格域名，或源对象的URL。  - `subscriptionName[string]`: 给予该订阅号的一个（简短）名称。在NGSI-LD标准中定义。  - `temporalQ[string]`: 时间查询只存在于 "查询实体的时间演变 "操作中。在NGSI-LD标准中定义。  - `throttling[string]`: 两个连续通知之间应间隔的最小时间（秒）。在NGSI-LD标准中定义。  - `type[string]`: 它必须是SubscriptionQuery。Enum:'SubscriptionQuery'。  - `watchedAttributes[array]`: 应由实体匹配的属性列表，以便被检索。如果不存在，所有的属性都会被检索到。在NGSI-LD标准中定义。  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
所需属性  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 数据模型的属性描述  
按字母顺序排列（点击查看详情）。  
<!-- /50-DataModelHeader -->  
<!-- 60-ModelYaml -->  
<details><summary><strong>full yaml details</strong></summary>    
```yaml  
SubscriptionQuery:    
  description: 'Subscription Query model for Machine Learning models'    
  properties:    
    alternateName:    
      description: 'An alternative name for this item'    
      type: string    
      x-ngsi:    
        type: Property    
    csf:    
      description: 'Context source filter that shall be matched by Context Source Registrations describing Context Sources to be used for retrieving Entities. Defined in NGSI-LD standard.'    
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
    entities:    
      description: 'Entity ids, id pattern and Entity types that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard.'    
      items:    
        properties:    
          type:    
            type: string    
        type: object    
      type: array    
      x-ngsi:    
        type: Property    
    expiresAt:    
      description: 'Expiration date for the subscription. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    geoQ:    
      description: 'Geo-Query that shall be matched by Entities in order be retrieved. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    id:    
      anyOf: &subscriptionquery_-_properties_-_owner_-_items_-_anyof    
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
    notification:    
      description: 'Parameters of the notification for the subscription. Defined in NGSI-LD standard.'    
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
          description: 'Property. Format of the output'    
          type: string    
      type: object    
      x-ngsi:    
        type: Property    
    owner:    
      description: 'A List containing a JSON encoded sequence of characters referencing the unique Ids of the owner(s)'    
      items:    
        anyOf: *subscriptionquery_-_properties_-_owner_-_items_-_anyof    
        description: 'Property. Unique identifier of the entity'    
      type: array    
      x-ngsi:    
        type: Property    
    q:    
      description: 'Query that shall be matched by Entities in order to be retrieved. Defined in NGSI-LD standard.'    
      type: string    
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
    subscriptionName:    
      description: 'A (short) name given to this Subscription. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    temporalQ:    
      description: 'Temporal Query to be present only for ''Query Temporal Evolution of Entities'' operation. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    throttling:    
      description: 'Minimal period of time in seconds which shall elapse between two consecutive notifications. Defined in NGSI-LD standard.'    
      type: string    
      x-ngsi:    
        type: Property    
    type:    
      description: 'It has to be SubscriptionQuery. Enum:''SubscriptionQuery'''    
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
  x-disclaimer: 'Redistribution and use in source and binary forms, with or without modification, are permitted  provided that the license conditions are met. Copyleft (c) 2021 Contributors to Smart Data Models Program'    
  x-license-url: https://github.com/smart-data-models/dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md    
  x-model-schema: https://smart-data-models.github.io/dataModel.MLModel/SubscriptionQuery/schema.json    
  x-model-tags: ""    
  x-version: 0.0.1    
```  
</details>    
<!-- /60-ModelYaml -->  
<!-- 70-MiddleNotes -->  
<!-- /70-MiddleNotes -->  
<!-- 80-Examples -->  
## ＃＃＃＃有效载荷的例子  
#### SubscriptionQuery NGSI-v2 key-values 示例  
这里是一个以JSON-LD格式作为key-values的SubscriptionQuery的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### SubscriptionQuery NGSI-v2规范化示例  
这里是一个以JSON-LD格式规范化的SubscriptionQuery的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### SubscriptionQuery NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的SubscriptionQuery的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### SubscriptionQuery NGSI-LD规范化示例  
这里是一个以JSON-LD格式规范化的SubscriptionQuery的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
