<!-- 10-Header -->  
[![Smart Data Models](https://smartdatamodels.org/wp-content/uploads/2022/01/SmartDataModels_logo.png "Logo")](https://smartdatamodels.org)  
实体。淘宝网  
======<!-- /10-Header -->  
<!-- 15-License -->  
[开放许可](https://github.com/smart-data-models//dataModel.MachineLearning/blob/master/MLModel/LICENSE.md)  
[文件自动生成](https://docs.google.com/presentation/d/e/2PACX-1vTs-Ng5dIAwkg91oTTUdt8ua7woBXhPnwavZ0FxgR8BsAI_Ek3C5q97Nd94HS8KhP-r_quD4H0fgyt3/pub?start=false&loop=false&delayms=3000#slide=id.gb715ace035_0_60)  
<!-- /15-License -->  
<!-- 20-Description -->  
全局描述。**用于汇编机器学习模型元素的数据模型。  
版本：0.0.2  
<!-- /20-Description -->  
<!-- 30-PropertiesList -->  

##属性列表  

<sup><sub>[*] 如果一个属性中没有一个类型，是因为它可能有几种类型或不同的格式/模式</sub></sup>。  
- `acceptableDataSources[array]`: 运行机器学习模型的有效输入数据源类型  - `algorithm[string]`: 底层机器学习模型使用的算法（例如线性回归、K-means、SVM、MLP...）。  - `alternateName[string]`: 这个项目的一个替代名称  - `dataProvider[string]`: 一串识别统一数据实体提供者的字符。  - `dateCreated[string]`: 实体创建时间戳。这通常会由存储平台分配。  - `dateModified[string]`: 实体最后一次修改的时间戳。这通常会由存储平台分配。  - `description[string]`: 对这个项目的描述  - `dockerImage[string]`: 包含机器学习模型的Docker镜像  - `id[*]`: 实体的唯一标识符  - `inputAttributes[array]`: 逗号分隔的属性名称列表（根据定义应该有一个给定的类型）。  - `mlFramework[string]`: 用于准备模型的机器学习框架（如scikit-learn、H2O、Spark MLib等）。  - `name[string]`: 这个项目的名称。  - `outputAttributes[array]`: 用逗号分隔的用于发布结果的属性名称列表。  - `outputDataTypes[array]`: 机器学习模型产生的输出数据的类型  - `owner[array]`: 一个包含JSON编码的字符序列的列表，引用所有者的唯一Ids。  - `refMLProcessing[array]`:   - `seeAlso[*]`: 指向有关该项目的其他资源的URI列表  - `source[string]`: 提供实体数据原始来源的一连串字符，作为一个URL。建议为源提供者的完全合格域名，或源对象的URL。  - `type[string]`: NGSI实体类型。它必须是MLModel  - `typeOfAlgorithm[string]`: 枚举  . Model: [https://schema.org/Text](https://schema.org/Text)- `version[string]`: 模型的版本。  <!-- /30-PropertiesList -->  
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
## ＃＃＃＃有效载荷的例子  
#### MLModel NGSI-v2 关键值示例  
这里是一个以JSON-LD格式作为key-values的MLModel的例子。当使用`options=keyValues`时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### MLModel NGSI-v2规范化示例  
下面是一个以JSON-LD格式规范化的MLModel的例子。当不使用选项时，这与NGSI-v2兼容，并返回单个实体的上下文数据。  
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
#### MLModel NGSI-LD关键值示例  
这里是一个以JSON-LD格式作为key-values的MLModel的例子。当使用`options=keyValues`时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
#### MLModel NGSI-LD归一化实例  
下面是一个以JSON-LD格式规范化的MLModel的例子。当不使用选项时，这与NGSI-LD兼容，并返回单个实体的上下文数据。  
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
参见[常见问题10](https://smartdatamodels.org/index.php/faqs/)，以获得关于如何处理量级单位的答案。  
<!-- /95-Units -->  
<!-- 97-LastFooter -->  
---  
[Smart Data Models](https://smartdatamodels.org) +++ [Contribution Manual](https://bit.ly/contribution_manual) +++ [About](https://bit.ly/Introduction_SDM)<!-- /97-LastFooter -->  
