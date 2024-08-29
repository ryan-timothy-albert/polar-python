# PolarBenefits
(*users.benefits*)

## Overview

### Available Operations

* [list](#list) - List Benefits
* [retrieve](#retrieve) - Get Benefit

## list

List my granted benefits.

### Example Usage

```python
from polar import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.benefits.list()

if res is not None:
    while True:
        # handle items

        res = res.Next()
        if res is None:
            break


```

### Parameters

| Parameter                                                                                                                                                               | Type                                                                                                                                                                    | Required                                                                                                                                                                | Description                                                                                                                                                             |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type_filter`                                                                                                                                                           | [OptionalNullable[models.BenefitTypeFilter]](../../models/benefittypefilter.md)                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Filter by benefit type.                                                                                                                                                 |
| `organization_id`                                                                                                                                                       | [OptionalNullable[models.OrganizationIDFilter]](../../models/organizationidfilter.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by organization ID.                                                                                                                                              |
| `order_id`                                                                                                                                                              | [OptionalNullable[models.OrderIDFilter]](../../models/orderidfilter.md)                                                                                                 | :heavy_minus_sign:                                                                                                                                                      | Filter by order ID.                                                                                                                                                     |
| `subscription_id`                                                                                                                                                       | [OptionalNullable[models.SubscriptionIDFilter]](../../models/subscriptionidfilter.md)                                                                                   | :heavy_minus_sign:                                                                                                                                                      | Filter by subscription ID.                                                                                                                                              |
| `page`                                                                                                                                                                  | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Page number, defaults to 1.                                                                                                                                             |
| `limit`                                                                                                                                                                 | *Optional[int]*                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Size of a page, defaults to 10. Maximum is 100.                                                                                                                         |
| `sorting`                                                                                                                                                               | List[[models.UserBenefitSortProperty](../../models/userbenefitsortproperty.md)]                                                                                         | :heavy_minus_sign:                                                                                                                                                      | Sorting criterion. Several criteria can be used simultaneously and will be applied in order. Add a minus sign `-` before the criteria name to sort by descending order. |
| `retries`                                                                                                                                                               | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                        | :heavy_minus_sign:                                                                                                                                                      | Configuration to override the default retry behavior of the client.                                                                                                     |

### Response

**[models.UsersBenefitsListResponse](../../models/usersbenefitslistresponse.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |


## retrieve

Get a granted benefit by ID.

### Example Usage

```python
from polar import Polar

s = Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
)


res = s.users.benefits.retrieve(id="<value>")

if res is not None:
    # handle response
    pass

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `id`                                                                | *str*                                                               | :heavy_check_mark:                                                  | The benefit ID.                                                     |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.UsersBenefitsGetResponseUsersBenefitsGet](../../models/usersbenefitsgetresponseusersbenefitsget.md)**

### Errors

| Error Object               | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.ResourceNotFound    | 404                        | application/json           |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4xx-5xx                    | */*                        |