# CheckoutLinkUpdate

Schema to update an existing checkout link.


## Fields

| Field                                                                                                                                                                                                                                                    | Type                                                                                                                                                                                                                                                     | Required                                                                                                                                                                                                                                                 | Description                                                                                                                                                                                                                                              |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `metadata`                                                                                                                                                                                                                                               | Dict[str, *str*]                                                                                                                                                                                                                                         | :heavy_minus_sign:                                                                                                                                                                                                                                       | Key-value object allowing you to store additional information.<br/><br/>The key must be a string with a maximum length of **40 characters**.<br/>The value must be a string with a maximum length of **500 characters**.<br/>You can store up to **50 key-value pairs**. |
| `success_url`                                                                                                                                                                                                                                            | *OptionalNullable[str]*                                                                                                                                                                                                                                  | :heavy_minus_sign:                                                                                                                                                                                                                                       | URL where the customer will be redirected after a successful payment.You can add the `checkout_id={CHECKOUT_ID}` query parameter to retrieve the checkout session id.                                                                                    |