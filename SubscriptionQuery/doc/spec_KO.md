<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
엔티티: 구독 쿼리  
==========<!-- /10-Header -->  
<!-- 15-License -->  
[오픈 라이선스](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/SubscriptionQuery/LICENSE.md)  
[문서 자동 생성](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
글로벌 설명: **머신 러닝 모델을 위한 구독 쿼리 모델**  
버전: 0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

## 속성 목록  

<sup><sub>[*] 속성에 유형이 없는 것은 여러 유형 또는 다른 형식/패턴을 가질 수 있기 때문입니다</sub></sup>.  
- `alternateName[string]`: 이 항목의 대체 이름  - `csf[string]`: 엔티티를 검색하는 데 사용할 컨텍스트 소스를 설명하는 컨텍스트 소스 등록과 일치해야 하는 컨텍스트 소스 필터입니다. NGSI-LD 표준에 정의됨  - `dataProvider[string]`: 조화된 데이터 엔티티의 공급자를 식별하는 일련의 문자  - `dateCreated[date-time]`: 엔티티 생성 타임스탬프. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `dateModified[date-time]`: 엔티티의 마지막 수정 타임스탬프입니다. 이는 일반적으로 스토리지 플랫폼에서 할당합니다.  - `description[string]`: 이 항목에 대한 설명  - `entities[array]`: 검색하기 위해 엔티티가 일치시켜야 하는 엔티티 아이디, 아이디 패턴 및 엔티티 유형입니다. NGSI-LD 표준에 정의됨  - `expiresAt[string]`: 구독 만료일. NGSI-LD 표준에 정의됨  - `geoQ[string]`: 엔티티가 검색할 순서대로 일치시켜야 하는 지리적 쿼리입니다. NGSI-LD 표준에 정의됨  - `id[*]`: 엔티티의 고유 식별자  - `name[string]`: 이 항목의 이름  - `notification[object]`: 구독에 대한 알림의 매개변수입니다. NGSI-LD 표준에 정의됨  	- `attributes`:     
	- `endPoint`:     
	- `format[string]`: 출력 형식    
- `owner[array]`: 소유자의 고유 ID를 참조하는 JSON 인코딩된 문자 시퀀스가 포함된 목록입니다.  - `q[string]`: 검색하기 위해 엔티티가 일치시켜야 하는 쿼리입니다. NGSI-LD 표준에 정의됨  - `seeAlso[*]`: 항목에 대한 추가 리소스를 가리키는 URL 목록  - `source[string]`: 엔티티 데이터의 원본 소스를 URL로 제공하는 문자 시퀀스입니다. 소스 공급자의 정규화된 도메인 이름 또는 소스 개체에 대한 URL을 사용하는 것이 좋습니다.  - `subscriptionName[string]`: 이 구독에 부여된 (짧은) 이름입니다. NGSI-LD 표준에 정의됨  - `temporalQ[string]`: '엔티티의 시간적 진화 쿼리' 연산에만 존재할 수 있는 시간적 쿼리. NGSI-LD 표준에 정의됨  - `throttling[string]`: 두 개의 연속 알림 사이에 경과해야 하는 최소 시간(초)입니다. NGSI-LD 표준에 정의됨  - `type[string]`: 구독 쿼리여야 합니다. NGSI 엔티티 유형이어야 합니다. Enum:'구독 쿼리'  - `watchedAttributes[array]`: 검색하기 위해 엔티티가 일치시켜야 하는 어트리뷰트 목록입니다. 존재하지 않으면 모든 어트리뷰트가 검색됩니다. NGSI-LD 표준에 정의되어 있습니다.  <!-- /30-PropertiesList -->  
<!-- 35-RequiredProperties -->  
필수 속성  
- `id`  - `type`  <!-- /35-RequiredProperties -->  
<!-- 40-RequiredProperties -->  
<!-- /40-RequiredProperties -->  
<!-- 50-DataModelHeader -->  
## 속성에 대한 데이터 모델 설명  
알파벳순으로 정렬(자세한 내용을 보려면 클릭)  
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
## 페이로드 예시  
#### SubscriptionQuery NGSI-v2 키-값 예제  
다음은 JSON-LD 형식의 구독 쿼리를 키 값으로 사용하는 예입니다. 이 쿼리는 `옵션=키값`을 사용할 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### SubscriptionQuery NGSI-v2 정규화 예제  
다음은 정규화된 JSON-LD 형식의 구독 쿼리 예제입니다. 이 쿼리는 옵션을 사용하지 않을 때 NGSI-v2와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### SubscriptionQuery NGSI-LD 키-값 예제  
다음은 JSON-LD 형식의 구독 쿼리를 키 값으로 사용하는 예입니다. 이 쿼리는 `옵션=키값`을 사용할 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
#### SubscriptionQuery NGSI-LD 정규화 예제  
다음은 정규화된 JSON-LD 형식의 구독 쿼리 예제입니다. 이 쿼리는 옵션을 사용하지 않을 때 NGSI-LD와 호환되며 개별 엔티티의 컨텍스트 데이터를 반환합니다.  
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
[FAQ 10](https://smartdatamodels.org/index.php/faqs/)을 참조하여 규모 단위를 다루는 방법에 대한 답변을 확인하세요.  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
