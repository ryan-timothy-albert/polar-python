# MetricsSDK
(*metrics*)

## Overview

### Available Operations

* [get](#get) - Get Metrics
* [limits](#limits) - Get Metrics Limits

## get

Get metrics about your orders and subscriptions.

### Example Usage

```python
import dateutil.parser
import polar_sdk
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.get(start_date=dateutil.parser.parse("2024-02-07").date(), end_date=dateutil.parser.parse("2022-04-09").date(), interval=polar_sdk.Interval.WEEK)

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                                                                                                                                         | Type                                                                                                                                                                              | Required                                                                                                                                                                          | Description                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `start_date`                                                                                                                                                                      | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                      | :heavy_check_mark:                                                                                                                                                                | Start date.                                                                                                                                                                       |
| `end_date`                                                                                                                                                                        | [datetime](https://docs.python.org/3/library/datetime.html#datetime-objects)                                                                                                      | :heavy_check_mark:                                                                                                                                                                | End date.                                                                                                                                                                         |
| `interval`                                                                                                                                                                        | [models.Interval](../../models/interval.md)                                                                                                                                       | :heavy_check_mark:                                                                                                                                                                | Interval between two timestamps.                                                                                                                                                  |
| `organization_id`                                                                                                                                                                 | [OptionalNullable[models.MetricsGetQueryParamOrganizationIDFilter]](../../models/metricsgetqueryparamorganizationidfilter.md)                                                     | :heavy_minus_sign:                                                                                                                                                                | Filter by organization ID.                                                                                                                                                        |
| `product_id`                                                                                                                                                                      | [OptionalNullable[models.MetricsGetQueryParamProductIDFilter]](../../models/metricsgetqueryparamproductidfilter.md)                                                               | :heavy_minus_sign:                                                                                                                                                                | Filter by product ID.                                                                                                                                                             |
| `product_price_type`                                                                                                                                                              | [OptionalNullable[models.QueryParamProductPriceTypeFilter]](../../models/queryparamproductpricetypefilter.md)                                                                     | :heavy_minus_sign:                                                                                                                                                                | Filter by product price type. `recurring` will filter data corresponding to subscriptions creations or renewals. `one_time` will filter data corresponding to one-time purchases. |
| `retries`                                                                                                                                                                         | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                | Configuration to override the default retry behavior of the client.                                                                                                               |

### Response

**[models.MetricsResponse](../../models/metricsresponse.md)**

### Errors

| Error Type                 | Status Code                | Content Type               |
| -------------------------- | -------------------------- | -------------------------- |
| models.HTTPValidationError | 422                        | application/json           |
| models.SDKError            | 4XX, 5XX                   | \*/\*                      |

## limits

Get the interval limits for the metrics endpoint.

### Example Usage

```python
from polar_sdk import Polar

with Polar(
    access_token="<YOUR_BEARER_TOKEN_HERE>",
) as polar:

    res = polar.metrics.limits()

    # Handle response
    print(res)

```

### Parameters

| Parameter                                                           | Type                                                                | Required                                                            | Description                                                         |
| ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `retries`                                                           | [Optional[utils.RetryConfig]](../../models/utils/retryconfig.md)    | :heavy_minus_sign:                                                  | Configuration to override the default retry behavior of the client. |

### Response

**[models.MetricsLimits](../../models/metricslimits.md)**

### Errors

| Error Type      | Status Code     | Content Type    |
| --------------- | --------------- | --------------- |
| models.SDKError | 4XX, 5XX        | \*/\*           |