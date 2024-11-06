# CustomFieldCreateText

Schema to create a custom field of type text.


## Fields

| Field                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `slug`                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                       | Identifier of the custom field. It'll be used as key when storing the value. Must be unique across the organization.                                                                                                                                     |
| `name`                                                                                                                                                                                                                                                   | *str*                                                                                                                                                                                                                                                    | :heavy_check_mark:                                                                                                                                                                                                                                       | Name of the custom field.                                                                                                                                                                                                                                |
| `properties`                                                                                                                                                                                                                                             | [models.CustomFieldTextProperties](../models/customfieldtextproperties.md)                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                      |
| `metadata`                                                                                                                                                                                                                                               | Dict[str, *str*]                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                       | Key-value object allowing you to store additional information.<br/><br/>The key must be a string with a maximum length of **40 characters**.<br/>The value must be a string with a maximum length of **500 characters**.<br/>You can store up to **50 key-value pairs**. |
| `type`                                                                                                                                                                                                                                                   | [models.CustomFieldCreateTextType](../models/customfieldcreatetexttype.md)                                                                                                                                                                               | :heavy_check_mark:                                                                                                                                                                                                                                       | N/A                                                                                                                                                                                                                                                      |
| `organization_id`                                                                                                                                                                                                                                        | *OptionalNullable[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                       | The ID of the organization owning the custom field. **Required unless you use an organization token.**                                                                                                                                                   |